from __future__ import annotations

import tempfile
from pathlib import Path
from typing import Any

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from src.alignment import TranscriptSegment
from src.config import build_settings
from src.pipeline import run_pipeline


SUPPORTED_FORMATS = ["mp3", "wav", "m4a", "ogg", "flac", "mp4", "webm"]


def run_transcription(audio_bytes: bytes, filename: str) -> dict[str, Any] | str:
    """Executa o pipeline de transcrição em um arquivo de áudio enviado.

    Salva o áudio em um arquivo temporário e chama ``run_pipeline``.

    Returns:
        Dicionário com ``"segments"``, ``"md"`` e ``"pdf"`` em caso de sucesso,
        ou string de mensagem de erro.
    """
    cfg = build_settings()

    if not cfg.hf_token:
        return (
            "HF_TOKEN não configurado. Defina a variável de ambiente HF_TOKEN "
            "com seu token do Hugging Face e reinicie o app."
        )

    suffix = Path(filename).suffix or ".wav"
    with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as tmp:
        tmp.write(audio_bytes)
        tmp_path = Path(tmp.name)

    try:
        result = run_pipeline(audio_path=tmp_path, config=cfg)
    finally:
        tmp_path.unlink(missing_ok=True)

    return result


def render_transcript(segments: list[TranscriptSegment]) -> None:
    """Exibe a transcrição formatada por speaker."""
    if not segments:
        st.info("Nenhum segmento encontrado na transcrição.")
        return

    current_speaker: str | None = None
    for seg in segments:
        if seg.speaker != current_speaker:
            current_speaker = seg.speaker
            st.markdown(f"### {seg.speaker}")

        h_s = int(seg.start) // 3600
        m_s = (int(seg.start) % 3600) // 60
        s_s = int(seg.start) % 60
        h_e = int(seg.end) // 3600
        m_e = (int(seg.end) % 3600) // 60
        s_e = int(seg.end) % 60
        ts = f"{h_s:02d}:{m_s:02d}:{s_s:02d} → {h_e:02d}:{m_e:02d}:{s_e:02d}"
        st.markdown(f"**[{ts}]** {seg.text}")


def main() -> None:
    st.set_page_config(page_title="Transcrição de Reuniões", page_icon=":microphone:")
    st.title("Transcrição de Reuniões com Identificação de Speakers")
    st.caption(
        "Faça upload de um arquivo de áudio para obter a transcrição segmentada "
        "por speaker, com timestamps, exportada em .md e .pdf."
    )

    uploaded_file = st.file_uploader(
        "Arquivo de áudio",
        type=SUPPORTED_FORMATS,
        help=f"Formatos suportados: {', '.join(SUPPORTED_FORMATS)}",
    )

    if uploaded_file is None:
        st.info("Aguardando upload do arquivo de áudio.")
        return

    st.audio(uploaded_file)

    if st.button("Transcrever", type="primary"):
        with st.spinner("Transcrevendo e identificando speakers... isso pode levar alguns minutos."):
            result = run_transcription(
                audio_bytes=uploaded_file.getvalue(),
                filename=uploaded_file.name,
            )

        if isinstance(result, str):
            st.error(result)
            return

        segments: list[TranscriptSegment] = result["segments"]
        md_path: Path = result["md"]
        pdf_path: Path = result["pdf"]

        st.success(f"Transcrição concluída — {len(segments)} segmentos identificados.")

        st.subheader("Transcrição")
        render_transcript(segments)

        st.divider()
        st.subheader("Downloads")

        col1, col2 = st.columns(2)
        with col1:
            st.download_button(
                label="Baixar .md",
                data=md_path.read_text(encoding="utf-8"),
                file_name=md_path.name,
                mime="text/markdown",
            )
        with col2:
            st.download_button(
                label="Baixar .pdf",
                data=pdf_path.read_bytes(),
                file_name=pdf_path.name,
                mime="application/pdf",
            )


if __name__ == "__main__":
    main()
