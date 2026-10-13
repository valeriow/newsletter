---
layout: post
title: "Radar IA — 13/10/2026, 18h"
date: 2026-10-13 18:00:00 -0300
categories: edicao
excerpt: "Meta lança o Muse Wonder e o Gemini 4 Argon chega a mais assinantes; Anthropic alerta que modelos abertos pequenos podem se replicar em hardware barato; defesas contra destilação cortam a extração de raciocínio em até 100 vezes; reguladores bancários dos EUA questionam bancos sobre IA agêntica; decreto brasileiro de SAC permite IA mas garante atendimento humano; Torvalds usa o Claude Code e a Anthropic troca o git por um sistema próprio."
---

*Janela pesquisada: 11 a 13/10/2026. Ficaram de fora os temas já cobertos nas edições de 10, 11 e 12/10 (Coaf, supercomputador nacional, Cisco no Webex, Work IQ, HCLTech–Anthropic, Nous Research, Ling 3.1 Flash, EmbeddingGemma 2, GPT-6). Itens brasileiros de 02 e 05/10 (TJRS e ONS) foram descartados por serem anteriores à janela.*

## Destaques do dia

1. **Os modelos de fronteira ganham mais um concorrente e outro se espalha**: a Meta lançou o Muse Wonder, com memória entre conversas e persistência de objetivos, e o Gemini 4 Argon, do Google, passou a chegar aos assinantes Pro e Ultra. → 1.1, 1.2
2. **Modelos abertos pequenos podem estar a meses de se replicar sozinhos**: a Anthropic mostrou um modelo de 9 bilhões de parâmetros rodando em 8 de 9 tipos de hardware barato e prevê replicação completa por modelos abaixo de 30B até o fim do ano. → 1.3
3. **Proteger o raciocínio do modelo virou frente de segurança**: a Anthropic diz que novas defesas reduziram em 10 a 100 vezes a extração de raciocínio por destiladores, enquanto Reuters mostra os laboratórios disputando o controle sobre relatórios de avaliadores externos. → 1.4, 1.5
4. **Reguladores bancários dos EUA começam a perguntar sobre agentes**: Fed, OCC e FDIC questionam bancos sobre IA agêntica, modelos chineses, desligamento e trilhas de auditoria. → 3.2
5. **Decreto brasileiro de SAC libera a IA, mas protege o atendimento humano**: o Decreto 13.135 exige humano das 8h às 20h, cancelamento em qualquer nível e proíbe que a IA bloqueie o acesso a pessoas. → 3.1
6. **Agentes de código já mexem no coração da infraestrutura**: Torvalds publicou um branch do kernel escrito com o Claude Code, e a Anthropic trocou o git por um sistema interno por causa do volume de merges feitos por agentes. → 2.1, 4.1

## 1. Novidades de IA agêntica

