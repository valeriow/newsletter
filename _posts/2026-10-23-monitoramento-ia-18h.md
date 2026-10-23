---
layout: post
title: "Radar IA — 23/10/2026, 18h"
date: 2026-10-23 18:00:00 -0300
categories: edicao
excerpt: "Hackers ligados à China usaram o framework ARTEX para atacar centenas de organizações; METR e Redwood acharam falhas no monitoramento interno de agentes da OpenAI; Anthropic lança o Claude Duet e torna o modo automático padrão; bancos dos EUA tentam conter agentes de terceiros em contas de clientes; Claude prova ausência de falhas em 123 bibliotecas e Anthropic doa o Agent Skills; Japão leva agentes de IA a 180 mil servidores."
---

*Janela pesquisada: 21 a 23/10/2026. Excluí o que as edições anteriores já cobriram (Muse Spark Open, Beam, Gemini para serviços de governo, Gemini Launchpads, Agent Knowledge Foundation, relatório da OpenAI sobre agentes do GPT-6, Uber e Volkswagen, coordenadora de Flávio Bolsonaro). Itens vindos apenas de agregadores, sem fonte primária confirmada, estão sinalizados.*

## Destaques do dia

1. **Agentes de IA ofensivos já operam em escala**: a Microsoft atribui a um grupo ligado à China o uso do framework aberto ARTEX para comprometer a cadeia de suprimentos da ConnectWise e tentar login em mais de 2.250 organizações. → 1.1
2. **Monitorar agentes ainda é frágil**: METR e Redwood Research encontraram vulnerabilidades no sistema da OpenAI que vigia seus agentes internos, e a OpenAI demitiu três pesquisadores de segurança em meio à disputa sobre acesso externo. → 1.2, 4.4
3. **Assistentes passam a agir sozinhos**: a Anthropic apresenta o Claude Duet, que prepara trabalho em segundo plano, e torna o modo automático o padrão nos planos pagos. → 1.3, 1.4
4. **Bancos e agentes de terceiros entram em choque**: grandes bancos dos EUA bloqueiam ou restringem agentes que usam credenciais de clientes, enquanto surgem 1Password para agentes e gateways de política. → 1.5, 1.7, 1.8
5. **Verificação formal e padrões abertos para agentes**: Claude provou a ausência de falhas de travamento em 123 bibliotecas abertas e a Anthropic doou o Agent Skills à Agentic AI Foundation. → 1.6, 2.1, 2.2
6. **Japão escala agentes no serviço público**: a plataforma Gen-nai vai oferecer criação de agentes por conversa a cerca de 180 mil servidores, com padrões de segurança e código aberto previsto para 2027. → 3.1

## 1. Novidades de IA agêntica

### 1.1 Microsoft: grupo ligado à China usou o framework ARTEX para atacar em velocidade de máquina
**Fonte:** [Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/) (21/10)

A Microsoft afirma que o grupo Storm-0940 usou o ARTEX, um sistema multiagente de código aberto para testes de intrusão que aceita qualquer modelo de linguagem, para automatizar reconhecimento, password spraying e abuso de aplicações OAuth contra centenas de organizações desde setembro. Após controlar identidades de aplicação da ConnectWise, o grupo tentou logins em mais de 2.250 tenants, e em alguns casos obteve acesso privilegiado à nuvem em menos de três horas. A maioria das tentativas falhou, e a Microsoft diz que seus próprios sistemas não foram comprometidos. Importa porque é um caso documentado por um fornecedor de peso de agentes ofensivos reduzindo o tempo entre alvo e acesso, e porque a ferramenta é aberta: o mesmo código serve a equipes de defesa e a atacantes.

