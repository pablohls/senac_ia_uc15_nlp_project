from langchain_core.documents import Document

from src.config import settings
from src.ingestion import chunk_pages, load_pdf_pages


def test_load_pdf_pages_reads_current_pdf():
    pages = load_pdf_pages(settings.pdf_path)

    assert len(pages) > 0
    assert pages[0]["page"] == 1
    assert all("page" in page and "text" in page for page in pages)
    assert any(page["text"] for page in pages)


def test_chunk_pages_creates_documents_with_required_metadata():
    pages = load_pdf_pages(settings.pdf_path)

    chunks = chunk_pages(
        pages,
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap,
        source=settings.pdf_path.name,
        tokenizer_name=settings.tokenizer_name,
    )

    assert len(chunks) > 0
    assert all(isinstance(chunk, Document) for chunk in chunks)
    assert all(chunk.page_content for chunk in chunks)
    assert all(chunk.metadata["source"] == settings.pdf_path.name for chunk in chunks)
    assert all(isinstance(chunk.metadata["page"], int) and chunk.metadata["page"] >= 1 for chunk in chunks)
    assert all(chunk.metadata["chunk_id"] for chunk in chunks)


def test_chunk_pages_rejects_invalid_overlap():
    try:
        chunk_pages(
            pages=[{"page": 1, "text": "texto de exemplo"}],
            chunk_size=10,
            chunk_overlap=10,
            source="sample.pdf",
            tokenizer_name=settings.tokenizer_name,
        )
    except ValueError as exc:
        assert "chunk_overlap" in str(exc)
    else:
        raise AssertionError("chunk_pages should reject chunk_overlap >= chunk_size.")
