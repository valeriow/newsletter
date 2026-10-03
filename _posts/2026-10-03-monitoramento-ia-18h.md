---
layout: post
title: "Radar IA — 03/10/2026, 18h"
date: 2026-10-03 18:00:00 -0300
categories: edicao
excerpt: "DigitalOcean empacota agentes gerenciados em planos mensais fixos; Microsoft lança transcrição em tempo real para agentes de voz; Autonomize cria camada de contexto para agentes de saúde; o TJRS desenvolve agentes próprios com a AWS para cortar custo de tokens; Samsung promete celulares que agem em nome do usuário; startup de ataques com IA do fundador da Mandiant capta US$ 255,5 milhões."
---

*Janela pesquisada: 01/10 a 03/10/2026. Excluídos os temas já cobertos nas edições de 28/09 a 02/10 (dots e GPT-6.1 Sol da OpenAI, Gemini 4 Argon e Fairwind, FTC, Strands Decider e Clef, Nvidia Open Agent Safety Platform, VigIA, Nuvem Brasileira). Sábado, com poucas novidades técnicas: onde não houve fato novo, isso está dito.*

## Destaques do dia

1. **DigitalOcean vende agentes em pacote fixo**: os planos Agent Droplets (US$ 50 e US$ 200 por mês) juntam runtime gerenciado, inferência, memória persistente e governança de ferramentas, para dar previsibilidade de custo. → 1.1
2. **Microsoft mira agentes de voz**: o MAI-Transcribe-2-Streaming é o primeiro modelo de transcrição em tempo real da empresa, pensado para conversas com latência baixa. → 1.2
3. **Agentes de saúde ganham camada de contexto**: a Autonomize lança o Context AI, com ontologias e políticas compartilhadas, rastreabilidade e auditoria para autorizações e pagamentos. → 1.3
4. **Tribunal gaúcho constrói os próprios agentes**: o TJRS, com a AWS, quer cortar o custo de tokens enquanto o GAIA já atende 1.500 dos 5.000 processos diários. → 3.1
5. **Samsung aposta no celular que age por você**: o Samsung AI Forum apresentou o "Agentic Shift", com plataforma agêntica no aparelho. → 4.1
6. **Segurança ofensiva com IA atrai capital**: a Armadin, do fundador da Mandiant, levantou US$ 255,5 milhões para encadear vulnerabilidades em caminhos de ataque. → 4.2, 1.4

## 1. Novidades de IA agêntica

