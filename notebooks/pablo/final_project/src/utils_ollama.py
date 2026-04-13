from __future__ import annotations

from typing import Any

import requests


DEFAULT_CONNECT_TIMEOUT_SECONDS = 10
DEFAULT_GENERATE_TIMEOUT_SECONDS = 120


def _build_url(base_url: str, path: str) -> str:
    return f"{base_url.rstrip('/')}{path}"


def ollama_tags(base_url: str) -> dict[str, Any]:
    response = requests.get(
        _build_url(base_url, "/api/tags"),
        timeout=DEFAULT_CONNECT_TIMEOUT_SECONDS,
    )
    response.raise_for_status()

    payload = response.json()
    if not isinstance(payload, dict):
        raise ValueError("Ollama /api/tags must return a JSON object.")
    return payload


def ollama_generate(
    base_url: str,
    model: str,
    prompt: str,
    *,
    system: str | None = None,
    options: dict[str, Any] | None = None,
    timeout: int = DEFAULT_GENERATE_TIMEOUT_SECONDS,
) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "model": model,
        "prompt": prompt,
        "stream": False,
    }
    if system is not None:
        payload["system"] = system
    if options is not None:
        payload["options"] = options

    response = requests.post(
        _build_url(base_url, "/api/generate"),
        json=payload,
        timeout=timeout,
    )
    response.raise_for_status()

    data = response.json()
    if not isinstance(data, dict):
        raise ValueError("Ollama /api/generate must return a JSON object.")
    if "response" not in data:
        raise ValueError("Ollama /api/generate response did not include 'response'.")
    return data
