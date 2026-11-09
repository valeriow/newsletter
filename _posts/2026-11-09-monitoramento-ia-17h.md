---
layout: post
title: "Radar IA — 09/11/2026, 17h"
date: 2026-11-09 17:06:00 -0300
categories: edicao
excerpt: "DeepSeek lança o Creator Mode no Harness para criar plugins de agente por conversa; Google teria entregue seu runtime de agentes à CNCF; Perplexity oferece agentes sempre ativos por US$ 200 ao mês; Anthropic atualiza a política de uso a partir de 12/11; big techs apoiam mecanismo comum de opt-out contra scraping; Qwen 4 segue sem pesos nem data."
---

*Janela pesquisada: 6 a 9/11/2026, com itens de 2 a 4/11 que não haviam entrado nas edições anteriores. Excluídos por já terem sido cobertos nas edições de 5 a 8/11: Meta/Conductor, Android Studio "Rabbit 2", Kimi K3.1 Pro, ERNIE 5.5 Flash Base, IPO da Anthropic, Claude Marketplace, Message Threads, blueprint multiagente da AWS, Semana de IA do Serpro e INPS. Segunda-feira com poucas novidades primárias: vários sites não puderam ser abertos nesta execução e os itens abaixo se apoiam em resultados de busca e agregadores, o que está sinalizado em cada caso.*

## Destaques do dia

1. **DeepSeek leva o "Creator Mode" ao Harness**: o framework open source de agentes agora permite criar plugins descrevendo-os em conversa, o que aproxima o desenvolvimento de agentes da linguagem natural, com ressalvas de segurança. → 1.1, 2.1
2. **Google teria doado seu runtime de agentes à CNCF**: relato de agregador, sem confirmação primária, aponta para padronização do ambiente de execução de agentes sob governança neutra. → 1.2
3. **Perplexity vende agentes sempre ativos por US$ 200 ao mês**: agentes persistentes viram assinatura de consumidor avançado. → 1.3
4. **Anthropic atualiza sua Política de Uso a partir de 12/11**: novas regras sobre campanhas enganosas, decisões de alto risco e agentes que agem no mundo físico. → 1.4
5. **Big techs convergem em um sinal comum de opt-out contra scraping**: OpenAI, Google, Microsoft e Anthropic apoiam o mecanismo, mas a OpenAI só o implementará nos próximos meses. → 4.1
6. **Qwen 4 continua sem pesos, data ou licença**: a Alibaba declara intenção de abrir os modelos, mas nada foi publicado, e o Command A+ da Cohere, que circula nos agregadores, é de maio. → 2.2

## 1. Novidades de IA agêntica

