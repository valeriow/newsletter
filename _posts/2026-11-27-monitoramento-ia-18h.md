---
layout: post
title: "Radar IA — 27/11/2026, 18h"
date: 2026-11-27 18:00:00 -0300
categories: edicao
excerpt: "Versões do Microsoft Agent Framework com código roubador de credenciais retiradas do PyPI; portaria do CNPq sobre IA em pesquisas financiadas; Emirados Árabes Unidos ampliam IA no governo com 17 parceiros; IBM e Microsoft lançam plataforma de agentes por setor; prova atribuída ao GPT-6.2 Astra revisita palpite de Erdős, com verificação parcial; Agent S v0.3.3 traz agente aberto de uso de computador"
---

*Janela pesquisada: 25 a 27/11/2026 para os temas 1 a 4 (com itens mais antigos marcados pela data, quando ainda não cobertos) e 20 a 27/11/2026 para o tema 5. Excluídos por já terem sido cobertos nas edições anteriores: GPT-6.2 Astra e Sol, o IPO da Anthropic, o Genie ZeroOps, o contrato de voz do governo britânico, o registro de modelos de IA no Reino Unido, a Febraban e os desdobramentos da alegada prova de Riemann e de Navier–Stokes.*

## Destaques do dia

1. **Versões do Microsoft Agent Framework com código roubador de credenciais**: as versões 1.26.1 e 1.26.2, publicadas em 17/11, foram retiradas; a 1.26.0 é a última limpa e vale fixar a versão. → 1.1
2. **Portaria do CNPq regula IA em pesquisas financiadas**: os autores continuam responsáveis pela validação final do conteúdo e essa checagem não pode ser delegada a ferramentas de IA. → 3.1
3. **Emirados Árabes Unidos ampliam IA no governo**: 17 novos parceiros entram no ecossistema e a meta é usar agentes em 50% dos processos em dois anos, mas ainda sem resultados verificados. → 3.2
4. **IBM e Microsoft lançam plataforma de agentes por setor**: a Imagine Enterprise traz mais de 6 mil agentes pré-construídos, com estreia em serviços financeiros, seguros e varejo. → 4.1
5. **Prova atribuída ao GPT-6.2 Astra desafia palpite de Erdős de 1987**: a checagem em Lean cobre apenas parte do argumento, e o restante do artigo ainda não foi verificado. → 5.1
6. **Agent S v0.3.3 traz agente de código aberto para uso do computador**: a versão inclui instalador notarizado e suporte a modelos locais, o que facilita rodar a ferramenta sem depender de API externa. → 2.1

## 1. Novidades de IA agêntica

