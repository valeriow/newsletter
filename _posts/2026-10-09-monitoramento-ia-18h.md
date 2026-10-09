---
layout: post
title: "Radar IA — 09/10/2026, 18h"
date: 2026-10-09 18:00:00 -0300
categories: edicao
excerpt: "Google lança um agente Gemini persistente com identidade própria e sub-agentes; falhas no AWS AgentCore deixavam um prompt comprometer todos os agentes da conta; Memento 3 zera o ARC-AGI-3 com LLM congelado; Claude Haiku 5.5 chega com preço agressivo; ferramenta aberta de pentest usada em ataques a bancos coreanos vira código fechado; supercomputador de IA do governo brasileiro é adiado e a OAB-SP processa uma plataforma de IA jurídica."
---

*Janela pesquisada: 07 a 09/10/2026. Excluídos por já terem sido cobertos nas edições de 06 a 08/10: Cyber Mission e política de uso da Anthropic, Alignment Index da Arena, rodada da Manus, Clef da Cloudflare, Decisions API, conselho de IA do Canadá e a AGU com quatro LLMs.*

## Destaques do dia

1. **Google lança um agente Gemini "universal" e persistente**: roda por horas ou dias, monta times de sub-agentes e pode ter conta própria no Workspace, em prévia privada. → 1.1
2. **Falhas no AWS AgentCore ("AgentCorruption")**: um único prompt a um agente público levava às credenciais que alcançavam todos os agentes da mesma conta e região. → 1.2
3. **Memento 3 zera o ARC-AGI-3 com um LLM congelado**: o agente aprende reescrevendo um livro de regras em Markdown e um simulador em Python, segundo o paper. → 1.3
4. **Claude Haiku 5.5 chega com preço e controles de esforço**: modelo pequeno voltado a subagentes e uso de computador, com salto reportado no OSWorld. → 1.4
5. **Ferramenta aberta de pentest agêntico vira código fechado após ser ligada a ataques a bancos coreanos**: o caso ARTEX reacende o debate sobre liberar agentes ofensivos. → 2.3
6. **Brasil: supercomputador de IA é adiado e a OAB-SP processa uma plataforma de IA jurídica**: a compra de cerca de R$ 959 milhões ficou para 4 de novembro, e a disputa sobre supervisão humana na advocacia chegou à Justiça. → 3.1, 3.2

## 1. Novidades de IA agêntica

