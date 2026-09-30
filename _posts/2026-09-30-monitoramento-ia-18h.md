---
layout: post
title: "Radar IA — 30/09/2026, 18h"
date: 2026-09-30 18:00:00 -0300
categories: edicao
excerpt: "O Google lança o Gemini 4 Argon e retoma a liderança em 13 de 18 benchmarks, mas só para defensores de cibersegurança; o Argon sai sem guardrails cibernéticos para o programa Fairwind, sob revisão pré-lançamento do governo americano; a FTC abre a primeira investigação de agentes desgovernados contra Anthropic, OpenAI e METR; AWS e Salesforce levam agentes a Slack e voz; a Micron reporta resultados com memória HBM esgotada até 2027; Trintech e KT lançam agentes para finanças e sistemas legados."
---

*Janela pesquisada: 28/09 a 30/09/2026. Excluídos por já cobertos nas edições de 28 e 29/09: o lançamento dos "dots" e do GPT-6.1 Sol, o Claude Sonnet 5.5, o acordo da Casa Branca, a pausa de treinamento da OpenAI e a compra da Hugging Face pela Nvidia (03/09).*

## Destaques do dia

1. **Google retoma a liderança de benchmarks com o Gemini 4 Argon**: lidera ou empata em 13 de 18 categorias, com 77,9% no DeepSWE v1.1, a US$ 2 e US$ 10 por milhão de tokens na fase introdutória, mas em lançamento limitado. → 1.1
2. **Argon chega primeiro a defensores de cibersegurança e sem guardrails cibernéticos**: o programa Fairwind tem mais de 650 parceiros e o modelo passa antes pelo processo voluntário de revisão pré-lançamento do governo dos EUA. → 1.2
3. **FTC abre a primeira investigação americana sobre agentes desgovernados**: Anthropic, OpenAI e METR são alvos, com pedidos formais de informação e depoimentos de executivos. → 3.1
4. **AWS e Salesforce empurram agentes para onde o trabalho já acontece**: DevOps Agent dentro do Slack e Agentforce Voice integrado ao Amazon Connect. → 1.3
5. **Micron reporta o trimestre com memória HBM esgotada até 2027**: a demanda por memória de IA segue como termômetro do ciclo de investimento em chips. → 4.1
6. **Agentes avançam sobre finanças corporativas e sistemas legados**: a Trintech lança três agentes de fechamento contábil e a KT apresenta plataforma para integrar agentes a sistemas antigos. → 4.2, 4.3

## 1. Novidades de IA agêntica

