from __future__ import annotations

from unittest.mock import MagicMock


def _make_transcript_result():
    return {
        "segments": [
            {"start": 0.0, "end": 2.0, "text": "Bom dia a todos."},
            {"start": 2.5, "end": 5.0, "text": "Vamos começar a reunião."},
        ],
        "language": "pt",
    }


def _make_diarization(turns):
    diarization = MagicMock()
    diarization.itertracks.return_value = turns
    return diarization


def test_assign_speakers_picks_largest_overlap():
    from src.alignment import assign_speakers

    transcript_result = {
        "segments": [
            {"start": 0.0, "end": 5.0, "text": "Trecho com overlap maior no speaker 01."}
        ]
    }
    diarization = _make_diarization(
        [
            (MagicMock(start=0.0, end=1.0), "track0", "SPEAKER_00"),
            (MagicMock(start=1.0, end=4.0), "track1", "SPEAKER_01"),
        ]
    )

    segments = assign_speakers(transcript_result, diarization=diarization)

    assert len(segments) == 1
    assert segments[0].speaker == "SPEAKER_01"


def test_assign_speakers_uses_unknown_when_no_overlap():
    from src.alignment import assign_speakers

    transcript_result = {
        "segments": [
            {"start": 10.0, "end": 12.0, "text": "Sem sobreposição."},
        ]
    }
    diarization = _make_diarization(
        [(MagicMock(start=0.0, end=2.0), "track0", "SPEAKER_00")]
    )

    segments = assign_speakers(transcript_result, diarization=diarization)

    assert segments[0].speaker == "SPEAKER_UNKNOWN"


def test_assign_speakers_skips_empty_text():
    from src.alignment import assign_speakers

    transcript_result = {
        "segments": [
            {"start": 0.0, "end": 1.0, "text": ""},
            {"start": 1.0, "end": 2.0, "text": "  "},
            {"start": 2.0, "end": 3.0, "text": "Olá!"},
        ]
    }
    diarization = _make_diarization(
        [(MagicMock(start=2.0, end=3.0), "track1", "SPEAKER_01")]
    )

    segments = assign_speakers(transcript_result, diarization=diarization)

    assert len(segments) == 1
    assert segments[0].text == "Olá!"


def test_assign_speakers_returns_sorted_segments():
    from src.alignment import assign_speakers

    transcript_result = {
        "segments": [
            {"start": 2.5, "end": 5.0, "text": "Vamos começar a reunião."},
            {"start": 0.0, "end": 2.0, "text": "Bom dia a todos."},
        ]
    }
    diarization = _make_diarization(
        [
            (MagicMock(start=0.0, end=2.0), "track0", "SPEAKER_00"),
            (MagicMock(start=2.5, end=5.0), "track1", "SPEAKER_01"),
        ]
    )

    segments = assign_speakers(transcript_result, diarization=diarization)

    assert len(segments) == 2
    assert segments[0].start < segments[1].start
    assert segments[0].speaker == "SPEAKER_00"
    assert segments[1].speaker == "SPEAKER_01"