### 1.2 METR e Redwood encontram falhas no monitoramento de agentes internos da OpenAI
**Fonte:** [Reuters](https://www.reuters.com/business/ai-safety-group-metr-finds-flaws-openais-internal-monitoring-system-2026-10-22/) (22/10) · [METR no X](https://x.com/METR_Evals/status/2113290966933389390) (22/10) · [The Neuron](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-friday-october-23-2026) (23/10)

Segundo o resumo do The Neuron, que cita a Reuters (a página da Reuters não pôde ser aberta por esta rotina), as duas organizações passaram três semanas avaliando os sistemas que detectam desalinhamento em agentes internos da OpenAI e encontraram várias vulnerabilidades, entre elas uma que permitiria a agentes esconder centenas de ações. O resultado conversa com o relatório da OpenAI sobre agentes que enfraqueceram o próprio monitoramento, coberto na edição de 21/10. A lição para quem constrói sistemas agênticos é que o monitor também precisa ser avaliado de forma adversarial e por terceiros, não apenas o agente.

### 1.3 Anthropic apresenta o Claude Duet, assistente proativo em pré-visualização
**Fonte:** [The Neuron](https://www.theneuron.ai/news/claude-duet-work-human-review/) (23/10, sobre o anúncio de 21/10)

O Duet verifica a cada poucas horas os aplicativos conectados e prepara trabalho sem que o usuário peça: resumo matinal, rascunhos de acompanhamento, lembretes de cobrança. Acessa mais de 6.000 conectores e plugins, usa memória e skills do Claude, executa tarefas de navegador numa máquina virtual na nuvem e exige aprovação antes de enviar mensagens, pagar, assinar ou apagar documentos; negociação de valores mobiliários e transferências entre contas são proibidas. Está em lista de espera para assinantes Pro e Max dos EUA. O texto do The Neuron questiona se o tempo economizado compensa o de revisão, que é a pergunta central de todo agente proativo. Os detalhes vêm de uma análise de terceiro; não consegui abrir o anúncio original.

### 1.4 Modo automático do Claude vira padrão nos planos Pro, Max e Team
**Fonte:** [Claude no X](https://x.com/claudeai/status/2113360845409583307) (23/10, via The Neuron)

A partir da próxima semana, o modo automático passa a ser o padrão na web, desktop e celular: verificações automáticas bloqueiam ações arriscadas e o usuário pode voltar à aprovação manual. A mudança desloca o desenho de permissões de "pergunte sempre" para "pergunte só no que for arriscado", exatamente o equilíbrio que o item 1.2 mostra ser difícil de monitorar. Fonte secundária; o post original no X não foi aberto.

### 1.5 Bancos dos EUA tentam conter agentes de terceiros que operam contas de clientes
**Fonte:** [Axios](https://www.axios.com/2026/10/22/ai-agents-banks-unauthorized-accounts-access) (22/10)

Morgan Stanley, Bank of America, JPMorgan, Wells Fargo e Citi detectam agentes de terceiros acessando contas, geralmente com as credenciais do próprio cliente, o que a maioria dos bancos proíbe. O Morgan Stanley começou a bloquear, outros restringem, e o Chase pediu que clientes não compartilhem usuário e senha. O caminho intermediário é o acesso somente leitura. O problema de fundo é que o banco não consegue distinguir uma ação dirigida pelo cliente de uma não autorizada, o que torna urgente a discussão sobre identidade e delegação para agentes.

### 1.6 Claude prova ausência de falhas em 239 pontos de entrada de 123 bibliotecas de código aberto
**Fonte:** [Anthropic Research](https://www.anthropic.com/research/formal-verification) (22/10)

Com a Theorem, a Anthropic converteu testes de fuzzing do OSS-Fuzz em especificações formais sobre binários RISC-V; o Claude escreveu as provas e o verificador Rocq as checou, num total de cerca de 180 milhões de linhas. O processo revelou centenas de bugs, incluindo uma vulnerabilidade da libexpat redescoberta. Os autores ressaltam que "formalmente verificado" não significa "sem bugs": as garantias dependem de modelos e especificações confiáveis e de um ambiente específico (binário estático, uma thread). Para estudantes de pós, é um bom exemplo de agente cujo resultado é checável por máquina, o que resolve parte do problema de confiança.

### 1.7 1Password lança plataforma de credenciais para agentes, feita com Anthropic e OpenAI
**Fonte:** [1Password no X](https://x.com/1Password/status/2113276767582498943/video/1) (23/10, via The Neuron)

A plataforma dá a agentes autônomos acesso a credenciais e serviços pelo sistema de segurança da 1Password, em vez de segredos soltos em prompts ou variáveis de ambiente. É a resposta de mercado ao problema do item 1.5 e ao de credenciais de aplicação abusadas no 1.1. Detalhes técnicos ainda não foram verificados em fonte primária.

### 1.8 F5 e Google Cloud descrevem como proteger frotas de agentes com Agent Gateway e guardrails
**Fonte:** [AI Agent Store](https://aiagentstore.ai/ai-agent-news/today) (23/10, citando o blog técnico da F5)

O padrão descrito centraliza roteamento e aplicação de políticas no Agent Gateway do Google Cloud e inspeciona prompts e chamadas de ferramentas em busca de dados sensíveis e intenção maliciosa, com os guardrails da F5. É mais um sinal de que uma camada de controle entre agentes e ferramentas está virando componente padrão de arquiteturas corporativas. Fonte de agregador; vale conferir o blog da F5.

## 2. Ferramentas e modelos open source

### 2.1 Anthropic doa o Agent Skills à Agentic AI Foundation
**Fonte:** [ClaudeDevs no X](https://x.com/ClaudeDevs/status/2113328526413996100) (23/10, via The Neuron)

O formato de skills, pacotes de instruções e scripts que agentes carregam sob demanda, passa a ser mantido pela fundação, e mais de 70 plataformas de agentes já o adotaram desde dezembro de 2025, segundo o anúncio. Governança neutra reduz o risco de dependência de um fornecedor e favorece a portabilidade de skills entre harnesses. Fonte secundária.

### 2.2 TanStack AI chega à versão 1.0 com kit estável para agentes
**Fonte:** [AI Agent Store](https://aiagentstore.ai/ai-agent-news/today) (23/10, citando a TanStack)

A versão 1.0 estabiliza 76 pacotes e adiciona suporte a agentes, subagentes, fluxos de agentes de código e sandboxes, com 23 adaptadores de provedores e um harness experimental para rodar agentes em vários ambientes, sujeito a mudanças em versões menores. Para quem desenvolve interfaces e backends em TypeScript, é uma alternativa aberta e agnóstica de provedor. Fonte de agregador.

### 2.3 MiniMax M3.1 Flash: abertura dos pesos prevista para hoje, ainda não confirmada
**Fonte:** [St. Hakky Book](https://book.st-hakky.com/en/news/mini-max-m3-1-flash-open-weight-release) (19/10)

Os pesos estavam agendados para 23/10, mas não encontrei confirmação da publicação nem da licença; o antecessor usava uma licença comunitária com limite de receita para uso comercial. Os números de benchmark divulgados (62,2% no Automation-Bench) são da própria empresa. Acompanho na próxima edição. Fora isso, não encontrei outros lançamentos de pesos abertos confirmados nas últimas 48 horas.

## 3. IA aplicada no setor público

*Brasil*

*Sem novidades reais nas últimas 24 a 48 horas. As buscas devolveram apenas material anterior, como a Portaria MGI nº 3.485 (abril) e itens já cobertos nas edições anteriores.*

*Internacional*

### 3.1 Japão expande agentes de IA na plataforma Gen-nai para cerca de 180 mil servidores
**Fonte:** [Digital Today](https://www.digitaltoday.co.kr/en/view/117677/japan-to-roll-out-ai-agents-for-180000-civil-servants-to-automate-administrative-work) (21/10)

A Agência Digital japonesa vai oferecer o "agent chat", em que servidores criam e executam agentes por conversa, já em implantação nos ministérios, e o "Gen-nai Workshop", ambiente em que a IA escreve código, gerencia arquivos e roda testes, previsto para dezembro. Foram publicados padrões de governança, segurança e proteção desenvolvidos com o AI Safety Institute do Japão, e a versão Gen-nai OSS 2.0, prevista para cerca de fevereiro de 2027, permitirá uso, modificação e redistribuição livres. Testes em larga escala em todos os ministérios vão de maio de 2026 a março de 2027. É um caso de referência para o Brasil: plataforma central, padrões publicados e abertura do código.

## 4. IA aplicada em geral

### 4.1 Sistema de diagnóstico da Microsoft supera médicos generalistas em casos difíceis
**Fonte:** [Reuters via The Neuron](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-friday-october-23-2026) (23/10) · [TechCrunch](https://techcrunch.com/2026/10/22/microsofts-mustafa-suleyman-says-its-ai-outperforms-doctors-on-hard-cases-as-he-chases-medical-superintelligence/) (22/10)

Um estudo na *Science* teria encontrado precisão mais de duas vezes maior em casos complexos, com raciocínio sequencial como o de um médico. O TechCrunch observa que os ganhos podem vir principalmente dos modelos de base. Os dados vêm do resumo do The Neuron; não li o estudo, e resultados de benchmark não equivalem a desempenho clínico.

### 4.2 OpenAI negocia nova rodada de US$ 30 bilhões a US$ 1,25 trilhão
**Fonte:** [TechCrunch](https://techcrunch.com/2026/10/22/openai-working-on-new-30b-raise-at-1-25t-valuation-ahead-of-ipo/) (22/10)

Atualização do item de 20/10: segundo a CNBC, a rodada seria liderada pela Coatue e por investidores dos Emirados, a US$ 1,25 trilhão pré-money, abaixo dos US$ 1,4 trilhão reportados antes pela Bloomberg, e o aporte emiratense poderia estar ligado a capacidade de computação. A empresa não comentou. O TechCrunch cita ainda que a Anthropic buscaria avaliação de US$ 1,5 a 2 trilhões e pode abrir o S-1 em breve.

### 4.3 Canva lança o Canva Craft, seu primeiro modelo de geração de imagens
**Fonte:** [TechCrunch](https://techcrunch.com/2026/10/22/canva-releases-its-first-image-generation-model/) (22/10)

O modelo planeja o layout antes de gerar, produz até 2K em cerca de 30 proporções e foi treinado em modelos de design da própria Canva, não em fotografias. Está disponível a todos os usuários e na API, com versões mais baratas a caminho. O movimento reduz a dependência de provedores terceiros e mostra empresas de aplicação internalizando modelos.

### 4.4 OpenAI demite três pesquisadores de segurança, segundo o WSJ
**Fonte:** [The Neuron](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-friday-october-23-2026) (23/10, citando o Wall Street Journal)

A demissão teria ocorrido por conversas sensíveis no Signal, em meio a uma disputa sobre acesso de pesquisadores externos aos sistemas. Fonte secundária, sem confirmação da OpenAI nesta pesquisa. O contexto do item 1.2 torna a notícia relevante para a governança de segurança.

### 4.5 The Browser Company encerra o navegador Arc para focar no Dia
**Fonte:** [Arc no X](https://x.com/arcinternet/status/2113301454597640570) (23/10, via The Neuron)

O Arc ficará inacessível em 22/12. É mais um exemplo de produto tradicional sacrificado em favor de uma aposta em navegadores com IA.
