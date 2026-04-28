from __future__ import annotations

from pathlib import Path

from chromadb.api.types import Documents, Embeddings

from src.config import settings
from src.indexing import rebuild_chroma
from src.ingestion import chunk_pages, load_pdf_pages
from src.retrieval import RetrieverService


class DummyEmbeddingFunction:
    def __call__(self, input: Documents) -> Embeddings:
        vectors: Embeddings = []
        for text in input:
            seed = float(sum(ord(char) for char in text) % 1000)
            vectors.append([seed / 1000.0, len(text) / 1000.0, 1.0])
        return vectors

    @staticmethod
    def name() -> str:
        return "dummy-embedding"

    def get_config(self) -> dict[str, str]:
        return {"name": "dummy-embedding"}

    @staticmethod
    def build_from_config(config: dict[str, str]) -> "DummyEmbeddingFunction":
        return DummyEmbeddingFunction()

    def embed_documents(self, input: Documents) -> Embeddings:
        return self(input)

    def embed_query(self, input: Documents) -> Embeddings:
        return self(input)

    def is_legacy(self) -> bool:
        return False

    def supported_spaces(self) -> tuple[str, ...]:
        return ("cosine",)


class DummyCollection:
    def query(self, *args, **kwargs):
        raise AssertionError("query should not be called for invalid input.")


def test_retriever_service_returns_top_k_with_expected_fields(tmp_path: Path):
    pages = load_pdf_pages(settings.pdf_path)
    docs = chunk_pages(
        pages,
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap,
        source=settings.pdf_path.name,
        tokenizer_name=settings.tokenizer_name,
    )
    persist_dir = tmp_path / "chroma"
    embeddings = DummyEmbeddingFunction()

    rebuild_chroma(docs[:12], persist_dir, embeddings)
    retriever = RetrieverService(persist_dir=persist_dir, embeddings=embeddings, default_k=3)

    results = retriever.retrieve("jornada de trabalho no comercio")

    assert len(results) == 3
    assert all(result.text for result in results)
    assert all(0.0 <= result.score <= 1.0 for result in results)
    assert all(result.page >= 1 for result in results)
    assert all(result.source == settings.pdf_path.name for result in results)
    assert all(result.chunk_id for result in results)


def test_retriever_service_uses_real_persisted_index():
    retriever = RetrieverService()

    results = retriever.retrieve("qual e a vigencia da convencao coletiva?", k=3)

    assert len(results) == 3
    assert all(result.text for result in results)
    assert all(0.0 <= result.score <= 1.0 for result in results)
    assert all(result.page >= 1 for result in results)
    assert all(result.source == settings.pdf_path.name for result in results)


def test_retriever_service_rejects_invalid_query():
    retriever = RetrieverService(embeddings=DummyEmbeddingFunction(), collection=DummyCollection())

    try:
        retriever.retrieve("   ")
    except ValueError as exc:
        assert "query" in str(exc)
    else:
        raise AssertionError("retrieve should reject empty queries.")
