from __future__ import annotations

from pathlib import Path

from fpdf import FPDF

from .alignment import TranscriptSegment


def _format_timestamp(seconds: float) -> str:
    """Converte segundos para formato ``HH:MM:SS``."""
    total = int(seconds)
    h = total // 3600
    m = (total % 3600) // 60
    s = total % 60
    return f"{h:02d}:{m:02d}:{s:02d}"


def _build_lines(segments: list[TranscriptSegment]) -> list[str]:
    """Gera as linhas de texto formatadas da transcrição."""
    lines: list[str] = []
    current_speaker: str | None = None

    for seg in segments:
        if seg.speaker != current_speaker:
            current_speaker = seg.speaker
            lines.append("")
            lines.append(f"**{seg.speaker}**")

        ts_start = _format_timestamp(seg.start)
        ts_end = _format_timestamp(seg.end)
        lines.append(f"[{ts_start} -> {ts_end}] {seg.text}")

    # Remove primeira linha em branco
    if lines and lines[0] == "":
        lines = lines[1:]

    return lines


def to_markdown(
    segments: list[TranscriptSegment],
    output_path: str | Path,
    title: str = "Transcrição de Reunião",
) -> Path:
    """Gera um arquivo Markdown com a transcrição segmentada por speaker.

    Args:
        segments: Lista de segmentos com speaker, timestamps e texto.
        output_path: Caminho de destino do arquivo ``.md``.
        title: Título do documento.

    Returns:
        Caminho resolvido do arquivo gerado.
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    lines: list[str] = [f"# {title}", ""]
    current_speaker: str | None = None

    for seg in segments:
        if seg.speaker != current_speaker:
            current_speaker = seg.speaker
            lines.append(f"\n## {seg.speaker}\n")

        ts_start = _format_timestamp(seg.start)
        ts_end = _format_timestamp(seg.end)
        lines.append(f"**[{ts_start} -> {ts_end}]** {seg.text}")
        lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path.resolve()


def to_pdf(
    segments: list[TranscriptSegment],
    output_path: str | Path,
    title: str = "Transcrição de Reunião",
) -> Path:
    """Gera um arquivo PDF com a transcrição segmentada por speaker.

    Args:
        segments: Lista de segmentos com speaker, timestamps e texto.
        output_path: Caminho de destino do arquivo ``.pdf``.
        title: Título do documento.

    Returns:
        Caminho resolvido do arquivo gerado.
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Título
    pdf.set_font("Helvetica", style="B", size=16)
    pdf.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.ln(4)

    current_speaker: str | None = None

    for seg in segments:
        if seg.speaker != current_speaker:
            current_speaker = seg.speaker
            pdf.ln(4)
            pdf.set_font("Helvetica", style="B", size=12)
            pdf.cell(0, 8, seg.speaker, new_x="LMARGIN", new_y="NEXT")

        ts_start = _format_timestamp(seg.start)
        ts_end = _format_timestamp(seg.end)

        pdf.set_font("Helvetica", style="B", size=9)
        pdf.cell(0, 5, f"[{ts_start} -> {ts_end}]", new_x="LMARGIN", new_y="NEXT")

        pdf.set_font("Helvetica", size=10)
        pdf.multi_cell(0, 6, seg.text)
        pdf.ln(1)

    pdf.output(str(output_path))
    return output_path.resolve()
