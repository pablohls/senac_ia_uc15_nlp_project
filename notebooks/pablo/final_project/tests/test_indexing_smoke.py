from __future__ import annotations

from pathlib import Path

from chromadb.api.types import Documents, Embeddings

from src.config import settings
from src.indexing import build_embeddings, open_chroma, rebuild_chroma
from src.ingestion import chunk_pages, load_pdf_pages


class DummyEmbeddingFunction:
    def __init__(self) -> None:
        pass

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


def test_build_embeddings_uses_sentence_transformer(monkeypatch):
    captured: dict[str, object] = {}

    class FakeSentenceTransformer:
        def __init__(self, model_name: str):
            captured["model_name"] = model_name

        def encode(self, texts, convert_to_numpy, normalize_embeddings):
            captured["texts"] = list(texts)
            captured["convert_to_numpy"] = convert_to_numpy
            captured["normalize_embeddings"] = normalize_embeddings
            return [[0.1, 0.2, 0.3] for _ in texts]

    monkeypatch.setattr("src.indexing.SentenceTransformer", FakeSentenceTransformer)

    embeddings = build_embeddings("fake-model")
    result = embeddings(["alpha", "beta"])

    assert captured["model_name"] == "fake-model"
    assert captured["texts"] == ["alpha", "beta"]
    assert captured["convert_to_numpy"] is True
    assert captured["normalize_embeddings"] is True
    assert [list(vector) for vector in result] == [[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]]


def test_rebuild_and_open_chroma_persist_and_query(tmp_path: Path):
    pages = load_pdf_pages(settings.pdf_path)
    docs = chunk_pages(
        pages,
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap,
        source=settings.pdf_path.name,
    )
    persist_dir = tmp_path / "chroma"

    rebuild_chroma(docs[:8], persist_dir, DummyEmbeddingFunction())

    chroma_files = list(persist_dir.rglob("*"))
    assert chroma_files

    collection = open_chroma(persist_dir, DummyEmbeddingFunction())
    assert collection.count() == 8

    result = collection.query(
        query_texts=["jornada de trabalho no comercio"],
        n_results=3,
    )

    assert result["documents"]
    assert result["metadatas"]
    assert result["metadatas"][0][0]["source"] == settings.pdf_path.name
    assert "page" in result["metadatas"][0][0]
