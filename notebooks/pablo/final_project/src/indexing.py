from __future__ import annotations

import shutil
from pathlib import Path
from typing import Sequence

import chromadb
from chromadb.api.models.Collection import Collection
from chromadb.api.types import Documents, EmbeddingFunction, Embeddings
from langchain_core.documents import Document
from sentence_transformers import SentenceTransformer

from src.config import settings


class SentenceTransformerEmbeddingFunction(EmbeddingFunction[Documents]):
    def __init__(self, model_name: str, model: SentenceTransformer):
        self.model_name = model_name
        self.model = model

    def __call__(self, input: Documents) -> Embeddings:
        vectors = self.model.encode(list(input), convert_to_numpy=True, normalize_embeddings=True)
        if hasattr(vectors, "tolist"):
            return vectors.tolist()
        return [list(vector) for vector in vectors]

    def name(self) -> str:
        return f"sentence-transformer::{self.model_name}"

    def get_config(self) -> dict[str, str]:
        return {"model_name": self.model_name}

    @staticmethod
    def build_from_config(config: dict[str, str]) -> "SentenceTransformerEmbeddingFunction":
        return build_embeddings(config["model_name"])


def build_embeddings(model_name: str) -> SentenceTransformerEmbeddingFunction:
    model = SentenceTransformer(model_name)
    return SentenceTransformerEmbeddingFunction(model_name, model)


def _client_for_path(persist_dir: str | Path) -> chromadb.ClientAPI:
    path = Path(persist_dir)
    path.mkdir(parents=True, exist_ok=True)
    return chromadb.PersistentClient(path=str(path))


def _documents_to_payload(docs: Sequence[Document]) -> tuple[list[str], list[str], list[dict]]:
    ids: list[str] = []
    texts: list[str] = []
    metadatas: list[dict] = []

    for doc in docs:
        chunk_id = str(doc.metadata["chunk_id"])
        ids.append(chunk_id)
        texts.append(doc.page_content)
        metadatas.append(dict(doc.metadata))

    return ids, texts, metadatas


def rebuild_chroma(
    docs: Sequence[Document],
    persist_dir: str | Path,
    embeddings: EmbeddingFunction[Documents],
) -> Collection:
    persist_path = Path(persist_dir)
    if persist_path.exists():
        shutil.rmtree(persist_path)

    client = _client_for_path(persist_path)
    collection = client.create_collection(
        name=settings.chroma_collection_name,
        embedding_function=embeddings,
        metadata={"hnsw:space": "cosine"},
    )

    if docs:
        ids, texts, metadatas = _documents_to_payload(docs)
        collection.add(
            ids=ids,
            documents=texts,
            metadatas=metadatas,
        )

    return collection


def open_chroma(
    persist_dir: str | Path,
    embeddings: EmbeddingFunction[Documents],
) -> Collection:
    client = _client_for_path(persist_dir)
    return client.get_collection(
        name=settings.chroma_collection_name,
        embedding_function=embeddings,
    )
