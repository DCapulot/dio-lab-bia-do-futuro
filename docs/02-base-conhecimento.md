# Base de Conhecimento

## Dados Utilizados

Os dados utilizados pelo Otiniel serão armazenados na pasta `data` e terão como objetivo fornecer uma base de conhecimento para explicar termos financeiros utilizados no dia a dia.

| Arquivo                     | Formato | Utilização no Agente                                                                            |
| --------------------------- | ------- | ----------------------------------------------------------------------------------------------- |
| `termos_financeiros.json`   | JSON    | Armazenar os principais termos financeiros, suas definições e explicações simplificadas.        |
| `exemplos_financeiros.json` | JSON    | Armazenar exemplos práticos para ajudar o agente a explicar os termos de forma contextualizada. |
| `fontes.json`               | JSON    | Armazenar as fontes utilizadas para construir as explicações dos termos financeiros.            |

Os arquivos serão utilizados como base de conhecimento do Otiniel, permitindo que o agente consulte informações antes de gerar suas respostas.


> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.


---

## Adaptações nos Dados

Os dados mockados foram adaptados para o contexto do Otiniel, com foco em termos financeiros utilizados no dia a dia. Foram incluídos termos como Pix, chave Pix, cartão de crédito, débito, juros, limite, fatura, boleto, saldo e parcelamento, acompanhados de definições simples e exemplos práticos.

A estrutura dos dados foi organizada para facilitar a consulta pelo agente e permitir que as respostas sejam apresentadas de forma clara, acessível e educativa. Também foram consideradas fontes de referência para aumentar a confiabilidade das informações utilizadas pelo Otiniel.


---

## Estratégia de Integração

### Como os dados são carregados?

Os dados da base de conhecimento são armazenados em arquivos JSON dentro da pasta `data`. Quando o agente é iniciado, esses arquivos são carregados pelo sistema e ficam disponíveis para consulta durante as interações.

### Como os dados são usados no prompt?

Os dados são consultados dinamicamente de acordo com a pergunta do usuário. O Otiniel identifica o termo financeiro solicitado, busca as informações correspondentes na base de conhecimento e utiliza esses dados como contexto para gerar uma resposta simples, clara e objetiva.

Dessa forma, apenas as informações relevantes são utilizadas em cada interação, evitando a necessidade de colocar toda a base de conhecimento diretamente no prompt.

---
### Como os dados são carregados?

Os dados da base de conhecimento são armazenados em arquivos JSON dentro da pasta `data`. Quando o agente é iniciado, esses arquivos são carregados pelo sistema e disponibilizados para consulta durante as interações.

Ao receber uma pergunta, o Otiniel busca na base de conhecimento informações relacionadas ao termo financeiro solicitado e utiliza esses dados para gerar uma explicação simples e objetiva. Caso não encontre informações suficientes, o agente informa sua limitação em vez de inventar uma resposta.


### Como os dados são usados no prompt?

Os dados não são colocados diretamente no system prompt. Eles são consultados dinamicamente de acordo com a pergunta do usuário. O Otiniel identifica o termo financeiro solicitado, busca as informações correspondentes na base de conhecimento e utiliza esses dados como contexto para gerar uma resposta simples, clara e objetiva.

Dessa forma, o agente consegue utilizar informações específicas da base sem precisar carregar todos os dados no prompt a cada interação.


## Exemplo de Contexto Montado

Para o Otiniel, como o contexto é sobre **termos financeiros** e não sobre dados pessoais de clientes, você pode usar este exemplo:

```text
Termo solicitado pelo usuário:
- Termo: Chave Pix

Informações da Base de Conhecimento:
- Definição: A chave Pix é um identificador utilizado para receber ou enviar dinheiro por meio do Pix.
- Exemplos de chave: CPF, e-mail, número de telefone ou chave aleatória.
- Exemplo prático: Uma pessoa pode cadastrar seu número de telefone como chave Pix para facilitar o recebimento de dinheiro.

Orientação para o agente:
- Explicar o termo de forma simples e objetiva.
- Utilizar exemplos do dia a dia quando necessário.
- Não inventar informações que não estejam disponíveis na base.
```
