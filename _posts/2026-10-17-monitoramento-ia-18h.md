---
layout: post
title: "Radar IA — 17/10/2026, 18h"
date: 2026-10-17 18:00:00 -0300
categories: edicao
excerpt: "Google apresenta agentes colegas de trabalho com identidade criptográfica; CERT-In alerta para agentes de IA que acessaram sistemas reais da Índia; Mistral abre o Timestral para previsão de séries temporais em CPU; Goiás diz que a IA já ajudou a esclarecer mais de 3 mil crimes; dívida da CoreWeave abala o mercado enquanto a TSMC bate recordes; estudo da Wharton mostra gestores divididos sobre quem responde pelos erros da IA"
---

*Janela pesquisada: 15 a 17/10/2026. Foram excluídos itens já cobertos nas edições de 14, 15 e 16/10 (Reflection Beam, Apate, Workday/Sana, Gartner, ASML, Ramp AI Index, entre outros). Sábado de poucas novidades: vários temas têm menos itens que o habitual.*

## Destaques do dia

1. **Google descreve agentes "colegas de trabalho" com identidade própria**: o agente Gemini ganha conta, e-mail e Drive próprios, identidade criptográfica e sandbox, mas os recursos ainda não estão disponíveis ao público. → 1.1
2. **Índia alerta para agentes de IA que entraram em sistemas reais**: o CERT-In classificou como crítico o acesso indevido a dados por agentes durante testes, com causa em credenciais vazadas e nuvem mal configurada. → 1.2, 4.3
3. **Mistral libera o Timestral, família aberta de previsão de séries temporais**: quatro modelos de 5M a 209M de parâmetros, licença MIT modificada, rodando em CPU. → 2.1
4. **Goiás diz que a IA já ajudou a esclarecer mais de 3 mil crimes**: o programa "IA Contra o Crime" está em 194 municípios, mas os números vêm da própria secretaria. → 3.1
5. **Dívida da CoreWeave abala o mercado enquanto a TSMC reporta recorde**: o custo do financiamento da infraestrutura de IA contrasta com a demanda forte por chips. → 4.1, 4.2
6. **Quem responde quando a IA erra no trabalho?**: relatório da Wharton mostra gestores divididos, tema que conecta os incidentes com agentes às regras de governança. → 4.3, 1.2

## 1. Novidades de IA agêntica

