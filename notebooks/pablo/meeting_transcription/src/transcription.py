from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np
import soundfile as sf
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor


def _resolve_model_id(model_name: str) -> str:
    if "/" in model_name:
        return model_name
    return f"openai/whisper-{model_name}"


def _decode_segment_text(processor: AutoProcessor, tokens: Any) -> str:
    token_tensor = torch.as_tensor(tokens).detach().cpu().unsqueeze(0)
    return processor.batch_decode(token_tensor, skip_special_tokens=True)[0].strip()


def _normalize_segments(
    generated: dict[str, Any],
    processor: AutoProcessor,
    language: str,
) -> dict[str, Any]:
    generated_segments = generated.get("segments", [])
    segments: list[dict[str, Any]] = []

    for item_segments in generated_segments:
        for item in item_segments:
            text = _decode_segment_text(processor, item["tokens"])
            if not text:
                continue

            start = item.get("start", 0.0)
            end = item.get("end", start)
            segments.append(
                {
                    "start": float(start),
                    "end": float(end),
                    "text": text,
                }
            )

    full_text = processor.batch_decode(
        generated["sequences"],
        skip_special_tokens=True,
    )[0].strip()

    if not segments and full_text:
        segments.append(
            {
                "start": 0.0,
                "end": 0.0,
                "text": full_text,
            }
        )

    return {
        "text": full_text,
        "language": language,
        "segments": segments,
    }


def transcribe_audio(
    audio_path: str | Path,
    model_name: str = "large-v3",
    language: str = "pt",
    device: str | None = None,
    batch_size: int = 16,
    compute_type: str | None = None,
) -> dict[str, Any]:
    """Transcreve um arquivo de áudio usando WhisperX.

    Retorna um dicionário com a chave ``segments``, onde cada segmento contém
    ``start``, ``end`` e ``text``.

    Args:
        audio_path: Caminho para o arquivo de áudio (.mp3, .wav, .m4a, etc.).
        model_name: Identificador do modelo Whisper (ex.: ``"large-v3"``).
        language: Código do idioma (ex.: ``"pt"`` para português).
        device: ``"cuda"`` ou ``"cpu"``. Se None, detecta automaticamente.
        batch_size: Tamanho do lote para inferência. Reduza se faltar VRAM.
        compute_type: Tipo de computação (``"float16"``, ``"int8"``, etc.).
            Se None, usa ``"float16"`` em GPU e ``"int8"`` em CPU.

    Returns:
        Dicionário com ``segments`` (lista de dicts com ``start``, ``end``, ``text``,
        ``words``) e ``language``.

    Raises:
        FileNotFoundError: Se o arquivo de áudio não existir.
    """
    audio_path = Path(audio_path)
    if not audio_path.exists():
        raise FileNotFoundError(f"Arquivo de áudio não encontrado: {audio_path}")

    if device is None:
        device = "cuda" if torch.cuda.is_available() else "cpu"

    torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

    model_id = _resolve_model_id(model_name)

    model = AutoModelForSpeechSeq2Seq.from_pretrained(
        model_id,
        torch_dtype=torch_dtype,
        low_cpu_mem_usage=True,
        use_safetensors=True,
    )

    model.to(device)

    processor = AutoProcessor.from_pretrained(model_id)

    audio_array, sample_rate = sf.read(str(audio_path), always_2d=False)
    if isinstance(audio_array, np.ndarray) and audio_array.ndim > 1:
        audio_array = audio_array.mean(axis=1)

    audio_array = np.asarray(audio_array, dtype=np.float32)

    inputs = processor(
        audio_array,
        sampling_rate=sample_rate,
        return_tensors="pt",
        return_attention_mask=True,
    )

    input_features = inputs.input_features.to(device=device, dtype=torch_dtype)
    attention_mask = inputs.get("attention_mask")
    if attention_mask is not None:
        attention_mask = attention_mask.to(device=device)

    generated = model.generate(
        input_features,
        attention_mask=attention_mask,
        return_timestamps=True,
        return_dict_in_generate=True,
        task="transcribe",
        language=language,
    )

    return _normalize_segments(generated, processor=processor, language=language)
