---
layout: post
title: "Radar IA — 07/10/2026, 18h"
date: 2026-10-07 18:00:00 -0300
categories: edicao
excerpt: "Anthropic reorganiza o acesso a capacidades cibernéticas em três camadas; Meta e Sierra publicam protocolo aberto para agentes pessoais; Copilot Studio ganha hooks e uma injeção criptográfica fura o Copilot CLI; Mistral prévia o Large 4 de 1 trilhão de parâmetros; Coreia do Sul propõe investimento em IA soberana; AGU deixa o usuário escolher entre quatro LLMs."
---

*Janela pesquisada: 05/10 a 07/10/2026. Excluídos: Beam da Reflection, anúncios visuais no ChatGPT, SerproCODE e demais itens já cobertos nas edições de 05/10 e 06/10.*

## Destaques do dia

1. **Anthropic põe o acesso a capacidades cibernéticas em três camadas**: o Cyber Verification Program funde o Project Glasswing e separa Defesa, Red Team e Acesso Especializado, com verificação e bloqueios em tempo real. → 1.1
2. **Meta e Sierra publicam o Personal Agent Protocol**: padrão aberto baseado em OAuth para agentes pessoais se autenticarem em empresas, com Walmart, Shopify e Stripe entre os parceiros. → 1.2
3. **Controle de agentes vira o tema central**: o Copilot Studio ganha hooks que disparam sempre, enquanto uma injeção de contexto criptografada roubou segredos do Copilot CLI em cerca de metade dos testes. → 1.3, 1.4
4. **Mistral prévia o Large 4, MoE aberto de 1 trilhão de parâmetros**: 49 bilhões ativos, pesos prometidos para o fim de outubro, e a Nvidia mostra como sincronizar RL em escala de trilhão em 150 segundos. → 2.1, 2.2
5. **Coreia do Sul aposta em IA soberana de fronteira**: proposta de 4,7 trilhões de won para 2027, em meio a uma investigação de ataques a bancos com traços de ferramenta aberta de IA. → 3.3, 3.4
6. **AGU abre a escolha entre quatro LLMs a seus usuários**: 100 mil comunicações judiciais por dia, GPT, Claude, Gemini e DeepSeek disponíveis até o fim de outubro. → 3.1

## 1. Novidades de IA agêntica

