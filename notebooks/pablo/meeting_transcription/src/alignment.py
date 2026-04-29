from __future__ import annotations

from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class TranscriptSegment:
    """Segmento de transcrição com speaker identificado."""

    speaker: str
    start: float
    end: float
    text: str


def assign_speakers(
    transcript_result: dict[str, Any],
    diarization: Any,
) -> list[TranscriptSegment]:
    """Atribui speakers aos segmentos de transcrição.

    Combina os segmentos de transcrição com os turns de diarização do pyannote
    e atribui o speaker por maior sobreposição temporal.

    Args:
        transcript_result: Dicionário retornado por ``transcribe_audio``,
            com a chave ``segments`` contendo os segmentos alinhados.
        diarization: ``pyannote.core.Annotation`` com os turns por speaker.

    Returns:
        Lista de ``TranscriptSegment`` ordenados por tempo de início.
    """
    turns: list[tuple[float, float, str]] = []
    for segment, _, label in diarization.itertracks(yield_label=True):
        turns.append((float(segment.start), float(segment.end), str(label)))

    segments: list[TranscriptSegment] = []
    for seg in transcript_result.get("segments", []):
        text = seg.get("text", "").strip()
        if not text:
            continue

        start = float(seg.get("start", 0.0))
        end = float(seg.get("end", 0.0))

        best_speaker = "SPEAKER_UNKNOWN"
        best_overlap = 0.0
        for turn_start, turn_end, turn_label in turns:
            overlap = max(0.0, min(end, turn_end) - max(start, turn_start))
            if overlap > best_overlap:
                best_overlap = overlap
                best_speaker = turn_label

        segments.append(
            TranscriptSegment(
                speaker=best_speaker,
                start=start,
                end=end,
                text=text,
            )
        )

    return sorted(segments, key=lambda s: s.start)