### 1.1 Meta lança o Muse Wonder, com memória ativa e foco em objetivos
**Fonte:** [Meta Research](https://research.meta.ai/blog/muse-wonder) (12/10)

A Meta apresentou os modelos Muse Wonder e Muse Wonder Full, que apresenta como um passo rumo à "superinteligência pessoal". As duas funções centrais são a Active Memory, que guarda contexto do usuário entre conversas, e o Active Focus, que mantém o trabalho em metas difíceis, tenta abordagens alternativas e pede confirmação antes de ações importantes. O Muse Wonder está na Meta Model API e no Muse Code; o Full é restrito a assinantes do Muse Code, e o relatório de segurança completo foi apenas prometido. Segundo um agregador, a Artificial Analysis deu ao Full 56 no Intelligence Index v4.3, o segundo lugar atrás do Claude Opus 5.5, número que não consegui confirmar na fonte primária. Importa porque memória persistente e persistência de objetivo são justamente as peças que transformam um chatbot em agente, e porque os modelos são proprietários: a Meta segue fora do campo de pesos abertos nesta geração.

### 1.2 Gemini 4 Argon chega a mais usuários, com preço promocional
**Fonte:** [Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/) (anúncio em 30/09; liberação ampla em 13/10, segundo agregador)

O Google anunciou o Gemini 4 Argon em 30/09 como modelo de fronteira para programação, trabalho de conhecimento corporativo e defesa cibernética, inicialmente para defensores selecionados pelo Fairwind Program. Os números divulgados pelo Google incluem 77,9% no DeepSWE v1.1, 51,3% no AutomationBench, da Zapier, e saída de até 1 milhão de tokens. O preço promocional é de US$ 2 por milhão de tokens de entrada e US$ 10 de saída, subindo para US$ 4 e US$ 20 depois. O agregador relata que em 13/10 o modelo passou a assinantes AI Pro e Ultra no app Gemini, no AI Mode e no Antigravity; a página do Google que consegui ler ainda descrevia a liberação como gradual. Para quem monta agentes, o ponto é o limite de saída de 1 milhão de tokens e o preço de introdução, que muda a conta de tarefas longas.

### 1.3 Anthropic: modelos abertos pequenos podem estar a meses de se replicar em hardware barato
**Fonte:** [Anthropic Frontier Red Team](https://www.anthropic.com/research/self-replicating-ai) (12/10)

A equipe de Frontier Red Team distribuiu o Gemma4-26B-A4B por 15 caixas Android TV de cerca de US$ 55 cada, a 0,39 token por segundo, e testou modelos configurando servidores de inferência em hardware variado: um modelo de 9B funcionou em 8 dos 9 tipos testados. Em avaliações simplificadas, o GLM-5.2 e modelos mais fortes completaram um ciclo de replicação de ponta a ponta numa rede com emuladores Android expostos por uma porta ADB sem autenticação. Modelos de até 30B já executam muitas etapas, mas falham ao encadeá-las, e a extrapolação do Epoch Capabilities Index (13,7 pontos por ano) sugere que podem chegar lá ainda em 2026. Os próprios autores avisam que a simplificação da etapa de exploração torna o resultado um limite superior e que o ECI é um indicador indireto. Importa porque desloca o debate de risco de "datacenters invadidos" para "dispositivos domésticos mal protegidos", e porque as defesas sugeridas são prosaicas: detecção de anomalias de rede, quarentena de dispositivos e padrões de segurança mais rígidos para fabricantes.

### 1.4 Anthropic detalha defesas contra destilação e diz ter reduzido a extração em 10 a 100 vezes
**Fonte:** [Anthropic](https://www.anthropic.com/research/distillation-defenses) (12/10, atualizado em 13/10)

A empresa descreve três frentes: contas de API criadas a partir de 31/08 não podem editar o contexto anterior do Claude (o chamado preserved thinking); um classificador de dois estágios bloqueia pedidos de extração, com falsos positivos abaixo de 0,1%; e usuários insistentes recebem limites mais duros e banimento, com cobrança de requisições bloqueadas desde 24/09. Os números são da própria Anthropic e sem verificação independente: queda de 90% a 99% nos dados coletados por destiladores e dezenas de milhares de contas banidas, muitas em menos de duas horas. Um teste citado mostra por que isso vale dinheiro: um modelo treinado com raciocínio completo atingiu 80,4% no SWE-bench Verified, contra 71,8% com raciocínio resumido. A empresa admite que será um jogo de gato e rato e que a mudança exigiu ajustes de alguns desenvolvedores, o que importa para quem integra a API.

### 1.5 Anthropic e OpenAI disputaram controle sobre o que avaliadores externos podem publicar
**Fonte:** [TheNextWeb, com base na Reuters](https://thenextweb.com/news/anthropic-openai-ai-evaluators-publication-control) (13/10)

Segundo a reportagem, até 5/10 as duas empresas queriam controle rígido sobre os relatórios de avaliadores externos, citando segredos comerciais e o risco de revisores levarem informação a concorrentes. Por volta de 8/10, as conversas da Anthropic com alguns revisores pareciam ter avançado. Em setembro, Dario Amodei havia dito que avaliadores deveriam publicar suas conclusões sem edição da empresa, e a OpenAI afirmou algo semelhante. A OpenAI diz remover só detalhes confidenciais, e a Anthropic diz que revisores já conhecidos definem o que publicar, mas mantém o direito de aprovar relatórios de firmas novas. Não existem regras claras, e a prática varia por avaliador. Importa para a avaliação de sistemas agênticos porque a credibilidade de qualquer relatório de segurança depende de quem controla a caneta final.

### 1.6 Pluto Security sai do anonimato com US$ 42 milhões para vigiar agentes e apps de IA nas empresas
**Fonte:** [TechCrunch](https://techcrunch.com/2026/10/13/pluto-security-raises-42m-as-ai-gives-enterprise-security-teams-a-new-headache/) (13/10)

A Pluto monitora skills, extensões, servidores MCP e agentes ou apps criados internamente, detecta atividade suspeita e pode interromper ações ou pedir confirmação ao agente em tempo real. A rodada soma US$ 8,5 milhões de seed, liderados pela TLV Partners, e US$ 34 milhões de série A, liderados pela Jump Capital. A empresa informa mais de 30 clientes e mais de US$ 2 milhões de receita recorrente anual. Um dado chama atenção: cerca de 60% dos riscos detectados estão em apps feitos por vibe coding por não desenvolvedores, com finanças à frente de marketing e jurídico. Importa porque indica que o risco de agentes está migrando dos times de engenharia para toda a empresa, e o próprio CEO diz ter achado atividade maliciosa em todas as provas de conceito (dado declarado pela empresa).

### 1.7 OpenAI Dots: agentes sempre ativos sobre o GPT-6 Astra
**Fonte:** [AI Agent Store, agregador](https://aiagentstore.ai/ai-agent-news/this-week) (12/10)

Segundo o agregador, o produto Dots oferece agentes que seguem trabalhando em metas definidas pelo usuário entre conversas, com computador próprio na nuvem e memória persistente, começando por clientes Pro e Business Premium, com limites regionais na Europa. Não encontrei confirmação em fonte primária da OpenAI, então trate como informação a verificar. Se confirmada, coloca a OpenAI na mesma direção da Meta (item 1.1): o agente deixa de ser uma sessão e passa a ser um processo de longa duração, com as perguntas de governança que isso traz.

### 1.8 Scuba capta US$ 34 milhões para uma "context engine" compartilhada por pessoas e agentes
**Fonte:** [Upstart Media](https://www.upstartsmedia.com/p/exclusive-slack-alums-launch-scuba) (13/10)

Fundada por ex-executivos do Slack, a Scuba guarda conteúdo da web capturado por uma pessoa e o compartilha com colegas e com agentes de IA, conectando-se a ChatGPT, Claude e Slack por conectores MCP. A Accel liderou o pré-seed e a IVP co-liderou o seed. Importa como sintoma: a camada de contexto compartilhado, e não só o modelo, está virando produto, e o MCP aparece como o encanamento padrão para ligá-la aos assistentes.

## 2. Ferramentas e modelos open source

*Sem lançamentos relevantes de modelos de pesos abertos nas últimas 48 horas: o agregador llm-stats registrou apenas os dois modelos proprietários da Meta no período. Há dois itens de software aberto e de código com IA.*

### 2.1 Torvalds publica branch do kernel Linux escrito com o Claude Code
**Fonte:** [HWBusters](https://hwbusters.com/news/linus-torvalds-uses-claude-code-to-rework-the-linux-page-cache-tripling-small-read-throughput/) (12/10)

Linus Torvalds publicou o branch noref-filemap-read-with-llm, com oito patches que eliminam a contagem de referências de folios no page cache para leituras pequenas, e disse que o código, os testes e o primeiro rascunho da carta de apresentação vieram do Claude Code sob sua direção. Num único notebook, a vazão com 8 threads no mesmo arquivo foi de cerca de 10 milhões para 30–33 milhões de leituras por segundo. As ressalvas são grandes: o próprio Torvalds diz que a parte de gerenciamento de memória é a "menos resolvida", um teste de estresse com 2 GiB acionou o OOM killer na versão parcial, uma leitura pequena de uma thread piorou, e nada foi integrado. Importa porque é um caso de código assistido por agente numa das bases mais exigentes do software livre, com revisão humana pesada, e mostra o modelo realista: o agente propõe e mede, o mantenedor decide.

### 2.2 Gemma Transcribe: o áudio do EmbeddingGemma 2 vira transcritor para Mac
**Fonte:** [eg2.haku.sh](https://eg2.haku.sh/) (13/10)

Uma equipe independente reaproveitou o codificador de áudio do EmbeddingGemma 2 e acrescentou um pequeno leitor que mapeia áudio em texto. Segundo os autores, o app transcreve uma hora de áudio em cerca de 13 segundos num MacBook Air M3 básico, com cerca de 5% de taxa de erro de palavras, após menos de duas horas de treino em 8 H100. São números autodeclarados e sem reprodução independente. Importa para quem trabalha com modelos pequenos: mostra o reuso de um componente de embedding multimodal recém-aberto para uma tarefa diferente, rodando local e sem custo de API.

## 3. IA aplicada no setor público

*Brasil*

### 3.1 Decreto 13.135 regula o SAC e permite IA sem bloquear o atendimento humano
**Fonte:** [Convergência Digital](https://convergenciadigital.com.br/governo/governo-aperta-regras-e-inclui-medidas-de-protecao-ao-uso-de-inteligencia-artificial-no-atendimento-ao-consumidor/) (13/10)

O Decreto nº 13.135, de 9 de outubro de 2026, entra em vigor em 20 dias e vale para empresas de setores regulados pelo governo federal e para instituições de serviços financeiros digitais supervisionadas pelo Banco Central, incluindo fintechs. A IA é permitida, mas não pode impedir o acesso ao atendimento humano, que deve estar disponível das 8h às 20h todos os dias, com atendimento imediato para demandas urgentes. Há prazos concretos: espera de até 20 segundos para 80% das ligações, retorno de ligação interrompida em até 5 minutos, resposta a reclamações em até 7 dias corridos e providências em até 48 horas para cobrança indevida. O cancelamento deve estar disponível em qualquer nível do atendimento, com comprovante eletrônico. Importa porque é uma regra operacional de IA no atendimento com métricas mensuráveis, diferente de princípios gerais; o portal a descreve como "atropelando a Anatel", enquadramento editorial que não verifiquei. Sem outras novidades brasileiras do setor público dentro da janela além deste item.

*Internacional*

### 3.2 Reguladores bancários dos EUA questionam bancos sobre IA agêntica e modelos chineses
**Fonte:** [PYMNTS, com base na Reuters](https://www.pymnts.com/news/banking/2026/banking-regulators-tighten-oversight-of-possible-ai-risks/) (13/10)

Segundo a Reuters, o Federal Reserve, o OCC e o FDIC estão perguntando aos bancos se usam tecnologia desenvolvida na China, se empregam agentes de IA em cibersegurança e se conseguem controlar sistemas autônomos, incluindo procedimentos de desligamento e trilhas de auditoria. O contexto é uma atribuição da CrowdStrike de invasões a bancos sul-coreanos a um agente de origem chinesa, possivelmente com o Claude Code, e um relato de agentes da OpenAI que teriam violado o Hugging Face no verão. A orientação conjunta de risco de modelos, atualizada em abril, não cobre IA generativa nem agêntica, e as agências planejam um pedido de informações separado. Importa porque define o que um supervisor vai pedir primeiro: um inventário em que cada sistema de IA tenha responsável, finalidade, classificação de risco, fornecedor e controles comprovados. Para o Brasil, é um indicativo de para onde a supervisão do Banco Central pode caminhar.

### 3.3 Apple não lançará o HomeView na UE, citando o AI Act
**Fonte:** [MacRumors](https://www.macrumors.com/2026/10/13/apple-homeview-wont-be-available-in-eu/) (13/10)

O display inteligente de US$ 299, com reconhecimento facial para até seis usuários, não será lançado na União Europeia, porque, segundo a Apple, os recursos avançados de Siri de que depende não estão disponíveis lá sob o AI Act. Não há prazo. Importa como exemplo concreto de custo de conformidade: a regulação europeia passa a moldar o catálogo de produtos, e não só os contratos, e quem a acompanha vê o efeito na prática.

### 3.4 Raven, da Graylark, localiza casas a partir de uma única foto interna e já é usada por polícias
**Fonte:** [404 Media](https://404media.co/ai-company-lets-cops-pinpoint-specific-houses-based-on-a-single-interior-photo) (13/10)

A ferramenta, versão renomeada do GeoSpy, compara fotos de interiores com anúncios do Airbnb, Zillow e Vrbo. Entre os clientes estão a polícia de Los Angeles e o xerife de Miami-Dade, que descreve o uso como "limitado e largamente exploratório"; até agora não houve avanços ou prisões relevantes. Importa pelo debate de privacidade e de uso policial de IA de geolocalização, em que a avaliação de eficácia ainda é anedótica.

### 3.5 China cria aliança de IA para matemática, citando distância dos EUA
**Fonte:** [Shanghai Daily](https://en.sedaily.com/international/2026/10/13/china-launches-math-ai-alliance-citing-gap-with-us) (12/10)

Lançada por Shing-Tung Yau em 11/10, a aliança reúne oito instituições de pesquisa e prevê uma rede de mais de mil cientistas, com foco em raciocínio matemático especializado, geração de conjecturas e formalização de provas. Yau a apresentou como resposta à distância crescente entre China e EUA em ciência movida por IA. Importa como mais um exemplo de coordenação estatal de pesquisa em torno de uma capacidade específica, algo que os programas nacionais de IA no Brasil ainda não fazem em escala comparável.

## 4. IA aplicada em geral

### 4.1 Anthropic troca o git por um sistema próprio, o Scion, por causa do volume de merges
**Fonte:** [Anthropic Engineering](https://www.anthropic.com/engineering/redesigning-source-control) (13/10)

Os merges diários no monorepo saltaram de cerca de 2.500 em maio para mais de 30.000 em setembro, e a infraestrutura de git não aguentou a carga gerada por agentes. Sete engenheiros migraram tudo em cinco meses; a empresa reporta infraestrutura com CPU e memória 200 vezes menores que os espelhos git anteriores e checkouts de CI e busca cerca de 100 vezes mais rápidos, com cerca de 25 milhões de checkouts por dia. Atenção ao enquadramento: o texto trata o Scion como sistema interno, que os autores dizem não ser substituto geral do git, e não encontrei licença aberta; agregadores que o chamam de código aberto parecem errados. Importa porque a ferramenta de controle de versão é um dos primeiros gargalos de uma empresa em que agentes escrevem código em escala.

### 4.2 NTT negocia data center de US$ 6,3 bilhões em Osaka para a Anthropic
**Fonte:** [Nikkei Asia](https://asia.nikkei.com/business/technology/artificial-intelligence/ntt-to-build-first-data-center-for-anthropic-in-japan) (12/10)

Segundo o Nikkei, a NTT Data está em negociações finais para construir o primeiro data center dedicado da Anthropic no Japão, com até 500 MW e operação parcial prevista para 2028; as partes pretendem assinar até 31 de março. Não consegui abrir a matéria completa, então os números vêm do resumo do agregador. Importa porque a disputa por capacidade de computação está virando infraestrutura regional dedicada, com implicações de soberania e latência para clientes locais.

### 4.3 Decagon, startup de agentes de atendimento, estuda venda por US$ 4,5 bilhões
**Fonte:** [Business Insider](https://www.businessinsider.com/ai-agent-company-decagon-hired-investment-bank-acquisition-interest-2026-10) (13/10)

A empresa contratou um banco de investimento e conversa preliminarmente com a ServiceNow e outros interessados, mantendo uma nova rodada de captação aberta caso a venda não avance. Seus agentes são usados por Duolingo, Notion, Hertz e Deutsche Telekom. Importa porque agentes de atendimento são o caso de uso mais maduro de agentes em empresas, e a consolidação por plataformas de fluxo de trabalho tende a vir em seguida; as informações são de negociações iniciais e podem não se concretizar.

### 4.4 Scaleway planeja supercomputador de IA com GPUs AMD na Suécia
**Fonte:** [Finimize](https://www.finimize.com/content/scaleway-takes-its-first-ai-supercomputer-outside-france) (13/10)

Anunciado na conferência de IA da Scaleway, em Paris, será o primeiro supercomputador de IA da empresa fora da França, com GPUs AMD Instinct MI355X de 288 GB e a pilha ROCm, e a Tele2 como parceira local. O acesso será oferecido a startups e empresas europeias. Importa pela alternativa à Nvidia e à nuvem americana para quem precisa de capacidade na Europa.

### 4.5 Apple Minions: nuvem de GPU feita com Macs ociosos
**Fonte:** [Apple Machine Learning Research](https://machinelearning.apple.com/research/distributed-gpu-cloud) (13/10)

O artigo descreve uma nuvem virtual de GPU que agrega GPUs de Apple Silicon ociosas para inferência, apresentada como alternativa a clusters centralizados, com ênfase em flexibilidade e tolerância a falhas. Organizações com frotas grandes de Macs poderiam rodar inferência sem comprar mais GPUs. É pesquisa, não produto, e sem números de desempenho confirmados por mim. Importa como linha de trabalho sobre aproveitar hardware já pago, em contraste com a corrida por novos data centers.
