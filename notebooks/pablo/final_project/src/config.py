from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


def _read_int_env(name: str, default: int) -> int:
    raw_value = os.getenv(name)
    if raw_value is None:
        return default
    try:
        return int(raw_value)
    except ValueError as exc:
        raise ValueError(f"Environment variable {name!r} must be an integer.") from exc


def _project_root() -> Path:
    return Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Settings:
    project_root: Path
    pdf_path: Path
    chroma_path: Path
    chroma_collection_name: str
    default_embedding_model: str
    default_ollama_base_url: str
    default_ollama_model: str
    tokenizer_name: str
    chunk_size: int
    chunk_overlap: int
    default_retrieval_k: int


def build_settings() -> Settings:
    project_root = Path(os.getenv("PROJECT_ROOT", _project_root())).resolve()
    pdf_path = Path(
        os.getenv("PDF_PATH", project_root / "data" / "pdf" / "sindilojas_2025_2026.pdf")
    ).resolve()
    chroma_path = Path(
        os.getenv("CHROMA_PATH", project_root / "data" / "chroma")
    ).resolve()

    return Settings(
        project_root=project_root,
        pdf_path=pdf_path,
        chroma_path=chroma_path,
        chroma_collection_name=os.getenv("CHROMA_COLLECTION_NAME", "sindilojas_pdf"),
        default_embedding_model=os.getenv(
            "EMBEDDING_MODEL",
            "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
        ),
        default_ollama_base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
        default_ollama_model=os.getenv("OLLAMA_MODEL", "qwen2.5:7b"),
        tokenizer_name=os.getenv(
            "TOKENIZER_NAME",
            "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
        ),
        chunk_size=_read_int_env("CHUNK_SIZE", 512),
        chunk_overlap=_read_int_env("CHUNK_OVERLAP", 20),
        default_retrieval_k=_read_int_env("RETRIEVAL_K", 5),
    )


settings = build_settings()
