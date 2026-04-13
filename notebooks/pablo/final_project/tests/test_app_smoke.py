from __future__ import annotations

from pathlib import Path

from requests import ConnectionError
from streamlit.testing.v1 import AppTest

from app import OLLAMA_UNAVAILABLE_MESSAGE, ask_question
from src.prompts import INSUFFICIENT_EVIDENCE_MESSAGE


class StubRAGService:
    def __init__(self, result=None, error: Exception | None = None):
        self.result = result
        self.error = error
        self.calls: list[str] = []

    def answer(self, query: str):
        self.calls.append(query)
        if self.error is not None:
            raise self.error
        return self.result


def test_ask_question_returns_success_payload():
    service = StubRAGService(
        result={
            "answer": "A vigencia esta descrita na convencao coletiva.",
            "sources": [
                {
                    "page": 24,
                    "source": "sindilojas_2025_2026.pdf",
                    "chunk_id": "24-2",
                    "score": 0.822,
                    "snippet": "Convencao coletiva...",
                }
            ],
        }
    )

    status, payload = ask_question("Qual e a vigencia da convencao coletiva?", service)

    assert status == "success"
    assert isinstance(payload, dict)
    assert payload["answer"] == "A vigencia esta descrita na convencao coletiva."
    assert service.calls == ["Qual e a vigencia da convencao coletiva?"]


def test_ask_question_returns_warning_for_blank_query():
    service = StubRAGService(result={})

    status, payload = ask_question("   ", service)

    assert status == "warning"
    assert "Digite uma pergunta" in str(payload)
    assert service.calls == []


def test_ask_question_returns_explicit_error_for_ollama_failure():
    service = StubRAGService(error=ConnectionError("localhost:11434 unavailable"))

    status, payload = ask_question("Como funciona o aviso previo?", service)

    assert status == "error"
    assert OLLAMA_UNAVAILABLE_MESSAGE in str(payload)
    assert "localhost:11434" in str(payload)


def test_streamlit_app_renders_base_ui():
    app_path = Path(__file__).resolve().parents[1] / "app.py"

    at = AppTest.from_file(str(app_path))
    at.run()

    assert at.title[0].value == "Consulta RAG do PDF"
    assert at.text_input[0].label == "Pergunta"
    assert at.button[0].label == "Perguntar"


def test_ask_question_returns_success_for_insufficient_evidence_message():
    service = StubRAGService(
        result={
            "answer": INSUFFICIENT_EVIDENCE_MESSAGE,
            "sources": [],
        }
    )

    status, payload = ask_question("Quem ganhou a copa do mundo de 2022?", service)

    assert status == "success"
    assert isinstance(payload, dict)
    assert payload["answer"] == INSUFFICIENT_EVIDENCE_MESSAGE
    assert payload["sources"] == []
