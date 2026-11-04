---
layout: post
title: "Radar IA — 04/11/2026, 17h"
date: 2026-11-04 17:06:00 -0300
categories: edicao
excerpt: "Anthropic estende a marca d'água invisível a modelos mais antigos do Claude; advogado-geral da UE diz que o Gemini pode violar direitos de editoras ao responder com notícias; AT&T, Snowflake e Saab levam agentes a operações reais; OpenAI compra a Pierre Computer para o Codex e a CrowdStrike compra empresas para proteger agentes; pesos do Kimi K3.1 Pro são esperados em 4 de novembro; Semana de IA Serpro debate soberania em Brasília"
---

*Janela pesquisada: 02/11 a 04/11/2026. Ficaram de fora, por já estarem fora da janela ou já cobertos em edições anteriores: GPT-6.1 Terra e Gemini 4 Carbon (26–28/10), o relato de que a OpenAI compraria TPUs do Google (27–28/10), o protocolo do S-1 da Anthropic e o vídeo de agent-desktop (edições de 01/11 e 03/11). A cobertura de busca desta rodada foi irregular: itens com data ou status incerto estão sinalizados no texto.*

## Destaques do dia

1. **Marca d'água invisível chega a mais modelos do Claude**: desde 3/11, o texto de modelos mais antigos da Anthropic passa a carregar um padrão estatístico detectável, sem opção de desligar, por conformidade com o AI Act europeu. → 4.1
2. **Primeiro caso de IA generativa no tribunal da UE**: o advogado-geral Szpunar opinou que o Gemini pode infringir direitos de editoras ao reutilizar notícias em respostas, mas tratou o treinamento como permitido. → 3.3
3. **Agentes saem do piloto**: AT&T fecha contrato de oito anos com a Amdocs, a Snowflake abre uma ontologia de negócio para agentes e a Saab põe agentes próprios para pilotar um caça Gripen E em testes. → 1.1, 1.2, 1.3
4. **Segurança e ferramentas de agentes puxam fusões**: a OpenAI compra a Pierre Computer para reforçar o Codex e a CrowdStrike adquire duas empresas para proteger agentes corporativos. → 1.4, 1.5
5. **Open source em compasso de espera**: os pesos do Kimi K3.1 Pro eram esperados até 4/11 com relatos conflitantes, o Qwen4 27B segue sem data e projetos de orquestração local ganham tração. → 2.1, 2.2, 2.3, 2.4
6. **Soberania em IA vai à pauta do governo brasileiro**: a II Semana de IA Serpro começa hoje em Brasília, enquanto o marco legal (PL 2338) continua parado na Câmara. → 3.1, 3.2

## 1. Novidades de IA agêntica

