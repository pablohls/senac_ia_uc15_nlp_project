from __future__ import annotations

import pytest
from pathlib import Path
from unittest.mock import MagicMock, patch

from src.alignment import TranscriptSegment


FAKE_SEGMENTS = [
    TranscriptSegment(speaker="SPEAKER_00", start=0.0, end=2.0, text="Olá!"),
    TranscriptSegment(speaker="SPEAKER_01", start=2.5, end=5.0, text="Tudo certo."),
]


def _make_fake_config(tmp_path: Path, hf_token: str = "hf_fake"):
    from src.config import Settings

    return Settings(
        project_root=tmp_path,
        audio_dir=tmp_path / "audio",
        output_dir=tmp_path / "output",
        whisper_model="tiny",
        language="pt",
        hf_token=hf_token,
        num_speakers=None,
        min_speakers=None,
        max_speakers=None,
    )


def test_run_pipeline_raises_on_missing_audio(tmp_path):
    from src.pipeline import run_pipeline

    cfg = _make_fake_config(tmp_path)

    with pytest.raises(FileNotFoundError):
        run_pipeline(audio_path=tmp_path / "nao_existe.mp3", config=cfg)


def test_run_pipeline_end_to_end(tmp_path):
    from src.pipeline import run_pipeline

    cfg = _make_fake_config(tmp_path)

    audio_file = tmp_path / "audio" / "test.wav"
    audio_file.parent.mkdir(parents=True)
    audio_file.write_bytes(b"\x00" * 100)

    fake_transcript = {"segments": [], "language": "pt"}
    fake_diarization = MagicMock()

    with (
        patch("src.pipeline.transcribe_audio", return_value=fake_transcript),
        patch("src.pipeline.diarize_audio", return_value=fake_diarization),
        patch("src.pipeline.assign_speakers", return_value=FAKE_SEGMENTS),
    ):
        result = run_pipeline(audio_path=audio_file, config=cfg)

    assert "md" in result
    assert "pdf" in result
    assert "segments" in result
    assert result["md"].exists()
    assert result["pdf"].exists()
    assert result["segments"] == FAKE_SEGMENTS