### 1.1 DeepSeek lança o Creator Mode no Harness
**Fonte:** [Implicator](https://www.implicator.ai/deepseek-releases-creator-mode-allows-deepseek-harness-users/) (02/11) · [DeepSeek Harness (developer preview)](https://deepseek.com/harness/en/) · [Unite.AI](https://www.unite.ai/deepseek-harness-adds-plugin-creation-entry-for-creator-mode/)

O Harness é o framework de agentes da DeepSeek, organizado em torno de plugins intercambiáveis. O Creator Mode é um preset que herda o modo padrão e acrescenta inspeção do runtime, testes de plugins em memória e orientação para compor novos modos, de modo que o usuário descreve em linguagem natural o plugin que deseja e o agente o constrói. As demonstrações incluem um timer pomodoro, um renderizador 3D e uma bancada de edição de vídeo. Por que importa: reduz a barreira para personalizar harnesses de agentes e é um bom objeto de estudo para quem pesquisa orquestração e extensibilidade. A ressalva é que plugins são código executável; um relato secundário (Tech Jacks Solutions) afirma que as diretrizes de contenção em sandbox do Creator Mode ainda não foram avaliadas de forma independente, e a própria DeepSeek chama o Harness de experimental. A data (2/11) é anterior à janela, mas o item não havia sido coberto.

### 1.2 Google teria entregue seu runtime de agentes à CNCF, e big techs falam em fundação para padrões de agentes
**Fonte:** [Resultado de busca sobre roundup n8n Lab](https://n8nlab.io/news/ai-news-roundup-november-five) (início de novembro) · [Machina Nova](https://machinanova.beehiiv.com/p/ai-deals-chip-smuggling-and-wall) (sem data clara)

Dois agregadores relatam que o Google transferiu seu runtime de agentes para a Cloud Native Computing Foundation (CNCF), a fundação que abriga o Kubernetes, e que OpenAI, Anthropic, Google, Microsoft e Amazon estariam se reunindo em um grupo chamado Agentic Artificial Intelligence Foundation para padrões compartilhados. Não foi possível abrir as páginas nem localizar anúncio primário, portanto trate como informação não confirmada. Se verdadeira, a mudança importa porque um runtime sob governança neutra reduz o risco de aprisionamento a fornecedor e pode se tornar base comum para interoperabilidade, semelhante ao que o MCP fez com ferramentas.

### 1.3 Perplexity coloca agentes sempre ativos em plano de US$ 200 ao mês
**Fonte:** [Resultado de busca sobre roundup n8n Lab](https://n8nlab.io/news/ai-news-roundup-november-five) (início de novembro)

O mesmo agregador afirma que a Perplexity passou a oferecer agentes que rodam continuamente atrás de uma assinatura de US$ 200 mensais. Sem fonte primária acessível, os detalhes de funcionalidade e limites não puderam ser verificados. O sinal relevante é de mercado: agentes persistentes, que monitoram e agem sem pedido a cada passo, saem do nicho corporativo para planos de consumidor avançado, o que traz à tona perguntas de custo, permissões e auditoria.

### 1.4 Anthropic atualiza a Política de Uso, com vigência em 12/11
**Fonte:** [Resultado de busca sobre roundup n8n Lab](https://n8nlab.io/news/ai-news-roundup-november-five) (início de novembro)

Segundo o resumo encontrado, a política atualizada, em vigor a partir de 12 de novembro, esclarece regras para campanhas de desinformação, decisões de alto risco em saúde e finanças, vigilância e agentes que executam ações físicas. Não foi possível ler o texto oficial; confira a página de políticas da Anthropic antes de citar. Para equipes que constroem sistemas agênticos sobre a API, vale revisar os casos de uso, pois a menção a agentes com ação física indica que a responsabilidade do desenvolvedor sobre o comportamento do agente está sendo explicitada.

## 2. Ferramentas e modelos open source

### 2.1 DeepSeek Harness é open source, com licença reportada como MIT
**Fonte:** [Better Stack](https://betterstack.com/community/guides/ai/deepseek-harness-plugin/) · [The New Stack](https://thenewstack.io/deepseek-harness-open-source-plugins/?p=22833516)

O código do Harness, incluindo o Creator Mode, é descrito por uma fonte como publicado sob licença MIT; outra ressalva que a licença é "reportada" e que não está claro se cobre todos os componentes. Para estudantes, é um framework de agentes com arquitetura de plugins que pode ser lido, modificado e usado em experimentos de pesquisa. Verifique o arquivo de licença do repositório antes de uso comercial.

### 2.2 Qwen 4: ainda sem pesos, data ou licença
**Fonte:** [Overchat](https://overchat.ai/ai-hub/qwen-4-release-date) (atualizado em 07/11) · [Tech Insider](https://tech-insider.org/qwen4-four-variants-no-confirmed-open-weights-alibaba-2026/)

A Alibaba apresentou a família Qwen 4 no evento Apsara de 22/09, incluindo uma faixa de 27B prometida como open weights, mas até 7/11 não havia data oficial, preço nem pesos publicados. O Qwen3.8-Flash-Next (26/08) foi lançado como prévia da arquitetura, sob licença qwen-community, não Apache. O ponto prático: não planeje projetos assumindo disponibilidade ou licença do Qwen 4. O Command A+ da Cohere (218B MoE, 25B ativos, Apache 2.0), que ainda aparece em roundups, foi lançado em 20/05/2026 e por isso não é novidade desta janela.

## 3. IA aplicada no setor público

*Brasil e internacional: sem novidades reais e datadas nas últimas 24-48 horas. O ataque "sem precedentes" ao Gov.br e a proposta de plataforma comum de IA do MGI já foram cobertos na edição de 8/11, e as buscas não encontraram medida federal, regulamentação ou caso internacional novo. Os casos que aparecem nos resultados (agentes de IA no governo dos Emirados, testes de agentes no GOV.UK a partir de 2027, Estônia) são de meses anteriores. Preferi não preencher o tema com conteúdo antigo.*

## 4. IA aplicada em geral

### 4.1 OpenAI, Google, Microsoft e Anthropic apoiam mecanismo comum de opt-out contra scraping
**Fonte:** [Resultado de busca sobre roundup n8n Lab](https://n8nlab.io/news/ai-news-roundup-november-five) (início de novembro)

De acordo com o resumo encontrado, as quatro empresas respaldam um sinal padronizado para que publicadores recusem o uso de seus conteúdos em coleta para IA. A Anthropic já respeitaria o sinal; a OpenAI planeja implementá-lo nos próximos meses. Não foi possível acessar a fonte original, então detalhes técnicos (formato do sinal, escopo) não foram verificados. Importa para empresas e órgãos que publicam conteúdo e para quem treina modelos, pois um padrão único simplifica a conformidade e pressiona as demais empresas a seguir.
