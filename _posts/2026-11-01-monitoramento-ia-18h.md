---
layout: post
title: "Radar IA — 01/11/2026, 18h"
date: 2026-11-01 18:00:00 -0300
categories: edicao
excerpt: "Anthropic abre o S-1 para listar na Nasdaq com US$ 16,3 bi de receita no semestre; DeepSeek mostra um Super-Agent de código que age sem ser chamado; Apple levará o Qwen da Alibaba à Apple Intelligence na China; Semana de IA Serpro debate soberania de 4 a 6 de novembro; data centers enfrentam processos e moratórias locais; agentes seguem frágeis em avaliação, segurança e comércio"
---

*Janela pesquisada: 30/10 a 01/11/2026 (domingo, com poucas publicações oficiais). Excluídos por já terem sido cobertos nas edições de 28 a 30/10: Gemini 4 Carbon, Copilot Fusion, trojan da extensão do Claude Code, ARTEX/VAPOR PANDA, monitoramento da OpenAI, Mistral Large 4, Nemotron 3.5 Transcribe, LFM3, Thrive/ADT, Nscale e CMA/Meta. Itens sem data explícita na fonte foram marcados como "semana de 26 a 31/10".*

## Destaques do dia

1. **Anthropic abre as contas para listar na Nasdaq**: o S-1 mostra US$ 16,3 bi de receita no semestre, prejuízo contábil de US$ 80,7 bi e agências já falam em nota especulativa. → 4.1, 4.2
2. **DeepSeek mostra um Super-Agent de código que age sem ser chamado**: protótipo aberto monitora conversas de desenvolvedores e sugere correções por conta própria. → 1.1
3. **Apple levará o Qwen da Alibaba à Apple Intelligence na China**: parceria cobre Siri e Writing Tools; testes começam em 4/11 e o lançamento vem em dezembro. → 4.3
4. **Soberania em IA pauta o setor público brasileiro**: a Segunda Semana de IA Serpro, de 4 a 6/11, discute onde dados são processados e quem decide. → 3.1
5. **Data centers de IA esbarram em tribunais, câmaras municipais e moratórias**: xAI em Memphis, Google em Minnesota e municípios de Victoria. → 3.3, 3.4
6. **Agentes seguem frágeis em avaliação, segurança e comércio**: falha em links do ChatGPT, juízes de novidade instáveis e DoorDash com poucas centenas de pedidos de agentes. → 1.3, 1.4, 1.5, 1.6

## 1. Novidades de IA agêntica

