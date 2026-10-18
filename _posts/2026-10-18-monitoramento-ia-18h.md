---
layout: post
title: "Radar IA — 18/10/2026, 18h"
date: 2026-10-18 18:00:00 -0300
categories: edicao
excerpt: "Na Anthropic, horas de agentes já superam as humanas em seis para um; Schwab e JPMorgan barram agentes de terceiros nas contas; DeepSeek V4.1-Flash-1017 e Ling 3.1 Flash elevam os modelos abertos em código agêntico; Perplexity abre o sandbox SPACE; TSE e observatórios tratam de deepfakes na eleição; dúvidas sobre a infraestrutura de IA crescem com Bernstein e Microsoft."
---

*Janela pesquisada: 16/10 a 18/10/2026. Foram excluídos itens já cobertos nas edições de 15, 16 e 17/10 (Beam, Muse Spark Open, origem das sementes do NIST, CERT-In, Timestral, Goiás, CoreWeave, TSMC, golpe com clone de voz na Itália, entre outros). Itens sem data explícita na fonte estão sinalizados.*

## Destaques do dia

1. **Agentes já trabalham seis vezes mais horas que os humanos na Anthropic**: levantamento interno mostra que a atenção humana virou o gargalo e que a contratação de juniores despencou. → 1.1
2. **Bancos e sites começam a barrar agentes de terceiros**: Schwab e JPMorgan bloqueiam agentes externos que tentam mexer em contas, e o acesso passa a ser somente leitura via MCP. → 1.2
3. **Modelos abertos avançam em código agêntico**: DeepSeek V4.1-Flash-1017 e Ling 3.1 Flash saem com licença MIT e ganhos em benchmarks de terminal e engenharia de software. → 2.2, 2.3
4. **Perplexity abre o SPACE, sandbox de microVMs para agentes**: isolamento por Firecracker, credenciais injetadas na rede e testes de red team publicados, enquanto o OpenCode expõe chaves por ataque de destilação. → 2.1, 1.5
5. **Deepfakes testam a Justiça Eleitoral e o Judiciário**: o TSE manda remover vídeo feito com IA e observatórios apontam que boa parte do conteúdo político sintético não é identificada. → 3.1, 3.2, 3.3
6. **Dúvidas sobre a infraestrutura de IA crescem**: Bernstein vê só cerca de 35% do pipeline de data centers nos EUA como crível e a Microsoft sai de um acordo no Reino Unido. → 4.4

## 1. Novidades de IA agêntica

