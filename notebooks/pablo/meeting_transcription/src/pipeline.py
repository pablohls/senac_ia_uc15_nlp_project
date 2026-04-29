from __future__ import annotations

from pathlib import Path

from .alignment import TranscriptSegment, assign_speakers
from .config import Settings, settings as default_settings
from .diarization import diarize_audio
from .export import to_markdown, to_pdf
from .transcription import transcribe_audio


def run_pipeline(
    audio_path: str | Path,
    config: Settings | None = None,
) -> dict[str, Path]:
    """Executa o pipeline completo de transcrição com identificação de speakers.

    Etapas:
    1. Transcrição do áudio via WhisperX (ASR + alinhamento de timestamps).
    2. Diarização via pyannote.audio (identificação de quem fala quando).
    3. Atribuição de speakers aos segmentos de transcrição.
    4. Exportação para ``.md`` e ``.pdf``.

    Args:
        audio_path: Caminho para o arquivo de áudio de entrada.
        config: Instância de ``Settings``. Se None, usa o singleton ``settings``.

    Returns:
        Dicionário com as chaves ``"md"`` e ``"pdf"`` apontando para os arquivos
        gerados.

    Raises:
        FileNotFoundError: Se o arquivo de áudio não existir.
        ValueError: Se ``hf_token`` não estiver configurado.
    """
    cfg = config or default_settings
    audio_path = Path(audio_path)

    stem = audio_path.stem

    # 1. Transcrição
    transcript_result = transcribe_audio(
        audio_path=audio_path,
        model_name=cfg.whisper_model,
        language=cfg.language,
    )

    # 2. Diarização
    diarization = diarize_audio(
        audio_path=audio_path,
        hf_token=cfg.hf_token or "",
        num_speakers=cfg.num_speakers,
        min_speakers=cfg.min_speakers,
        max_speakers=cfg.max_speakers,
    )

    # 3. Alinhamento
    segments: list[TranscriptSegment] = assign_speakers(transcript_result, diarization)

    # 4. Exportação
    cfg.output_dir.mkdir(parents=True, exist_ok=True)

    md_path = to_markdown(
        segments=segments,
        output_path=cfg.output_dir / f"{stem}.md",
        title=f"Transcricao - {stem}",
    )
    pdf_path = to_pdf(
        segments=segments,
        output_path=cfg.output_dir / f"{stem}.pdf",
        title=f"Transcricao - {stem}",
    )

    return {"md": md_path, "pdf": pdf_path, "segments": segments}
