from __future__ import annotations

from pathlib import Path
import inspect
from typing import TYPE_CHECKING

import torch
from .torchaudio_compat import ensure_torchaudio_compat
from pyannote.audio import Pipeline


ensure_torchaudio_compat()

if TYPE_CHECKING:
    from pyannote.core import Annotation


def diarize_audio(
    audio_path: str | Path,
    hf_token: str,
    num_speakers: int | None = None,
    min_speakers: int | None = None,
    max_speakers: int | None = None,
    device: str | None = None,
) -> "Annotation":
    """Executa diarização de speakers em um arquivo de áudio usando pyannote.audio.

    Identifica os intervalos de tempo em que cada speaker está falando.

    Args:
        audio_path: Caminho para o arquivo de áudio.
        hf_token: Token de acesso do Hugging Face. Necessário para carregar o
            modelo ``pyannote/speaker-diarization-3.1``.
        num_speakers: Número exato de speakers, se conhecido. Se None, o modelo
            detecta automaticamente.
        min_speakers: Número mínimo esperado de speakers.
        max_speakers: Número máximo esperado de speakers.
        device: ``"cuda"`` ou ``"cpu"``. Se None, detecta automaticamente.

    Returns:
        ``pyannote.core.Annotation`` com os segmentos e labels de cada speaker.

    Raises:
        FileNotFoundError: Se o arquivo de áudio não existir.
        ValueError: Se ``hf_token`` estiver vazio.
    """
    audio_path = Path(audio_path)
    if not audio_path.exists():
        raise FileNotFoundError(f"Arquivo de áudio não encontrado: {audio_path}")

    if not hf_token or not hf_token.strip():
        raise ValueError(
            "HF_TOKEN não configurado. Defina a variável de ambiente HF_TOKEN com "
            "seu token do Hugging Face."
        )

    if device is None:
        device = "cuda" if torch.cuda.is_available() else "cpu"

    # from pyannote.audio import Pipeline
    # import pyannote.audio.core.pipeline as pyannote_pipeline

    # # Compatibilidade entre versões de pyannote e huggingface_hub.
    # hf_download = pyannote_pipeline.hf_hub_download
    # if "use_auth_token" not in inspect.signature(hf_download).parameters:
    #     def _hf_hub_download_compat(*args, use_auth_token=None, **kwargs):
    #         if use_auth_token is not None and "token" not in kwargs:
    #             kwargs["token"] = use_auth_token
    #         return hf_download(*args, **kwargs)

    #     pyannote_pipeline.hf_hub_download = _hf_hub_download_compat

    # try:
    #     diarize_model = Pipeline.from_pretrained(
    #         "pyannote/speaker-diarization-3.1",
    #         token=hf_token,
    #     )
    # except TypeError:
    #     # Compatibilidade com versões antigas da API do pyannote.
    #     diarize_model = Pipeline.from_pretrained(
    #         "pyannote/speaker-diarization-3.1",
    #         use_auth_token=hf_token,
    #     )
    # diarize_model.to(torch.device(device))

    # kwargs: dict = {}
    # if num_speakers is not None:
    #     kwargs["num_speakers"] = num_speakers
    # else:
    #     if min_speakers is not None:
    #         kwargs["min_speakers"] = min_speakers
    #     if max_speakers is not None:
    #         kwargs["max_speakers"] = max_speakers

    # diarization = diarize_model(str(audio_path), **kwargs)
    # return diarization
