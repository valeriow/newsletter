---
layout: post
title: "Radar IA — 06/10/2026, 18h"
date: 2026-10-06 18:00:00 -0300
categories: edicao
excerpt: "Reflection anuncia o Beam, MoE aberto de 501 bilhões de parâmetros sob Apache 2.0; Supabase levanta US$ 150 milhões e compra a Turso porque 70% dos novos bancos já são criados por agentes; OpenAI lança a marca d'água textGrain para atender ao AI Act europeu; TikTok põe checkout direto e MCP no centro da publicidade agêntica; Cohere atualiza a North e a Vida cobra agentes por resultado; Google troca os limites do Gemini por cotas de computação a partir de 9 de outubro."
---

*Janela pesquisada: 04 a 06/10/2026. Foram excluídos Dots, Mods do Claude Code, SerproCODE, Olmo-core 3, llama.cpp /v1/systemone, anúncios no ChatGPT, Superintelligence Force e demais itens já publicados nas edições de 02 a 05/10. Dia de poucas novidades verificáveis: os temas 3 e 4 são curtos de propósito.*

## Destaques do dia

1. **Reflection anuncia o Beam, um MoE aberto de 501 bilhões de parâmetros**: 23 bilhões ativos por token, licença Apache 2.0 e pesos prometidos para este mês, com 80,1 no Terminal-Bench v2.1. → 2.1
2. **Supabase compra a Turso e diz que 70% dos novos bancos nascem de agentes**: US$ 150 milhões de rodada e bancos de dados baratos como arquivos para cada agente. → 1.1
3. **OpenAI lança a marca d'água textGrain por causa do AI Act**: API com adesão opcional desde 5/10 e ChatGPT/Codex na UE nas próximas semanas, mas 25% de sinônimos derrubam a detecção a 17%. → 3.1
4. **TikTok transforma o feed em vitrine de agentes**: checkout direto, assistente de compras e MCP próprio, anunciados na Advertising Week. → 4.1
5. **Agentes corporativos ganham plataforma e novo modelo de cobrança**: Cohere atualiza a North para empresas e governos, e a Vida cobra agentes por resultado de vendas. → 1.2, 1.3
6. **Google troca limites do Gemini por cotas de computação**: a partir de 9/10, janelas de cinco horas e múltiplos de 2x a 20x conforme o plano. → 4.2

## 1. Novidades de IA agêntica

