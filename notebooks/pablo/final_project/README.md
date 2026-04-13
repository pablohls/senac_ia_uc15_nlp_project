# RAG local com PDF, Chroma, Ollama e Streamlit

Projeto em Python para consultar um PDF local com:

- ingestao e chunking do documento
- indexacao persistente no Chroma
- retrieval com score normalizado
- RAG com Ollama
- interface Streamlit

## Estado da v1

O subprojeto cobre:

- **M0**: bootstrap, configuracao e utilitarios de Ollama
- **M1**: ingestao do PDF e chunking
- **M2**: indexacao persistente no Chroma
- **M3**: retrieval sobre o indice persistido
- **M4**: RAG com resposta em PT-BR e fontes
- **M5**: interface Streamlit

## Estrutura

```text
.
|-- app.py
|-- data/
|   |-- chroma/
|   `-- pdf/
|-- notebooks/
|   |-- 01_ingest_and_index.ipynb
|   `-- 02_query_rag.ipynb
|-- specs/
|-- src/
|-- tests/
|-- README.md
`-- requirements.txt
```

> Este subprojeto usa o ambiente do Poetry definido na raiz do repositorio.

## Setup

1. Na raiz do repositorio, instale as dependencias:

   ```bash
   poetry install
   ```

2. Inicie o Ollama:

   ```bash
   ollama serve
   ```

3. Baixe o modelo padrao:

   ```bash
   ollama pull qwen2.5:7b
   ```

4. Garanta que o PDF esteja em:

   ```text
   data/pdf/sindilojas_2025_2026.pdf
   ```

## Configuracao

Os defaults ficam em `src/config.py` e podem ser sobrescritos por variaveis de ambiente:

- `PROJECT_ROOT`
- `PDF_PATH`
- `CHROMA_PATH`
- `CHROMA_COLLECTION_NAME`
- `EMBEDDING_MODEL`
- `OLLAMA_BASE_URL`
- `OLLAMA_MODEL`
- `CHUNK_SIZE`
- `CHUNK_OVERLAP`
- `RETRIEVAL_K`

## Fluxo recomendado

Os comandos abaixo assumem que voce esta na **raiz do repositorio** e usam o Poetry desse diretorio.

Para evitar problemas de import no subprojeto, os exemplos executam um shell no ambiente do Poetry e entram em `notebooks/pablo/final_project/`.

### 1. Validar configuracao basica

```bash
REPO_ROOT="$(git rev-parse --show-toplevel)"
poetry -C "$REPO_ROOT" run bash -lc 'cd "$0/notebooks/pablo/final_project" && PYTHONPATH=. python -c "from src.config import settings; print(settings)"' "$REPO_ROOT"
```

### 2. Ingerir e indexar o PDF

```bash
REPO_ROOT="$(git rev-parse --show-toplevel)"
poetry -C "$REPO_ROOT" run bash -lc 'cd "$0/notebooks/pablo/final_project" && PYTHONPATH=. python - <<'"'"'PY'"'"'
from src.config import settings
from src.indexing import build_embeddings, rebuild_chroma
from src.ingestion import chunk_pages, load_pdf_pages

pages = load_pdf_pages(settings.pdf_path)
chunks = chunk_pages(
    pages,
    chunk_size=settings.chunk_size,
    chunk_overlap=settings.chunk_overlap,
    source=settings.pdf_path.name,
)
embeddings = build_embeddings(settings.default_embedding_model)
collection = rebuild_chroma(chunks, settings.chroma_path, embeddings)
print(f"pages={len(pages)}")
print(f"chunks={len(chunks)}")
print(f"indexed={collection.count()}")
PY' "$REPO_ROOT"
```

### 3. Consultar o retrieval

```bash
REPO_ROOT="$(git rev-parse --show-toplevel)"
poetry -C "$REPO_ROOT" run bash -lc 'cd "$0/notebooks/pablo/final_project" && PYTHONPATH=. python - <<'"'"'PY'"'"'
from src.retrieval import RetrieverService

retriever = RetrieverService()
results = retriever.retrieve("qual e a vigencia da convencao coletiva?", k=3)

for chunk in results:
    print(chunk.score, chunk.page, chunk.source, chunk.chunk_id)
    print(chunk.text[:200])
    print("-" * 80)
PY' "$REPO_ROOT"
```

O `score` do retrieval e uma similaridade normalizada entre `0` e `1`.

### 4. Consultar o RAG

```bash
REPO_ROOT="$(git rev-parse --show-toplevel)"
poetry -C "$REPO_ROOT" run bash -lc 'cd "$0/notebooks/pablo/final_project" && PYTHONPATH=. python - <<'"'"'PY'"'"'
from src.rag import RAGService

rag = RAGService()
result = rag.answer("Qual e a vigencia da convencao coletiva?")

print(result["answer"])
print("\nFontes:")
for source in result["sources"]:
    print(source)
PY' "$REPO_ROOT"
```

Se nao houver evidencia suficiente no documento, o sistema responde explicitamente com essa mensagem. Se o Ollama nao estiver acessivel, o fluxo falha explicitamente.

### 5. Subir a interface Streamlit

```bash
REPO_ROOT="$(git rev-parse --show-toplevel)"
poetry -C "$REPO_ROOT" run bash -lc 'cd "$0/notebooks/pablo/final_project" && PYTHONPATH=. streamlit run app.py --server.address 0.0.0.0 --server.port 8501' "$REPO_ROOT"
```

A UI exibe:

- campo de pergunta
- resposta em PT-BR
- expander com fontes
- pagina, origem, chunk, score e snippet para cada fonte

## Notebooks

- `notebooks/01_ingest_and_index.ipynb`: ingestao, chunking, indexacao e retrieval basico
- `notebooks/02_query_rag.ipynb`: retrieval + RAG com chamada real ao Ollama habilitada manualmente

## Limitacoes de ambiente

- O desenvolvimento pode acontecer sem acesso a uma VM com GPU
- Os testes automatizados do RAG usam mocks para nao depender do Ollama
- O fluxo real de geracao exige um endpoint Ollama acessivel em `http://localhost:11434`
- Quando o Ollama nao estiver acessivel, o RAG e a UI mostram falha explicita; nao existe fallback automatico

## Testes

Para rodar a suite completa:

```bash
REPO_ROOT="$(git rev-parse --show-toplevel)"
poetry -C "$REPO_ROOT" run bash -lc 'cd "$0/notebooks/pablo/final_project" && PYTHONPATH=. pytest -q' "$REPO_ROOT"
```

## Reproducao minima da v1

Uma reproducao minima da v1 segue estes passos:

1. instalar dependencias com Poetry
2. garantir o PDF em `data/pdf/`
3. iniciar o Ollama e baixar `qwen2.5:7b`
4. rebuild do indice em `data/chroma/`
5. consultar o RAG ou subir o Streamlit (streamlit run app.py --server.address 0.0.0.0 --server.port 8501)

## Status final

A v1 fica pronta quando:

- o indice pode ser recriado localmente
- o retrieval retorna trechos e metadados
- o RAG responde em PT-BR com fontes
- a UI Streamlit sobe e exibe resposta e fontes
- `pytest` passa