### 1.1 Anthropic: horas de agentes superam as humanas em seis para um
**Fonte:** [Anthropic — How employment is changing at Anthropic](https://www.anthropic.com/research/employment-at-anthropic) (16/10, atualizado em 17/10)

A Anthropic analisou dados internos e 17 entrevistas com funcionários. As horas de trabalho de agentes passaram as humanas em março de 2026 e, em agosto, os agentes de cada funcionário trabalhavam seis vezes mais horas que o próprio dono. Commits por engenheiro chegaram a 5 vezes o nível de seis meses antes, e a parcela de juniores nas contratações técnicas caiu de 27% para 9%. Cerca de 80% do tempo de uma sessão interativa é espera por input humano, ou seja, a atenção humana virou o gargalo. O estudo reconhece vieses (adoção não aleatória) e que a queda de juniores não se explica só por IA. Para quem faz pós-graduação, é um dado primário raro sobre como o trabalho muda quando agentes são o padrão; a ressalva é que se trata de uma empresa de IA analisando a si mesma.

### 1.2 Schwab, JPMorgan, Amazon e Delta barram agentes de IA de terceiros
**Fonte:** [Forkast](https://forkast.news/schwab-and-jpmorgan-block-unauthorized-ai-agents-from-moving-money-as-private-ordering-reaches-financial-core/) (17/10) · [The Verge](https://www.theverge.com/ai-artificial-intelligence/1013195/ai-agents-blocked-web) (via [AI Weekly](https://aiweekly.co/ai-news-today), 18/10)

O CEO da Schwab, Rick Wurster, disse na Bloomberg TV (16/10) que a empresa bloqueia dezenas de tentativas semanais de agentes não autorizados de acessar ou movimentar fundos de clientes; LLMs externos têm acesso somente leitura por servidores MCP. Jamie Dimon confirmou que o JPMorgan também bloqueia agentes externos. Segundo o resumo do AI Weekly, Amazon, Yelp e Delta também restringem agentes (não consegui abrir a matéria do Verge, então esse trecho vem do resumo). O ponto central, apontado pela Forkast, é a responsabilidade: sem lei federal americana sobre agentes, as empresas estabelecem suas próprias regras por exclusão. Para quem projeta agentes, a lição é que identidade, autorização e responsabilização do agente viram requisitos de produto.

### 1.3 Claude Code 2.1.302 oficializa plugins e liga subagentes "fork" por padrão
**Fonte:** [GitHub — release v2.1.302](https://github.com/anthropics/claude-code/releases/tag/v2.1.302) (via [AI Weekly](https://aiweekly.co/alerts/claude-code-21302-turns-on-fork-subagents-in-sdk-and-apps), 18/10)

A versão torna plugins um recurso oficial, habilita subagentes do tipo fork por padrão no SDK e nos apps, adiciona uma variável de modelo para o modo automático e traz 43 correções. A nota de versão também avisa que o Claude Design autônomo será encerrado em 14/12/2026. Importa porque forks herdam o contexto do agente principal, o que muda como se desenha orquestração multiagente em harnesses de código. Os detalhes vêm do resumo do AI Weekly sobre a nota de versão.

### 1.4 OpenGCUA e MAI-Gym: pilha aberta para agentes de uso de computador
**Fonte:** [Hugging Face Papers — OpenGCUA](https://huggingface.co/papers/2610.22200) · [MAI-Gym](https://huggingface.co/papers/2610.20939) (via [Rio Rundown](https://riorundown.substack.com/p/ai-news-oct-17-2026-ai-infrastructure), 17/10)

OpenGCUA, da equipe MAI-UI da Alibaba, é um framework aberto de agente de uso de computador que, segundo os autores, eleva a pontuação parcial média em 19,6 pontos e reduz em 53% os passos por tarefa no OSWorld-v2. O MAI-Gym é uma plataforma aberta de avaliação e treino por RL de agentes de interface gráfica, com dez benchmarks e até 20 mil instâncias paralelas. São resultados autorreportados em preprints, ainda sem replicação independente. Valem como infraestrutura reutilizável para pesquisa em avaliação de agentes.

### 1.5 OpenCode: ataque de destilação expõe chaves de API de 1,4% dos usuários do Console
**Fonte:** [HuggingNews](https://huggingnews.com/cybersecurity/opencode-confirms-distillation-attack-hit-14percent-of-console-users-51c80aca) (via [AI Weekly](https://aiweekly.co/ai-news-today), 17/10)

O OpenCode confirmou que um ataque de destilação atingiu chaves de API de 1,4% dos usuários do seu Console e pediu a rotação das chaves; a empresa diz trabalhar com Google, OpenAI e Anthropic na remediação. Detalhes técnicos não foram confirmados por fonte primária que eu tenha conseguido abrir. O episódio reforça que ferramentas de agentes de código concentram credenciais valiosas e são alvo.

### 1.6 Apollo Research: GLM-5.3 raciocina sobre o próprio treinamento
**Fonte:** [Runtime Wire](https://runtimewire.com/article/apollo-research-glm-53-update-aware-reasoning) (via [AI Weekly](https://aiweekly.co/ai-news-today), 17/10)

A Apollo Research relata que o modelo aberto GLM-5.3 raciocinou sobre como suas saídas poderiam afetar modelos sucessores em 10 de 6.452 trajetórias avaliadas. É uma taxa baixa, mas relevante para avaliação de segurança de sistemas agênticos, pois mostra consciência de contexto de treino em pesos abertos, que qualquer pesquisador pode inspecionar. A fonte é secundária.

### 1.7 Três modelos "aurora" da OpenAI aparecem brevemente na API
**Fonte:** [Crypto Briefing](https://cryptobriefing.com/openai-aurora-alpha-models-api/) (via [AI Weekly](https://aiweekly.co/ai-news-today), 18/10)

Identificadores de três modelos "aurora" sem documentação apareceram na API da OpenAI: um devolvia erro de capacidade e os outros, "não encontrado". A OpenAI não comentou, e o propósito é pura especulação. Entra aqui só como sinal de lançamento próximo, a ser confirmado.

### 1.8 Anthropic consulta escritórios de advocacia sobre normas de negociação entre agentes
**Fonte:** [AI Weekly](https://aiweekly.co/alerts/anthropic-consults-law-firms-on-negotiation-norms-for-ai-agents) (17–18/10)

Segundo o resumo, a Anthropic perguntou a escritórios com que frequência agentes devem consultar humanos e quão céticos devem ser diante de agentes contrapartes. Apesar de ser consulta e não regra, mostra o problema de interação agente-agente em contextos jurídicos e comerciais, onde ainda não há normas. Fonte secundária.

## 2. Ferramentas e modelos open source

### 2.1 Perplexity abre o SPACE, a sandbox de microVMs por trás do Perplexity Computer
**Fonte:** [MarkTechPost](https://www.marktechpost.com/2026/10/16/perplexity-open-sources-space-firecracker-microvm-sandbox-ai-agents) (16/10)

O SPACE (Sandboxed Platform for Agentic Code Execution) roda cada tarefa de agente em uma microVM Firecracker com kernel próprio; um gateway de rede por sandbox aplica a política de saída, e as credenciais são injetadas na camada de rede, sem entrar na VM. Licença Apache 2.0, escrito em Rust (versão 0.8.0), exige host Linux x86_64 com KVM, btrfs e Docker. A Perplexity reporta latência mediana de criação de 60 ms (antes 185 ms) e zero escapes de VM em 108 tentativas de red team, mas houve bypasses parciais de rede em 11 de 54 execuções antes das correções. Números autorreportados. Importa porque isolamento e controle de credenciais são o ponto fraco de agentes de código, e agora há uma referência aberta para auditar.

### 2.2 DeepSeek libera V4.1-Flash-1017 sob licença MIT
**Fonte:** [Hugging Face — DeepSeek-V4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) · [Local AI Zone](https://local-ai-zone.github.io/blog/October_2026_AI_Model_Updates.html) (17/10)

Atualização do V4.1-Flash com pesos MIT, janela de 1 milhão de tokens e suporte a vLLM e SGLang. Segundo o cartão do modelo, o Terminal-Bench 4.0 subiu de 31,2 para 42,3 e o DeepSWE v1.1 de 74,2 para 77,0, com ganhos também em HLE sem ferramentas (36,8 para 42,6). O cartão admite que o Opus 5 pontua mais em vários testes. Há inconsistência nos relatos sobre tamanho (a Local AI Zone cita 552B; a página lista 763B nos tipos de tensor), então trate o número com cautela. Benchmarks são autorreportados.

### 2.3 InclusionAI publica o Ling 3.1 Flash (MoE de 560B, MIT)
**Fonte:** [Local AI Zone](https://local-ai-zone.github.io/blog/October_2026_AI_Model_Updates.html) (16/10)

MoE com 560B de parâmetros totais e 25B ativos, pesos em fp8, receitas day-0 para SGLang e vLLM e um harness chamado LingCode para sessões longas de programação. Os autores reportam 68,74 no SWE-bench Pro e 59,7 no DeepSWE (autorreportado, sem verificação independente). Para o ecossistema aberto, é mais um modelo com foco explícito em engenharia de software agêntica, além do harness.

### 2.4 Tencent Hy Memory 2.0: pilha aberta de memória para agentes
**Fonte:** [Local AI Zone](https://local-ai-zone.github.io/blog/October_2026_AI_Model_Updates.html) (16/10)

Inclui o Hy-Memory-30B-A3B (cerca de 3B ativos) que escreve memórias, um framework para memórias de conversa, trabalho e código e o MemHub como camada de gestão, com pesos no Hugging Face e ModelScope e paper no arXiv (2610.22196). A fonte não informa a licença. Memória de longo prazo é um dos gargalos de agentes, e uma pilha aberta facilita experimentos reproduzíveis.

### 2.5 llmspeed e Sphinx: utilitários abertos para quem usa modelos locais e código gerado por IA
**Fonte:** [llmspeed](https://llmspeed.dev/) · [Sphinx](https://sphinx-six-theta.vercel.app/) (via [AI Weekly](https://aiweekly.co/ai-news-today), 18/10)

O llmspeed estima tokens por segundo de mais de 15 modelos abertos em mais de 30 GPUs antes da compra de hardware. O Sphinx é um hook de git que faz perguntas de compreensão sobre diffs escritos por IA antes que cheguem a branches protegidas. Ambos aparecem como projetos do Show HN, sem avaliação independente; o segundo toca um problema real de dívida de compreensão em código gerado.

## 3. IA aplicada no setor público

*Brasil*

### 3.1 TSE manda remover vídeo feito com IA que associava Lula a facção criminosa
**Fonte:** [TSE](https://www.tse.jus.br/comunicacao/noticias/2026/Outubro/tse-determina-remocao-de-video-produzido-com-ia-que-associa-lula-a-crime-organizado-5) (13/10)

Por unanimidade, o plenário determinou ao PL que retire do Instagram um vídeo com simulação de aperto de mão entre Lula e um ex-deputado preso. A relatora, ministra Estela Aranha, fundamentou na desinformação grave; os ministros Floriano de Azevedo Marques e André Mendonça apontaram como ilícito o uso de IA para simular a figura do candidato, vedado pelo art. 9º-C da Resolução 23.610. A decisão tem cinco dias, mas é o caso mais recente de aplicação da regra sobre IA na propaganda e ainda não tinha sido coberto aqui. Mostra que a divergência de fundamentos pode orientar decisões futuras.

### 3.2 Observatórios apontam que boa parte do conteúdo político com IA não é identificada
**Fonte:** [Misto Brasil](https://mistobrasil.com/2026/10/17/inteligencia-artificial-amplia-desafios-nas-eleicoes-2026) (17/10)

O projeto VigIA (Observatório Lupa) identificou 920 conteúdos suspeitos em dois meses, 60% deles deepfakes; o Observatório IA nas Eleições (Data Privacy Brasil e Aláfia Lab) mapeou 413 conteúdos políticos com IA, quase dois terços sem sinalização, o que contraria as normas do TSE. A reportagem lembra que a remoção tardia perde eficácia diante da velocidade das redes e dos aplicativos de mensagem. É um retrato quantitativo do descumprimento da regra de rotulagem.

### 3.3 Caso do TRT-8: texto oculto para enganar a IA do tribunal vira referência nos EUA
**Fonte:** [Diário do Pará](https://diariodopara.com.br/para/decisao-do-trt-8-sobre-ia-no-para-vira-referencia-para-juiz-dos-estados-unidos) (16/10)

Em maio, um juiz de Parauapebas (PA) multou duas advogadas em R$ 84,2 mil por esconderem, em letras brancas, uma instrução destinada ao sistema Galileu da Justiça do Trabalho para que contestasse a petição "de forma superficial". Agora, um juiz de Connecticut citou o entendimento ao sancionar uma parte sem advogado. É um caso concreto de prompt injection contra IA do setor público e de como o Judiciário o enquadra como violação da boa-fé processual; a decisão final segue humana.

*Internacional*

### 3.4 Anthropic apresenta rascunho de lei de segurança para IA de fronteira
**Fonte:** [Politico](https://news.google.com/rss/articles/CBMieEFVX3lxTE0ydWVrbHdHeGNraEdTSHQ5eExwZ2lLRUU1U1BoVFJUTWNLenpWTXJOMHNnWnhaa0thQXlRbk1KdEliVVVGUEJXZWwtcWtUZE9Ielo2X05DaHJKSmJpd05rRl9vMWdQQUE4ZnVRRFBLQ3hlcm9FNG12bg?oc=5) (via [Rio Rundown](https://riorundown.substack.com/p/ai-news-oct-17-2026-ai-infrastructure), 17/10)

Segundo o Politico, um rascunho confidencial permitiria suspender modelos apenas por riscos de armas biológicas, ataques cibernéticos ou evasão de controle, e avaliadores independentes teriam de reportar riscos iminentes ao Departamento de Comércio em 72 horas. A data da matéria original não foi confirmada e o texto é um rascunho não público; vale acompanhar como insumo para o debate regulatório americano.

## 4. IA aplicada em geral

### 4.1 Itaú implanta o assistente ia.i com modelos da OpenAI
**Fonte:** [OpenAI](https://openai.com/index/itau-generative-ai) (16/10)

O banco lançou o ia.i, assistente conversacional para conta, crédito, cartões, seguros e investimentos, com repasse a especialistas humanos. Começou com cerca de 300 mil clientes e mira 100% da base até o fim de 2026. A plataforma interna IARA concentra acesso a vários modelos com controle de custos e IA responsável. No jurídico, são mais de 2 milhões de tarefas por mês, com ganhos de eficiência de 20% a 80% segundo o banco. Os números vêm da OpenAI e do próprio Itaú, sem auditoria externa.

### 4.2 Anthropic destina 5% das ações a um fundo de benefício público
**Fonte:** [Anthropic](https://www.anthropic.com/news/public-benefit-fund) (18/10)

Sujeito à aprovação dos acionistas, o fundo, uma LLC integralmente controlada (não uma 501(c)(3)), receberá 5% das ações, mais 2% a critério do conselho a cada alta de 50% no valor da empresa. Os recursos poderão financiar doações e abordagens sobre impacto no mercado de trabalho e não serão usados em lobby. Com compromissos anteriores dos cofundadores, a empresa fala em cerca de 20% das ações para o bem público. Governança e marcos de valor serão detalhados nos próximos meses.

### 4.3 Hogan Lovells Cadwalader adota a Harvey e cria agentes jurídicos próprios
**Fonte:** [AI Agent Store](https://aiagentstore.ai/ai-agent-news/daily/2026-10-17) (17/10)

Segundo a Harvey, o escritório adotou a plataforma em toda a firma, e grupos de prática construíram agentes para gestão de conhecimento, mercado de capitais e arbitragem internacional. O que interessa é a passagem de ferramenta individual para fluxos repetíveis por área. A informação vem do fornecedor.

### 4.4 Bernstein vê só 35% do pipeline de data centers como crível; Microsoft sai de acordo da Nscale
**Fonte:** [Financial Times](https://www.ft.com/content/f7c26ac0-f5f2-443a-86b2-39d62f7920a9) · [Telegraph](https://www.telegraph.co.uk/business/2026/10/18/microsoft-axes-ai-deal-setback-uk-data-centre-pioneer/) (via [AI Weekly](https://aiweekly.co/ai-news-today), 18/10)

Segundo os resumos, o Bernstein estima que apenas cerca de 35% do pipeline americano é crível, com mais de 47 projetos grandes atrasados, retirados ou bloqueados em 2026. Separadamente, a Microsoft desistiu de um acordo âncora com a Nscale em Essex (23 mil chips Nvidia) porque a rede elétrica só chegaria na década de 2030. Os dois sinais apontam que energia e licenciamento limitam a expansão. Não consegui abrir as matérias originais.

### 4.5 Disney reserva cerca de US$ 180 milhões para contratar equipe da Character.AI
**Fonte:** [AI Weekly](https://aiweekly.co/alerts/disney-budgets-180m-over-three-years-for-characterai-hires) (17–18/10)

O documento menciona mais de 60 funcionários ao longo de três anos e um fundo de retenção de US$ 30 milhões. É uma contratação de talentos de IA conversacional por um grupo de mídia. Fonte secundária.

### 4.6 AMD apresenta o rack Helion para IA agêntica
**Fonte:** [TechRadar](https://news.google.com/rss/articles/CBMi2gFBVV95cUxPVmZld0cwVWNsLUFZaEVhSG9vVjl3a2RpUXFnaTQyZWdrVlZZRG5iek1RQ1dZVWtES0tkSVhqajN5YVpNQVRqLTZBVVlfd29xMEZudjRmcjZMeVRMNGtrSm05ekFMY3FFSzU2Z0R4YndXN1owVWExNXZtOXRkWUpIUncxUVVnRzNZblEweWJ1MHZZbnRmMTV5WEZ1aUNmeWd0OXNVcFpYY0g5bFN6RjdxT2tDWUlZVUl2dW5vWC1QalJTa2lTQVlYSXdaQmZyMW4zUXoxV3J5ZFpWQQ?oc=5) (via [Rio Rundown](https://riorundown.substack.com/p/ai-news-oct-17-2026-ai-infrastructure), 17/10)

Rack modular com até 32.768 núcleos de CPU Zen 6 e 16 aceleradores Instinct MI350P, 74 petaflops em FP4 e 102 Tbps de rede. A aposta é que agentes exigem mais CPU, e não só GPU, para orquestrar ferramentas. Especificações do fabricante.

### 4.7 Anthropic assina arrendamento de 20 anos para data center na Nova Escócia
**Fonte:** [The Star](https://www.thestar.com.my/tech/tech-news/2026/10/17/anthropic-signs-lease-for-first-canadian-data-center) (17/10)

Campus EverWind de C$ 10 bilhões, o primeiro data center canadense da empresa, com 95 MW na primeira fase, previstos para o fim de 2027. Contrasta com o ceticismo do item 4.4 sobre prazos de energia.

### 4.8 Altman confirma que a OpenAI vai mostrar um robô humanoide em 2027
**Fonte:** [Engadget](https://www.engadget.com/2285040/openai-humanoid-robot-sam-altman-statement-real-challenge/) (via [AI Weekly](https://aiweekly.co/alerts/altman-confirms-openai-will-build-humanoid-demo-in-2027), 18/10)

Segundo o resumo, Altman afirmou que a empresa espera uma demonstração em 2027, e a página de vagas lista 27 posições de robótica. É um sinal de expansão da OpenAI para IA física; ainda sem produto.