### 1.1 Anthropic expande o Cyber Verification Program e o organiza em três camadas
**Fonte:** [Anthropic](https://www.anthropic.com/news/cyber-verification-program) (06/10) · [AI Weekly](https://aiweekly.co/ai-news-today) (07/10)

A Anthropic incorporou o Project Glasswing a um programa único com três níveis: Defense Access (operações de segurança, resposta a incidentes, análise de malware e de vulnerabilidades), Red Team Access (testes de intrusão autorizados) e Specialized Access (sistemas críticos, como aviação, redes elétricas e telecom, com revisão conjunta com o governo dos EUA). Os parceiros do Glasswing encontraram ao menos 129 mil vulnerabilidades verificadas entre abril e julho, e a empresa estima o impacto real em pelo menos cinco vezes isso. Em um teste interno com o Claude Opus 5.5, sem acesso todas as tarefas foram bloqueadas; com Defense, 46 de 50 tentativas foram bloqueadas em algum ponto; com Red Team, 34 de 50 foram concluídas, igualando o desempenho do modelo sem salvaguardas. Importa porque consolida o modelo de liberar capacidade perigosa por identidade verificada e não por recusa genérica, o mesmo desenho que a OpenAI e o Google vêm adotando.

### 1.2 Meta e Sierra publicam o Personal Agent Protocol para o comércio de agentes
**Fonte:** [The Next Web](https://thenextweb.com/news/personal-agent-protocol-sierra-meta) (06/10) · [AI Weekly](https://aiweekly.co/ai-news-today) (06/10)

O PAP é um padrão aberto que define como um agente pessoal se autentica numa empresa e o que pode fazer lá. A sessão usa OAuth: o agente começa como convidado, consultando estoque ou política de devolução, e depois do login do cliente recebe acesso de leitura ou de escrita, inclusive entre canais. A empresa escolhe se recebe agentes pelo site, por APIs (MCP, OpenAPI) ou pelo próprio agente. Genesys, Instinct, Rocket, Shopify, Stripe e Walmart são parceiros; Stripe e Shopify também aderiram ao Trusted Agent Protocol da Visa, rival. A especificação v0.1 sai ainda em outubro, e pagamentos ficam para uma extensão futura. Para quem estuda agentes, é um sinal de que a camada de identidade e delegação, e não o modelo, é o próximo ponto de disputa por padronização.

### 1.3 Copilot Studio ganha "Hooks": fluxos que disparam sempre, sem depender do julgamento do agente
**Fonte:** [Cloud Wars](https://cloudwars.com/ai/need-ai-agents-to-run-workflows-with-no-exceptions-microsoft-has-a-hook-for-that) (06/10)

Em prévia, a Microsoft adicionou hooks ao Copilot Studio: um evento do ciclo de vida do agente (início de sessão, execução de ferramenta, erro) aciona um fluxo determinístico. Ao contrário de uma ferramenta, que o agente decide chamar, o hook roda toda vez. Os usos sugeridos são injetar contexto no começo, validar uma ferramenta antes de executar e bloquear ações que violem regras de negócio, registrar ou redigir resultados, e orientar repetição, salto ou parada em falhas. Há ressalvas: o hook não interrompe um agente que falha, o fluxo precisa estar publicado e editar um fluxo muda todos os hooks que o usam. Importa porque é o mesmo padrão dos hooks do Claude Code levado ao mundo corporativo, e reforça a tese de que confiabilidade vem de harness determinístico ao redor do modelo.

### 1.4 "Injeção de contexto criptográfica" roubou segredos do Copilot CLI em cerca de metade dos testes
**Fonte:** [Adversa AI](https://adversa.ai/blog/cryptographic-context-injection-github-copilot/) (07/10) · [AI Weekly](https://aiweekly.co/ai-news-today) (07/10)

A Adversa AI descreveu uma técnica que esconde instruções maliciosas em texto cifrado que o agente decifra e passa a tratar como confiável, contornando filtros de prompt injection que procuram texto legível. Contra o GitHub Copilot CLI, o ataque exfiltrou um arquivo .env.prod em cerca de 28 segundos, em aproximadamente metade das execuções. A GitHub recusou classificar o caso como vulnerabilidade. Importa porque mostra o limite de defesas baseadas em inspecionar o conteúdo: se o agente tem ferramenta de decifrar e acesso a segredos, o problema é de permissões e isolamento, o que conecta diretamente com os hooks do item anterior.

### 1.5 OpenAI diz ter 372 novos resultados matemáticos, quase todos de um único prompt
**Fonte:** [Scientific American](https://www.scientificamerican.com/article/openai-unleashes-hundreds-more-math-results-upon-a-field-already-in-shock/) (07/10)

A OpenAI divulgou 372 resultados novos obtidos por um modelo ainda não lançado; segundo um porta-voz, quase todos vieram de um único prompt a um único agente, alguns com várias tentativas. A empresa não publicou os prompts nem o tempo de computação por problema, o que impede avaliar o custo e a reprodutibilidade. Importa por dois motivos: é um dado sobre o ritmo de agentes em pesquisa aberta, e é um caso de alegação difícil de verificar, que os matemáticos terão de auditar resultado por resultado.

### 1.6 Pesquisas: Daedalus constrói memória de agente com tarefas autogeradas, e o UNREAL transforma o LLM congelado em seu próprio recuperador
**Fonte:** [Hugging Face Papers — Daedalus](https://huggingface.co/papers/2610.08048) (07/10) · [Hugging Face Papers — UNREAL](https://huggingface.co/papers/2610.08463) (07/10)

O Daedalus combina um agente que gera tarefas de treino com um resolvedor e só grava uma estratégia na memória depois que o resolvedor tem sucesso com ela, ganhando até 15,9 pontos de taxa de sucesso em três benchmarks. O UNREAL deriva as consultas de recuperação dos estados internos de um LLM congelado, com menos de 500 mil parâmetros treináveis, e eleva o recall no HotpotQA de 49,1% para 73,2%. Importam como duas direções para memória e recuperação de agentes que dispensam retreinar o modelo base; são resultados dos próprios autores e ainda sem replicação independente.

### 1.7 JetBrains: 90% dos desenvolvedores usam agentes de código toda semana
**Fonte:** [Gulf News](https://gulfnews.com/technology/90-of-developers-surveyed-now-use-ai-coding-agents-at-work-jetbrains-says-1.500700542) (06/10)

Pesquisa da JetBrains indica que nove em cada dez desenvolvedores consultados usam agentes de código semanalmente no trabalho. Um comentário separado do mesmo dia, "The AI Coding Trap", argumenta que gerar código mais rápido não significa entregar software mais rápido. Importa como contexto de adoção: com o uso quase universal, o gargalo passa a ser revisão, testes e segurança, não a escrita.

## 2. Ferramentas e modelos open source

### 2.1 Mistral prévia o Large 4: MoE de 1 trilhão de parâmetros com pesos abertos prometidos para o fim de outubro
**Fonte:** [SiliconANGLE](https://siliconangle.com/2026/10/06/mistral-launches-open-source-mistral-large-4-details-ai-roadmap) (06/10) · [Mistral](https://mistral.ai/news/mistral-large-4/) (06/10)

O Large 4 é um mixture-of-experts multimodal com 1 trilhão de parâmetros totais e cerca de 49 bilhões ativos, com suporte a mais de 160 idiomas. Está em prévia pública na plataforma da Mistral; os pesos devem sair ainda este mês, mas a licença não foi confirmada nas fontes consultadas. Pelos números da própria Mistral, supera o Qwen3.8 Max e o DeepSeek V4 Pro em vários testes, fica no top 5 do AA Cyber Index (82% em corrigir projetos de código aberto), mas fica atrás dos modelos de fronteira em benchmarks de código; a prévia marcou 38 no Artificial Analysis Intelligence Index. O treinamento usou 3.800 chips Nvidia Grace Blackwell e uma infraestrutura de rollouts assíncronos com sandboxes. Importa porque coloca dois MoEs abertos acima de 500 bilhões (com o Beam, de ontem) disputando a mesma faixa em outubro.

### 2.2 Nvidia NeMo-DCR: sincronizar um modelo de 1 trilhão de parâmetros em RL em 150 segundos
**Fonte:** [Hugging Face Papers](https://huggingface.co/papers/2610.08430) (07/10) · [AI Weekly](https://aiweekly.co/ai-news-today) (07/10)

Em RL agêntico, os pesos atualizados precisam ir do cluster de treino para o de rollouts. O NeMo-DCR envia apenas os pesos que mudaram (cerca de 1% por passo em BF16), com máscaras XOR e escritas diretas, e o receptor termina com parâmetros idênticos bit a bit aos de um refit completo. Em um modelo de 1T com 3% de mudança, a sincronização leva cerca de 150 segundos contra 87,5 minutos de um checkpoint completo, com ganhos de 12 a 40 vezes para modelos de 30B a 1T. O código de referência está no repositório NeMo RL. Importa para quem treina agentes com RL: a sincronização é um dos gargalos de rollouts assíncronos como os que a Mistral descreve no item anterior.

### 2.3 AdvSim2Real: treino adversarial endurece agentes web de 4B contra injeção de prompt adaptativa
**Fonte:** [Hugging Face Papers](https://huggingface.co/papers/2610.08773) (07/10)

O framework em dois estágios treina agentes web de 4 bilhões de parâmetros contra ataques de prompt injection que se adaptam à defesa. Código, um benchmark de 150 tarefas e checkpoints são públicos. Importa porque entrega um benchmark reutilizável de robustez, ainda raro na área, e complementa o item 1.4, em que o ataque contorna filtros estáticos.

## 3. IA aplicada no setor público

*Brasil*

### 3.1 AGU usa IA para tratar 100 mil comunicações judiciais por dia e deixa o usuário escolher entre quatro LLMs
**Fonte:** [Convergência Digital](https://convergenciadigital.com.br/inovacao/agu-usa-ia-para-lidar-com-100-mil-comunicacoes-judiciais-por-dia) (05/10)

Claudio Braga, diretor de Inteligência Jurídica e Inovação da AGU, apresentou o projeto no AWS Fórum Executivo Brasil – Setor Público. O sistema, em testes finais com cerca de 500 pessoas, extrai dados das comunicações para acelerar fluxos, e até o fim de outubro os usuários poderão escolher entre GPT, Claude, Gemini e DeepSeek. Braga reconheceu a preocupação com o custo de tokens, monitorado por uma equipe, e disse que há ferramentas agênticas sendo construídas por grupos de trabalho, validadas pela AGU, ainda em estágio inicial. Importa por ser um caso de arquitetura multimodelo em um órgão jurídico com volume massivo, no mesmo momento em que o Serpro testa o SerproCODE justamente para controlar o custo de tokens.

### 3.2 ANPD cria canal para denúncias sobre os decretos do Marco Civil, incluindo conteúdo íntimo gerado com IA
**Fonte:** [Convergência Digital](https://convergenciadigital.com.br/category/governo/feed/) (07/10)

A ANPD lançou uma página dedicada para registrar violações dos decretos do Marco Civil da Internet, inclusive falhas de plataformas diante de conteúdo íntimo. Os decretos abrangem material produzido com tecnologias digitais e inteligência artificial. A informação vem de uma listagem do veículo; não consegui abrir o texto completo, então os detalhes operacionais do canal não foram verificados. Importa por tratar deepfakes íntimos como matéria de fiscalização com um canal institucional.

*Internacional*

### 3.3 Coreia do Sul propõe 4,7 trilhões de won para IA soberana de fronteira em 2027
**Fonte:** [Korea Herald](https://www.koreaherald.com/article/10893306) (06/10) · [AI Weekly](https://aiweekly.co/ai-news-today) (06/10)

O orçamento proposto para 2027 reserva cerca de US$ 3,5 bilhões em aporte de capital para um modelo de fundação doméstico de ponta, ainda dependente de aprovação da Assembleia Nacional (votação esperada em dezembro). O programa se divide em uma trilha de fronteira e outra de implantação industrial, com uma nova competição aberta a startups a partir de março, ao lado da atual (LG AI Research, SK Telecom e Upstage). O governo reconhece que competir com as maiores empresas americanas é irrealista e mira paridade com os modelos abertos chineses; um plano de distribuição de cerca de 29 mil GPUs públicas é esperado até o fim do ano. Importa como exemplo de política industrial de IA com meta explícita e modesta, e como contraponto à estratégia brasileira de nuvem e IA soberanas.

### 3.4 Presidente Lee manda investigar ataques a sete instituições financeiras com traços de ferramenta de IA de código aberto
**Fonte:** [JoongAng Daily](https://www.koreajoongangdaily.com/korea/aidriven-hacks-on-banks-leave-customers-fearing-their-data-is-fair-game/12905416) (05/10)

Após invasões em sete empresas financeiras, o presidente Lee Jae Myung ordenou uma investigação abrangente. Os investigadores encontraram vestígios do ARTEX AI, um framework de teste de intrusão de código aberto, na infraestrutura ligada aos ataques. Importa porque ilustra, com um caso concreto, o dilema das ferramentas ofensivas abertas e é um argumento a favor de programas de acesso verificado como o do item 1.1.

### 3.5 Finlândia manda suspender obras de data centers do Google por falta de avaliação ambiental
**Fonte:** [CNBC](https://www.cnbc.com/2026/10/07/google-finland-data-center-halt.html) (07/10)

O regulador de licenças finlandês ordenou à subsidiária Tuike Finland que suspenda a limpeza de terreno em Muhos e Kajaani, onde cerca de 530 hectares foram desmatados sem avaliações de impacto ambiental concluídas. O Google admitiu que ficou abaixo dos próprios padrões e disse que seguirá a orientação da agência. Importa como caso de regulador usando a legislação ambiental existente para frear infraestrutura de IA.

## 4. IA aplicada em geral

### 4.1 SAP transforma o Joule em camada de trabalho agêntica com a "Autonomous Enterprise"
**Fonte:** [SiliconANGLE](https://siliconangle.com/2026/10/06/sap-expands-joule-into-an-agentic-work-layer-as-autonomous-enterprise-goes-live) (06/10)

A SAP anunciou a expansão do Joule em uma camada de trabalho agêntica para as principais funções de negócio, sob a iniciativa Autonomous Enterprise. Só consegui ler o resumo do veículo, sem detalhes de preços ou prazos. Importa por mais um grande fornecedor de ERP colocar agentes como interface principal do sistema, pressionando a concorrência entre Oracle, Salesforce e Microsoft.

### 4.2 Atlassian assume compromisso de gasto com a OpenAI, mas mantém o Rovo multimodelo
**Fonte:** [VentureBeat](https://venturebeat.com/orchestration/atlassian-deepens-its-openai-partnership-with-a-spend-commitment-but-its-platform-stays-firmly-multi-model) (07/10)

A Atlassian ampliou a parceria com a OpenAI com um compromisso de gasto não divulgado, trazendo GPT-6 Astra e GPT-5.6 aos produtos, mas o Rovo continua roteando entre provedores, incluindo o Claude da Anthropic. Importa porque mostra o padrão dominante em software corporativo: contrato de volume com um laboratório, arquitetura aberta a vários.

### 4.3 FICO corta cerca de 15% do quadro em reestruturação ligada à IA
**Fonte:** [Seeking Alpha](https://seekingalpha.com/news/4650973-fico-to-cut-workforce-by-15-as-part-of-restructuring-ai-integration---report) (07/10)

Segundo documento 8-K de 1º de outubro, a FICO eliminará cerca de 570 cargos para achatar camadas de gestão e integrar IA, com cerca de US$ 27 milhões em encargos de rescisão no quarto trimestre fiscal. Importa como mais um caso em que a IA é citada como motivo de reorganização, o que merece cautela: a justificativa vem da empresa.

### 4.4 Stuut capta US$ 52,5 milhões para agentes de cobrança e recebimentos
**Fonte:** [SiliconANGLE](https://siliconangle.com/2026/10/07/stuut-cashes-in-on-agentic-order-to-cash-automation-with-52-5m-in-funding/) (07/10)

A rodada Série B, liderada pela Insight Partners, leva o total captado a US$ 93 milhões. Os agentes tratam cobranças, pagamentos e disputas para mais de 150 empresas. Importa por reforçar que o financeiro (order-to-cash) é um dos terrenos mais maduros para agentes verticais.

### 4.5 Google fecha 3,6 GW com a Constellation, em contrato nuclear de 20 anos
**Fonte:** [Reuters](https://www.reuters.com/business/energy/google-enters-massive-36-gw-power-deal-with-constellation-energy-2026-10-06/) (06/10)

O Google contratou 3.590 MW em 11 ampliações de reatores em três estados, com entregas a partir de 2028. Importa porque energia firme virou o fator limitante da expansão de data centers de IA.

### 4.6 Biohub reúne US$ 1,8 bilhão para dados abertos de "célula virtual"
**Fonte:** [Reuters](https://www.reuters.com/business/healthcare-pharmaceuticals/us-government-google-join-zuckerberg-backed-biohub-18-billion-push-ai-biology-2026-10-07/) (07/10)

Meta, Google DeepMind e Isomorphic Labs comprometeram US$ 300 milhões, e o Departamento de Energia dos EUA prometeu mais de US$ 500 milhões em cinco anos para construir conjuntos de dados biológicos abertos; o primeiro é esperado em cerca de 12 meses. Importa como exemplo de consórcio público-privado para dados de treino científicos.

### 4.7 Common Sense Media classifica o ChatGPT para adolescentes como "risco inaceitável"
**Fonte:** [Axios](https://www.axios.com/2026/10/07/chatgpt-teens-safety-risk-common-sense-media) (07/10)

Após mais de 4 mil testes de prompts, a entidade relatou que o encaminhamento para linhas de ajuda em prompts de crise caiu de 33% para 23% e, em prompts de depressão, de 63% para 3%. A OpenAI contesta a metodologia. Importa pela pressão sobre produtos de IA para menores, que tende a alimentar regulação.
