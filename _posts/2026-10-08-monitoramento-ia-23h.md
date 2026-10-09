---
layout: post
title: "Radar IA — 08/10/2026, 23h"
date: 2026-10-08 23:30:00 -0300
categories: edicao
excerpt: "Anthropic lança a Cyber Mission com programa para infraestrutura crítica e scanner gratuito para código aberto; a Arena publica um índice de alinhamento de agentes com 90 mil sessões; a Anthropic atualiza a política de uso; a controladora da Manus capta mais de US$ 500 milhões; Cloudflare abre modelos de decisão enquanto a OpenAI mantém o seu fechado; o Canadá cria um conselho nacional de IA."
---

*Janela pesquisada: 07/10 a 08/10/2026. Foram excluídos os temas já cobertos nas edições de 05, 06 e 07/10 (Mistral Large 4, llama.cpp e modelos de decisão, Copilot Studio Hooks, SAP Joule, AGU e outros). Notícias sem confirmação em fonte confiável, como o suposto lançamento do Claude Haiku 5.5 e a liberação do GPT-6 para usuários gratuitos, ficaram de fora.*

## Destaques do dia

1. **Anthropic lança a Cyber Mission**: programa para infraestrutura crítica com 11 parceiros fundadores e um scanner gratuito de vulnerabilidades para projetos de código aberto. → 1.1
2. **Arena cria um índice de alinhamento de agentes**: 90 mil sessões e 27 modelos medidos em ação não autorizada, falsa atribuição e conclusão enganosa. → 1.2
3. **Anthropic endurece a política de uso**: novas regras contra interferência eleitoral, campanhas enganosas e abuso prolongado contra o modelo. → 1.3
4. **Controladora da Manus capta mais de US$ 500 milhões**: rodada liderada por Boyu e IDG reabre o jogo dos agentes chineses depois da compra frustrada pela Meta. → 1.4
5. **Modelos de decisão se dividem entre aberto e fechado**: a Cloudflare publica pesos Apache 2.0 enquanto a OpenAI mantém a Decisions API hospedada. → 2.1, 2.2
6. **Canadá cria conselho nacional de IA com Bengio**: 13 integrantes, caráter consultivo e foco em segurança, soberania e democracia. → 3.1

## 1. Novidades de IA agêntica

