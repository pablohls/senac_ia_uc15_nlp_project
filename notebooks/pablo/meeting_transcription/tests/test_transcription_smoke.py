from __future__ import annotations

import pytest
import numpy as np
import torch
from unittest.mock import MagicMock, patch


def test_transcribe_audio_raises_on_missing_file():
    from src.transcription import transcribe_audio

    with pytest.raises(FileNotFoundError):
        transcribe_audio(audio_path="/nao/existe.mp3")


def test_transcribe_audio_normalizes_transformers_output(tmp_path):
    """Verifica que transcribe_audio converte a saída do Transformers para segments."""
    from src.transcription import transcribe_audio

    audio_file = tmp_path / "audio.wav"
    audio_file.write_bytes(b"\x00" * 100)

    fake_generated = {
        "sequences": torch.tensor([[101, 102, 103]]),
        "segments": [
            [
                {"start": 0.0, "end": 1.0, "tokens": torch.tensor([11, 12])},
                {"start": 1.0, "end": 2.5, "tokens": torch.tensor([13, 14])},
            ]
        ],
    }

    with (
        patch("src.transcription.sf.read", return_value=(np.array([0.1, 0.2, 0.3]), 16000)),
        patch("src.transcription.AutoModelForSpeechSeq2Seq.from_pretrained") as mock_model_loader,
        patch("src.transcription.AutoProcessor.from_pretrained") as mock_processor_loader,
        patch("src.transcription.torch.cuda.is_available", return_value=False),
    ):
        mock_model = MagicMock()
        mock_model.generate.return_value = fake_generated
        mock_model_loader.return_value = mock_model

        mock_processor = MagicMock()
        mock_inputs = MagicMock()
        mock_inputs.input_features = torch.tensor([[1.0, 2.0]])
        mock_inputs.get.return_value = torch.tensor([[1, 1]])
        mock_processor.return_value = mock_inputs
        mock_processor.batch_decode.side_effect = [
            ["Oi"],
            ["mundo"],
            ["Oi mundo"],
        ]
        mock_processor_loader.return_value = mock_processor

        result = transcribe_audio(audio_path=audio_file, model_name="tiny", language="pt")

    assert "segments" in result
    assert result["segments"][0]["text"] == "Oi"
    assert result["segments"][1]["end"] == 2.5
    assert result["language"] == "pt"
    assert result["text"] == "Oi mundo"
