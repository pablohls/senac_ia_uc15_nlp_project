from __future__ import annotations

import pytest
from pathlib import Path
from unittest.mock import MagicMock, patch


def test_diarize_audio_raises_on_missing_file():
    from src.diarization import diarize_audio

    with pytest.raises(FileNotFoundError):
        diarize_audio(audio_path="/nao/existe.mp3", hf_token="fake_token")


def test_diarize_audio_raises_on_empty_token(tmp_path):
    from src.diarization import diarize_audio

    audio_file = tmp_path / "audio.wav"
    audio_file.write_bytes(b"\x00" * 100)

    with pytest.raises(ValueError, match="HF_TOKEN"):
        diarize_audio(audio_path=audio_file, hf_token="")


def test_diarize_audio_calls_pipeline(tmp_path):
    from src.diarization import diarize_audio

    audio_file = tmp_path / "audio.wav"
    audio_file.write_bytes(b"\x00" * 100)

    fake_diarization = MagicMock()

    with (
        patch("pyannote.audio.Pipeline.from_pretrained") as mock_from_pretrained,
        patch("src.diarization.torch.cuda.is_available", return_value=False),
    ):
        mock_pipeline = MagicMock()
        mock_pipeline.return_value = fake_diarization
        mock_from_pretrained.return_value = mock_pipeline

        result = diarize_audio(
            audio_path=audio_file,
            hf_token="hf_fake",
            num_speakers=2,
        )

    mock_from_pretrained.assert_called_once_with(
        "pyannote/speaker-diarization-3.1", token="hf_fake"
    )
    mock_pipeline.to.assert_called_once()
    mock_pipeline.assert_called_once_with(str(audio_file), num_speakers=2)
    assert result is fake_diarization


def test_diarize_audio_forwards_min_max_speakers_when_num_not_set(tmp_path):
    from src.diarization import diarize_audio

    audio_file = tmp_path / "audio.wav"
    audio_file.write_bytes(b"\x00" * 100)

    with (
        patch("pyannote.audio.Pipeline.from_pretrained") as mock_from_pretrained,
        patch("src.diarization.torch.cuda.is_available", return_value=False),
    ):
        mock_pipeline = MagicMock()
        mock_from_pretrained.return_value = mock_pipeline

        diarize_audio(
            audio_path=audio_file,
            hf_token="hf_fake",
            min_speakers=1,
            max_speakers=3,
        )

    mock_pipeline.assert_called_once_with(
        str(audio_file), min_speakers=1, max_speakers=3
    )
