from __future__ import annotations

from typing import Sequence

from src.retrieval import RetrievedChunk


INSUFFICIENT_EVIDENCE_MESSAGE = (
    "Não há evidência suficiente no documento para responder a essa pergunta."
)

RAG_SYSTEM_PROMPT = """\
Você é um assistente de RAG em PT-BR.
Responda somente com base no contexto fornecido.
Não invente fatos, datas, nomes, valores ou regras que não estejam no contexto.
Se o contexto não trouxer evidência suficiente para responder com segurança, diga exatamente:
"Não há evidência suficiente no documento para responder a essa pergunta."
Não mencione conhecimento externo, internet, treinamento do modelo ou suposições.
Responda de forma objetiva e clara em PT-BR.
"""


def build_context_block(chunks: Sequence[RetrievedChunk]) -> str:
    context_lines: list[str] = []
    for index, chunk in enumerate(chunks, start=1):
        context_lines.append(
            "\n".join(
                [
                    f"[Trecho {index}]",
                    f"source: {chunk.source}",
                    f"page: {chunk.page}",
                    f"chunk_id: {chunk.chunk_id}",
                    f"score: {chunk.score:.3f}",
                    f"text: {chunk.text}",
                ]
            )
        )
    return "\n\n".join(context_lines)


def build_rag_prompt(query: str, chunks: Sequence[RetrievedChunk]) -> str:
    context_block = build_context_block(chunks)
    return "\n\n".join(
        [
            "Pergunta do usuario:",
            query.strip(),
            "Contexto recuperado do documento:",
            context_block,
            (
                "Instrução: responda apenas com base no contexto recuperado. "
                "Se a evidência for insuficiente, use exatamente a mensagem definida."
            ),
        ]
    )
