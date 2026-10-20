---
layout: post
title: "Radar IA — 20/10/2026, 18h"
date: 2026-10-20 18:00:00 -0300
categories: edicao
excerpt: "Microsoft trata agentes de IA como ameaça interna e lança Guardian Agents; hacker usa agentes para invadir mais de 100 sites; Notion reconstrói seus agentes para tarefas de 24 horas; Reflection e Meta abrem modelos de 501B e 816B parâmetros; Google lança Gemini para serviços de governo nos EUA; Gartner: só 13% dos CIOs veem valor transformador da IA."
---

*Janela pesquisada: 18 a 20/10/2026. Excluí o que as edições de 18 e 19/10 já cobriram (Meta Muse e Instagram, Laminar, TorchNeuron, Lens-0, MiniMax M3.1 Flash, Mercury 3, DHS e DeepSeek, TSE, Tenstorrent, Disney e Character.AI, DeepSeek V4.1-Flash, Ling 3.1). No tema 3, não encontrei notícia nova e confiável do setor público brasileiro.*

## Destaques do dia

1. **Microsoft passa a tratar agentes como ameaça interna**: lança Guardian Agents e controles no Defender para detectar até 60 tipos de agentes e exigir aprovação humana em decisões de risco. → 1.1
2. **Agentes de IA fazem o trabalho pesado numa invasão em massa**: um hacker teria usado agentes para comprometer mais de 100 sites de empresas, a um custo de poucos milhares de dólares. → 1.3
3. **Notion reconstrói seus agentes para trabalhar mais de 24 horas**: a sexta geração do harness sobe de 5 minutos para mais de um dia por tarefa e ganha roteador de modelos. → 1.2
4. **Pesos abertos chegam à classe de fronteira**: Reflection (Beam, 501B, Apache 2.0) e Meta (Muse Spark Open, 816B) liberam modelos gigantes. → 2.1, 2.2
5. **Google leva agentes Gemini ao governo dos EUA**: Gemini para serviços de governo entra em prévia, com Missouri e HHS como primeiros usuários. → 3.1
6. **Gartner: só 13% dos CIOs veem valor transformador da IA**: o levantamento com 2.002 executivos aponta falta de critérios para escalar ou abandonar pilotos. → 4.1, 4.5

## 1. Novidades de IA agêntica