### 1.1 Microsoft Agent Framework: versões 1.26.1 e 1.26.2 publicadas com código roubador de credenciais
**Fonte:** [StepSecurity](https://www.stepsecurity.io/blog/microsoft-agent-framework-pypi-package-compromised) (17/11)

O pacote `agent-framework`, o framework de código aberto da Microsoft para construir e orquestrar agentes em Python e .NET, teve duas versões publicadas no PyPI com código malicioso capaz de roubar credenciais, segundo a análise da StepSecurity. As versões foram colocadas em quarentena e a última limpa é a 1.26.0, lançada normalmente em 12/11. O caso importa para quem roda agentes em pipelines de CI ou com acesso a nuvem, porque um pacote de dependência comprometido costuma ter acesso exatamente aos segredos que o agente usa. A recomendação prática é fixar a versão 1.26.0 e revisar o ambiente caso alguma das versões retiradas tenha sido instalada. Ressalva: o detalhe técnico vem de trechos de busca do relatório, e não da leitura completa da análise.

### 1.2 Microsoft amplia o Agent 365 no Ignite e informa mais de 50 milhões de agentes registrados
**Fonte:** [Dellenny](https://dellenny.com/microsoft-agent-365-at-ignite-2026-enterprise-ai-governance-security-and-management-explained/) (17 a 20/11)

Durante o Ignite, a Microsoft expandiu o Agent 365, plataforma para observar, governar e proteger agentes dentro das empresas, com melhor descoberta de agentes, gestão de identidade e controles de segurança adaptativos. Segundo a cobertura, mais de 50 milhões de agentes foram registrados desde o lançamento em maio. Esse número é da própria empresa, reproduzido por um veículo secundário, e não foi verificado de forma independente. O movimento mostra que a camada de governança (inventário, identidade e auditoria de agentes) está virando produto, e não apenas uma preocupação de compliance.

## 2. Ferramentas e modelos open source

### 2.1 Agent S v0.3.3: agente de código aberto para uso do computador, com instalador notarizado e modelos locais
**Fonte:** [Repositório Agent S no GitHub (Simular AI)](https://github.com/simular-ai/Agent-S) (24/11)

A versão 0.3.3 do Agent S, um agente de código aberto que controla o computador por meio de interface gráfica, foi publicada em 24/11, segundo o README do projeto. As novidades são um instalador para desktop notarizado e suporte a modelos locais, o que permite rodar o agente sem enviar a tela para uma API externa. Para pesquisa e para testes de automação, isso reduz custo e facilita reprodução de experimentos. Ponto de atenção: a publicação é de três dias atrás, fora da janela de 48 horas, e ainda não há benchmark independente que compare a versão com outros agentes de uso do computador.

*Nenhum outro lançamento open-weight ou de biblioteca com data confirmada nas últimas 48 horas foi encontrado. Os modelos recentes que apareceram nas buscas (MiniMax H3-Image, em 10/11; Tencent Hy4, em 04/11; Meta Muse Spark Open e StepFun Step 5 Preview, sem data confirmada) ficaram de fora por estarem fora da janela ou sem data verificável.*

## 3. IA aplicada no setor público

*Brasil*

### 3.1 Portaria do CNPq estabelece regras para uso de IA generativa e preditiva em pesquisas financiadas
**Fonte:** [Portaria CNPq nº 3.004/2026, no Diário Oficial da União (via Atlas Público)](https://atlaspublico.com.br/regulacao/dou/portaria-cnpq-n-3-004-de-16-de-novembro-de-2026-931501) (publicada em 18/11)

A Portaria CNPq nº 3.004, de 16/11/2026, define orientações para o emprego de ferramentas de IA generativa e preditiva em projetos financiados pelo CNPq. O ponto central é a responsabilidade: os autores respondem pela validação final do conteúdo produzido com apoio de IA, e essa verificação não pode ser delegada a uma ferramenta de IA. Para quem orienta ou publica pesquisa no Brasil, é um sinal de que a agência tende a tratar o uso de IA como questão de integridade científica, e não só de ferramenta. A fonte consultada é um espelho do DOU; o texto oficial deve ser conferido no Diário Oficial antes de citação formal.

*Internacional*

### 3.2 Emirados Árabes Unidos expandem o ecossistema de IA do governo para 17 parceiros
**Fonte:** [The National](https://www.thenationalnews.com/news/uae/2026/11/27/sheikh-hamdan-oversees-expansion-of-government-ai-ecosystem-as-17-partners-join/) (27/11) · [Gulf News](https://gulfnews.com/business/uae-enlists-17-ai-partners-in-push-to-transform-50-of-government-operations-1.500762957) (27/11)

O governo dos Emirados anunciou a entrada de 17 parceiros nacionais e internacionais no FedAI, seu ecossistema de IA para o setor público. A meta declarada é aplicar IA agêntica a 50% dos setores, serviços e processos governamentais em dois anos. Está prevista ainda a Mira, um agente de atendimento que permitirá ao cidadão acessar serviços no próprio idioma a partir de março. É um anúncio de política e de parcerias, sem métricas de resultado nem auditoria independente. Vale acompanhar se a meta de 50% é acompanhada de indicadores publicados.

## 4. IA aplicada em geral

### 4.1 IBM e Microsoft lançam Imagine Enterprise, plataforma para construir e governar agentes por setor
**Fonte:** [IBM Newsroom](https://newsroom.ibm.com/2026-11-10-ibm-and-microsoft-announce-a-new-ai-agent-platform-designed-for-industry-specific-transformation) (10/11)

A IBM e a Microsoft anunciaram a Imagine Enterprise, uma plataforma para empresas construírem, executarem e governarem agentes específicos por indústria. A IBM Consulting entra com mais de 6 mil agentes e ativos pré-construídos, e a Microsoft com as ferramentas de IA, nuvem e segurança. A estreia é em serviços financeiros, seguros e varejo. O anúncio é de 10/11, fora da janela de 48 horas, e entra aqui porque não foi coberto nas edições anteriores e é um bom exemplo do modelo de venda de agentes prontos por setor, que depende de como os agentes são avaliados em produção, algo que o comunicado não detalha.

### 4.2 Visa amplia o programa Agentic Ready para pagamentos iniciados por agentes entre empresas
**Fonte:** [NDMais](https://ndmais.com.br/economia/negocios/pagamentos-agentes-ia-empresas-visa/) (17/11)

A Visa ampliou em 17/11 o programa Agentic Ready para testar se comerciantes, fornecedores B2B e processadores de pagamento aceitam transações iniciadas por agentes. O piloto anunciado em outubro, com BILL e Billtrust, prevê que o agente execute o pagamento de faturas já aprovadas, sem escolher fornecedor nem assumir compromissos financeiros por conta própria. O caso é relevante porque mostra o desenho de autonomia limitada que o setor financeiro está adotando. A fonte é um veículo de imprensa secundário; o comunicado da Visa não foi consultado.

## 5. Ciência e descobertas com IA

### 5.1 Prova atribuída ao GPT-6.2 Astra desafia palpite de Erdős de 1987; checagem em Lean cobre só parte do argumento
**Fonte:** [Pasquale Pillitteri (notícia)](https://pasqualepillitteri.it/en/news/37114/gpt-6-2-astra-proof-challenges-erdos-s-1987) (26/11)

Uma prova publicada no GitHub em 26/11 e atribuída ao modelo GPT-6.2 Astra contesta um palpite de Paul Erdős, de 1987, sobre fatores primos. Segundo a planilha de formalização que acompanha o caso, duas limitações do resultado original foram verificadas em Lean; o selo de Lean, porém, não cobre tudo, e as partes que existem só no artigo continuam sem verificação. O que está demonstrado é uma versão enfraquecida do palpite; o palpite completo segue em aberto. A autoria da ideia central e o grau de intervenção humana não foram detalhados na fonte consultada. O estado é de preprint/publicação em repositório, sem revisão por pares, e a leitura que a fonte faz da prova não foi conferida no texto original, que não foi aberto nesta sessão. A ressalva importa porque o caso mistura verificação por máquina e afirmações só em prosa, exatamente o ponto que os matemáticos vêm questionando nas últimas semanas.

*Ainda sem novidades de 20 a 27/11 em física, biologia, química ou materiais com resultado verificado. Os desdobramentos da alegada prova de Riemann e de Navier–Stokes já estão cobertos nas edições de 22 a 26/11 e não foram repetidos. Uma retratação de artigo de biomecânica (Taylor & Francis, 19/11) foi descartada: envolve prompt oculto em texto enviado a revisores, não um resultado científico obtido com IA.*
