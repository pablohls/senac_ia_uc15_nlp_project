from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from chromadb.api.models.Collection import Collection
from chromadb.api.types import Documents, EmbeddingFunction

from src.config import settings
from src.indexing import build_embeddings, open_chroma


@dataclass(frozen=True)
class RetrievedChunk:
    text: str
    score: float
    page: int
    source: str
    chunk_id: str
    metadata: dict[str, Any]


def _distance_to_similarity(distance: float) -> float:
    return max(0.0, min(1.0, 1.0 - (distance / 2.0)))


class RetrieverService:
    def __init__(
        self,
        *,
        persist_dir: str | Path | None = None,
        model_name: str | None = None,
        default_k: int | None = None,
        embeddings: EmbeddingFunction[Documents] | None = None,
        collection: Collection | None = None,
    ) -> None:
        self.persist_dir = Path(settings.chroma_path if persist_dir is None else persist_dir)
        self.model_name = settings.default_embedding_model if model_name is None else model_name
        self.default_k = settings.default_retrieval_k if default_k is None else default_k
        self._embeddings = embeddings
        self._collection = collection

    @property
    def embeddings(self) -> EmbeddingFunction[Documents]:
        if self._embeddings is None:
            self._embeddings = build_embeddings(self.model_name)
        return self._embeddings

    @property
    def collection(self) -> Collection:
        if self._collection is None:
            self._collection = open_chroma(self.persist_dir, self.embeddings)
        return self._collection

    def retrieve(self, query: str, k: int | None = None) -> list[RetrievedChunk]:
        normalized_query = query.strip()
        if not normalized_query:
            raise ValueError("query must not be empty.")

        limit = k if k is not None else self.default_k
        if limit <= 0:
            raise ValueError("k must be greater than zero.")

        result = self.collection.query(
            query_texts=[normalized_query],
            n_results=limit,
            include=["documents", "metadatas", "distances"],
        )

        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]

        retrieved_chunks: list[RetrievedChunk] = []
        for text, metadata, distance in zip(documents, metadatas, distances):
            chunk_metadata = dict(metadata or {})
            retrieved_chunks.append(
                RetrievedChunk(
                    text=text,
                    score=_distance_to_similarity(float(distance)),
                    page=int(chunk_metadata["page"]),
                    source=str(chunk_metadata["source"]),
                    chunk_id=str(chunk_metadata["chunk_id"]),
                    metadata=chunk_metadata,
                )
            )

        return retrieved_chunks
