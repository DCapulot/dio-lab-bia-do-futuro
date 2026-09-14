Claro. Vou manter **a mesma estrutura do seu arquivo**, mas adaptar tudo para o Otiniel, sem colocar coisas que ele não faz, como consulta de saldo ou recomendação de investimento.

# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação do Otiniel pode ser feita de duas formas complementares:

1. **Testes estruturados:** definir perguntas sobre termos financeiros e verificar se as respostas estão corretas e de acordo com a base de conhecimento;
2. **Feedback real:** pessoas testam o agente e avaliam a qualidade das respostas.

---

## Métricas de Qualidade

| Métrica           | O que avalia                                                             | Exemplo de teste                                                                           |
| ----------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| **Assertividade** | O agente explicou corretamente o termo perguntado?                       | Perguntar "O que é Pix?" e verificar se a explicação está correta.                         |
| **Segurança**     | O agente evita inventar informações quando não possui dados suficientes? | Perguntar sobre um termo que não está na base e verificar se o agente admite que não sabe. |
| **Clareza**       | A resposta é simples e fácil de entender?                                | Perguntar "O que são juros?" e verificar se a explicação utiliza uma linguagem acessível.  |
| **Coerência**     | A resposta está de acordo com as informações da base de conhecimento?    | Comparar a resposta do agente com a definição armazenada na base.                          |

> [!TIP]
> Peça para 3-5 pessoas (amigos, família ou colegas) testarem o Otiniel e avaliarem cada métrica com notas de 1 a 5. Isso ajuda a identificar pontos fortes e oportunidades de melhoria.

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de termo financeiro

* **Pergunta:** "O que é cartão de crédito?"
* **Resposta esperada:** Explicação simples e correta baseada na base de conhecimento.
* **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 2: Explicação com exemplo

* **Pergunta:** "O que são juros?"
* **Resposta esperada:** Explicação clara sobre o significado de juros, acompanhada de um exemplo prático quando necessário.
* **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo

* **Pergunta:** "Qual a previsão do tempo?"
* **Resposta esperada:** Agente informa que é especializado em termos financeiros e não possui informações sobre previsão do tempo.
* **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 4: Informação inexistente

* **Pergunta:** "O que é o termo XYZ?"
* **Resposta esperada:** Agente informa que não encontrou informações suficientes na base de conhecimento e não inventa uma definição.
* **Resultado:** [ ] Correto  [ ] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**

* O Otiniel conseguiu explicar os termos financeiros de forma simples e objetiva.
* As respostas ficaram de acordo com as informações disponíveis na base de conhecimento.
* O agente conseguiu utilizar exemplos do cotidiano para facilitar a compreensão.
* O agente demonstrou segurança ao admitir quando não possuía informações suficientes.

**O que pode melhorar:**

* Aumentar a quantidade de termos disponíveis na base de conhecimento.
* Adicionar mais exemplos práticos para diferentes termos financeiros.
* Melhorar a compreensão de perguntas escritas de formas diferentes.
* Realizar mais testes com usuários para identificar possíveis dificuldades nas respostas.

---

## Métricas Avançadas (Opcional)

Para quem quer explorar mais, algumas métricas técnicas de observabilidade também podem fazer parte da solução, como:

* Latência e tempo de resposta;
* Consumo de tokens e custos;
* Logs e taxa de erros;
* Quantidade de perguntas respondidas corretamente;
* Taxa de respostas que precisam ser corrigidas.

Ferramentas especializadas em LLMs, como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/), são exemplos que podem ajudar nesse monitoramento. Entretanto, outras ferramentas de observabilidade também podem ser utilizadas.
