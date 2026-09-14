"""Aplicação principal do Otiniel - chatbot educativo de termos financeiros."""

import streamlit as st
from anthropic import Anthropic

from config import ANTHROPIC_API_KEY
from agente import gerar_resposta

st.set_page_config(page_title="Otiniel - Agente Financeiro", page_icon="💬")

st.title("💬 Otiniel")
st.caption("Seu agente educativo para entender termos financeiros do dia a dia.")

client = Anthropic(api_key=ANTHROPIC_API_KEY)

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
