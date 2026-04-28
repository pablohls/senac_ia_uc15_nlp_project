from __future__ import annotations

from pathlib import Path
from typing import Any

from langchain_core.documents import Document
from pypdf import PdfReader
from transformers import AutoTokenizer


def _normalize_text(text: str) -> str:
    return " ".join(text.replace("\x00", " ").split())


def _validate_chunking(chunk_size: int, chunk_overlap: int) -> None:
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero.")
    if chunk_overlap < 0:
        raise ValueError("chunk_overlap must be zero or greater.")
    if chunk_overlap >= chunk_size:
        raise ValueError("chunk_overlap must be smaller than chunk_size.")


def _next_chunk_end(text: str, start: int, chunk_size: int) -> int:
    target_end = min(len(text), start + chunk_size)
    if target_end == len(text):
        return target_end

    last_space = text.rfind(" ", start, target_end)
    if last_space <= start:
        return target_end
    return last_space


def load_pdf_pages(pdf_path: str | Path) -> list[dict[str, Any]]:
    path = Path(pdf_path)
    if not path.exists():
        raise FileNotFoundError(f"PDF file not found: {path}")

    reader = PdfReader(str(path))
    pages: list[dict[str, Any]] = []

    for page_number, page in enumerate(reader.pages, start=1):
        raw_text = page.extract_text() or ""
        pages.append(
            {
                "page": page_number,
                "text": _normalize_text(raw_text),
            }
        )

    return pages


def chunk_pages(
    pages: list[dict[str, Any]],
    chunk_size: int,
    chunk_overlap: int,
    source: str,
    tokenizer_name: str,
) -> list[Document]:
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
    _validate_chunking(chunk_size, chunk_overlap)

    documents: list[Document] = []

    for page_data in pages:
        page_number = int(page_data["page"])
        text = _normalize_text(str(page_data.get("text", "")))
        if not text:
            continue

        token_ids = tokenizer.encode(text, add_special_tokens=False)
        step = chunk_size - chunk_overlap
        chunk_index = 1

        for start in range(0, len(token_ids), step):
            window = token_ids[start : start + chunk_size]
            if not window:
                continue
            chunk_text = tokenizer.decode(window, skip_special_tokens=True).strip()
            if chunk_text:
                documents.append(
                    Document(
                        page_content=chunk_text,
                        metadata={
                            "source": source,
                            "page": page_number,
                            "chunk_id": f"{page_number}-{chunk_index}",},
                    ),
                )
            chunk_index += 1

        # start = 0
        # chunk_index = 1

        # while start < len(text):
        #     end = _next_chunk_end(text, start, chunk_size)
        #     chunk_text = text[start:end].strip()

        #     if chunk_text:
        #         documents.append(
        #             Document(
        #                 page_content=chunk_text,
        #                 metadata={
        #                     "source": source,
        #                     "page": page_number,
        #                     "chunk_id": f"{page_number}-{chunk_index}",
        #                 },
        #             )
        #         )

        #     if end >= len(text):
        #         break

        #     next_start = max(0, end - chunk_overlap)
        #     if next_start <= start:
        #         next_start = end

        #     start = next_start
        #     chunk_index += 1

    return documents
