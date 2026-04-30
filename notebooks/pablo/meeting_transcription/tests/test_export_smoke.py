from __future__ import annotations

from pathlib import Path

from src.alignment import TranscriptSegment


SAMPLE_SEGMENTS = [
    TranscriptSegment(speaker="SPEAKER_00", start=0.0, end=3.5, text="Bom dia a todos."),
    TranscriptSegment(speaker="SPEAKER_01", start=4.0, end=7.2, text="Olá, tudo bem?"),
    TranscriptSegment(speaker="SPEAKER_00", start=8.0, end=11.0, text="Vamos começar a pauta do dia."),
]


def test_to_markdown_creates_file(tmp_path):
    from src.export import to_markdown

    out = tmp_path / "transcricao.md"
    result = to_markdown(SAMPLE_SEGMENTS, output_path=out, title="Teste")

    assert result.exists()
    content = result.read_text(encoding="utf-8")
    assert "# Teste" in content
    assert "SPEAKER_00" in content
    assert "SPEAKER_01" in content
    assert "Bom dia a todos." in content
    assert "00:00:00" in content


def test_to_markdown_creates_parent_dirs(tmp_path):
    from src.export import to_markdown

    out = tmp_path / "subdir" / "nested" / "transcricao.md"
    result = to_markdown(SAMPLE_SEGMENTS, output_path=out)

    assert result.exists()


def test_to_pdf_creates_file(tmp_path):
    from src.export import to_pdf

    out = tmp_path / "transcricao.pdf"
    result = to_pdf(SAMPLE_SEGMENTS, output_path=out, title="Teste PDF")

    assert result.exists()
    assert result.stat().st_size > 0


def test_to_pdf_creates_parent_dirs(tmp_path):
    from src.export import to_pdf

    out = tmp_path / "subdir" / "transcricao.pdf"
    result = to_pdf(SAMPLE_SEGMENTS, output_path=out)

    assert result.exists()


def test_export_empty_segments(tmp_path):
    from src.export import to_markdown, to_pdf

    md_out = tmp_path / "empty.md"
    pdf_out = tmp_path / "empty.pdf"

    to_markdown([], output_path=md_out, title="Vazio")
    to_pdf([], output_path=pdf_out, title="Vazio")

    assert md_out.exists()
    assert pdf_out.exists()