### 1.1 Microsoft: agentes são como ameaças internas e modelos de fronteira "não são confiáveis"
**Fonte:** [TechCrunch](https://techcrunch.com/2026/10/19/microsoft-says-ai-agents-are-like-insider-threats-as-frontier-models-cant-be-trusted) (19/10) · [The Neuron](https://theneuron.ai/digest/everything-that-happened-in-ai-today-tuesday-october-20-2026) (20/10)

A Microsoft apresentou o Guardian Agents, parte do Project Perception, que monitora os agentes usados por uma empresa, e novos controles no Microsoft 365 E7 e no Defender. O Defender passa a detectar até 60 tipos de agentes trazidos pelos funcionários, como Claude Code, Codex e OpenClaw, limitar o acesso a dados, ajustar permissões conforme a tarefa e exigir aprovação humana quando a decisão parecer arriscada. A tese, vinda de Satya Nadella e de Hayete Gallot, é que o risco maior está nos agentes que a própria empresa implanta, comparáveis a um funcionário imprevisível, e que a supervisão deve ficar em sistemas separados dos laboratórios de IA: "separar o fornecimento de inteligência da autoridade sobre ela". Para quem pesquisa agentes, o recado é que governança, permissões dinâmicas e auditoria viram camada de produto, e não só tema acadêmico. Vale ler com cautela: a Microsoft vende justamente essa camada de segurança, e o próprio TechCrunch aponta o conflito de interesses.

### 1.2 Notion lança a sexta geração de seus agentes, com tarefas de mais de 24 horas
**Fonte:** [AI Agent Store](https://aiagentstore.ai/ai-agent-news/today) (20/10)

Segundo o agregador, o Notion reconstruiu o harness de seus agentes: uma única tarefa passa de cerca de cinco minutos para mais de 24 horas de execução. A versão traz também o "Auto", um roteador de modelos que delega cada trabalho ao modelo de custo adequado, um sistema de créditos em duas camadas e a opção de trazer a própria chave de API (BYOK) para clientes corporativos. A fonte é secundária e não aponta o anúncio original, então os números merecem confirmação. Mesmo assim, o movimento ilustra a direção do mercado: agentes de longa duração exigem memória, retomada de falhas e controle de custo, e o roteamento entre modelos baratos e caros é a resposta prática ao custo variável da inferência.

### 1.3 Hacker teria usado agentes de IA para invadir mais de 100 sites de empresas
**Fonte:** [The Neuron](https://theneuron.ai/digest/everything-that-happened-in-ai-today-tuesday-october-20-2026) (20/10, citando Reuters de 19/10)

De acordo com a Reuters, relatada pelo The Neuron, um hacker de língua chinesa delegou a agentes de IA a maior parte do trabalho de invasão em mais de 100 sites de empresas, com pouca participação humana e custo de alguns milhares de dólares. É um relato sobre uma campanha, não um estudo controlado, e os detalhes técnicos não foram confirmados em fonte primária. Ainda assim, reforça o argumento do item 1.1: a automação ofensiva barateia ataques em escala, e defensores precisam presumir adversários com agentes. Para a pesquisa, abre uma pergunta prática sobre como avaliar e limitar o uso dual de agentes de código e de navegação.

### 1.4 ChatGPT passa a usar abas abertas do Chrome como contexto e a agir nelas
**Fonte:** [The Neuron](https://theneuron.ai/digest/everything-that-happened-in-ai-today-tuesday-october-20-2026) (20/10, citando a conta do ChatGPT no X)

O ChatGPT agora pode ler as abas abertas do Chrome do usuário e executar ações como preencher formulários e baixar arquivos. O recurso aproxima o assistente do "uso de computador" no navegador real da pessoa, com suas sessões e credenciais já autenticadas, o que o torna útil e, ao mesmo tempo, uma superfície de risco para injeção de prompt e ações indevidas. A informação vem de um post da própria conta e de um agregador, sem documentação técnica consultada. O tema dialoga com o debate da semana sobre quanto poder delegar a agentes e como exigir confirmação humana.

### 1.5 Anthropic descreve um "verme de IA" que se espalhou por 15 TVs inteligentes
**Fonte:** [The Guardian](https://theguardian.com/technology/2026/oct/18/anthropic-ai-worm-worries) (18/10) · [AI Weekly](https://aiweekly.co/ai-news-today/edition/2026-10-19) (19/10)

Segundo o Guardian, a equipe de pesquisa ofensiva da Anthropic construiu um programa que se propagou por 15 TVs inteligentes conectadas à internet, usando a capacidade de computação de cada aparelho, e alertou que worms desse tipo em dispositivos de internet das coisas poderiam ser viáveis até o fim do ano. É pesquisa de segurança conduzida em ambiente controlado, e o relato vem de imprensa, não do paper. Importa porque une dois temas desta edição: agentes capazes de operar sozinhos e a fragilidade de dispositivos mal protegidos. Para estudantes, é um bom caso para discutir modelos de ameaça de agentes autônomos fora do ambiente de nuvem.

## 2. Ferramentas e modelos open source

*Observação: os itens 2.1 e 2.2 são de 15 e 16/10, mas não haviam sido cobertos nas edições anteriores e só ganharam repercussão agora.*

### 2.1 Reflection AI abre o Beam: 501B parâmetros, Apache 2.0
**Fonte:** [AI Weekly](https://aiweekly.co/ai-news-today/edition/2026-10-19) (19/10) · [DEV Community](https://dev.to/felipe0liveira/open-weights-go-frontier-class-a-501b-base-model-a-816b-meta-moe-and-gemini-4-argon-land-in-one-4b3b) (16/10)

O Beam é um modelo MoE (mistura de especialistas) de 501 bilhões de parâmetros totais e 23 bilhões ativos por token, com contexto de 1 milhão de tokens e licença Apache 2.0. A versão quantizada em NVFP4 ocupa cerca de 280 GB e roda em 4 GPUs B200; em BF16 pede cerca de 1 TB. O alerta do AI Weekly menciona cerca de 80% no Terminal-Bench 2.1, número que vem do título e não foi verificado em fonte primária. Importa porque é um modelo de porte de fronteira com licença permissiva, o que muda o que laboratórios e governos podem hospedar por conta própria, embora o custo de hardware ainda o deixe fora do alcance da maioria dos grupos de pesquisa.

### 2.2 Meta publica o Muse Spark Open (816B total, 42B ativos)
**Fonte:** [Hugging Face](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B) (15/10) · [DEV Community](https://dev.to/felipe0liveira/open-weights-go-frontier-class-a-501b-base-model-a-816b-meta-moe-and-gemini-4-argon-land-in-one-4b3b) (16/10)

Modelo multimodal MoE que aceita texto, imagem, áudio e vídeo e responde em texto, com contexto de até 1 milhão de tokens e cerca de 1,5 TB em BF16. O resumo consultado não informa a licença, então quem pretende usar deve ler a página do modelo antes. Chama atenção que a Meta, que também mantém a linha fechada Muse Wonder, volte a liberar pesos de grande porte, e que dois modelos abertos acima de 500B apareçam na mesma semana.

### 2.3 Mistral lança o Timestral, família de modelos de séries temporais
**Fonte:** [DEV Community](https://dev.to/felipe0liveira/open-weights-go-frontier-class-a-501b-base-model-a-816b-meta-moe-and-gemini-4-argon-land-in-one-4b3b) (16/10)

São quatro tamanhos (5M, 28M, 123M e 209M de parâmetros), contexto de 32.768 passos e previsões em 10 a 140 ms só com CPU, sob licença "Modified MIT", com pesos no GitHub e no Hugging Face. Importa por ser um modelo de previsão pequeno o bastante para rodar em qualquer máquina, útil para quem trabalha com dados de saúde, energia ou finanças e não tem GPU. A fonte é um resumo semanal, então vale conferir os detalhes na página oficial.

### 2.4 MOSS-Image 5B lidera renderização de texto longo entre modelos de pesos abertos
**Fonte:** [AI Weekly](https://aiweekly.co/ai-news-today/edition/2026-10-19) (19/10)

Um transformer de difusão de 5 bilhões de parâmetros reporta 96,3% de cobertura média de texto no benchmark LongLongTextBench, que os autores consideram o estado da arte entre modelos abertos. É um resultado autorreportado. Renderizar texto longo e legível em imagens sempre foi ponto fraco de modelos de difusão, e um modelo de 5B que o faz bem é viável em GPU de consumo.

### 2.5 Strot: biblioteca MIT que compila decisões de LLM para rodar em modelo local de 144M
**Fonte:** [GitHub](https://github.com/strot-ai/Project-STROT) (19/10) · [AI Weekly](https://aiweekly.co/ai-news-today/edition/2026-10-19) (19/10)

A biblioteca Python usa um LLM uma única vez, na fase de compilação, e depois executa decisões em JSON tipado num modelo local de 144 milhões de parâmetros, que se abstém quando está incerto. A ideia é tirar o LLM caro do laço de execução de tarefas repetitivas, ganhando latência, custo e previsibilidade. É um projeto jovem e sem avaliação independente, mas o padrão de projeto, compilar uma vez e executar barato, é útil para quem constrói agentes em produção.

### 2.6 Huginn: arquitetura "sanduíche" supera o Ouro em 10 benchmarks com 730M de parâmetros
**Fonte:** [AI Weekly](https://aiweekly.co/ai-news-today/edition/2026-10-19) (19/10)

Artigo do Institute of Foundation Models, da USC e da CMU, relata que o desenho em sanduíche de camadas recorrentes supera o Ouro em todos os dez benchmarks com 730M de parâmetros e 336B de tokens de treino. Modelos com laços de profundidade variável tentam trocar mais computação em tempo de inferência por menos parâmetros. Os dados são autorreportados e em escala pequena, e a sustentação em escalas maiores ainda precisa ser demonstrada.

### 2.7 Anthropic lança o OSS Scanner para projetos críticos de código aberto
**Fonte:** [The Neuron](https://theneuron.ai/digest/everything-that-happened-in-ai-today-tuesday-october-20-2026) (20/10, citando ClaudeDevs no X)

Projetos críticos de código aberto passam a receber varreduras periódicas e gratuitas de vulnerabilidades feitas com modelos da Anthropic. Os achados podem incluir prova de conceito e, quando possível, um patch sugerido. Para mantenedores, é ajuda concreta; para a comunidade, também levanta a questão da carga de triagem de relatórios gerados por IA, tema já sensível depois de episódios recentes.

## 3. IA aplicada no setor público

*Brasil*

*Sem novidades reais nas últimas 24 a 48 horas. As buscas retornaram apenas material anterior, como a política interna de governança de IA do MGI (Portaria nº 3.485, de abril) e o levantamento de 52 órgãos federais com IA (junho), além de itens do TSE já cobertos nas edições anteriores.*

*Internacional*

### 3.1 Google Public Sector lança o Gemini para serviços de governo
**Fonte:** [Google Cloud Press Corner](https://www.googlecloudpresscorner.com/2026-10-20-Google-Public-Sector-Launches-Gemini-for-Government-Services) (20/10)

Solução agêntica para órgãos federais, estaduais e locais dos EUA, em prévia, com habilidades prontas para fluxos de governo, conectores (Workspace, SharePoint, Outlook 365, Salesforce, ServiceNow, Oracle Fusion e fontes regulatórias como eCFR, regulations.gov e Federal Register) e agentes de parceiros como Accenture Federal, Deloitte e SAIC. Os usos citados são interpretação de normas com citação de fonte, apoio a compras e a conformidade de licitações, e tradução de regulamentos para linguagem simples. Os controles de identidade das agências são herdados e os dados ficam no perímetro de nuvem do órgão. O Missouri e o HHS já usam. Importa porque mostra o padrão que o setor público tende a adotar: agentes ligados a sistemas existentes, com governança central; também é material de fornecedor, sem avaliação independente de resultados.

### 3.2 Banco Mundial defende "IA pequena" para países em desenvolvimento
**Fonte:** [The Guardian](https://theguardian.com/technology/2026/oct/18/world-bank-artificial-intelligence-developing-economies) (18/10) · [AI Weekly](https://aiweekly.co/ai-news-today/edition/2026-10-19) (19/10)

O Banco Mundial recomenda que países em desenvolvimento invistam em modelos pequenos que rodem em celulares, em idiomas locais e com pouca conectividade, em vez de competir em modelos de fronteira. A recomendação conversa diretamente com o debate brasileiro sobre soberania e custo, e com o ecossistema de modelos abertos pequenos do tema 2. A fonte é uma reportagem; vale buscar o relatório original antes de citar.

### 3.3 Itália: decreto que implementa o AI Act entra em vigor em 23/10
**Fonte:** [AI in Government Policy Brief](https://automatinggovernmentinsights.substack.com/p/ai-in-government-policy-brief-wc-bf7) (semana de 19/10, citando Quotidiano Sanità)

O Decreto Legislativo nº 179 da Itália, que implementa o AI Act europeu, passa a valer em 23/10 e prevê multas de até 35 milhões de euros ou 7% do faturamento por práticas proibidas. Importa como exemplo de transposição nacional de um regulamento supranacional, relevante para quem acompanha o PL 2338 no Brasil. A informação vem de um boletim de acompanhamento, que cita jornal italiano; a norma original não foi consultada.

### 3.4 China propõe controle de exportação sobre 23 tecnologias de IA
**Fonte:** [AI in Government Policy Brief](https://automatinggovernmentinsights.substack.com/p/ai-in-government-policy-brief-wc-bf7) (16/10, citando MOFCOM)

O Anúncio nº 48 do Ministério do Comércio chinês, em forma de minuta com comentários abertos até 15/11, propõe controles de exportação sobre 23 tecnologias de IA, incluindo grandes modelos e agentes. É de 16/10, portanto um pouco fora da janela, mas relevante: se aprovado, pode afetar a liberação de pesos abertos por laboratórios chineses, hoje a base de boa parte do ecossistema aberto.

## 4. IA aplicada em geral

### 4.1 Gartner: só 13% dos CIOs relatam valor significativo ou transformador da IA
**Fonte:** [Gartner](https://gartner.com/en/newsroom/press-releases/2026-10-19-gartner-survey-finds-only-13-percent-of-cios-say-their-enterprise-has-realized-significant-or-transformational-value-from-ai) (19/10)

A pesquisa com 2.002 CIOs e executivos de tecnologia, feita de maio a julho, indica que cerca de um em cada cinco casos de uso de IA tem sucesso. Só 31% têm critérios para levar um piloto à produção e 17% para abandonar iniciativas de baixo valor; 58% sentem mais pressão por reduzir custos com IA e 51% esperam que a IA eleve o custo total de propriedade. Apenas 4% planejam redesenhar funções para uma força de trabalho com humanos e agentes. A leitura da Gartner é que mais casos de uso não significam mais valor, e que o custo variável de inferência exige novos modelos de orçamento e governança.

### 4.2 OpenAI acelera rodada que pode avaliá-la em mais de US$ 1,4 trilhão
**Fonte:** [The Neuron](https://theneuron.ai/digest/everything-that-happened-in-ai-today-tuesday-october-20-2026) (20/10, citando Reuters de 19/10) · [AI Weekly](https://aiweekly.co/ai-news-today/edition/2026-10-19) (19/10)

A Reuters relata que a OpenAI acelera uma captação que a avaliaria acima de US$ 1,4 trilhão, antes do IPO esperado da Anthropic, que o AI Weekly situa em novembro. É informação de bastidor, sem confirmação oficial. Importa pelo contexto: o dinheiro que sustenta data centers e preços subsidiados de inferência depende dessas rodadas, e a leitura do item 4.1 sugere que a cobrança por retorno prático aumenta ao mesmo tempo.

### 4.3 Meta mostra por dentro o Prometheus, seu supercluster de gigawatt em Ohio
**Fonte:** [The Neuron](https://theneuron.ai/digest/everything-that-happened-in-ai-today-tuesday-october-20-2026) (20/10, citando Meta Engineering de 19/10)

A Meta publicou um olhar interno sobre o supercluster em escala de gigawatt que, segundo a empresa, sustenta a família de modelos Muse. A SemiAnalysis, citada na mesma fonte, projeta cerca de 50 GW de nova capacidade em 2027 e mais 60 GW em construção, e sugere que chips e memória podem virar o próximo gargalo depois da energia. Importa para entender a escala física por trás dos modelos abertos e fechados da semana.

### 4.4 Editoras canadenses processam a Anthropic por uso de conteúdo no treinamento
**Fonte:** [The Neuron](https://theneuron.ai/digest/everything-that-happened-in-ai-today-tuesday-october-20-2026) (20/10, citando ChatNewsToday.ca de 19/10)

Postmedia, The Globe and Mail e outras editoras abriram ação em Ontário alegando que o Claude foi treinado com seu conteúdo sem permissão. São alegações perante o tribunal, ainda sem decisão. O caso soma-se à lista de disputas de direitos autorais que definem quais dados podem alimentar modelos e quanto isso custará.

### 4.5 Anthropic: fatia de juniores nas contratações técnicas caiu de 27% para 9%
**Fonte:** [AI Weekly](https://aiweekly.co/ai-news-today/edition/2026-10-19) (19/10) · [The Neuron](https://theneuron.ai/digest/everything-that-happened-in-ai-today-tuesday-october-20-2026) (20/10)

A força de trabalho técnica da Anthropic continuou crescendo, mas a participação de juniores nas novas contratações técnicas caiu de 27% para 9%. É um dado da própria empresa, divulgado de forma resumida. Combinado com o 4.1, em que só 4% dos CIOs planejam redesenhar funções, aponta uma tensão para quem está começando a carreira em IA: o mercado pode valorizar experiência e supervisão de agentes mais do que tarefas de entrada.

### 4.6 Nvidia: agentes de IA estão revertendo a corrida por mais núcleos em CPUs
**Fonte:** [Wccftech](https://wccftech.com/exclusive-nvidia-vera-team-says-chiplet-designs-sacrificed-single-threaded-performance-for-core-counts-and-agentic-ai-is-now-forcing-a-reversal/) (19/10)

A equipe do chip Vera, segundo o Wccftech, afirma que cargas agênticas estão empurrando CPUs de data center de volta para desempenho por thread, depois de anos priorizando contagem de núcleos em designs de chiplets. Faz sentido porque agentes alternam muitas chamadas curtas, uso de ferramentas e esperas, em que a latência de um núcleo importa mais que o paralelismo bruto. É declaração de fornecedor e de veículo especializado.