### 1.1 Supabase levanta US$ 150 milhões e compra a Turso para dar um banco de dados a cada agente
**Fonte:** [Pulse 2.0](https://pulse2.com/supabase-raises-150-million-and-acquires-turso/) (02/10) · [Dealroom](https://dealroom.co/news/158564-supabase-raises-150m-buys-turso-to-chase-the-agent-database-boom/) (02/10)

A Supabase anunciou uma Série G de US$ 150 milhões, liderada pela GIC, e a aquisição da Turso, cuja arquitetura permite provisionar um número enorme de bancos isolados a baixo custo, na nuvem pública ou no ambiente do cliente. O número que justifica a compra: segundo a empresa, cerca de 70% dos bancos criados hoje na plataforma são abertos por agentes ou ferramentas de IA, e a base cresce mais de 1 milhão de usuários e 4 milhões de bancos por mês. Glauber Costa, fundador da Turso, vira Head of Agentic Services. Para quem projeta sistemas agênticos, o sinal é arquitetural: o padrão "um banco por agente ou por tarefa" está virando infraestrutura de produção, e isso traz questões de isolamento, custo por instância e governança dos dados que o agente cria sozinho. Os números são declarados pela própria empresa e não foram verificados de forma independente.

### 1.2 Cohere atualiza a plataforma North com mais autonomia para empresas e governos
**Fonte:** [The Globe and Mail](https://www.theglobeandmail.com/business/technology/article-cohere-new-ai-north-platform-more-agentic-features-for-businesses) (05/10)

A Cohere lançou uma versão atualizada da North, sua plataforma de agentes para o ambiente corporativo, com recursos agênticos que vão além de recuperação de documentos e automação de fluxos, segundo o resumo do veículo. Não foi possível ler a matéria completa (o site bloqueia leitura automatizada), então detalhes de recursos, preços e clientes ficam pendentes de confirmação em fonte primária. O contexto importa: a Cohere se posiciona em implantações privadas e soberanas para clientes regulados e públicos, nicho em que a decisão de compra passa por controle de dados mais do que por ranking de benchmark.

### 1.3 Vida cobra agentes de IA por resultado de vendas, não por licença
**Fonte:** [wallstreet:online](https://www.wallstreet-online.de/nachricht/21478627-vida-introduces-outcome-based-billing-for-ai-agents) (05/10)

A Vida passou a oferecer cobrança por resultado para agentes que qualificam leads, transferem clientes, fazem onboarding e retenção: a tarifa fica atrelada a resultados comerciais mensuráveis. É um comunicado da própria empresa, mas aponta uma tendência real: se o agente é pago por resultado, a avaliação do sistema agêntico deixa de ser exercício acadêmico e vira cláusula contratual, com definição de métrica, atribuição e auditoria. Para pesquisadores, é um campo aberto para trabalhos sobre medição causal do desempenho de agentes em produção.

### 1.4 Meta Muse teria criado perfis de pessoas do círculo dos usuários sem consentimento
**Fonte:** Gizmodo, citado pelo [AI Agents Directory](https://aiagentsdirectory.com/news) (05/10)

Segundo o resumo diário do AI Agents Directory, que cita o Gizmodo, o agente Muse da Meta teria montado perfis de pessoas do entorno social dos usuários sem consentimento delas. Não consegui acessar a reportagem original, por isso trato como alegação ainda não confirmada. Se verdadeira, é um caso típico do risco de agentes pessoais que acumulam memória sobre terceiros, com implicações diretas para a LGPD e o GDPR, que protegem quem não é o usuário do serviço.

## 2. Ferramentas e modelos open source

### 2.1 Reflection anuncia o Beam: MoE de 501 bilhões de parâmetros, Apache 2.0, pesos ainda neste mês
**Fonte:** [Reflection AI](https://reflection.ai/blog/introducing-beam) (05/10)

O Beam é o primeiro modelo aberto da Reflection, voltado a código, raciocínio e tarefas agênticas: um Mixture-of-Experts esparso com 501 bilhões de parâmetros no total e 23 bilhões ativos por token, treinado com 23,8 trilhões de tokens e mais de 100 milhões de rollouts de aprendizado por reforço em 10.500 GPUs GB300, segundo a empresa. Os resultados divulgados incluem 77,2 no SWE-Bench Pro v2-Hard e 80,1 no Terminal-Bench v2.1, comparáveis a GLM 5.2 e Qwen 3.8-Max, com a alegação de usar de 3 a 4 vezes menos computação de inferência. Atenção: hoje há apenas anúncio e inscrição para acesso antecipado; pesos, ficha técnica e ferramentas estão prometidos para outubro, sob Apache 2.0, e não houve divulgação de preços. Importa porque seria um modelo de fronteira aberto feito nos Estados Unidos, onde a oferta aberta competitiva vinha majoritariamente de laboratórios chineses. Vale esperar a liberação dos pesos e a replicação independente dos benchmarks.

### 2.2 Together Link: CLI com licença MIT liga Claude Code, Codex e OpenCode a modelos abertos
**Fonte:** [LLM Stats](https://llm-stats.com/ai-news) (05/10), citando Planet AI

A Together AI lançou o Together Link, ferramenta de linha de comando gratuita sob licença MIT que conecta agentes de código como Claude Code, Codex e OpenCode, além de aplicativos de desktop, a modelos abertos como Kimi K3 e GLM 5.3. Só consegui confirmar o item por um agregador, sem a página primária. O interesse prático está em trocar o modelo por trás de um harness conhecido sem reescrever o fluxo, o que facilita comparar modelos abertos em tarefas reais de engenharia de software.

### 2.3 Runway apresenta o Praxis-1, modelo de ação de mundo de pesos abertos para robótica
**Fonte:** [The Deep View](https://www.thedeepview.com/articles/runway-ceo-sees-a-much-bigger-future-for-video-ai) (02/10)

A Runway descreve o Praxis-1 como um "world action model" de pesos abertos que se adapta a novos corpos robóticos com ajuste fino leve. O CEO, Cristóbal Valenzuela, afirma que modelos de vídeo e de mundo são "máquinas de generalização" e projeta de 12 a 18 meses até implantações em produção. A matéria não traz licença, benchmarks nem detalhes de treinamento, então é um sinal de direção (previsão de próximo quadro aplicada à robótica), não um modelo avaliado. Data de 02/10, um pouco fora da janela, incluída por não ter sido coberta antes.

## 3. IA aplicada no setor público

*Brasil*

*Nenhuma novidade nova e verificável nas últimas 48 horas. Seguem valendo, já noticiados em edições anteriores, o prazo de 8 de outubro para as propostas do supercomputador de IA do MCTI e a compra unificada de multicloud de TCU, CGU e CNJ.*

*Internacional*

### 3.1 OpenAI lança a marca d'água textGrain para cumprir a transparência exigida pelo AI Act europeu
**Fonte:** [OpenAI](https://openai.com/index/eu-text-provenance/) (05/10)

O textGrain embute um sinal estatístico invisível nas escolhas de palavras do modelo, detectável depois por um verificador. A OpenAI diz que o AI Act exige que provedores de IA generativa tornem o texto identificável por meios legíveis por máquina. Desde 05/10, clientes da API em todo o mundo podem ativar a marca de forma opcional; nas próximas semanas, ChatGPT e Codex passam a marcar saídas na União Europeia, e o detector fica restrito a pesquisadores e organizações aprovadas. Com 1% de falsos positivos, a detecção chega a cerca de 80% em trechos de 200 tokens e 95% em 400 tokens, cai para 66% se 10% das palavras forem trocadas e para 17% com 25% de troca, e é pior em matemática do que em psicologia. A leitura honesta é que serve para texto copiado sem edição, não para provar autoria em casos adversariais, o que importa para quem pensa em fiscalização, ensino e integridade de documentos públicos.

### 3.2 Campanha "Team Human" reúne assinaturas por uma desaceleração internacional da IA de fronteira
**Fonte:** [Team Human](https://www.teamhuman.org/) (05/10), citada pelo [AI-Weekly](https://ai-weekly.ai/newsletter-10-06-2026)

Uma campanha liderada por criadores de conteúdo e apoiada pelo Center for AI Safety busca assinaturas por uma desaceleração internacional do desenvolvimento de IA de fronteira, propondo controle de chips, limites nacionais e um órgão fiscalizador inspirado na supervisão nuclear. Não é ato de governo, mas alimenta o debate regulatório que já inclui o pacto voluntário e a investigação da FTC cobertos na edição semanal de 04/10. Registro apenas o fato e a proposta; a adesão efetiva não foi verificada.

## 4. IA aplicada em geral

### 4.1 TikTok leva checkout direto, assistente de compras e MCP próprio à publicidade
**Fonte:** [TikTok Newsroom](https://newsroom.tiktok.com/tiktok-unveils-ai-powered-updates-for-advertisers-driving-discovery-action-and-measurable-business-outcomes) (05/10)

Na Advertising Week de Nova York, o TikTok apresentou o "Buy Direct" (compra com um toque a partir do feed), o Shopping Assistant conversacional, o Agentic Leads para captação e qualificação de leads e a expansão da rede de anúncios para cerca de 400 mil aplicativos. O TikTok for Business MCP, protocolo aberto para agentes em fluxos de publicidade, já está disponível em Claude, Perplexity e Snowflake, e a empresa afirma que o uso por anunciantes cresceu 200% desde o lançamento (dado da própria empresa). Importa porque confirma que o MCP saiu do universo de desenvolvedores e virou interface de plataformas de anúncio, e que o comércio por agentes avança, depois do movimento da Shopify na semana passada.

### 4.2 Google troca limites fixos do Gemini por cotas de computação a partir de 9 de outubro
**Fonte:** [Google Support](https://support.google.com/gemini/answer/17004136) (05/10), citado pelo [AI-Weekly](https://ai-weekly.ai/newsletter-10-06-2026)

Segundo o resumo do AI-Weekly, o Gemini passa a usar limites baseados em computação, renovados a cada cinco horas, com múltiplos de 2x no AI Plus, 4x no Pro e de 5x a 20x no Ultra; usuários sem assinatura são afetados a partir de 9 de outubro. Não abri a página oficial, então os detalhes devem ser conferidos nela. O movimento mostra a mudança de "mensagens por dia" para orçamento de computação, coerente com agentes que consomem muito mais tokens por tarefa, e é um dado relevante para quem planeja uso de ferramentas em pesquisa.

### 4.3 a16z: tecnologia responde por 76% do crescimento dos lucros do S&P 500, mas só 2% das empresas medem IA ao longo do tempo
**Fonte:** [a16z](https://a16z.com/state-of-markets-ii) (04/10), citado pelo [AI-Weekly](https://ai-weekly.ai/newsletter-10-06-2026)

O relatório "State of Markets" da a16z afirma que tecnologia explica 76% do crescimento de lucros do S&P 500 neste ano, que apenas 2% das empresas divulgam métricas de IA acompanhadas ao longo do tempo e que o capex passou de US$ 416 bilhões em 2025 para uma estimativa de US$ 777 bilhões em 2026 e US$ 1,1 trilhão em 2027. Dados de segunda mão, a conferir no relatório. Complementa a discussão da semana passada sobre a conta dos laboratórios: o investimento é visível, o retorno medido ainda não.
