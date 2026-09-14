"""Configurações do Otiniel: carrega variáveis de ambiente."""

import os

from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")

if not ANTHROPIC_API_KEY:
    raise RuntimeError(
        "ANTHROPIC_API_KEY não encontrada. Crie um arquivo .env na raiz de "
        "src/ (ou defina a variável de ambiente) com sua chave da API da "
        "Anthropic. Veja o .env.example."
    )
