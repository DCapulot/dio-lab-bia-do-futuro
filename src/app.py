"""Aplicação principal do Otiniel - chatbot educativo de termos financeiros.

Roda 100% local usando o Ollama como servidor de LLM - gratuito e sem
necessidade de chave de API."""

import ollama
import streamlit as st

from config import OLLAMA_HOST, OTINIEL_MODEL
from agente import gerar_resposta

st.set_page_config(page_title="Otiniel - Agente Financeiro", page_icon="💬")

st.title("💬 Otiniel")
st.caption("Seu agente educativo para entender termos financeiros do dia a dia.")

client = ollama.Client(host=OLLAMA_HOST)

# Verifica se o Ollama está no ar e se o modelo já foi baixado antes de
# liberar o chat, mostrando um aviso claro em vez de travar sem explicação.
try:
    modelos_instalados = {m["model"].split(":")[0] for m in client.list().get("models", [])}
    if OTINIEL_MODEL.split(":")[0] not in modelos_instalados:
        st.error(
            f"O modelo `{OTINIEL_MODEL}` ainda não foi baixado no Ollama.\n\n"
            f"Abra um terminal e rode: `ollama pull {OTINIEL_MODEL}`"
        )
        st.stop()
except Exception:
    st.error(
        "Não consegui conectar ao Ollama. Confirme que ele está instalado e "
        "rodando (abra o app do Ollama, ou rode `ollama serve` em um "
        "terminal) e recarregue esta página."
    )
    st.stop()

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []
    st.session_state.mensagens.append(
        {
            "role": "assistant",
            "content": "Olá! Eu sou o Otiniel. Qual termo financeiro você quer entender hoje? "
            "(ex: Pix, chave Pix, cartão de crédito, juros, boleto, CDB...)",
        }
    )

for msg in st.session_state.mensagens:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

pergunta = st.chat_input("Digite sua pergunta sobre um termo financeiro...")

if pergunta:
    st.session_state.mensagens.append({"role": "user", "content": pergunta})
    with st.chat_message("user"):
        st.markdown(pergunta)

    # histórico enviado ao modelo (sem a mensagem de saudação inicial fixa)
    historico_llm = [
        {"role": m["role"], "content": m["content"]}
        for m in st.session_state.mensagens[1:-1]
    ]

    with st.chat_message("assistant"):
        with st.spinner("Otiniel está pensando..."):
            resposta = gerar_resposta(pergunta, historico_llm, client)
            st.markdown(resposta)

    st.session_state.mensagens.append({"role": "assistant", "content": resposta})

with st.sidebar:
    st.header("Sobre o Otiniel")
    st.write(
        "O Otiniel explica termos financeiros do cotidiano (Pix, cartão de "
        "crédito, juros, boleto, investimentos básicos e outros) de forma "
        "simples, com base em uma base de conhecimento fixa."
    )
    st.write("**O que ele não faz:**")
    st.markdown(
        "- Não recomenda investimentos\n"
        "- Não acessa contas ou saldos reais\n"
        "- Não pede dados sensíveis\n"
        "- Não inventa informações fora da base de conhecimento"
    )
    if st.button("🔄 Reiniciar conversa"):
        st.session_state.mensagens = []
        st.rerun()
