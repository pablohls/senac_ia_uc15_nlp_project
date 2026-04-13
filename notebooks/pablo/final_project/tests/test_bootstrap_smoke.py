from pathlib import Path

from src.config import build_settings
from src.utils_ollama import ollama_generate, ollama_tags


class DummyResponse:
    def __init__(self, payload):
        self.payload = payload

    def raise_for_status(self) -> None:
        return None

    def json(self):
        return self.payload


def test_build_settings_uses_expected_defaults(monkeypatch):
    for env_var in (
        "PROJECT_ROOT",
        "PDF_PATH",
        "CHROMA_PATH",
        "EMBEDDING_MODEL",
        "OLLAMA_BASE_URL",
        "OLLAMA_MODEL",
        "CHUNK_SIZE",
        "CHUNK_OVERLAP",
        "RETRIEVAL_K",
    ):
        monkeypatch.delenv(env_var, raising=False)

    settings = build_settings()

    assert settings.project_root == Path(__file__).resolve().parents[1]
    assert settings.pdf_path == settings.project_root / "data" / "pdf" / "sindilojas_2025_2026.pdf"
    assert settings.chroma_path == settings.project_root / "data" / "chroma"
    assert settings.chroma_collection_name == "sindilojas_pdf"
    assert settings.default_ollama_model == "qwen2.5:7b"
    assert settings.chunk_size == 1200
    assert settings.chunk_overlap == 200


def test_ollama_tags_returns_json_object(monkeypatch):
    def fake_get(url, timeout):
        assert url == "http://localhost:11434/api/tags"
        assert timeout == 10
        return DummyResponse({"models": []})

    monkeypatch.setattr("src.utils_ollama.requests.get", fake_get)

    assert ollama_tags("http://localhost:11434") == {"models": []}


def test_ollama_generate_returns_json_object(monkeypatch):
    def fake_post(url, json, timeout):
        assert url == "http://localhost:11434/api/generate"
        assert json["model"] == "qwen2.5:7b"
        assert json["prompt"] == "Ola"
        assert json["stream"] is False
        assert json["system"] == "Responda em PT-BR."
        assert json["options"] == {"temperature": 0}
        assert timeout == 99
        return DummyResponse({"response": "Tudo certo."})

    monkeypatch.setattr("src.utils_ollama.requests.post", fake_post)

    response = ollama_generate(
        "http://localhost:11434",
        "qwen2.5:7b",
        "Ola",
        system="Responda em PT-BR.",
        options={"temperature": 0},
        timeout=99,
    )

    assert response == {"response": "Tudo certo."}
