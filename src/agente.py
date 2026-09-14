"""Lógica central do agente Otiniel: carrega a base de conhecimento,
busca o termo perguntado e monta o contexto para o LLM."""

import json
import os
import re
import unicodedata

from anthropic import Anthropic

from prompts import SYSTEM_PROMPT, NO_CONTEXT_NOTICE

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

MODEL = os.environ.get("OTINIEL_MODEL", "claude-sonnet-4-6")


def _normalizar(texto: str) -> str:
    """Remove acentos e caixa para facilitar a comparação de termos."""
    texto = texto.lower().strip()
    texto = unicodedata.normalize("NFKD", texto)
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    return texto


def carregar_base_conhecimento():
    """Carrega os arquivos JSON da base de conhecimento em memória."""
    with open(os.path.join(DATA_DIR, "termos_financeiros.json"), encoding="utf-8") as f:
        termos = json.load(f)
    with open(os.path.join(DATA_DIR, "exemplos_financeiros.json"), encoding="utf-8") as f:
        exemplos = json.load(f)
    with open(os.path.join(DATA_DIR, "fontes.json"), encoding="utf-8") as f:
        fontes = json.load(f)
    return termos, exemplos, fontes


def buscar_termos_relevantes(pergunta: str, termos: list) -> list:
    """Busca simples por palavra-chave: retorna os termos da base cujo nome
    (ou sinônimo) aparece mencionado na pergunta do usuário."""
    pergunta_norm = _normalizar(pergunta)
    encontrados = []

    for item in termos:
        candidatos = [item["termo"]] + item.get("sinonimos", [])
        for candidato in candidatos:
            candidato_norm = _normalizar(candidato)
            # word-boundary-ish match para evitar falsos positivos em termos curtos
            padrao = r"\b" + re.escape(candidato_norm) + r"\b"
            if re.search(padrao, pergunta_norm):
                encontrados.append(item)
                break

    return encontrados


def montar_contexto(pergunta: str, termos: list, exemplos: list, fontes: list) -> str:
    """Monta o bloco de contexto (base de conhecimento) que será enviado ao LLM,
    contendo apenas as informações relevantes para a pergunta."""
    relevantes = buscar_termos_relevantes(pergunta, termos)

    if not relevantes:
        return ""

    blocos = []
    for item in relevantes:
        termo = item["termo"]
        bloco = [f"- Termo: {termo}", f"  Definição: {item['definicao']}"]

        exemplo = next((e["exemplo"] for e in exemplos if e["termo"] == termo), None)
        if exemplo:
            bloco.append(f"  Exemplo prático: {exemplo}")

        fonte = next((s["fonte"] for s in fontes if s["categoria"] == item.get("categoria")), None)
        if fonte:
            bloco.append(f"  Fonte de referência: {fonte}")

        blocos.append("\n".join(bloco))

    return "Informações da Base de Conhecimento:\n\n" + "\n\n".join(blocos)


def gerar_resposta(pergunta: str, historico: list, client: Anthropic) -> str:
    """Gera a resposta do Otiniel usando a base de conhecimento + histórico da conversa."""
    termos, exemplos, fontes = carregar_base_conhecimento()
    contexto = montar_contexto(pergunta, termos, exemplos, fontes)

    system = SYSTEM_PROMPT
    if contexto:
        pergunta_com_contexto = f"{contexto}\n\nPergunta do usuário: {pergunta}"
    else:
        system = SYSTEM_PROMPT + NO_CONTEXT_NOTICE
        pergunta_com_contexto = f"Pergunta do usuário: {pergunta}"

    mensagens = historico + [{"role": "user", "content": pergunta_com_contexto}]

    resposta = client.messages.create(
        model=MODEL,
        max_tokens=600,
        system=system,
        messages=mensagens,
    )

    return "".join(bloco.text for bloco in resposta.content if bloco.type == "text")
