"""Configurações do Otiniel: carrega variáveis de ambiente.

Não é necessária nenhuma chave de API: o modelo roda localmente via
Ollama (https://ollama.com)."""

import os

from dotenv import load_dotenv

load_dotenv()

# Endereço do servidor local do Ollama (o padrão já funciona na grande
# maioria dos casos, não precisa mexer).
OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://localhost:11434")

# Nome do modelo a ser usado (precisa ter sido baixado antes com
# `ollama pull <nome-do-modelo>`).
OTINIEL_MODEL = os.environ.get("OTINIEL_MODEL", "llama3.2")
