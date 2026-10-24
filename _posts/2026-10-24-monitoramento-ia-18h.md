---
layout: post
title: "Radar IA — 24/10/2026, 18h"
date: 2026-10-24 18:00:00 -0300
categories: edicao
excerpt: "Moonshot lança o Kimi K3.1 Pro, que briga com os melhores modelos fechados em agentes de código; Fundação Agentic AI chega a 10 projetos com quatro novos padrões abertos; Moonshot tirou dados de hacking do modelo cujos pesos serão abertos; STJ fixa limites para IA em provas e decisões; Itália exige decisor humano em contratações e demissões; Texas processa a OpenAI e Sam Altman."
---

*Janela pesquisada: 22 a 24/10/2026. Ficaram de fora itens já cobertos nas edições de 21, 22 e 23/10 (como Daytona, TanStack AI 1.0, F5 e Google Cloud, Kognitos) e notícias que só apareciam em agregadores sem fonte primária verificável. Quando uma notícia tinha data incerta, ela foi descartada.*

## Destaques do dia

1. **Kimi K3.1 Pro chega ao mercado**: modelo da Moonshot com 2,8 trilhões de parâmetros e contexto de 1 milhão de tokens aponta 65,7% no Terminal-Bench 4.0, perto do Claude Opus 5.5. → 1.1, 2.1
2. **Padrões abertos para agentes ganham escala**: a Agentic AI Foundation aceitou Agent Skills, Open Responses, OpenEnv e OpenSandbox e chegou a 10 projetos. → 1.2, 2.2
3. **Pesos abertos com dados de hacking removidos**: a Moonshot diz ter cortado dados cibernéticos do treino do K3.1 Pro antes de abrir os pesos, previstos até 4 de novembro. → 2.1
4. **STJ traça limites para a IA no processo**: tribunal multa injeção de prompt, rejeita jurisprudência inventada e não aceita relatório policial de IA sem validação humana. → 3.1
5. **Itália exige decisor humano em RH**: decreto em vigor desde 23/10 anula decisões de contratação, avaliação ou demissão tomadas só por automação. → 3.2
6. **Texas processa a OpenAI e Sam Altman**: o procurador-geral Ken Paxton alega prática comercial enganosa em torno da segurança do ChatGPT. → 4.1

## 1. Novidades de IA agêntica