### 1.1 AT&T e Amdocs fecham contrato de oito anos para operar a empresa com IA agêntica
**Fonte:** [Converge Digest](https://convergedigest.com/att-amdocs-eight-year-agentic-ai-telecom-operations/) (03/11)

A AT&T ampliou a parceria com a Amdocs num acordo de oito anos para modernizar operações de negócio e atendimento usando o sistema operacional agêntico da Amdocs. O que importa é o horizonte: contratos plurianuais indicam que operadoras tratam agentes como infraestrutura de operação, não como experimento. Para quem estuda o tema, é um bom caso para observar governança, métricas de qualidade e a fronteira entre automação e supervisão humana em telecomunicações. Os termos financeiros não foram detalhados nas fontes consultadas.

### 1.2 Snowflake abre "Business Ontology" e Cortex AI Gateway para agentes corporativos
**Fonte:** [AI Weekly](https://aiweekly.co/alerts/snowflake-expedition-2026-opens-business-ontology-and-cortex-ai-gateway-for) (03/11)

No Expedition 2026, a Snowflake apresentou, em prévia privada, uma camada que dá aos agentes um conjunto único e aprovado de definições de termos de negócio (o que é "receita", "cliente ativo"), além de um gateway para controlar o acesso a modelos. A ideia ataca um problema recorrente: agentes que respondem com números diferentes porque cada equipe define métricas de um jeito. Ontologias compartilhadas tendem a se tornar parte central da camada de dados para agentes, e vale acompanhar se o formato será aberto ou preso à plataforma.

### 1.3 Saab diz que agentes próprios controlaram um Gripen E em combate aéreo além do alcance visual
**Fonte:** [Army Recognition](https://www.armyrecognition.com/news/aerospace-news/2026/saab-tests-its-own-ai-agents-on-gripen-e-fighter-for-autonomous-beyond-visual-range-air-combat) (03/11)

A Saab afirmou ter testado agentes de IA desenvolvidos internamente no controle de um caça Gripen E em cenários de combate além do alcance visual. É um dos exemplos mais claros de agentes com autonomia em sistemas críticos, e levanta o debate sobre verificação, limites de autonomia e responsabilidade. O anúncio é da própria fabricante e não há avaliação independente; o Gripen é também o caça adquirido pelo Brasil, o que dá relevância local ao tema.

### 1.4 OpenAI compra a Pierre Computer para fortalecer o Codex
**Fonte:** [TechBuzz](https://www.techbuzz.ai/articles/openai-acquires-pierre-computer-to-supercharge-codex) (04/11)

A OpenAI anunciou a aquisição da Pierre Computer Company para reforçar sua plataforma de programação Codex. Os termos não constam nas fontes consultadas e a cobertura vem de veículo secundário, então convém aguardar o comunicado oficial. O movimento reforça a disputa por ferramentas de desenvolvimento agênticas, em que a diferenciação passa cada vez mais pelo ambiente de execução em torno do modelo.

### 1.5 CrowdStrike vai adquirir duas empresas para proteger agentes de IA corporativos
**Fonte:** [PYMNTS](https://www.pymnts.com/news/acquiring/2026/crowdstrike-to-acquire-2-firms-to-secure-enterprise-ai-agents/) (data de publicação não confirmada; cobertura na semana de 03/11)

A CrowdStrike planeja comprar duas empresas que acrescentarão observabilidade de IA e testes automatizados de segurança à plataforma Falcon. Quando agentes passam a agir com credenciais e ferramentas reais, monitorar o que fazem e testar suas falhas vira categoria de produto própria. Para profissionais, é um sinal de que "segurança de agentes" está se consolidando como disciplina.

## 2. Ferramentas e modelos open source

### 2.1 Kimi K3.1 Pro: pesos esperados até 4/11, com relatos conflitantes sobre a publicação
**Fonte:** [PANews](https://panews.io/articles/01a1a756-6484-7325-8f81-acd957cdb56c) (05/11, data como exibida) · [AlphaSignal](https://alphasignal.ai/news/moonshot-ai-opens-kimi-k3-1-pro-weights-to-beat-claude-on-coding-agents) · [Braindetox](https://braindetox.kr/en/posts/kimi_k3_1_pro_release_2026.html) (04/11)

O modelo (MoE de 2,8 trilhões de parâmetros totais e 104 bilhões ativos, contexto de 1 milhão de tokens) foi lançado por API em outubro, com pesos prometidos até 4/11. Algumas fontes afirmam que os pesos já foram publicados no Hugging Face; outras, mais cautelosas, dizem não haver ainda ficha do modelo nem licença confirmada. Verifique o repositório oficial antes de usar. A licença do K3 era quase permissiva, mas exigia acordo à parte para quem oferece o modelo como serviço, e não há garantia de que o K3.1 seja igual. Com cerca de 1,6 TB de pesos, rodar localmente está fora do alcance da maioria.

### 2.2 Orkas: equipe local de 16 agentes especializados em alta no GitHub
**Fonte:** [AI Open Source Trends, 04/11](https://github.com/yaojiejia/agents-radar/issues/412) (04/11)

Resumos automáticos de tendências do GitHub destacam o Orkas, descrito como uma "equipe" local-first de agentes que coordena 16 papéis especializados e passa de 7 mil estrelas. Os números variam entre os resumos e o projeto pode estar em alta por popularidade e não por lançamento recente. Útil como exemplo do padrão de orquestração multiagente rodando na máquina do desenvolvedor, mas avalie maturidade e segurança antes de adotar.

### 2.3 beacon.sh: ferramenta aberta de memória para agentes de código
**Fonte:** [AI Agents News, semana de 03/11](https://aiagentstore.ai/ai-agent-news/this-week) (03/11)

Um resumo diário registra o lançamento do beacon.sh, ferramenta de código aberto que dá memória persistente a agentes de programação. Memória entre sessões é uma das lacunas práticas de agentes de código, mas há poucos detalhes verificáveis; trate como ponto de partida para exploração, não como recomendação.

### 2.4 Qwen4 27B segue sem pesos publicados
**Fonte:** [Yotta Labs](https://www.yottalabs.ai/post/qwen-4-27b-release-date-specs-hardware-what-is-known-2026) · [Manifold Markets](https://manifold.markets/Terminator2/will-alibaba-publish-open-weights-f) (última checagem: 24/10)

A Alibaba anunciou em setembro uma faixa de 27B com pesos abertos, mas as últimas fontes que consegui verificar (fim de outubro) não mostravam pesos nem licença. Não há novidade confirmada nas últimas 48 horas; o item registra que a expectativa continua em aberto. O antecessor foi lançado sob Apache 2.0, mas isso não garante a licença do Qwen4.

## 3. IA aplicada no setor público

*Brasil*

### 3.1 II Semana de IA Serpro debate "IA Soberana" de 4 a 6 de novembro
**Fonte:** [Serpro, página do evento](https://campanhas.serpro.gov.br/semana-de-ia-serpro/) · [Serpro, notícia](https://www.serpro.gov.br/menu/noticias/noticias-2026/segunda-semana-ia-serpro) (04/11)

O evento começa hoje em Brasília e online, com o tema "IA Soberana: Dados, Tecnologia e Poder de Decisão". A programação inclui painéis sobre quem controla a IA no setor público, IA soberana em nuvem, uma aliança para infraestrutura soberana e apresentações sobre a Plataforma IA do Brasil e experiências do Tesouro Nacional. Em agosto, o Serpro anunciou parceria com a MeetKai Brasil para construir modelos soberanos de propriedade da estatal. Vale acompanhar se saem anúncios concretos (modelos, nuvem, contratos) além do debate. Edições anteriores já citaram o evento como futuro; aqui ele passa a ser notícia em andamento.

### 3.2 Marco legal da IA (PL 2338) continua parado na Câmara
**Fonte:** [Exame](https://exame.com/inteligencia-artificial/marco-legal-da-inteligencia-artificial-pl-2338-o-que-muda-para-empresas-com-a-nova-lei/) · [Central Izze](https://centralizze.pro/blog/marco-legal-da-ia-pl-2338-segue-na-camara-o-que-muda) (consultado em 04/11)

Aprovado no Senado em dezembro de 2024, o projeto aguarda votação na Câmara e as metas de 2026 não foram cumpridas; há relato de adiamento para depois das eleições. Também tramitam o PL 846/2026, sobre governança de IA no setor público, e um projeto do Executivo de dezembro de 2025 para criar um sistema nacional de IA. Não encontrei votação em novembro; o item registra o estado atual, não uma novidade nas últimas 48 horas.

*Internacional*

### 3.3 Advogado-geral da UE: Gemini pode infringir direitos de editoras ao responder com notícias
**Fonte:** [MarketScreener](https://www.marketscreener.com/news/google-weakened-by-european-legal-opinion-on-gemini-s-use-of-news-articles-ce785fdeda8ef025) · [ExplainX](https://explainx.ai/blog/eu-court-adviser-szpunar-gemini-may-infringe-press-publishers-right-training-tdm-exception-like-company-c-250-25-2026) (03/11)

No caso C-250/25 (Like Company contra Google Ireland), o primeiro de IA generativa no Tribunal de Justiça da UE, o advogado-geral Maciej Szpunar concluiu em 3/11 que um chatbot pode violar direitos de editoras de imprensa quando recupera um artigo e o reutiliza na resposta, em especial se acessou o conteúdo ilicitamente ou reproduz a expressão de modo que o usuário dispense o original. Já o treinamento foi tratado como coberto pela exceção de mineração de texto e dados. A opinião não é vinculante, mas costuma ser seguida pelo tribunal, cuja decisão deve vir em meses. Para quem trabalha com políticas públicas, separa dois debates que costumam ser misturados: treinar e responder.

## 4. IA aplicada em geral

### 4.1 Anthropic estende marca d'água invisível a modelos mais antigos do Claude
**Fonte:** [DEV Community](https://dev.to/delimitter/anthropic-switches-on-invisible-watermarks-in-four-older-claude-models-from-november-3) · [PhoneWorld](https://www.phoneworld.com.pk/claude-watermark-expands-older-models-november-3/) · [Winzheng](https://www.winzheng.com/en/article/anthropic-claude-invisible-watermark-eu-ai-act-compliance-20) (03/11)

Desde 3/11, o texto de modelos como Mythos 5, Opus 4.7 e Sonnet 4.6 (a nota oficial cita três; outras fontes falam em quatro, incluindo o Opus 4.6) carrega um padrão estatístico na escolha de palavras, sem tokens extras, sem custo e sem opção de desativar. Segundo os relatos, o objetivo é conformidade com o artigo 50 do AI Act; o detector está em prévia privada para reguladores, imprensa e pesquisadores. A marca sobrevive a copiar e colar, mas reescrever o texto com outra IA a quebra. Impacto prático: quem usa Claude em fluxos de texto deve assumir que a origem pode ser detectada por terceiros autorizados.

### 4.2 IPO da Anthropic: roadshow esperado a partir de 9–10 de novembro
**Fonte:** [Stock Titan](https://www.stocktitan.net/articles/anthropic-ipo-amended-s1-2026-guide) · [CNBC](https://www.cnbc.com/2026/10/26/anthropic-ipo-live-updates-ai-s-1-filing.html) (02/11 e consulta em 04/11)

Após o S-1 público de 26/10 e a emenda de 2/11, ainda não há faixa de preço nem data oficial. Pelas regras da SEC, a apresentação a investidores não pode começar antes de 10/11; a imprensa fala em semana de 9/11 e precificação em meados ou fim de novembro. As datas são relatos, não anúncios. O assunto já foi coberto nas edições anteriores; aqui entra apenas o calendário.

### 4.3 Menlo Ventures: gasto empresarial em IA chega a US$ 177 bilhões, alta de 5,4 vezes em um ano
**Fonte:** [The Neuron](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-tuesday-november-3-2026/) (03/11)

Segundo resumo do relatório da Menlo Ventures, o gasto empresarial em IA chegou a US$ 177 bi, com agentes assumindo parte do trabalho. Não consegui abrir o relatório original; o número vem de resumo secundário e deve ser verificado antes de citar. Contrasta com pesquisas recentes que mostram adoção ampla, mas baixa centralidade nas operações.

### 4.4 Fal levanta US$ 1,3 bilhão em Série B para infraestrutura de inferência
**Fonte:** [Tech Startups](https://techstartups.com/2026/11/04/startup-funding-news-today-november-4-2026-fal-traversal-lingchuan-technology-more/) (04/11)

A Fal, plataforma de inferência para modelos generativos, teria captado US$ 1,3 bi, com Kleiner Perkins, Redpoint e Khosla na liderança. Um valor desse tamanho em Série B mostra que o capital segue indo para a camada de execução de modelos. O dado vem de agregador de rodadas; confirme com um comunicado da empresa.
