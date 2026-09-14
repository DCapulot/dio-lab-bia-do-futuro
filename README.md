# 💬 Otiniel — Agente Financeiro Educativo

Agente de IA generativa que explica termos financeiros do dia a dia (Pix, cartão
de crédito, juros, boleto, investimentos básicos etc.) de forma simples, direta
e sem inventar informações. Projeto desenvolvido para o desafio **Agente
Financeiro Inteligente com IA Generativa**.

## Estrutura do Repositório

```
otiniel/
├── README.md
│
├── docs/                          # Documentação do projeto (as 6 entregas)
│   ├── 01-documentacao-agente.md  # Caso de uso, persona, arquitetura, segurança
│   ├── 02-base-conhecimento.md    # Estratégia de dados
│   ├── 03-prompts.md              # System prompt + exemplos + edge cases
│   ├── 04-metricas.md             # Avaliação e métricas
│   └── 05-pitch.md                # Roteiro do pitch (3 min)
│
├── data/                          # Base de conhecimento
│   ├── termos_financeiros.json    # ✅ usado pelo Otiniel (definições)
│   ├── exemplos_financeiros.json  # ✅ usado pelo Otiniel (exemplos práticos)
│   ├── fontes.json                # ✅ usado pelo Otiniel (fontes por categoria)
│   ├── perfil_investidor.json     # dado mockado original (não usado no MVP)
│   ├── produtos_financeiros.json  # dado mockado original (não usado no MVP)
│   ├── transacoes.csv             # dado mockado original (não usado no MVP)
│   └── historico_atendimento.csv  # dado mockado original (não usado no MVP)
│
├── src/                           # Aplicação funcional (Streamlit)
│   ├── app.py                     # Interface do chat
│   ├── agente.py                  # Busca na base + chamada ao modelo
│   ├── prompts.py                 # System prompt do Otiniel
│   ├── config.py                  # Variáveis de ambiente
│   ├── requirements.txt
│   └── .env.example
│
├── assets/                        # Diagramas, prints, roteiro dos vídeos
└── examples/                      # Referências do desafio original
```

## Por que só parte dos dados mockados é usada?

O repositório original trazia dados voltados para um agente de
**aconselhamento personalizado** (transações, perfil de investidor, produtos).
Como o caso de uso escolhido — o Otiniel — foi redefinido para **explicar
termos financeiros** (e não dar recomendações), os arquivos realmente usados
pelo agente são os três novos em `data/`: `termos_financeiros.json`,
`exemplos_financeiros.json` e `fontes.json`. Os quatro arquivos originais
foram mantidos no repositório (para não perder a entrega) mas não são
consultados no MVP atual — ficam como uma extensão futura possível (ver
"Próximos passos" abaixo).

## Como rodar

```bash
cd src
cp .env.example .env        # depois edite e cole sua ANTHROPIC_API_KEY
pip install -r requirements.txt
streamlit run app.py
```

Você pode conseguir uma chave de API em https://console.anthropic.com/.
Se preferir usar outro provedor (OpenAI, Gemini), basta trocar a chamada
dentro de `src/agente.py`.

## Como o agente funciona (resumo)

1. O usuário faz uma pergunta no chat.
2. `agente.py` procura, por palavra-chave, quais termos da base
   (`termos_financeiros.json`) aparecem na pergunta.
3. Se encontrar, monta um bloco de contexto com definição + exemplo + fonte
   e envia isso, junto com o `system prompt`, para o modelo.
4. Se **não** encontrar nenhum termo correspondente, o agente é instruído a
   admitir a limitação em vez de inventar uma resposta (anti-alucinação).

## Próximos passos (não implementados no MVP)

- Usar `perfil_investidor.json` e `produtos_financeiros.json` para uma segunda
  funcionalidade opcional: sugerir *qual produto combina com o perfil* do
  cliente (sempre deixando claro que não é uma recomendação de investimento).
- Trocar a busca por palavra-chave por busca semântica (embeddings) para
  lidar melhor com perguntas escritas de formas diferentes.
- Adicionar métricas de observabilidade (latência, tokens, taxa de erro).
