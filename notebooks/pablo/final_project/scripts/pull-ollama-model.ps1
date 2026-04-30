param(
    [string]$Model = "gemma4:e4b"
)

$ErrorActionPreference = "Stop"

Write-Host "[pull] Baixando modelo no container Ollama: $Model"
docker compose exec ollama ollama pull $Model
Write-Host "[pull] Modelo pronto: $Model"
