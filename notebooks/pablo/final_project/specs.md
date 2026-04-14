# SDD — Specs & Milestones (RAG local: PDF → Chroma → Ollama → Streamlit)

## Contexto
Projeto para uso local (VM), em Python, com foco em:
- 1 PDF com texto selecionável (`data/pdf/sindilojas_2025_2026.pdf`)
- Indexação local com Chroma (persistente)
- Embeddings multilíngues (sentence-transformers)
- Geração via Ollama (requests direto), modelo padrão `qwen2.5:7b`
- UI simples em Streamlit
- Cada pergunta é independente (sem memória)

## Objetivo da v1 (Definition of Done global)
- Rodar localmente na VM.
- Ingerir o PDF e criar um índice persistido em `data/chroma/`.
- Fazer uma pergunta e receber:
  1) resposta em PT-BR
  2) lista de fontes (2–5 trechos) com página e snippet
- Se a informação não estiver no PDF, responder explicitamente que não há evidência suficiente no documento.

---

## Milestones (SDD)
Cada milestone deve ser entregue com:
- código funcionando
- logs mínimos
- (quando fizer sentido) teste smoke em `tests/`
- documentação atualizada (`README.md`)

### M0 — Bootstrap do repo
**Entregáveis**
- Estrutura de pastas:
  - `src/`, `notebooks/`, `data/pdf/`, `data/chroma/`, `tests/`, `specs/`
- `requirements.txt`
- `src/config.py` com defaults
- `src/utils_ollama.py` com `ollama_tags()` e `ollama_generate()`
- `README.md` com setup mínimo (venv, pip install, ollama serve)

**Aceite**
- `python -c "from src.config import settings; print(settings)"` funciona
- `python -c "from src.utils_ollama import ollama_tags; print(ollama_tags('http://localhost:11434').keys())"` funciona

---

### M1 — Ingestão do PDF (texto por página + chunks)
**Entregáveis**
- `src/ingestion.py`
  - `load_pdf_pages(pdf_path) -> list[dict(page,text)]`
  - `chunk_pages(pages, chunk_size, chunk_overlap, source) -> list[Document]`
- notebook `notebooks/01_ingest_and_index.ipynb` com:
  - leitura do PDF
  - chunking
  - prints/estatísticas

**Aceite**
- `pages > 0` e `chunks > 0` para o PDF atual
- cada chunk tem metadata `source`, `page`, `chunk_id`

---

### M2 — Indexação no Chroma (persistência)
**Entregáveis**
- `src/indexing.py`
  - `build_embeddings(model_name)`
  - `rebuild_chroma(docs, persist_dir, embeddings)` (rebuild do zero)
  - `open_chroma(persist_dir, embeddings)`
- notebook 01 persiste em `data/chroma/`

**Aceite**
- após rodar, `data/chroma/` existe e não está vazio
- reabrir o índice e recuperar docs funciona

---

### M3 — Retrieval (top-k com score + metadados)
**Entregáveis**
- `src/retrieval.py`
  - `RetrieverService.retrieve(query, k) -> list[RetrievedChunk]`
- teste smoke em `tests/test_retrieval_smoke.py`

**Aceite**
- retorna top-k com `text` não vazio e metadata (page/source)
- funciona com queries simples

---

### M4 — RAG (prompt + geração + fontes)
**Entregáveis**
- `src/prompts.py` com prompt base PT-BR e regras anti-alucinação
- `src/rag.py`
  - `RAGService.answer(query) -> {answer, sources}`
  - monta prompt com contexto
  - chama `ollama_generate`
- notebook `notebooks/02_query_rag.ipynb`

**Aceite**
- resposta contém seção Fontes com 2–5 itens (quando houver contexto)
- fora do escopo do PDF: mensagem de insuficiência de evidência

---

### M5 — Streamlit UI (chat simples)
**Entregáveis**
- `app.py`
  - input de pergunta
  - exibir resposta
  - expander com fontes (page + snippet)
  - sem memória de conversa para geração (cada pergunta independente)

**Aceite**
- `streamlit run app.py --server.address 0.0.0.0 --server.port 8501` funciona
- uso real pelo navegador acessando a VM

---

### M6 — Qualidade mínima e documentação
**Entregáveis**
- `README.md` completo (setup, ingest, rodar app)
- mais 1–2 testes smoke
- script opcional `scripts/reindex.py` para rebuild

**Aceite**
- `pytest` passa
- qualquer pessoa consegue reproduzir seguindo README

---

## Regras de versionamento e organização
- Cada milestone pode ser desenvolvido em commits separados.
- Specs podem evoluir; sempre atualize este arquivo se mudar escopo/decisão.
- Prefira funções pequenas e testáveis.