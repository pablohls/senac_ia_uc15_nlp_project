from __future__ import annotations

from typing import Any

import streamlit as st
from requests.exceptions import RequestException

from src.rag import RAGService


OLLAMA_UNAVAILABLE_MESSAGE = (
    "Nao foi possivel gerar a resposta porque o Ollama nao esta acessivel neste ambiente."
)


def build_rag_service() -> RAGService:
    return RAGService()


def ask_question(query: str, rag_service: RAGService) -> tuple[str, dict[str, Any] | str]:
    normalized_query = query.strip()
    if not normalized_query:
        return ("warning", "Digite uma pergunta antes de enviar.")

    try:
        result = rag_service.answer(normalized_query)
    except RequestException as exc:
        return ("error", f"{OLLAMA_UNAVAILABLE_MESSAGE}\n\nDetalhes: {exc}")

    return ("success", result)


def render_sources(sources: list[dict[str, Any]]) -> None:
    if not sources:
        st.info("Nenhuma fonte foi exibida para esta resposta.")
        return

    with st.expander(f"Fontes ({len(sources)})", expanded=False):
        for index, source in enumerate(sources, start=1):
            st.markdown(
                "\n".join(
                    [
                        f"**Fonte {index}**",
                        f"- Pagina: {source['page']}",
                        f"- Origem: {source['source']}",
                        f"- Chunk: {source['chunk_id']}",
                        f"- Score: {source['score']}",
                        f"- Trecho: {source['snippet']}",
                    ]
                )
            )


def main(rag_service: RAGService | None = None) -> None:
    st.set_page_config(page_title="RAG Sindilojas", page_icon=":books:")
    st.title("Consulta RAG do PDF")
    st.caption("Cada pergunta e tratada de forma independente, sem memoria de conversa.")

    service = build_rag_service() if rag_service is None else rag_service

    query = st.text_input("Pergunta", placeholder="Ex.: Qual e a vigencia da convencao coletiva?")

    if st.button("Perguntar", type="primary"):
        status, payload = ask_question(query, service)
        if status == "warning":
            st.warning(str(payload))
            return
        if status == "error":
            st.error(str(payload))
            return

        result = payload
        if not isinstance(result, dict):
            raise ValueError("Expected dictionary result from RAGService.")

        st.subheader("Resposta")
        st.write(result["answer"])
        render_sources(list(result["sources"]))


if __name__ == "__main__":
    main()
