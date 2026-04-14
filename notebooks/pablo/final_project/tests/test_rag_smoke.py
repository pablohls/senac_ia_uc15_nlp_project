from __future__ import annotations

from requests import ConnectionError

from src.prompts import INSUFFICIENT_EVIDENCE_MESSAGE, RAG_SYSTEM_PROMPT, build_rag_prompt
from src.rag import RAGService
from src.retrieval import RetrievedChunk


class StubRetriever:
    def __init__(self, chunks: list[RetrievedChunk]):
        self.chunks = chunks
        self.calls: list[tuple[str, int | None]] = []

    def retrieve(self, query: str, k: int | None = None) -> list[RetrievedChunk]:
        self.calls.append((query, k))
        return self.chunks


def _chunk(
    *,
    text: str,
    score: float = 0.8,
    page: int = 1,
    source: str = "sindilojas_2025_2026.pdf",
    chunk_id: str = "1-1",
) -> RetrievedChunk:
    return RetrievedChunk(
        text=text,
        score=score,
        page=page,
        source=source,
        chunk_id=chunk_id,
        metadata={"page": page, "source": source, "chunk_id": chunk_id},
    )


def test_build_rag_prompt_includes_query_and_context():
    prompt = build_rag_prompt(
        "Como funciona o aviso previo?",
        [
            _chunk(
                text="O aviso previo deve respeitar as regras da convencao coletiva.",
                page=13,
                chunk_id="13-1",
            )
        ],
    )

    assert "Como funciona o aviso previo?" in prompt
    assert "Contexto recuperado do documento:" in prompt
    assert "chunk_id: 13-1" in prompt
    assert "page: 13" in prompt


def test_rag_service_returns_answer_and_sources_with_mocked_ollama():
    captured: dict[str, object] = {}
    retriever = StubRetriever(
        [
            _chunk(
                text="O aviso previo esta previsto na convencao coletiva e deve seguir as regras aplicaveis.",
                score=0.83,
                page=13,
                chunk_id="13-1",
            ),
            _chunk(
                text="A convencao coletiva descreve detalhes complementares do aviso previo.",
                score=0.8,
                page=14,
                chunk_id="14-2",
            ),
        ]
    )

    def fake_generate(base_url, model, prompt, *, system=None, options=None, timeout=120):
        captured["base_url"] = base_url
        captured["model"] = model
        captured["prompt"] = prompt
        captured["system"] = system
        return {"response": "Resposta: O aviso previo deve seguir as regras previstas na convencao coletiva."}

    service = RAGService(retriever=retriever, generate_fn=fake_generate, max_sources=3)
    result = service.answer("Como funciona o aviso previo?")

    assert retriever.calls == [("Como funciona o aviso previo?", 5)]
    assert result["answer"] == "O aviso previo deve seguir as regras previstas na convencao coletiva."
    assert len(result["sources"]) == 2
    assert result["sources"][0]["page"] == 13
    assert result["sources"][0]["source"] == "sindilojas_2025_2026.pdf"
    assert result["sources"][0]["chunk_id"] == "13-1"
    assert captured["system"] == RAG_SYSTEM_PROMPT
    assert "Como funciona o aviso previo?" in str(captured["prompt"])


def test_rag_service_returns_insufficient_evidence_without_calling_ollama():
    retriever = StubRetriever(
        [
            _chunk(
                text="A convencao coletiva trata de jornadas, pisos e beneficios da categoria.",
                score=0.7,
                page=9,
                chunk_id="9-1",
            ),
            _chunk(
                text="Ha regras sobre contribuicoes e acordos coletivos no documento.",
                score=0.69,
                page=10,
                chunk_id="10-2",
            ),
        ]
    )

    def should_not_run(*args, **kwargs):
        raise AssertionError("Ollama should not be called without sufficient evidence.")

    service = RAGService(retriever=retriever, generate_fn=should_not_run)
    result = service.answer("Quem ganhou a copa do mundo de 2022?")

    assert result == {"answer": INSUFFICIENT_EVIDENCE_MESSAGE, "sources": []}


def test_rag_service_propagates_ollama_connectivity_failures():
    retriever = StubRetriever(
        [
            _chunk(
                text="A convencao coletiva estabelece regras para aviso previo e rescisao.",
                score=0.84,
                page=15,
                chunk_id="15-1",
            ),
            _chunk(
                text="O aviso previo segue as previsoes da convencao coletiva.",
                score=0.81,
                page=16,
                chunk_id="16-1",
            ),
        ]
    )

    def failing_generate(*args, **kwargs):
        raise ConnectionError("localhost:11434 unavailable")

    service = RAGService(retriever=retriever, generate_fn=failing_generate)

    try:
        service.answer("Como funciona o aviso previo?")
    except ConnectionError as exc:
        assert "localhost:11434" in str(exc)
    else:
        raise AssertionError("RAGService should fail explicitly when Ollama is unavailable.")


def test_rag_service_limits_sources_to_five():
    retriever = StubRetriever(
        [
            _chunk(
                text=f"A convencao coletiva descreve a vigencia no trecho {index}.",
                score=0.9 - (index * 0.01),
                page=20 + index,
                chunk_id=f"{20 + index}-1",
            )
            for index in range(6)
        ]
    )

    def fake_generate(*args, **kwargs):
        return {"response": "A vigencia esta descrita na convencao coletiva."}

    service = RAGService(retriever=retriever, generate_fn=fake_generate, max_sources=5)
    result = service.answer("Qual e a vigencia da convencao coletiva?")

    assert len(result["sources"]) == 5