### 1.1 Moonshot lança o Kimi K3.1 Pro, focado em agentes de código
**Fonte:** [MarkTechPost](https://www.marktechpost.com/2026/10/23/moonshot-ai-kimi-k3-1-pro-open-weight-model/) (23/10) · [The Next Web](https://thenextweb.com/news/moonshot-kimi-k3-1-pro-open-weight-cyber) (23/10)

A Moonshot AI lançou o Kimi K3.1 Pro, primeiro modelo da série K3.1: arquitetura de mistura de especialistas (MoE) com 2,8 trilhões de parâmetros totais e 104 bilhões ativos por token, janela de contexto de 1 milhão de tokens e uma variante "Highspeed" que a empresa diz ser de duas a três vezes mais rápida. Segundo números da própria Moonshot, ainda não verificados de forma independente, o modelo marca 65,7% no Terminal-Bench 4.0 (agentes que trabalham em terminal), contra 66,4% do Claude Opus 5.5 e 58,2% do GPT-6 Astra. A API custa US$ 2 por milhão de tokens de entrada e US$ 10 por milhão de saída, abaixo dos US$ 3 e US$ 15 do K3. Importa porque, se o resultado se sustentar fora do laboratório, um modelo com pesos prometidos como abertos fica a menos de um ponto de distância do topo fechado em tarefas de agentes de código, o que pressiona preços e estratégias de dependência de fornecedor. Vale cautela: no Terminal-Bench Science, a própria empresa reporta 38,1 contra 68,1 do GPT-6 Astra.

### 1.2 Agentic AI Foundation chega a 10 projetos com quatro novos padrões abertos
**Fonte:** [Linux Foundation](https://www.linuxfoundation.org/press/agentic-ai-foundation-announces-four-new-projects-agent-skills-open-responses-openenv-and-opensandbox) (22/10)

Anunciada no AGNTCon + MCPCon América do Norte, em San Jose, a entrada de quatro projetos eleva a Agentic AI Foundation (AAIF) de três projetos, no lançamento em dezembro de 2025, para dez. Agent Skills (Anthropic) é um formato para empacotar instruções, scripts e recursos que o agente carrega sob demanda; Open Responses (OpenAI) é uma especificação de interface entre provedores de modelos, baseada na API Responses; OpenEnv (Hugging Face) é um framework para ambientes de aprendizado por reforço; e OpenSandbox (Alibaba) é uma plataforma de execução isolada. Os outros seis são A2A, Agent Router, agentgateway, AGENTS.md, goose e o MCP. A doação do Agent Skills já havia sido registrada na edição de 23/10; o fato novo é o pacote completo e a presença de quatro empresas concorrentes sob governança neutra. Para quem constrói agentes, isso reduz o risco de ficar preso a um único fornecedor, embora o suporte real a cada padrão ainda dependa de cada provedor.

## 2. Ferramentas e modelos open source

### 2.1 Kimi K3.1 Pro: pesos abertos previstos até 4/11, com dados de hacking removidos
**Fonte:** [The Next Web](https://thenextweb.com/news/moonshot-kimi-k3-1-pro-open-weight-cyber) (23/10) · [MarkTechPost](https://www.marktechpost.com/2026/10/23/moonshot-ai-kimi-k3-1-pro-open-weight-model/) (23/10)

O modelo já está disponível nos apps e na API da Kimi, mas os pesos completos só serão publicados até 4 de novembro (a MarkTechPost fala em novembro; a licença não foi informada). O ponto técnico mais interessante é que a Moonshot afirma ter removido dados relacionados a ataques cibernéticos do pré-treino intermediário e do aprendizado por reforço da versão aberta. Num teste interno de exploração de falhas reais, um checkpoint sem os cortes resolveu 90,5% das tarefas e o modelo entregue, 81%; o K3 anterior tinha 33,3%. Pesquisadores de segurança lembram que modelos abertos não podem ser recolhidos depois do download e que as salvaguardas ficam atrás das dos fechados, de modo que uma redução de 9,5 pontos é mais mitigação que barreira. Para a academia, é um caso concreto para estudar o custo, em desempenho, de filtrar capacidades perigosas dos dados de treino. A Moonshot também enfrenta acusações de autoridades americanas, feitas em julho sem evidências publicadas, sobre uso de chips proibidos e cópia de um modelo da Anthropic.

### 2.2 OpenEnv e OpenSandbox entram para a AAIF como infraestrutura aberta de treino e execução
**Fonte:** [Linux Foundation](https://www.linuxfoundation.org/press/agentic-ai-foundation-announces-four-new-projects-agent-skills-open-responses-openenv-and-opensandbox) (22/10)

Dos quatro projetos que entraram na AAIF, dois são ferramentas de infraestrutura de código aberto. O OpenEnv, da Hugging Face, é um framework e hub comunitário para criar ambientes de aprendizado por reforço em contêineres, que expõem uma interface de agente, MCP e o protocolo de treino Gym. O OpenSandbox, da Alibaba, oferece SDKs em várias linguagens, APIs unificadas de sandbox, ambientes de execução em Docker e Kubernetes e um protocolo para runtimes personalizados. Em conjunto, cobrem duas lacunas comuns na pesquisa com agentes: ambientes reprodutíveis para treinar e avaliar, e isolamento seguro para executar código gerado pelo modelo. Para estudantes de pós-graduação, o ganho prático é ter peças abertas e com governança neutra para montar experimentos de agentes sem depender de plataformas proprietárias.

## 3. IA aplicada no setor público

*Brasil*

### 3.1 STJ consolida limites para o uso de IA em processos, provas e decisões
**Fonte:** [Jornal Grande Bahia](https://jornalgrandebahia.com.br/2026/10/stj-pune-uso-indevido-de-inteligencia-artificial-em-processos-e-estabelece-limites-para-provas-e-decisoes-judiciais) (24/10)

Reportagem reúne decisões recentes do Superior Tribunal de Justiça sobre IA. A Segunda Turma multou em 10% do valor da causa, por litigância de má-fé, um procurador municipal que escondeu em petição uma instrução para a IA decidir a favor do cliente (uma injeção de prompt), com envio do caso a OAB, MPF, Polícia Federal e prefeitura. Peças com leis e precedentes inexistentes foram rejeitadas, e uma parte foi multada em junho por citar jurisprudência fictícia. A Quinta Turma, no HC 1.059.475, excluiu de um processo penal um relatório policial gerado por IA sem validação humana, que contradizia a perícia oficial de áudio. Ao mesmo tempo, o tribunal afirma que usar IA na advocacia não é irregular por si só, e que alegar que uma decisão foi feita por IA, sem prova concreta de prejuízo, não basta para anulá-la (AREsp 2.848.833). Os congressos do STJ aprovaram 11 enunciados sobre supervisão humana, verificação de provas digitais e responsabilidade de advogados e juízes. A fonte é um veículo regional que cita os julgados; vale conferir os acórdãos no site do tribunal. Para o setor público, o recado é que a IA é aceita, mas com revisão humana comprovável e responsabilização.

*Internacional*

### 3.2 Itália: decreto exige decisor humano com poder efetivo em contratações e demissões por IA
**Fonte:** [ActuIA](https://www.actuia.com/en/news/italy-from-23-october-ai-hiring-or-firing-requires-a-human-decision-maker/) (23/10)

O Decreto Legislativo 179/2026, publicado na Gazzetta Ufficiale em 8 de outubro, passou a valer em 23 de outubro. Empregadores que usam IA para contratar, avaliar, sancionar ou demitir devem deixar a decisão final a uma pessoa com poder "efetivo e autônomo", não meramente formal. Decisão tomada exclusivamente por tratamento automatizado é nula, e o consentimento do empregado não sana o vício. O empregador precisa informar previamente os funcionários e, a pedido, apresentar uma motivação inteligível que explique o peso e os principais parâmetros do sistema. A triagem de currículos não é considerada decisão final, mas o artigo 22 do GDPR continua valendo se for totalmente automatizada. A sanção direta do decreto é a nulidade, e as multas vêm do GDPR e, a partir de 2 de dezembro de 2027, do AI Act para sistemas de RH de alto risco. É um exemplo útil de regulação que define "supervisão humana" por efeito prático, tema central no debate brasileiro sobre o PL 2338.

## 4. IA aplicada em geral

### 4.1 Texas processa a OpenAI e Sam Altman por práticas comerciais enganosas
**Fonte:** [Bloomberg Law](https://news.bloomberglaw.com/artificial-intelligence/texas-ag-sues-openai-altman-for-negative-effects-on-consumers) (23/10) · [Texas Scorecard](https://texasscorecard.com/state/paxton-sues-openai-ceo-sam-altman-over-chatgpt-safety/)

O procurador-geral do Texas, Ken Paxton, ajuizou ação contra a OpenAI e seu presidente-executivo, Sam Altman, com base na lei texana de práticas comerciais enganosas e proteção ao consumidor. A alegação é de que o ChatGPT foi vendido como seguro e confiável, mas a empresa não protegeu os texanos, incluindo crianças, de seus danos. Os trechos acessíveis não detalham os danos alegados, o pedido nem o tribunal, e a OpenAI ainda não aparece com resposta nas fontes consultadas. O caso importa porque amplia a frente de litígios estaduais contra desenvolvedores de IA generativa e testa se a publicidade sobre segurança de modelos pode ser tratada como declaração ao consumidor sujeita a sanção.