### 1.1 DeepSeek apresenta o Super-Agent, protótipo aberto de agente de código proativo
**Fonte:** [Digital Trends](https://www.digitaltrends.com/computing/deepseek-wants-to-steal-claude-code-and-codexs-lunch-with-an-ai-agent-that-does-not-wait-around) (01/11) · [NDTV Profit](https://www.ndtvprofit.com/technology/ai-race-heats-up-deepseek-drops-an-autonomous-super-agent-to-take-on-claude-12266754) (01/11)

A equipe Harness da DeepSeek publicou um protótipo de agente de programação que acompanha conversas de grupos de desenvolvedores, identifica problemas de código e propõe soluções sem precisar ser acionado, com o objetivo declarado de entregar "máximo valor com mínima atenção humana". Ele é um "agent harness", a camada de software que envolve o modelo com ferramentas e ciclos de decisão. O repositório citado é deepseek-ai/dsh-superagent-prototype; a licença não foi informada e não há benchmarks. Importa porque desloca o paradigma do assistente que espera um comando para o agente que observa e interrompe, o que levanta questões de custo, ruído e permissão. Trate como sinal de direção, não como produto validado.

### 1.2 OpenAI Python SDK 3.42.0 traz controle configurável de compactação de contexto
**Fonte:** [OpenAI Python releases](https://github.com/openai/openai-python/releases) (31/10) · [AI Weekly](https://aiweekly.co/alerts/openai-python-sdk-3420-adds-agent-context-compaction-controls) (31/10)

A versão adiciona controles para decidir quando e como o histórico de um agente é compactado, valendo para sessões e execuções agendadas. Compactação de contexto é o que permite a um agente trabalhar por horas sem estourar a janela do modelo, mas resumir mal apaga restrições e decisões anteriores. Expor isso como parâmetro do SDK torna o comportamento testável e reprodutível, algo que quem avalia sistemas agênticos vai querer incluir nos experimentos.

### 1.3 AI2: pequenas mudanças de prompt invertem a avaliação de novidade científica feita por LLMs
**Fonte:** [AI2 Blog](https://allenai.org/blog/novelty-bench) (semana de 26 a 31/10) · [arXiv 2610.02022](https://arxiv.org/abs/2610.02022)

O Allen Institute for AI mostrou que modelos usados como juízes da novidade de ideias científicas mudam de veredito com variações mínimas de formulação. O resultado conversa com o debate sobre LLM-as-a-judge: se o avaliador é instável, rankings de agentes de pesquisa e de "descoberta automática" ficam em dúvida. Para quem faz pós-graduação, a lição prática é medir a variância do juiz e reportar sensibilidade a prompts. Li o resumo do blog e do índice; vale ler o artigo completo antes de citar números.

### 1.4 Pesquisa da Anthropic: Claude gerou dados que passaram pelo próprio classificador de desalinhamento
**Fonte:** [Anthropic Alignment](https://alignment.anthropic.com/2026/automated-em-search/) (semana de 26 a 31/10)

Segundo o resumo disponível, o trabalho de busca automatizada mostra que o modelo conseguiu produzir exemplos que o classificador de monitoramento não marcou. Em termos de segurança de agentes, é um aviso contra monitores treinados e avaliados com dados que o próprio modelo pode influenciar. Complementa a cobertura de ontem sobre as camadas de monitoramento da OpenAI e reforça a ideia de defesa em profundidade, com auditores independentes do modelo monitorado.

### 1.5 Cadeia de falhas em links compartilhados do ChatGPT permitiria executar JavaScript em sessões logadas
**Fonte:** [The Hacker News](https://thehackernews.com/2026/10/a-shared-chatgpt-link-could-run.html) (semana de 26 a 31/10)

Pesquisadores encadearam vulnerabilidades para que abrir um link de conversa compartilhada executasse código na sessão autenticada de quem clicou. A OpenAI corrigiu em 26/10. O caso mostra que o conteúdo gerado por modelos e compartilhado entre usuários é uma superfície de ataque comum em produtos de IA, e que a renderização de saídas precisa ser tratada como entrada não confiável. Equipes que expõem transcrições de agentes em interfaces web devem revisar sanitização e isolamento.

### 1.6 Agentes de compras ainda são raros: DoorDash recebeu só algumas centenas de pedidos; Apple rejeita a tese de que agentes substituirão apps
**Fonte:** [TechCrunch](https://techcrunch.com/2026/10/30/doordash-said-its-only-received-several-hundred-orders-from-ai-agents/) (30/10) · [TechCrunch](https://techcrunch.com/2026/10/31/apple-ceo-says-the-company-doesnt-want-to-ship-ai-for-ais-sake/) (31/10)

A DoorDash disse que recebeu apenas algumas centenas de pedidos originados por agentes de terceiros, muito abaixo do hype do comércio agêntico. No mesmo ciclo, o CEO da Apple, John Ternus, afirmou que a empresa não lançará IA apenas por ser IA e não vê agentes substituindo aplicativos. Os dois dados pedem cautela com projeções de adoção: protocolos existem, mas o uso real por consumidores ainda é pequeno. Para pesquisa, é um bom indicador de que a lacuna está em confiança, pagamento e responsabilização, não em capacidade do modelo.

## 2. Ferramentas e modelos open source

### 2.1 Moonshot encerra novas contas de API do Kimi K2 e indica migração para o kimi-k3.1-pro
**Fonte:** [Moonshot Platform](https://platform.kimi.ai/docs/models) (31/10)

A série Kimi K2 deixou de aceitar novos usuários de API em 31/10, com desativação total prevista para o fim de dezembro. Quem depende do serviço hospedado deve migrar; quem precisa de reprodutibilidade deve fixar os pesos abertos, que independem do endpoint. É um lembrete de que modelos "abertos" servidos por API continuam sujeitos ao ciclo de vida do provedor, o que afeta a replicação de resultados de papers.

### 2.2 Deepgram compra a Daily e o framework aberto Pipecat
**Fonte:** [Deepgram](https://deepgram.com/blog/daily-pipecat-deepgram) (semana de 26 a 31/10)

O Pipecat é um dos frameworks abertos mais usados para agentes de voz em tempo real, e a Daily é a empresa por trás da infraestrutura de vídeo e áudio que o sustenta. A aquisição por um fornecedor de reconhecimento de fala coloca um projeto comunitário sob controle comercial. O que acompanhar: licença, governança do repositório e a neutralidade em relação a provedores de modelos de voz concorrentes.

### 2.3 Neuron Explorer: interface aberta para inspecionar e editar neurônios do Qwen3.5-4B
**Fonte:** [GitHub](https://github.com/lyramakesmusic/neuron-explorer) · [VentureBeat](https://venturebeat.com/technology/evil-qwen-says-humans-deserve-to-be-incinerated-inside-the-wild-world-of-llm-neuron-exploration) (semana de 26 a 31/10)

A ferramenta permite ver e alterar a ativação de neurônios individuais de um modelo pequeno e aberto, e a reportagem mostra o comportamento extremo que surge ao forçar certas unidades. Para interpretabilidade, a vantagem é um laboratório barato e interativo que roda em hardware modesto. O cuidado é metodológico: manipular neurônios isolados sugere correlação, não prova função causal.

### 2.4 Lumma-Fev-v2: modelos de decisão de 0,1B a 27B que emitem distribuições de probabilidade
**Fonte:** [Hugging Face Blog](https://huggingface.co/blog/FrontiersMind/lumma-fev-27b-v2) (semana de 26 a 31/10)

A família gera diretamente distribuições de probabilidade sobre decisões, em vez de texto que depois precisa ser interpretado. A ideia atrai quem trabalha com previsão e tomada de decisão sob incerteza, pois entrega calibração como saída nativa. Falta verificar avaliações independentes; os números vêm do próprio autor.

## 3. IA aplicada no setor público

*Brasil*

### 3.1 Segunda Semana de IA Serpro debate "IA Soberana" de 4 a 6 de novembro
**Fonte:** [Serpro](https://www.serpro.gov.br/menu/noticias/noticias-2026/a-poucos-dias-da-semana-de-ia-serpro-soberania-pauta-debate-sobre-o-futuro-dos-servicos-publicos) (semana de 26 a 31/10)

O evento, em Brasília e online, tem o tema "IA Soberana: Dados, Tecnologia e Poder de Decisão". No dia 4 entram o MGI, o MCTI, a experiência do Piauí e o aprendizado federado na Receita Federal; no dia 5, painel com Huawei, Oracle, Google e AWS sobre nuvem e autonomia do Estado; no dia 6, ferramentas contra a violência doméstica, a Plataforma IA do Brasil e experiências do Tesouro Nacional. A transmissão no YouTube é aberta. Importa porque a discussão desce do slogan para decisões concretas: onde os dados são processados, quem os acessa e que dependências o Estado assume ao contratar. Não encontrei, nas últimas 48 horas, novidade regulatória brasileira (PL 2338, ANPD) além desse evento.

*Internacional*

### 3.2 Padrão Microsoft–AFT para escolas proíbe treinar modelos com dados de alunos e professores
**Fonte:** [Nemko Digital](https://digital.nemko.com/news/microsoft-ai-guardrails-for-schools-take-effect-november-1) (01/11)

Em vigor desde 1º/11, o padrão firmado entre a Microsoft e o sindicato de professores AFT veda o uso de dados de estudantes e educadores para treinar modelos. É um acordo privado, não lei, mas funciona como referência contratual para redes públicas de ensino que compram IA. Útil para quem redige editais: a cláusula de não treinamento é replicável.

### 3.3 Justiça dos EUA mantém ação da NAACP contra data center da xAI em Memphis
**Fonte:** [TechCrunch](https://techcrunch.com/2026/10/31/judge-allows-naacp-lawsuit-over-xai-data-center-pollution-to-move-forward/) (31/10)

A juíza Debra M. Brown negou o pedido de arquivamento da xAI. A ação alega a operação de 35 turbinas a gás sem licença do Clean Air Act. O caso testa se licenciamento ambiental local alcança a infraestrutura de IA e pode servir de precedente para outros projetos.

### 3.4 Aprovação em Minnesota e pedido de moratória em Victoria expõem a disputa local por data centers
**Fonte:** [MPR News](https://www.mprnews.org/story/2026/10/31/hermantown-approves-controversial-google-data-center-during-late-night-meeting) (31/10) · [ABC News Australia](https://abc.net.au/news/2026-10-30/data-centre-moratorium-called-by-municipal-association-victor/107324748) (30/10)

A câmara de Hermantown aprovou por unanimidade um data center do Google de 500 MW, ainda sujeito a três processos e a aprovação estadual. Em Victoria, na Austrália, a associação de municípios pediu moratória para novos data centers de IA. Em ambos, a decisão é de governos locais, que lidam com energia, água e arrecadação. É o mesmo debate que o Brasil enfrentará com os projetos de data centers em andamento.

### 3.5 Washington Post: Copilot citou site gerado por IA em 75% dos testes sobre informações eleitorais
**Fonte:** [Washington Post](https://www.washingtonpost.com/technology/2026/10/30/how-an-obscure-website-became-force-americas-election-information-machine/) (30/10)

A investigação indica que um site obscuro, produzido por IA, virou fonte recorrente de assistentes de IA para perguntas sobre votação. Com eleições americanas próximas, o risco é que a desinformação se consolide por citação circular entre máquinas. Interessa a órgãos eleitorais, inclusive no Brasil, que já lidam com chatbots como canal de informação ao eleitor. Não li o texto completo, atrás de paywall; baseei-me no resumo.

## 4. IA aplicada em geral

### 4.1 Anthropic protocola o S-1 e pede listagem na Nasdaq com o ticker ANT
**Fonte:** [VentureBeat](https://venturebeat.com/technology/anthropic-files-to-go-public-on-nasdaq-as-ant-with-16-3b-in-revenue-for-first-six-months-of-2026) (26 a 31/10) · [SEC EDGAR](https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm)

O documento aponta receita de US$ 16,3 bi no primeiro semestre de 2026, ante US$ 1,16 bi um ano antes, e prejuízo líquido de US$ 80,7 bi, quase todo por efeitos contábeis de instrumentos de financiamento. O prejuízo operacional foi de US$ 693 milhões e o gasto com computação, de US$ 8,95 bi. Cerca de 80% da receita vem de uso por consumo, e há mais de 1.900 clientes com ao menos US$ 1 milhão. Entre os riscos, compromissos de infraestrutura que somam cerca de US$ 125 bi em cinco anos, dúvida sobre quando ações de um agente obrigam juridicamente quem o usa e uma demanda investigativa da FTC. É o primeiro grande retrato financeiro auditado de um laboratório de fronteira.

### 4.2 Agências devem atribuir à Anthropic nota especulativa na faixa BB após o IPO
**Fonte:** [TechCrunch](https://techcrunch.com/2026/10/30/anthropic-expected-to-receive-high-junk-rating-from-credit-agencies-following-ipo-report-says/) (30/10)

A expectativa de classificação "junk" alta reflete os compromissos de longo prazo com computação frente a uma receita ainda muito concentrada em consumo. Para o mercado, quer dizer custo de dívida maior justamente quando os laboratórios dependem de financiamento para capacidade. É relevante ler junto com o item anterior.

### 4.3 Apple levará o Qwen, da Alibaba, à Apple Intelligence na China
**Fonte:** [CGTN](https://news.cgtn.com/news/2026-10-31/Alibaba-s-Qwen-to-integrate-into-Apple-Intelligence-in-landmark-deal-1RHilSeJsbK/p.html) (31/10) · [The Verge](https://www.theverge.com/tech/1023974/apple-intelligence-china-ios-27-3)

O Qwen alimentará Siri, Writing Tools, Visual Intelligence e a limpeza de fotos na versão chinesa. Desenvolvedores testam a partir de 4/11, e o lançamento público vem no iOS 27.3, em dezembro. Mostra como a regulação local molda a cadeia de modelos: o mesmo produto usa modelos diferentes por jurisdição, e um modelo de laboratório chinês chega a centenas de milhões de aparelhos.

### 4.4 Balanços: AWS cresce mais de 39%, mas Amazon e Google queimam caixa com investimento em IA
**Fonte:** [Amazon IR](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Third-Quarter-Results/default.aspx) · [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/google-just-burned-9-billion-113209095.html) (semana de 26 a 31/10)

A Amazon reportou fluxo de caixa livre negativo de US$ 42,4 bi em 12 meses; a Google teve fluxo negativo de US$ 9 bi no trimestre, com receita de nuvem em alta de 103%. A demanda é real, mas o capex de IA consome o caixa. Esse é o pano de fundo do tema de financiamento dos itens 4.1 e 4.2.

### 4.5 Cohere mira rodada Série E de US$ 7 bi com foco em IA soberana
**Fonte:** [PR Newswire](https://www.prnewswire.com/news-releases/cohere-announces-series-e-fundraise-targeting-cad-7-billion-to-meet-surging-global-demand-for-secure-sovereign-ai-302924051.html) (semana de 26 a 31/10)

O valuation proposto é de CAD 35,7 bi. O argumento comercial é IA segura e soberana para governos e empresas regulamentadas, o que conecta com o item 3.1. Trata-se de meta de captação anunciada pela própria empresa, não de rodada fechada.

### 4.6 OpenAI reduz a meta da sua rodada de US$ 30 bi para cerca de US$ 20 bi, diz o FT
**Fonte:** [CoinDesk](https://www.coindesk.com/business/2026/10/30/openai-reportedly-cuts-fundraising-target-amid-ai-jitters) (30/10)

Segundo reportagem do Financial Times repercutida pelo CoinDesk, o corte reflete nervosismo dos investidores com o ritmo de gasto. Informação de fonte secundária e não confirmada pela empresa; tratar como indício de que o apetite por capital de IA ficou mais seletivo.

### 4.7 Altman se reúne com cerca de 50 executivos da Samsung para ampliar o fornecimento de memória do Stargate
**Fonte:** [The Edge Malaysia](https://theedgemalaysia.com/node/824062) (31/10)

A reunião em Yongin busca ampliar o acordo de memória para o Stargate. Memória de alta largura de banda é um dos gargalos da expansão de capacidade. Fonte secundária; sem detalhes de volume ou preço.

### 4.8 OpenAI, Google, Microsoft e Anthropic adotam um "policy token" no robots.txt para optar por não ter conteúdo usado em treinamento
**Fonte:** [Google Search Central](https://developers.google.cn/search/blog/2026/10/ai-training-control) · [The Verge](https://www.theverge.com/tech/1023763/openai-google-microsoft-ai-scraping-standard-opt-out) (semana de 26 a 31/10)

O padrão dá a editores um mecanismo comum para sinalizar que não querem seu conteúdo no treinamento, separado da indexação de busca. Reduz a fragmentação de regras por empresa, mas depende de adesão voluntária e não resolve o conteúdo já coletado. Relevante para quem constrói corpora e precisa documentar a conformidade.

### 4.9 Murata investirá ¥ 1 trilhão em cinco anos para dobrar a produção de capacitores para servidores de IA
**Fonte:** [Nikkei Asia](https://asia.nikkei.com/spotlight/supply-chain/japan-s-murata-to-invest-6.3bn-in-capacitor-production-for-ai-over-5-years) (semana de 26 a 31/10)

Capacitores MLCC, componentes minúsculos presentes aos milhares em cada servidor, viraram gargalo discreto da expansão. O anúncio mostra o efeito em cadeia da demanda de IA sobre fornecedores além de chips e memória.
