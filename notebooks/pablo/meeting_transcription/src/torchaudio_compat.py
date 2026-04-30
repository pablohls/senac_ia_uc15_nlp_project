from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import torchaudio


@dataclass(frozen=True)
class _FallbackAudioMetaData:
    sample_rate: int
    num_frames: int
    num_channels: int
    bits_per_sample: int = 0
    encoding: str = "UNKNOWN"


def _fallback_info(path: str | Path, *args: Any, **kwargs: Any) -> _FallbackAudioMetaData:
    waveform, sample_rate = torchaudio.load(str(path))
    num_channels = int(waveform.shape[0]) if waveform.ndim >= 1 else 1
    num_frames = int(waveform.shape[-1]) if waveform.ndim >= 1 else 0
    return _FallbackAudioMetaData(
        sample_rate=sample_rate,
        num_frames=num_frames,
        num_channels=num_channels,
    )


def ensure_torchaudio_compat() -> None:
    """Adiciona APIs removidas do torchaudio usadas por pyannote/whisperx."""
    if not hasattr(torchaudio, "AudioMetaData"):
        torchaudio.AudioMetaData = _FallbackAudioMetaData  # type: ignore[attr-defined]

    if not hasattr(torchaudio, "list_audio_backends"):
        torchaudio.list_audio_backends = lambda: ["compat"]  # type: ignore[attr-defined]

    if not hasattr(torchaudio, "get_audio_backend"):
        torchaudio.get_audio_backend = lambda: "compat"  # type: ignore[attr-defined]

    if not hasattr(torchaudio, "set_audio_backend"):
        torchaudio.set_audio_backend = lambda backend: None  # type: ignore[attr-defined]

    if not hasattr(torchaudio, "info"):
        torchaudio.info = _fallback_info  # type: ignore[attr-defined]
