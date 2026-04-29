#!/usr/bin/env bash
set -euo pipefail

MODEL="${1:-gemma4:e4b}"

echo "[pull] Baixando modelo no container Ollama: ${MODEL}"
docker compose exec ollama ollama pull "${MODEL}"
echo "[pull] Modelo pronto: ${MODEL}"