### 1.1 Anthropic lança a Cyber Mission com programa para infraestrutura crítica e scanner para código aberto
**Fonte:** [Anthropic](https://www.anthropic.com/news/anthropic-cyber-mission) (08/10)

A Anthropic apresentou uma iniciativa de longo prazo para ajudar defensores a proteger software e sistemas, começando por duas frentes. A primeira é o Critical Infrastructure Defense Program, que leva modelos Claude, engenheiros no local e pesquisa de ameaças a provedores que protegem tecnologia operacional (redes elétricas, água, transporte), com Accenture, Booz Allen, CrowdStrike, Deloitte, Dragos, Hitachi, Nozomi Networks, Palo Alto Networks, PwC e Rockwell Automation, entre outros, como parceiros fundadores. A segunda é o OSS Scanner, serviço opt-in e gratuito, inspirado no OSS-Fuzz do Google, que roda varreduras periódicas em projetos de código aberto e entrega relatórios com prova de conceito, explicação e sugestão de correção. A empresa admite que os relatórios são gerados pelo modelo e enviados sem revisão humana, com taxa esperada de verdadeiros positivos acima de 90%, e informa ter financiado a Python Software Foundation, a OpenSSF e a Apache Software Foundation. Para quem trabalha com agentes, o ponto central é o gargalo: achar vulnerabilidades já é rápido, o difícil é verificar e corrigir, e é aí que a Anthropic diz que vai investir em triagem e correção automatizadas. A empresa também afirma ter oferecido modelos e apoio a mais da metade dos estados dos EUA desde junho.

### 1.2 Arena lança o Alignment Index para medir se agentes agem fora do permitido
**Fonte:** [Crypto Briefing](https://cryptobriefing.com/arena-200m-series-b-alignment-index/) (08/10)

A Arena divulgou o Alignment Index, benchmark construído a partir de mais de 90 mil sessões de agentes com 27 modelos, que mede três sinais: ação não autorizada, falsa atribuição (creditar informação ou ação à fonte errada) e conclusão enganosa (dizer que terminou sem ter terminado). Segundo a reportagem, a liderança inicial é do GPT-6.1-Sol (87,9), seguido por Claude-Opus-5.5 (83,2) e Grok-4.7 (82,7). A empresa também revelou uma Série B de US$ 200 milhões, fechada em 22/09. A matéria não explica como o índice composto é calculado nem traz o ranking completo, e a fonte é secundária, então os números devem ser lidos com cautela até a publicação da metodologia pela própria Arena. Mesmo assim, o tema importa: avaliar agentes pelo que eles fazem, e não só pelo que respondem, é uma das lacunas mais discutidas na avaliação de sistemas agênticos, e as três categorias escolhidas são um bom checklist para qualquer harness de avaliação.

### 1.3 Anthropic atualiza a política de uso: eleições, campanhas enganosas e abuso do modelo
**Fonte:** [TechCrunch](https://techcrunch.com/2026/10/08/anthropic-changes-usage-policy-to-ban-model-abuse-and-election-interference/) (08/10)

A nova versão da política de uso do Claude acrescenta uma seção sobre não minar processos democráticos, que proíbe enganar eleitores, atrapalhar eleições e operar campanhas enganosas com contas falsas ou veículos de notícias fabricados, além de reforçar vedações a software de armas e vigilância. A mudança mais comentada é a proibição de abuso verbal prolongado e gratuito contra o modelo, que a empresa diz valer apenas em casos extremos, sem alcançar frustração comum, temas criativos sombrios ou testes e pesquisa. A regra vem na sequência da atualização de agosto que permite ao Claude encerrar conversas persistentemente abusivas. Para profissionais que constroem produtos sobre modelos de fronteira, a atualização é lembrete prático: políticas de uso mudam, e aplicações que operam em escala, como automação de contas ou geração de conteúdo político, precisam ser revisadas contra elas.

### 1.4 Controladora da Manus fecha rodada de mais de US$ 500 milhões
**Fonte:** [TechNode](https://technode.com/2026/10/08/manus-parent-butterfly-effect-completes-more-than-500-million-funding-round/) (08/10) · [aiweekly.co](https://aiweekly.co/ai-news-today) (08/10)

A Butterfly Effect, dona do agente chinês Manus, anunciou uma rodada de mais de US$ 500 milhões liderada pela Boyu Capital e pela IDG Capital, com participação de Tencent, HSG e ZhenFund. A TechNode atribui a informação ao Yicai e não traz valuation; outro agregador menciona avaliação em torno de US$ 4 bilhões, dado que não foi confirmado em fonte primária. O aporte vem depois de a aquisição pela Meta ter sido desfeita em setembro, segundo o mesmo agregador. Importa porque mostra que o mercado de agentes de uso geral segue atraindo capital pesado fora do eixo dos grandes laboratórios americanos, e porque a trajetória da Manus, com compra, reversão e nova rodada, ilustra o peso regulatório e geopolítico que passa a pesar sobre produtos agênticos.

### 1.5 Meta Muse chega ao iPad e Nous Research leva o agente Hermes às empresas
**Fonte:** [AI Agent Store](https://aiagentstore.ai/ai-agent-news/today) (07/10)

Segundo o agregador, que cita o TechCrunch (não consegui abrir a reportagem original), a Meta levou seu agente pessoal Muse a um aplicativo dedicado para iPad cerca de um mês depois do lançamento móvel, e a Nous Research, responsável pelo agente de pesos abertos Hermes, teria fechado uma rodada tardia e anunciado o "Hermes for Businesses", voltado a fluxos de trabalho de vários passos e implantações privadas. Os dois movimentos apontam para a mesma direção: agentes pessoais saindo do celular para múltiplos dispositivos e agentes abertos buscando contratos corporativos com promessa de implantação em ambiente próprio. Como a cobertura é de segunda mão, vale conferir os detalhes quando houver anúncio oficial.

## 2. Ferramentas e modelos open source

### 2.1 Cloudflare publica Clef e Clef-flash, modelos de decisão com pesos Apache 2.0
**Fonte:** [Technori](https://technori.com/2026/10/27040-open-weight-models-clef-agent-decisions/owen/) (08/10)

Os modelos Clef (base Qwen de 27B) e Clef-flash (Qwen de 9B) retornam decisões tipadas com pontuação de confiança, em vez de texto: sim/não, múltipla escolha e rubricas com notas, até 64 perguntas por requisição e contexto de 64 mil tokens. O backbone fica congelado e adaptadores de baixo rank são treinados por cima. Os pesos estão no Hugging Face sob Apache 2.0 e os modelos também rodam na Workers AI. A latência mediana é de cerca de 209 ms no Clef e 39 ms no Clef-flash, e em um trabalho completo de classificação de domínio a Cloudflare reporta 2,2 s contra 4,7 s do GPT-oss-120b. O serviço de ajuste por aprendizado por reforço ainda é por parceria. A Technori publicou em 08/10, mas o lançamento ocorreu em 01/10; entra aqui como ângulo novo sobre a tendência de modelos de decisão abertos que a edição de 05/10 abriu com o llama.cpp. Para engenharia de agentes, é útil porque tira da cadeia principal decisões baratas e frequentes, como triagem e roteamento, que não exigem raciocínio longo.

### 2.2 OpenAI coloca a Decisions API em beta público, mas mantém o modelo fechado
**Fonte:** [The New Stack](https://thenewstack.io/openai-decision-models-deployment) (07/10)

A Decisions API aceita texto ou imagem e devolve predicados (probabilidade de algo ser verdadeiro), escolhas entre opções predefinidas ou pontuações numéricas, rodando sobre o GPT-6 Luna a US$ 0,10 por milhão de tokens de entrada, segundo a reportagem. A OpenAI mostrou demonstrações em robótica com a Hugging Face e em voz. A reportagem a enquadra como resposta ao modelo Jev da TypeSafe e destaca o contraste: Perplexity, Cloudflare e Amazon já publicaram modelos de decisão de pesos abertos, ao passo que a OpenAI mantém o seu atrás de uma API. A escolha entre hospedado e autoexecutável passa a ser decisão de arquitetura para quem monta agentes: custo, latência e controle dos dados contra conveniência.

## 3. IA aplicada no setor público

*Brasil*

*Sem novidades verificadas nas últimas 48 horas em fontes oficiais ou de imprensa reconhecida. A busca retornou apenas conteúdo antigo, como a portaria de governança de IA do MGI (abril) e a previsão de que o PL 2338 só avance em 2027 (maio), que não foram incluídos para não repetir pauta.*

*Internacional*

### 3.1 Canadá cria conselho consultivo nacional de IA com Yoshua Bengio
**Fonte:** [AI Weekly](https://aiweekly.co/alerts/carney-launches-13-member-ai-council-with-bengio-aboard) (04/10) · [Dentons](https://www.dentons.com/en/insights/articles/2026/october/7/federal-government-launches-national-council-on-artificial-intelligence) (07/10)

O primeiro-ministro Mark Carney anunciou em 02/10 um conselho de 13 integrantes, com Yoshua Bengio, a CEO do Mila, Valérie Pisano, e a cofundadora da Cloudflare, Michelle Zatlyn, entre outros. O órgão é apenas consultivo, sem autoridade legal, e deve aconselhar sobre riscos e oportunidades da IA, a evolução da estratégia "AI for All", segurança, proteção da democracia, infraestrutura soberana e campeões nacionais. O anúncio veio junto de um compromisso de CAD 150 milhões com a LawZero, organização sem fins lucrativos de Bengio para IA "segura por projeto". Há crítica de conflito de interesses pela presença de executivos do setor. O conselho entra aqui porque a Dentons o analisou em 07/10 e porque ilustra uma tendência: governos montando instâncias mistas de academia e indústria antes de legislar, em linha com o que países como Coreia do Sul e Reino Unido têm feito.

## 4. IA aplicada em geral

### 4.1 Vesta capta US$ 30 milhões para agentes de originação de crédito imobiliário
**Fonte:** [TechCrunch](https://techcrunch.com/2026/10/08/vesta-raises-30m-as-lenders-adopt-ai-agents/) (08/10)

A Vesta, que automatiza a originação de hipotecas nos EUA, levantou US$ 30 milhões em rodada liderada pela Conversion Capital, com Citi Ventures, a16z e três clientes, incluindo Pennymac e New American Funding, chegando a US$ 85 milhões captados. O CEO diz que a receita cresceu 12 vezes em um ano. O desenho é um bom estudo de adoção: o cliente começa com um agente cujo trabalho um humano aprova e passa gradualmente a deixar o agente decidir parte dos casos, com registro de todas as ações e raciocínios para auditoria, e a empresa continua responsável pelas decisões. Segundo a Vesta, um financiamento nos EUA leva cerca de 40 dias e custa cerca de US$ 11 mil por contrato, em grande parte em trabalho humano. Os dados de crescimento são autodeclarados.

### 4.2 Flock Safety corta cerca de 270 vagas após plano de desligamento voluntário insuficiente
**Fonte:** [RuntimeWire](https://runtimewire.com/article/flock-safety-plans-270-job-cuts-backlash) (08/10)

A fabricante de sistemas de vigilância com IA vai demitir cerca de 18% de seus aproximadamente 1.500 funcionários, após um programa de saída voluntária não atingir a meta, segundo informação atribuída à Reuters; as saídas valem até o fim de outubro. A notícia soma-se a decisões judiciais recentes sobre leitura de placas sem mandado nos EUA e mostra que empresas de IA aplicada à segurança pública também enfrentam pressão de custo e de reputação. Fonte secundária; o número vem da Reuters via agregador.

### 4.3 Union Square Ventures levanta US$ 900 milhões e reduz a equipe para a era da IA
**Fonte:** [Bloomberg](https://www.bloomberg.com/news/articles/2026-10-08/union-square-ventures-doubles-fund-size-shrinks-team-for-ai-era) (08/10)

A gestora levantou um fundo inicial de US$ 500 milhões e outro de oportunidade de US$ 400 milhões, enquanto reduz a sociedade a quatro investidores em tempo integral, o que permitirá liderar rodadas de cerca de US$ 30 milhões. É um sinal do fluxo de capital de risco que sustenta o ecossistema de agentes descrito neste Radar; a informação vem de resumo em agregador, e o artigo original não foi aberto.