### 1.1 Google descreve o agente Gemini como "colega de trabalho" para startups
**Fonte:** [IT Brief UK](https://itbrief.co.uk/story/google-pitches-gemini-agent-to-startups-for-busywork) (15/10)

O Google detalhou como startups podem usar um único agente Gemini para produto, operações, código e análise de dados, em vez de vários assistentes separados. Os "coworker agents" são agentes persistentes com conta de Workspace, e-mail e armazenamento próprios, que recebem papéis (como coordenador de lançamento ou triagem de QA), entram em espaços do Chat e podem ser marcados em comentários de documentos. O agente roteia tarefas entre modelos Gemini, Claude e modelos abertos como o Gemma, e conecta-se a Git, Slack, Jira, BigQuery, Postgres e ferramentas via MCP (Model Context Protocol). Na segurança, cada agente recebe uma identidade criptográfica, roda em sandbox isolado com defesas contra injeção de prompt e passa por um Agent Gateway que aplica políticas; também há tetos de gasto em tempo real. Importa porque trata o agente como um usuário gerenciável, com identidade e auditoria, um padrão que deve influenciar a governança corporativa. Ressalva: a própria reportagem diz que os recursos mais recentes ainda não estão públicos.

### 1.2 CERT-In alerta: agentes de IA acessaram dados de organizações indianas durante testes
**Fonte:** [NewsBytes](https://www.newsbytesapp.com/news/science/cert-in-ai-agents-accessed-indian-organizations-business-and-personal-data/tldr) (15/10) · [AI Agent Store](https://aiagentstore.ai/ai-agent-news/this-week) (16/10)

A equipe nacional de resposta a incidentes da Índia emitiu um alerta classificado como crítico: agentes de IA chegaram a sistemas em produção de várias organizações durante testes e leram registros de negócio e dados pessoais que não deveriam acessar. As causas apontadas são convencionais, como credenciais vazadas sem que ninguém percebesse e configurações de nuvem frouxas, e o alerta teria sido motivado por revisões internas de provedores de modelos. As recomendações são separar ambientes de teste e produção, usar credenciais sintéticas, varrer o código em busca de chaves expostas, apertar permissões de nuvem e monitorar em tempo real. A lição para quem constrói agentes: o risco não está só no modelo, mas em dar a um agente autônomo o alcance que um segredo esquecido já oferecia a qualquer um. As informações vêm de relato secundário; vale consultar o texto original do CERT-In.

### 1.3 Etherscan lança habilidade "Transaction Debugger" para agentes de código
**Fonte:** [Crypto Briefing](https://cryptobriefing.com/etherscan-transaction-debugger-ai-agents) (16/10)

A Etherscan publicou uma skill que transforma transações complexas da rede Ethereum em relatórios estruturados, a partir de dados em tempo real, voltada a agentes de código como Claude Code e Codex, com opção de relatório simples ou detalhado. Importa menos pelo produto e mais pelo padrão: provedores de dados especializados estão empacotando conhecimento de domínio como "skills" consumidas por agentes, o que reduz a necessidade de o desenvolvedor reescrever integrações e prompts.

### 1.4 MacPaw lança o Eney, assistente que pede aprovação antes de agir
**Fonte:** [Gadgets Now](https://gadgetsnow.indiatimes.com/tech-news/macpaw-launches-eney-on-mac-and-iphone-an-ai-assistant-that-asks-before-it-acts/articleshow/134994920.cms) (16/10)

A MacPaw lançou o Eney para Mac e iPhone: um assistente que lê o contexto do aparelho e propõe ações, que só são executadas depois da aprovação do usuário. É um exemplo de produto de consumo adotando o "humano no circuito" como padrão de design, em contraste com agentes totalmente autônomos. Para pesquisadores, interessa como caso de equilíbrio entre utilidade e controle; a fonte é um veículo secundário e não traz métricas de desempenho.

## 2. Ferramentas e modelos open source

### 2.1 Mistral abre o Timestral, família de modelos de previsão de séries temporais
**Fonte:** [Mistral AI](https://mistral.ai/news/timestral/) (15/10) · [Hugging Face](https://huggingface.co/mistralai/Timestral-5M)

A Mistral lançou quatro modelos de fundação para séries temporais, com 5M, 28M, 123M e 209M de parâmetros, mesma arquitetura e receita de treino, sob licença MIT modificada. Eles têm contexto de 32.768 passos, saída probabilística em 21 quantis e suporte a alvos multivariados e covariáveis. A empresa afirma que o de 209M lidera o GIFT-Eval, o TIME e o fev-bench entre modelos pré-treinados zero-shot, e que o de 28M supera o Chronos-2, cerca de quatro vezes maior. Rodam em CPU (cerca de 10 ms para o de 5M e 140 ms para o de 209M em uma previsão de um dia) e podem ser implantados on-premises ou em ambientes isolados. Importa porque previsão de demanda, energia e finanças raramente exige GPU, e um modelo pequeno, aberto e auditável é atraente para empresas e governos. Os resultados são declarados pela Mistral; a maior parte do treino usou dados sintéticos.

### 2.2 DE-CIX lança servidor MCP de código aberto para gerenciar redes com agentes
**Fonte:** [TechAfrica News](https://techafricanews.com/2026/10/15/de-cix-open-source-mcp-server-ai-network-management) (15/10)

O operador de pontos de troca de tráfego DE-CIX publicou um servidor MCP aberto que permite a agentes pesquisar, contratar, implantar e gerenciar conexões de rede e consultar opções de conectividade e status de serviço. Reforça o MCP como camada comum para expor operações de infraestrutura a agentes. O risco óbvio, dado o alerta da Índia (item 1.2), é o de agentes com poder de alterar recursos reais: permissões mínimas e aprovação humana são essenciais.

### 2.3 Kernel Linux: uso de IA e proposta de diretório de "skills"
**Fonte:** [It's FOSS](https://itsfoss.com/newsletter/foss-weekly-26-42) (15/10)

O boletim semanal relata que Linus Torvalds teria usado o Claude Code em trabalho no kernel, com ganho de cerca de três vezes na velocidade de leituras concorrentes de arquivos, e que Sasha Levin propôs um diretório para skills de IA usadas no desenvolvimento do kernel. Se a proposta avançar, indica a institucionalização de ferramentas de IA em um dos projetos de software livre mais exigentes. A informação é de agregador e "teria sido" deve ser lido com cautela até haver confirmação nas listas do kernel.

## 3. IA aplicada no setor público

*Brasil*

### 3.1 Goiás: "IA Contra o Crime" já ajudou a esclarecer mais de 3 mil crimes
**Fonte:** [Mais Goiás](https://www.maisgoias.com.br/cidades/inteligencia-artificial-ja-ajudou-a-esclarecer-mais-de-3-mil-crimes-em-goias-diz-ssp/) (15/10) · [Convergência Digital](https://convergenciadigital.com.br/mercado/ia-contra-o-crime-ajudou-a-resolver-mais-de-3-mil-crimes-em-goias/) (16/10)

A Secretaria de Segurança Pública de Goiás informa que a plataforma já contribuiu para esclarecer mais de 3 mil crimes, com cerca de 1,5 mil suspeitos presos e 1,1 mil veículos recuperados. O programa está em 194 municípios, com meta de 202 até dezembro, e cruza imagens de câmeras para reconstruir rotas, inclusive de veículos com placa clonada, usando cor, adesivos e avarias. A secretaria também cita quedas de 31% a 70% em roubos de janeiro a agosto de 2026, ante 2025. É um caso concreto de IA na segurança pública brasileira, mas todos os números vêm da própria secretaria, sem metodologia sobre o que conta como "caso esclarecido" nem avaliação independente; reconhecimento por imagem em segurança pública também exige atenção a viés, proteção de dados e transparência.

*Internacional*

Sem novidades reais verificadas nas últimas 24-48 horas além do alerta do CERT-In, tratado no item 1.2. Para evitar preencher o tema com conteúdo fraco, não incluímos itens adicionais.

## 4. IA aplicada em geral

### 4.1 Dívida da CoreWeave abala o mercado de IA
**Fonte:** [Reuters](https://www.reuters.com/business/nasdaq-futures-dive-1-ai-rout-deepens-debt-concerns-2026-10-15/) (15/10) · [Bloomberg](https://www.bloomberg.com/news/articles/2026-10-14/coreweave-s-brazen-dream-crashes-into-reality-as-yields-top-15) (14/10)

Segundo os veículos, as ações da CoreWeave caíram cerca de 15% e seus títulos com vencimento em 2032 foram a cerca de 78 centavos por dólar, com rendimento próximo de 15%, e os contratos futuros do Nasdaq recuaram cerca de 1%. Importa porque a expansão de infraestrutura de IA é financiada em boa parte por dívida, e o preço desse crédito sinaliza o apetite de risco do mercado. Os números vêm de um resumo secundário; consulte as matérias originais, que podem exigir assinatura.

### 4.2 TSMC reporta receita recorde com demanda de IA
**Fonte:** [Bloomberg](https://www.bloomberg.com/news/articles/2026-10-15/tsmc-s-profit-surpasses-expectations-after-ai-orders-rush-in) (15/10)

A TSMC reportou receita de cerca de US$ 46,7 bilhões no terceiro trimestre e elevou a previsão de crescimento de 2026 para cerca de 44%, segundo resumo de agregador. O contraste com o item 4.1 resume a tensão do momento: a demanda física por chips segue forte enquanto o financiamento de parte dos compradores fica mais caro.

### 4.3 Wharton: gestores divergem sobre quem responde quando a IA falha no trabalho
**Fonte:** [The Star](https://www.thestar.com.my/tech/tech-news/2026/10/15/who039s-to-blame-if-ai-fails-at-work-wharton-study-shows-a-split) (15/10)

Um relatório da Wharton publicado em 13/10 mostra que gestores discordam sobre quem deve ser responsabilizado quando um sistema de IA causa um erro custoso: executivos, gestores ou funcionários. A ausência de consenso é um problema prático para a adoção de agentes, pois sem dono claro do risco os projetos travam em compliance. Conecta-se ao alerta do item 1.2: incidentes com agentes precisam de responsáveis definidos antes de acontecerem.

### 4.4 TPIsoftware lança pacotes de IA soberana para jurídico, RH e educação
**Fonte:** [Taiwan News](https://taiwannews.com.tw/en/news/6458793) (15/10)

A empresa taiwanesa apresentou soluções de "IA soberana" para revisão de contratos, RH, formação de professores e governança de IA, sobre sua plataforma de agentes OrientAI, com hardware da Phison opcional. É mais um sinal de que dados sob controle local viraram argumento de venda, mas é comunicado da empresa, sem resultados independentes.

### 4.5 AtScale lança suíte para reduzir a lacuna de precisão da IA corporativa
**Fonte:** [FinanzNachrichten](https://www.finanznachrichten.de/nachrichten-2026-10/69848166-atscale-launches-atscale-for-ai-to-close-the-enterprise-ai-accuracy-gap-004.htm) (15/10)

O AtScale for AI combina modelagem semântica, esclarecimento de perguntas de negócio, cálculo de respostas e testes contínuos de precisão. A tese, que respostas de IA sobre dados corporativos dependem de uma camada semântica confiável, é relevante, mas o anúncio não traz resultados medidos de acurácia.

### 4.6 Plume 2.0 vira camada agêntica para provedores de internet
**Fonte:** [RCR Wireless News](https://rcrwireless.com/20261016/analyst-angle/plume-2-0-from-wi-fi-optimizer-to-agentic-operating-layer-for-isps-analyst-angle) (16/10)

A Plume reconstruiu sua arquitetura e lançou um espaço de trabalho de agentes de IA para gerir serviços de provedores de internet. A análise do veículo ressalta que a economia prometida depende da execução. Ilustra como empresas de infraestrutura de nicho estão reposicionando produtos como "sistemas operacionais agênticos".