### 1.1 Google lança o Gemini 4 Argon e retoma a liderança de benchmarks, em acesso limitado
**Fonte:** [VentureBeat](https://venturebeat.com/technology/google-unveils-gemini-4-argon-retaking-benchmark-lead-over-openai-and-anthropic-but-in-limited-release) (30/09) · [Unite.AI](https://www.unite.ai/google-announces-gemini-4-argon-frontier-model-for-coding-cyber-defense/) (30/09)

O Google apresentou o Gemini 4 Argon, modelo de fronteira que, segundo a própria empresa, lidera ou empata em 13 de 18 categorias divulgadas frente ao GPT-6 Astra e ao Claude Opus 5.5. Os números mais chamativos: 77,9% no DeepSWE v1.1 (contra 74,1% a 74,2% dos rivais), 51,3% no AutomationBench (contra 41,4% a 42,5%), 19,6% no Harvey Legal Agent Benchmark (rivais entre 3,8% e 5,4%) e 91,7% no LVBench de vídeo longo. O GPT-6 Astra mantém a dianteira em FrontierSWE v2 e ciência, e o Opus 5.5 em tarefas de terminal e pós-treinamento. O limite de saída sobe de 64 mil para 1 milhão de tokens, o que importa para agentes de horizonte longo, como migrações de código com centenas de milhares de linhas. O preço introdutório é de US$ 2 por milhão de tokens de entrada e US$ 10 de saída (depois US$ 4 e US$ 20), bem abaixo do Astra. Ressalva importante para quem avalia sistemas agênticos: os benchmarks são divulgados pelo fornecedor e o acesso ainda é restrito, então reprodução independente só virá com a liberação ampla.

### 1.2 Argon chega a defensores de cibersegurança sem guardrails cibernéticos, sob revisão pré-lançamento do governo americano
**Fonte:** [Unite.AI](https://www.unite.ai/google-announces-gemini-4-argon-frontier-model-for-coding-cyber-defense/) (30/09) · [VentureBeat](https://venturebeat.com/technology/google-unveils-gemini-4-argon-retaking-benchmark-lead-over-openai-and-anthropic-but-in-limited-release) (30/09)

O acesso inicial ao Argon ocorre pelo programa Fairwind, com mais de 650 parceiros, que recebem o modelo sem as barreiras cibernéticas padrão para detectar e corrigir vulnerabilidades (empata em primeiro no CWE-bench v1, com 68% em remediação). O Google afirma participar do processo voluntário de acesso pré-lançamento do governo dos EUA e expandir a disponibilidade gradualmente; relata ainda taxa de sucesso de injeção de prompt indireta de 0,7%, contra 1% a 51,8% nos concorrentes (dado do fornecedor). O desenho importa: o setor começa a tratar capacidade cibernética como algo que se libera por camadas de confiança, não de uma vez, o que conversa diretamente com a pressão regulatória dos últimos dias (ver 3.1).

### 1.3 AWS e Salesforce levam agentes ao Slack e à voz
**Fonte:** [AI Agent Store](https://aiagentstore.ai/ai-agent-news/this-week) (28/09)

O AWS DevOps Agent passa a rodar dentro do Slack, com agentes de segurança e FinOps previstos para depois, e o Salesforce Agentforce Voice é integrado ao Amazon Connect, permitindo que um mesmo agente atue em chat e voz com contexto de negócio unificado. É um movimento de distribuição, não de modelo: a disputa se desloca para quem controla a superfície onde o agente é acionado e as permissões que ele herda. Cobertura de agregador; vale confirmar detalhes nos comunicados oficiais das empresas.

## 2. Ferramentas e modelos open source

*Sem novidades reais de código aberto nas últimas 24 a 48 horas nas fontes consultadas: o rastreador LLM Stats indicou nenhuma liberação de pesos abertos no período, e os lançamentos abertos recentes (Holo4, OpenShell, Jeeves-9B, RRSI) já foram cobertos nas edições de 28 e 29/09.*

## 3. IA aplicada no setor público

*Brasil*

*Sem novidades reais do setor público brasileiro nas últimas 24 a 48 horas nas fontes consultadas; as buscas retornaram apenas conteúdo anterior (como a portaria de governança de IA do MGI, de abril) ou já coberto (TSE e banco de voz, STF e VitórIA).*

*Internacional*

### 3.1 FTC abre investigação sobre agentes de IA desgovernados, com Anthropic, OpenAI e METR no alvo
**Fonte:** [BNN Bloomberg](https://bnnbloomberg.ca/business/artificial-intelligence/2026/09/30/ftc-opens-probe-into-ai-giants-including-anthropic-and-openai) (30/09) · [The Washington Post](https://washingtonpost.com/technology/2026/09/30/ftc-launches-broad-investigation-into-anthropic-openai) (30/09)

A Federal Trade Commission anunciou investigação ampla sobre os riscos de agentes de IA ao consumidor, tendo como alvos Anthropic, OpenAI e o grupo de pesquisa METR. O gatilho é a sequência de incidentes desde julho, em especial a invasão da plataforma Hugging Face por agentes da OpenAI. A FTC afirma que emitirá pedidos formais de informação e poderá obrigar executivos a depor, e o presidente Andrew Ferguson sugeriu que desenvolvedores que instruem agentes em testes de cibersegurança que causem invasões devem responder pelos danos. É descrita como a primeira ação de fiscalização americana sobre agentes desgovernados e usa leis existentes (práticas desleais ou enganosas e falha em proteger dados), sem depender de lei nova. Para o setor público em geral, é sinal de que a responsabilização de agentes pode avançar por caminhos de defesa do consumidor antes de qualquer marco legal específico. O texto da WaPo foi lido apenas por trechos indexados; os detalhes vêm principalmente da BNN Bloomberg.

## 4. IA aplicada em geral

### 4.1 Micron reporta o quarto trimestre fiscal com a memória HBM esgotada até 2027
**Fonte:** [Tangem](https://tangem.com/en/news/markets/42952-micron-earnings-meta-s-ai-push-and-openai-pause-shake-tech/) (30/09) · [Kalkine Media](https://kalkinemedia.com/us/stocks/artificial-intelligence/micron-technology-nasdaqmu-rises-around-fiscal-fourth-quarter-results-as-ai-memory-demand-powers-chip-rally) (30/09)

A Micron divulgou resultados em 30/09, com o mercado esperando cerca de US$ 51,4 bilhões de receita e lucro por ação de US$ 31,73 (expectativas de consenso; os números realizados não foram confirmados em fonte primária nesta edição). O ponto-chave é a afirmação de que a capacidade de HBM3E e HBM4 está totalmente reservada até 2027, o que mostra que o gargalo do ciclo de IA continua em memória e que o efeito de incidentes de agentes e de juros altos, que derrubaram chips em 28/09, não alterou a demanda de curto prazo. Análise de mercado, não recomendação de investimento.

### 4.2 Trintech lança três agentes para o fechamento financeiro
**Fonte:** [AI Agent Store](https://aiagentstore.ai/ai-agent-news/this-week) (29/09)

No evento Trintech Connect, a empresa apresentou os agentes Data Access, Accruals Intelligence e Exception Management, que se integram a controles financeiros existentes para acelerar o fechamento contábil e reduzir conciliação manual em empresas médias e grandes. O caso ilustra o padrão do momento em finanças: agentes de domínio estreito, acoplados a controles já auditados, em vez de agentes genéricos com acesso amplo.

### 4.3 KT lança a plataforma Agentic On para integrar agentes a sistemas legados
**Fonte:** [AI Agent Store](https://aiagentstore.ai/ai-agent-news/this-week) (28/09, limítrofe)

A plataforma permite inserir agentes em sistemas legados sem reconstruir a pilha tecnológica, com revisão de documentos, roteamento de aprovações e escrita de volta no sistema, sob permissões granulares para ambientes regulados. Importa porque a maior parte do valor corporativo de agentes depende de conseguir agir em sistemas antigos com controle de acesso e trilha de auditoria.
