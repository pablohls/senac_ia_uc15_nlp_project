from __future__ import annotations

from dataclasses import replace

from sentence_transformers import CrossEncoder

from src.retrieval import RetrievedChunk


class RerankerService:
    def __init__(self, model_name: str, top_n: int = 5) -> None:
        if top_n <= 0:
            raise ValueError("top_n must be greater than zero.")
        self.model_name = model_name
        self.top_n = top_n
        self.model = CrossEncoder(model_name)

    def rerank(self, query: str, chunks: list[RetrievedChunk]) -> list[RetrievedChunk]:
        normalized_query = query.strip()
        if not normalized_query:
            raise ValueError("query must not be empty.")
        if not chunks:
            return []

        pairs = [(normalized_query, chunk.text) for chunk in chunks]
        raw_scores = self.model.predict(pairs)
        scored_chunks = []

        for chunk, raw_score in zip(chunks, raw_scores):
            score = float(raw_score)
            scored_chunks.append(
                replace(
                    chunk,
                    metadata={**chunk.metadata, "rerank_score": score},
                )
            )

        scored_chunks.sort(key=lambda chunk: float(chunk.metadata["rerank_score"]), reverse=True)
        return scored_chunks[: self.top_n]