### 1.1 DigitalOcean lança o Agent Droplets, agentes gerenciados em plano mensal fixo
**Fonte:** [AI Agent Store](https://aiagentstore.ai/ai-agent-news/this-week) (02/10) · [DigitalOcean, Managed Agents](https://digitalocean.com/blog/managed-agents-public-preview) (22/09, contexto)

A DigitalOcean passou a oferecer o Agent Droplets em duas faixas, Pro (US$ 50 por mês) e Team (US$ 200 por mês), reunindo runtime gerenciado de agentes, inferência serverless, memória persistente e governança de ferramentas. A base é o Managed Agents, aberto em prévia pública em 22/09, com microVMs, sandbox de código e um gateway de ações via MCP (Model Context Protocol) para milhares de ferramentas. Importa porque o custo imprevisível, cobrado por token e por segundo de CPU, é um dos obstáculos de levar agentes à produção; um preço fixo é uma resposta de produto a isso. Para quem estuda orquestração, é um exemplo de como o "harness" do agente (runtime, memória, permissões) está virando serviço de prateleira.

### 1.2 Microsoft apresenta o MAI-Transcribe-2-Streaming, transcrição em tempo real para agentes de voz
**Fonte:** [AI Agents Directory](https://aiagentsdirectory.com/news/ai-agents-news-brief-october-2-2026) (01/10 e 02/10) · [eWeek, MAI-Transcribe-2](https://www.eweek.com/news/microsoft-10-cent-ai-transcription-mai-transcribe-2/) (04/09, contexto)

A Microsoft lançou a variante em streaming do MAI-Transcribe-2, seu primeiro modelo de fala para texto em tempo real, segundo a cobertura da SiliconANGLE e da BigGo Finance reunida no resumo diário. A versão em lote, de setembro, custava US$ 0,10 por hora de áudio em tarifa promocional e continuava em prévia pública, sem SLA. Para agentes de voz, a latência da transcrição define se a conversa soa natural; por isso um modelo próprio reduz a dependência da Microsoft de provedores externos de fala. Os detalhes de preço e latência da versão streaming não puderam ser confirmados em fonte primária nesta edição.

### 1.3 Autonomize lança o Context AI, camada de contexto para agentes de saúde
**Fonte:** [AI Agent Store](https://aiagentstore.ai/ai-agent-news/this-week) (02/10)

A Autonomize anunciou uma camada de contexto compartilhada, com ontologias e políticas, para agentes que atuam em sinistros, autorização prévia e integridade de pagamentos na saúde. O foco declarado é rastreabilidade e auditabilidade em ambiente regulado. A tese é que agentes falham menos quando regras de negócio e vocabulário do domínio ficam em uma camada explícita, em vez de embutidas em prompts. É um padrão de arquitetura que vale acompanhar também em outros setores regulados, como o público.

### 1.4 Gemini 4 Argon enfrenta ceticismo interno no Google, segundo o Los Angeles Times
**Fonte:** [AI Agents Directory](https://aiagentsdirectory.com/news/ai-agents-news-brief-october-2-2026) (01/10, citando o Los Angeles Times)

Segundo o resumo diário que cita o Los Angeles Times, há dúvidas dentro do Google sobre o desempenho do Gemini 4 Argon em áreas como programação, apesar da liderança em benchmarks anunciada no lançamento, já coberto em 30/09. Trata-se de uma reportagem de imprensa, não de dado oficial, e não foi possível ler o texto original. Serve de lembrete de que ranking em benchmark e uso real em código nem sempre coincidem, e vale testar o modelo na sua própria tarefa antes de decidir.

## 2. Ferramentas e modelos open source

*Sem novidades reais nas últimas 24 a 48 horas: os lançamentos abertos mais recentes encontrados (Strands Decider 2B e Clef, da Cloudflare) já foram cobertos na edição de 01/10 e 02/10.*

## 3. IA aplicada no setor público

*Brasil*

### 3.1 TJRS desenvolve agentes de IA próprios com a AWS para reduzir o custo de tokens
**Fonte:** [Convergência Digital](https://convergenciadigital.com.br/inovacao/tribunal-de-justica-do-rio-grande-do-sul-cria-agentes-ia-proprios-para-reduzir-custo-dos-tokens) (02/10)

O Tribunal de Justiça do Rio Grande do Sul criou, em parceria com a AWS, agentes de IA próprios, hoje em fase de homologação, para reduzir o custo de tokens. O sistema GAIA já é usado em cerca de 1.500 dos 5.000 processos que o tribunal recebe por dia, na análise de petições iniciais, e deve chegar a 350 mil advogados nos próximos dias. O GAIA é desenvolvido em conjunto com outros cinco grandes tribunais brasileiros, e o TJRS montou uma força-tarefa de TI para detectar uso indevido de IA. O caso mostra o Judiciário migrando de pilotos para escala e tratando custo de inferência como variável de gestão, não só de tecnologia.

*Internacional*

*Sem novidades reais nas últimas 24 a 48 horas além do que já foi coberto nas edições anteriores.*

## 4. IA aplicada em geral

### 4.1 Samsung apresenta o "Agentic Shift" e promete celulares que agem em nome do usuário
**Fonte:** [AI Agent Store](https://aiagentstore.ai/ai-agent-news/this-week) (01/10)

No Samsung AI Forum 2026, com o tema "Agentic Shift: From Intelligence to Impact", a empresa disse que os Galaxy evoluirão para aparelhos que agem em nome do usuário, e que os próximos S26 e Z Fold8 terão uma plataforma agêntica no próprio dispositivo. É um anúncio de direção, sem datas nem especificações. Importa porque leva agentes ao hardware de consumo em massa, com questões de privacidade e de permissões muito mais sensíveis do que em ferramentas de nuvem.

### 4.2 Armadin, do fundador da Mandiant, capta US$ 255,5 milhões para testes ofensivos com IA
**Fonte:** [AI Agents Directory](https://aiagentsdirectory.com/news/ai-agents-news-brief-october-2-2026) (01/10 e 02/10)

A startup de segurança Armadin levantou uma Series B de US$ 255,5 milhões, com a a16z e a Accel, para desenvolver software que encadeia vulnerabilidades em caminhos de ataque acionáveis, usando IA para testar defesas de empresas. O volume do aporte confirma o apetite de investidores por IA ofensiva e defensiva, num momento em que modelos como o Gemini 4 Argon chegam primeiro a defensores de cibersegurança.

### 4.3 Reportagens indicam conversas da OpenAI por financiamento que a avaliaria em US$ 1,4 trilhão
**Fonte:** [AI Agents Directory](https://aiagentsdirectory.com/news/ai-agents-news-brief-october-2-2026) (01/10, citando Wowtale)

Segundo reportagens agregadas no resumo diário, a OpenAI estaria em conversas de financiamento que a avaliariam em US$ 1,4 trilhão, no mesmo período do DevDay. São informações de imprensa, sem confirmação da empresa. Importa como termômetro do tamanho da aposta do mercado em agentes pessoais e infraestrutura de IA.
