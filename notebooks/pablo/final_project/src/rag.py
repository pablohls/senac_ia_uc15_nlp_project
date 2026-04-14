from __future__ import annotations

import re
import unicodedata
from typing import Any, Callable

from src.config import settings
from src.prompts import INSUFFICIENT_EVIDENCE_MESSAGE, RAG_SYSTEM_PROMPT, build_rag_prompt
from src.retrieval import RetrievedChunk, RetrieverService
from src.utils_ollama import ollama_generate


OLLAMA_GENERATE_FN = Callable[..., dict[str, Any]]
STOPWORDS = {
    "a",
    "as",
    "o",
    "os",
    "e",
    "de",
    "da",
    "do",
    "das",
    "dos",
    "um",
    "uma",
    "em",
    "no",
    "na",
    "nos",
    "nas",
    "para",
    "por",
    "com",
    "sem",
    "que",
    "qual",
    "quais",
    "como",
    "sobre",
    "fala",
    "documento",
    "funciona",
    "quem",
    "onde",
    "quando",
}


def _normalize_text(text: str) -> str:
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii").lower()


def _query_terms(query: str) -> list[str]:
    normalized = _normalize_text(query)
    return [
        token
        for token in re.findall(r"[a-z0-9]+", normalized)
        if len(token) >= 3 and token not in STOPWORDS
    ]


def _has_sufficient_evidence(query: str, chunks: list[RetrievedChunk]) -> bool:
    if not chunks:
        return False

    query_terms = _query_terms(query)
    if not query_terms:
        return chunks[0].score >= 0.8

    normalized_context = _normalize_text(" ".join(chunk.text for chunk in chunks))
    matched_terms = sum(
        bool(re.search(rf"\b{re.escape(term)}\b", normalized_context)) for term in query_terms
    )
    bigrams = [" ".join(query_terms[index : index + 2]) for index in range(len(query_terms) - 1)]
    matched_bigrams = [bigram for bigram in bigrams if bigram in normalized_context]
    top_score = chunks[0].score

    if matched_bigrams:
        return True
    if matched_terms >= 2 and top_score >= 0.7:
        return True
    if len(query_terms) == 1 and matched_terms == 1 and top_score >= 0.8:
        return True

    return False


def _build_sources(chunks: list[RetrievedChunk], *, max_sources: int) -> list[dict[str, Any]]:
    sources: list[dict[str, Any]] = []
    for chunk in chunks[:max_sources]:
        sources.append(
            {
                "page": chunk.page,
                "source": chunk.source,
                "chunk_id": chunk.chunk_id,
                "score": round(chunk.score, 3),
                "snippet": chunk.text[:280].strip(),
            }
        )
    return sources


def _clean_answer(text: str) -> str:
    cleaned = text.strip()
    cleaned = re.sub(r"^\s*resposta:\s*", "", cleaned, flags=re.IGNORECASE)
    return cleaned.strip()


class RAGService:
    def __init__(
        self,
        *,
        retriever: RetrieverService | None = None,
        ollama_base_url: str | None = None,
        ollama_model: str | None = None,
        retrieval_k: int = 5,
        max_sources: int = 5,
        generate_fn: OLLAMA_GENERATE_FN = ollama_generate,
    ) -> None:
        self.retriever = RetrieverService() if retriever is None else retriever
        self.ollama_base_url = (
            settings.default_ollama_base_url if ollama_base_url is None else ollama_base_url
        )
        self.ollama_model = settings.default_ollama_model if ollama_model is None else ollama_model
        self.retrieval_k = retrieval_k
        self.max_sources = max(2, min(5, max_sources))
        self.generate_fn = generate_fn

    def answer(self, query: str) -> dict[str, Any]:
        normalized_query = query.strip()
        if not normalized_query:
            raise ValueError("query must not be empty.")

        retrieved_chunks = self.retriever.retrieve(normalized_query, k=self.retrieval_k)
        if not _has_sufficient_evidence(normalized_query, retrieved_chunks):
            return {
                "answer": INSUFFICIENT_EVIDENCE_MESSAGE,
                "sources": [],
            }

        context_chunks = retrieved_chunks[: self.max_sources]
        prompt = build_rag_prompt(normalized_query, context_chunks)
        response = self.generate_fn(
            self.ollama_base_url,
            self.ollama_model,
            prompt,
            system=RAG_SYSTEM_PROMPT,
        )
        answer = _clean_answer(str(response["response"]))
        if not answer:
            raise ValueError("Ollama returned an empty answer.")

        return {
            "answer": answer,
            "sources": _build_sources(context_chunks, max_sources=self.max_sources),
        }
