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
        raise ValueError(f"Variável de ambiente {name!r} deve ser um inteiro.") from exc


def _read_optional_int_env(name: str) -> int | None:
    raw_value = os.getenv(name)
    if raw_value is None:
        return None
    try:
        return int(raw_value)
    except ValueError as exc:
        raise ValueError(f"Variável de ambiente {name!r} deve ser um inteiro.") from exc


def _project_root() -> Path:
    return Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Settings:
    project_root: Path
    audio_dir: Path
    output_dir: Path
    whisper_model: str
    language: str
    hf_token: str | None
    num_speakers: int | None
    min_speakers: int | None
    max_speakers: int | None


def build_settings() -> Settings:
    project_root = Path(os.getenv("PROJECT_ROOT", _project_root())).resolve()

    return Settings(
        project_root=project_root,
        audio_dir=Path(
            os.getenv("AUDIO_DIR", project_root / "data" / "audio")
        ).resolve(),
        output_dir=Path(
            os.getenv("OUTPUT_DIR", project_root / "data" / "output")
        ).resolve(),
        whisper_model=os.getenv("WHISPER_MODEL", "large-v3"),
        language=os.getenv("WHISPER_LANGUAGE", "pt"),
        hf_token=os.getenv("HF_TOKEN"),
        num_speakers=_read_optional_int_env("NUM_SPEAKERS"),
        min_speakers=_read_optional_int_env("MIN_SPEAKERS"),
        max_speakers=_read_optional_int_env("MAX_SPEAKERS"),
    )


settings = build_settings()