### 1.1 Google apresenta um agente Gemini persistente para o trabalho corporativo
**Fonte:** [The Register](https://www.theregister.com/ai-and-ml/2026/10/08/there-can-be-only-one-google-cloud-casts-gemini-as-your-enterprise-ai-hero/5302086) (08/10) · [VentureBeat](https://venturebeat.com/orchestration/google-cloud-unveils-persistent-gemini-agents-for-long-running-tasks-and-they-get-their-own-gmail-calendar-and-drive-storage) (08/10) · [Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/welcome-to-gemini-at-work-2026) (08/10)

No Gemini at Work 2026, o Google Cloud apresentou o "Gemini agent", que substitui a ideia de várias ferramentas por um único agente que recebe objetivos, planeja, usa habilidades e conectores, e entrega o resultado final. Ele roda tarefas que duram horas ou dias na nuvem, mantém memória entre dispositivos, cria sub-agentes temporários e, na configuração de "colega de trabalho", pode ter conta, agenda, Drive e registro no diretório da empresa, com identidade atestada criptograficamente. Há roteamento entre modelos (hoje Gemini e Claude), contêineres isolados, um Agent Gateway para aplicar políticas e log de auditoria, além de orçamentos que pausam o agente quando acabam. O recurso está em prévia privada, sem data de disponibilidade e sem detalhes de licenciamento. Para quem estuda agentes, o ponto central é que identidade, permissões e custo por agente deixam de ser detalhe e viram parte do produto; os números de benchmark citados por executivos do Google são alegações da empresa, não verificadas de forma independente.

### 1.2 "AgentCorruption": cadeia de falhas no AWS AgentCore expunha todos os agentes de uma conta
**Fonte:** [Zenity Labs](https://zenity.io/press-release/zenity-labs-discloses-agentcorruption-a-chain-of-aws-agentcore-flaws) (08/10) · [AI Weekly](https://aiweekly.co/ai-news-today) (09/10)

A Zenity Labs divulgou, durante o SecTor 2026, uma cadeia de falhas em que um prompt enviado a um agente público com uma ferramenta comum de requisição externa o fazia consultar o serviço de metadados da instância (IMDS) e obter credenciais temporárias. Essas credenciais pertenciam a um papel IAM padrão com alcance sobre todos os agentes do AgentCore na mesma conta e região, permitindo listar e invocar agentes internos, ler conversas e memórias de longo prazo, baixar imagens de contêiner, extrair segredos e até plantar memórias maliciosas persistentes. A Zenity avisou a AWS em 25/12/2025; segundo a empresa, a AWS tornou o IMDSv2 padrão e reduziu as permissões do papel de execução (a AWS diz ter concluído as mitigações em 29/09). A lição para quem projeta sistemas agênticos: memória persistente e papéis padrão generosos transformam uma injeção de prompt em movimento lateral, então privilégio mínimo por agente e isolamento de memória precisam ser requisito de projeto.

### 1.3 Memento 3 reporta desempenho máximo no ARC-AGI-3 com LLM congelado
**Fonte:** [AI Weekly](https://aiweekly.co/alerts/memento-3-posts-1000-rhae-on-arc-agi-3-with-frozen-llm-rulebook) (09/10) · [Hugging Face Papers](https://huggingface.co/papers/2610.11794) (09/10)

Segundo o resumo noticioso do trabalho, de pesquisadores da UCL e do laboratório Noah's Ark da Huawei, o Memento 3 teria completado todos os níveis dos 25 jogos públicos do ARC-AGI-3 com RHAE médio de 100, usando 7.518 ações, cerca de 44% da linha de base humana. O modelo de linguagem permanece congelado; o aprendizado acontece entre episódios, quando o agente revisa um livro de regras em Markdown e reescreve um motor de modelo de mundo em Python sempre que as previsões falham. O paper também relata vitórias de 21 a 0 no Pong com um controlador aprendido, sem chamadas ao LLM na execução. Importa porque desloca o aprendizado de agentes dos pesos para artefatos legíveis e auditáveis. Ressalva: os números vêm de um resumo, sem checagem do paper original nesta edição, e o resultado cobre os jogos públicos.

### 1.4 Anthropic lança o Claude Haiku 5.5, modelo pequeno para subagentes e uso de computador
**Fonte:** [Let's Data Science](https://letsdatascience.com/news/anthropic-releases-claude-haiku-55-with-lower-prices-and-eff-f698c663) (07/10) · [AI Agent Store](https://aiagentstore.ai/ai-agent-news/this-week) (08/10)

O Haiku 5.5, de 07/10, é descrito como o modelo de menor custo da família, voltado a classificação, extração, roteamento e tarefas de subagentes, com controle configurável de esforço de raciocínio e suporte beta a uso de computador e navegador nos SDKs Python e TypeScript. A Anthropic reporta 72,4% na parte offline do OSWorld 2.1, contra 15,7% do Haiku 4.5. O preço informado é de US$ 0,10 por milhão de tokens de entrada e US$ 0,50 de saída até 100 mil tokens de prompt, mas fontes divergem sobre a janela de contexto e sobre o tamanho do corte de preço, então vale conferir a página oficial antes de planejar custos. O interesse prático é claro: em arquiteturas multiagente, o custo está nos subagentes que rodam em volume, e um modelo barato com uso de computador competente muda a conta.

## 2. Ferramentas e modelos open source

### 2.1 Liquid AI abre os modelos de decisão d1-3B e d1-omni-600M
**Fonte:** [Liquid AI](https://www.liquid.ai/blog/d1-open) (07/10)

A Liquid AI publicou no Hugging Face dois modelos de pesos abertos que respondem em uma única passagem direta, sem gerar tokens. O d1-3B aceita texto e imagem; o d1-omni-600M, experimental, aceita texto mais imagem ou áudio. A empresa afirma que o d1-3B lidera os modelos abaixo de 10 bilhões de parâmetros no Decision Index v0.2.1 (48,57) e responde em 8 ms numa RTX 4090 e 50 ms num Jetson Orin Nano. O post não nomeia a licença, que deve ser conferida nas páginas dos modelos. Para pesquisa, o interesse é uma classe de modelo pensada para decisões rápidas em borda e robótica, em linha com o movimento de "modelos de decisão" visto nesta semana.

### 2.2 StepFun prévia o Step 5, um MoE de 600 bilhões de parâmetros, com pesos prometidos para 15/10
**Fonte:** [OpenRouter](https://openrouter.ai/stepfun/step-5-preview) (08/10) · [AI Weekly](https://aiweekly.co/ai-news-today) (08/10)

O Step 5 apareceu em prévia no OpenRouter com 600 bilhões de parâmetros totais e cerca de 27 bilhões ativos, contexto de 1 milhão de tokens e saída máxima de 64 mil, a US$ 1 por milhão de tokens de entrada e US$ 2,70 de saída. A página do OpenRouter não fala em abertura de pesos; a promessa de liberação em 15/10 vem do resumo do AI Weekly e depende de confirmação oficial, assim como a licença. Se cumprida, soma-se a Mistral Large 4 e Beam como grandes MoE abertos previstos para outubro.

### 2.3 ARTEX: ferramenta aberta de pentest multiagente vira código fechado após ligação com ataques a bancos coreanos
**Fonte:** [The Hacker News](https://thehackernews.com/2026/10/artex-ai-pentesting-tool-used-in-data.html) (08/10)

O desenvolvedor do ARTEX, sistema multiagente aberto para testes de intrusão autônomos, retirou o código do GitHub e anunciou que o projeto passa a ser fechado e sem manutenção. A CrowdStrike relatou que um operador usou a ferramenta, com DeepSeek v4.1-flash como modelo principal e GLM-5.3 e Grok 4.6 de apoio, contra instituições financeiras sul-coreanas, entre elas o Shinhan Bank e o Yegaram Savings Bank, de fins de setembro a início de outubro. Diretórios expostos revelaram históricos de sessões do Claude Code e arquivos de configuração. Nenhum grupo foi atribuído. O caso é o contraponto prático ao debate sobre liberar agentes ofensivos: remover o repositório não recolhe as cópias já feitas, e a discussão sobre responsabilidade de quem publica ferramentas de dupla utilização ganha um exemplo concreto, após o relato da edição anterior sobre a investigação na Coreia do Sul.

### 2.4 Alibaba lança o Qwen-Image-2.1-Turbo, modelo de imagem em 8 passos
**Fonte:** [Hugging Face](https://huggingface.co/Qwen/Qwen-Image-2.1-Turbo) (08/10) · [AI Weekly](https://aiweekly.co/ai-news-today) (08/10)

A Alibaba publicou no Hugging Face uma variante "Turbo" do Qwen-Image 2.1 que gera imagens em apenas 8 passos de difusão. Não consegui verificar licença, tamanho e benchmarks nas páginas durante esta execução, por isso o registro se limita à existência do lançamento. O que importa é a tendência: destilar modelos de imagem para poucos passos reduz custo de inferência e aproxima a geração local de hardware comum.

## 3. IA aplicada no setor público

*Brasil*

### 3.1 Governo adia para 4 de novembro a compra do supercomputador de IA e muda critérios do edital
**Fonte:** [Convergência Digital](https://convergenciadigital.com.br/governo/governo-modifica-edital-e-adia-entrega-de-propostas-para-a-compra-do-supercomputador-de-inteligencia-artificial/) (08/10)

A sessão para escolher o fornecedor do supercomputador do Plano Brasileiro de IA foi remarcada para 4 de novembro, depois do segundo turno da eleição presidencial. O valor estimado é de R$ 959 milhões, com recursos da Finep. A pontuação passou de 70% técnica e 30% preço para 70% técnica, 20% produção nacional (comprovação do Processo Produtivo Básico) e 10% preço, com exigências novas de computação confidencial, operação sem conectividade externa e um "critério de IA agêntica" que o texto não detalha. A reportagem aponta ambiguidades, como a garantia de execução (10% na errata, 5% na minuta) e como o PPB será convertido em nota. Para quem acompanha política de computação soberana, o episódio mostra o custo de equilibrar conteúdo local e desempenho técnico em compra pública de hardware de ponta.

### 3.2 OAB-SP aciona a Justiça contra a plataforma de IA jurídica Enter
**Fonte:** [Convergência Digital](https://convergenciadigital.com.br/mercado/oab-sp-vai-a-justica-contra-plataforma-de-inteligencia-artificial/) (08/10)

A seccional paulista da OAB ajuizou ação civil pública contra a Enter, que oferece a departamentos jurídicos de grandes litigantes uma IA que lê autos, define estratégia e redige minutas. A entidade pede, em liminar, preservação de provas, suspensão de publicidade que a apresente como substituta do advogado e restrições a novas contratações sem identificação do profissional responsável; no mérito, supervisão humana "efetiva, verificável e auditável", auditoria independente, proteção de dados e vedação de oferta a quem não é inscrito na OAB. O texto não informa o juízo. Importa porque é um teste de como a exigência de supervisão humana, comum em regulações de IA, será traduzida em obrigações concretas de produto numa profissão regulamentada.

### 3.3 Gecex amplia ex-tarifários e zera imposto de importação de unidade de processamento de IA para veículos
**Fonte:** [Convergência Digital](https://convergenciadigital.com.br/governo/governo-zera-imposto-de-importacao-de-equipamentos-de-inteligencia-artificial-mas-nao-altera-o-redata/) (07/10)

As Resoluções Gecex nº 970, 971 e 973, de 6/10 e publicadas em 7/10, atualizaram as listas de bens de capital e de informática e telecomunicações. O Ex 044, na NCM 8471.50.10, cobre unidades de processamento de dados para IA, análise de vídeo e telemetria veicular (por exemplo, detecção de fadiga e uso de celular por motoristas) e vale até 30/09/2028. A medida não altera o Redata, regime de data centers, e seu alcance é restrito à descrição técnica do ex-tarifário, não a equipamentos de IA em geral. É um sinal de política industrial pontual, não da redução ampla de custos de infraestrutura que o setor reivindica.

*Internacional*

### 3.4 Raleigh (EUA) coloca um agente de IA na central de TI da prefeitura
**Fonte:** [GovTech](https://www.govtech.com/artificial-intelligence/this-new-raleigh-n-c-it-help-desk-agent-is-well-agentic) (08/10)

Segundo a chamada da matéria, funcionários de Raleigh, na Carolina do Norte, desenvolvem ferramentas de IA em conjunto com um parceiro tecnológico para entender possibilidades e riscos de modelos de fronteira, e um agente já atua no atendimento de TI. Só li o resumo da página, sem o texto integral. O interesse é a abordagem de co-desenvolvimento em escala municipal, começando por um caso interno de baixo risco.

### 3.5 Casper (EUA) aprova contrato de câmeras corporais policiais com IA
**Fonte:** [GovTech](https://www.govtech.com/artificial-intelligence/in-casper-wyo-a-green-light-for-ai-police-bodycams) (08/10)

A Câmara Municipal de Casper, em Wyoming, aprovou contrato em tempo integral para software de IA em câmeras corporais, após seis meses de teste pela polícia e meses de debate. Novamente com base apenas na chamada da matéria. Importa como exemplo de adoção precedida por piloto longo e deliberação pública em tecnologia sensível de vigilância.

### 3.6 Hillsboro (EUA) avança regras para restringir terrenos de data centers
**Fonte:** [GovTech](https://www.govtech.com/artificial-intelligence/hillsboro-ore-moves-to-restrict-land-for-data-centers) (08/10)

A prefeitura de Hillsboro, no Oregon, avançou uma ordem que cria faixa de proteção em torno de escolas e limita tamanho e localização de armazenamento em baterias, após uma moratória temporária de data centers. Segue o padrão, visto também na Finlândia nesta semana, de governos locais impondo limites territoriais à infraestrutura de IA.

## 4. IA aplicada em geral

### 4.1 TypeSafe levanta cerca de US$ 870 milhões com avaliação de US$ 7,5 bilhões
**Fonte:** [PANews](https://panews.io/articles/01a120c8-d15d-7429-875c-c064d0a8314c) (09/10) · [AI Weekly](https://aiweekly.co/ai-news-today) (09/10)

A rodada, liderada pela a16z segundo a Bloomberg via PANews, financia a empresa por trás do modelo de decisão Jev, que teria alcançado mais de 1 milhão de usuários em poucos dias e seria usado por cerca de um terço da Fortune 500, segundo o cofundador. Os números de adoção são declarações da empresa e o texto não detalha a arquitetura. Mostra o apetite do capital por modelos de decisão, o mesmo tema dos lançamentos abertos da Liquid AI e da Cloudflare.

### 4.2 Dona do USA Today processa a OpenAI por mais de US$ 250 milhões
**Fonte:** [Unite.AI](https://www.unite.ai/usa-today-sues-openai-over-copyrighted-news-content-in-ai-training/) (08/10)

A USA Today Co. (ex-Gannett) abriu ação no Distrito Sul de Nova York alegando treino de modelos GPT com centenas de milhares de artigos, inclusive atrás de paywall, remoção de informações de direitos autorais e resumos que substituiriam os originais. Pede indenização acima de US$ 250 milhões e júri, e solicita vinculação ao litígio consolidado já em curso. Importa para empresas de mídia e para quem usa modelos em produtos de conteúdo: o foco passa do treino para a saída que substitui a fonte.

### 4.3 OpenAI bane operação de influência ligada ao Irã que publicou cerca de 100 artigos em veículos pequenos
**Fonte:** [AI Weekly](https://aiweekly.co/alerts/openai-bans-iran-linked-chatgpt-op-that-placed-100-articles) (09/10)

Chamada "Bogus Bylines", a operação usou sete personas falsas de jornalistas para emplacar quase 100 artigos de opinião em mais de uma dúzia de publicações online, com ChatGPT para edição e e-mails de pauta. A OpenAI a classificou como categoria 4 de 6 e disse não ter conseguido identificar o responsável, descrevendo-a como compatível com serviço comercial de influência. É um lembrete de que o risco não está só em deepfakes, mas em canais editoriais de baixa checagem.

### 4.4 SemiAnalysis: só 3,6% dos lançamentos de laboratórios chineses trouxeram avaliação de segurança
**Fonte:** [SemiAnalysis](https://newsletter.semianalysis.com/p/beijing-will-not-pace-the-frontier) (08/10)

Em 857 lançamentos de nove grandes desenvolvedores chineses até 15/09/2026, apenas 31 tiveram algum resultado de segurança publicado e 9 o tiveram no lançamento; 94,9% não divulgaram nada. Modelos de raciocínio ficaram 93% sem resultados. Os autores ressalvam que "não encontrado" não significa "não testado" e que as taxas por empresa são indicativas. Para empresas que adotam modelos abertos chineses, a ausência de avaliações públicas transfere para o adotante o ônus de avaliar riscos.

### 4.5 Netflix planejaria cortar cerca de 5% do quadro
**Fonte:** [The Star](https://www.thestar.com.my/tech/tech-news/2026/10/09/netflix-plans-to-cut-5-of-its-workforce-puck-news-reports) (09/10)

Segundo a Puck, o corte seria de 800 a 850 vagas, com anúncio esperado na semana de 12/10. A matéria como resumida não atribui o corte à IA, então registro como dado de mercado de trabalho em tecnologia, sem relação causal confirmada, ao lado de outros ajustes recentes de quadro.

### 4.6 Ultra capta US$ 62 milhões para robôs de armazém com software da Physical Intelligence
**Fonte:** [Fortune](https://fortune.com/2026/10/09/ultra-raises-62-million-fast-growing-robots-service-tie-up-ai-research-firm-physical-intelligence) (09/10)

A Ultra anunciou a rodada e uma parceria com a Physical Intelligence para a política de controle dos robôs. Mostra modelos de fundação para robótica saindo do laboratório para logística, onde o retorno é mais fácil de medir.
