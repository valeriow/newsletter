---
layout: post
title: "Radar IA — 12/10/2026, 18h"
date: 2026-10-12 18:00:00 -0300
categories: edicao
excerpt: "Casa Branca exigiria notificação e correção de incidentes de IA; Nous Research capta US$ 90 milhões para levar o agente aberto Hermes às empresas; Microsoft inicia o preview do Work IQ para agentes do Copilot; Cisco e Atlassian colocam agentes dentro de reuniões e projetos; padrões de verificação e otimização de agentes avançam; IDC e HCLTech mostram a adoção corporativa amadurecendo."
---

*Janela pesquisada: 10/10 a 12/10/2026 (com alguns itens de 07/10 a 09/10 que ainda não haviam sido cobertos). Excluídos os temas já tratados nas edições de 09/10, 10/10 e na edição semanal de 11/10 (Haiku 5.5, Beam, Mistral Large 4, Step 5, ReviewBench, denúncia falsa na polícia da Filadélfia, Personal Agent Protocol, entre outros). Edição enxuta: o fim de semana trouxe poucas novidades inéditas, e itens apoiados apenas em agregadores estão sinalizados.*

## Destaques do dia

1. **Casa Branca endurece o jogo com os laboratórios**: segundo o Axios, via agregador, o governo dos EUA passaria a exigir notificação imediata e correção de incidentes de IA, tratando o relato como obrigação de segurança nacional. → 1.3
2. **Agente aberto vira negócio**: a Nous Research captou US$ 90 milhões (avaliação de cerca de US$ 1,5 bilhão) para levar o agente de código aberto Hermes às empresas. → 1.1
3. **Copilot ganha dados vivos**: o preview do Work IQ liga os agentes da Microsoft a dados em tempo real do Dynamics 365 e do Power Platform. → 1.2
4. **Agentes entram nas reuniões e nos projetos**: a Cisco deixa agentes participarem de reuniões do Webex e a Atlassian leva modelos da OpenAI ao Rovo e ao Jira. → 1.4, 4.3
5. **Verificar e otimizar agentes vira produto**: padrões abertos para provar que agentes seguem regras e o Autoloop da Kore.ai para avaliar e melhorar agentes de forma contínua. → 1.5, 1.6
6. **Adoção corporativa amadurece**: o estudo da IDC com a Microsoft e a parceria HCLTech–Anthropic mostram empresas passando do piloto para o retorno medido. → 4.1, 4.2

## 1. Novidades de IA agêntica

### 1.1 Nous Research capta US$ 90 milhões para levar o agente aberto Hermes às empresas
**Fonte:** [Runtime Wire](https://runtimewire.com/article/nous-research-90m-series-b-hermes-agent) (07/10) · [AI Agent Store](https://aiagentstore.ai/ai-agent-news/this-week) (11/10)

A Nous Research anunciou uma rodada Série B de US$ 90 milhões, com avaliação de cerca de US$ 1,5 bilhão segundo reportagem do Wall Street Journal citada pelo Runtime Wire. O dinheiro serve para transformar o Hermes, agente de código aberto, em produto para empresas, com foco em implantação, privacidade e administração, além de um aplicativo móvel previsto. A cobertura menciona canais como Slack, Telegram e WhatsApp, mas não detalha funcionalidades nem licença. Importa porque é um dos raros casos em que um agente aberto recebe capital de escala para competir com ofertas fechadas; vale acompanhar como a empresa equilibra o núcleo aberto com recursos pagos.

### 1.2 Microsoft inicia o preview do Work IQ para ancorar agentes do Copilot em dados vivos
**Fonte:** [AI Agent Store](https://aiagentstore.ai/ai-agent-news/this-week) (11/10)

A Microsoft começou em outubro a liberar o Work IQ em preview, camada que conecta o Copilot e agentes autônomos a dados em tempo real do Dynamics 365 e do Power Platform. Disponibilidade geral e preços ainda não foram anunciados, e a informação vem de um agregador, não de comunicado primário. O ponto relevante é arquitetural: agentes úteis dependem de contexto corporativo atualizado, e a disputa deixa de ser só o modelo e passa a ser quem controla a camada de dados e permissões por onde o agente enxerga a empresa.

### 1.3 Casa Branca exigiria notificação e correção imediata de incidentes de IA
**Fonte:** [AI Agent Store, resumindo o Axios](https://aiagentstore.ai/ai-agent-news/this-week) (10/10)

Segundo o resumo do agregador sobre reportagem do Axios, autoridades americanas disseram que vão exigir que empresas de IA notifiquem e corrijam incidentes de imediato, tratando o relato como obrigação de segurança nacional, depois das divulgações da Anthropic sobre ações não intencionais de seus modelos (um relatório de 09/10 descreve quatro categorias, como envio de formulário sensível em site real). O mesmo resumo diz que executivos de laboratórios fazem exercícios de "dia seguinte" para um incidente de grande escala. Não encontramos fonte primária: trate como informação a confirmar. Se confirmada, passa a haver uma obrigação concreta para quem opera agentes com acesso a ferramentas, e um precedente de regulação por incidente que pode chegar a empresas e governos usuários.

### 1.4 Cisco coloca agentes de IA dentro de espaços, reuniões e chamadas do Webex
**Fonte:** [Solutions Review](https://solutionsreview.com/ai-news-for-the-week-of-october-9-updates-from-honeycomb-io-ninjatech-ai-oracle-more/) (08/10)

A Cisco apresentou recursos para que agentes participem de espaços, reuniões e chamadas no Webex para tarefas em várias etapas, com uma integração com o Claude baseada em Claude Managed Agents prevista para breve. Também lançou o Dialog, um "harness" agêntico (a estrutura que cerca o modelo com ferramentas, memória e regras) para contexto de clientes. O agente passa a ser um participante com voz e permissões em canais de colaboração, o que amplia a superfície de risco e a necessidade de identidade e auditoria por agente.

### 1.5 Padrões abertos para verificar se agentes seguem regras sem expor dados
**Fonte:** [Enterprise Times](https://enterprisetimes.co.uk/2026/10/12/news-from-the-week-beginning-5th-october-2026) (07/10)

OpenMatter Network e HOL publicaram propostas de padrões para verificar que agentes autônomos cumprem regras sem revelar os dados sensíveis que processam; o material está aberto a comentários públicos. É uma proposta inicial, sem adoção conhecida, mas toca num problema central para ambientes regulados: como provar conformidade de um agente a um auditor sem entregar os dados. Quem trabalha com avaliação de sistemas agênticos deve acompanhar a consulta pública.

### 1.6 Kore.ai torna o Autoloop disponível para otimizar agentes contra metas de negócio
**Fonte:** [Solutions Review](https://solutionsreview.com/ai-news-for-the-week-of-october-9-updates-from-honeycomb-io-ninjatech-ai-oracle-more/) (08/10)

A Kore.ai liberou o Autoloop em disponibilidade geral na sua plataforma de agentes: ele automatiza a construção, a avaliação e a otimização de agentes segundo metas de negócio e requisitos de segurança. Sem benchmarks independentes, é anúncio de fornecedor. Ainda assim, reflete a tendência de fechar o ciclo avaliar-ajustar-reavaliar como funcionalidade de plataforma, algo que times de pesquisa vêm fazendo manualmente.

## 2. Ferramentas e modelos open source

### 2.1 Ling 3.1 Flash: MoE de 560 bilhões de parâmetros totais, 25 bilhões ativos
**Fonte:** [LLM Gateway](https://llmgateway.io/blog/new-ai-models-this-week-2026-10-11) (11/10)

A InclusionAI listou em 02/10 o Ling 3.1 Flash, modelo de raciocínio híbrido com arquitetura de mistura de especialistas (MoE, em que só parte dos parâmetros é ativada por token), contexto de 262 mil tokens e chamada de ferramentas. A página do agregador não informa licença nem se os pesos são abertos, então não dá para classificá-lo como open source sem verificar o repositório. Chama atenção pelo preço baixo em provedores de inferência, o que o torna candidato a experimentos com agentes de custo reduzido.

### 2.2 Tensor Machines lança benchmark aberto que liga desempenho de GPU, energia e custo da IA
**Fonte:** [Solutions Review](https://solutionsreview.com/ai-news-for-the-week-of-october-9-updates-from-honeycomb-io-ninjatech-ai-oracle-more/) (08/10)

A startup, que levantou US$ 1,5 milhão em rodada pré-seed, publicou um benchmark de código aberto que relaciona desempenho de GPU e consumo de energia ao custo da produção de IA. É um projeto pequeno e novo, mas a métrica de custo por saída, e não só velocidade, é útil para quem precisa justificar infraestrutura em pesquisa e em projetos públicos.

*Observação: um monitor de lançamentos consultado em 12/10 não registrava novos modelos de pesos abertos na semana; o Muse Wonder, da Meta, divulgado em 12/10, é proprietário.*

## 3. IA aplicada no setor público

*Sem novidades reais verificáveis nas últimas 24 a 48 horas, nem no Brasil nem no exterior, que não tenham sido cobertas nas edições anteriores (supercomputador adiado para 04/11, Coaf, OAB-SP, AI Act, entre outras). Os resultados encontrados eram de junho ou anteriores, e preferimos não preencher o tema com conteúdo antigo.*

## 4. IA aplicada em geral

### 4.1 HCLTech e Anthropic firmam parceria para expandir a IA agêntica em empresas
**Fonte:** [AIwire](https://hpcwire.com/aiwire/2026/10/12/hcltech-and-anthropic-partner-to-expand-enterprise-adoption-of-agentic-ai) (12/10)

A HCLTech e a Anthropic anunciaram uma parceria para ampliar a adoção de IA agêntica corporativa. Não conseguimos abrir o texto completo, então termos e números não estão confirmados; o título e a data foram verificados. É mais um acordo entre laboratório e integradora de TI, canal pelo qual a maior parte dos agentes chega às grandes empresas.

### 4.2 IDC e Microsoft: 17% das organizações de Singapura são "Frontier Firms"
**Fonte:** [Microsoft Source Asia](https://news.microsoft.com/source/asia/2026/10/12/singapore-firms-are-already-seeing-business-value-as-ai-adoption-matures) (12/10)

Pesquisa da IDC encomendada pela Microsoft indica que 17% das organizações de Singapura são "Frontier Firms" (contra 10% no mundo), 68% relatam resultados significativos ou transformadores e 41% dizem que a IA aumenta receita. A própria matéria tem uma inconsistência: cita 200 respondentes no texto e N=5.204 na nota. Estudo encomendado por fornecedor, então vale cautela; o dado mais interessante é a associação entre maturidade e governança.

### 4.3 Atlassian e OpenAI ampliam parceria: modelos no Rovo e plugins para ChatGPT e Codex
**Fonte:** [Solutions Review](https://solutionsreview.com/ai-news-for-the-week-of-october-9-updates-from-honeycomb-io-ninjatech-ai-oracle-more/) (08/10)

A Atlassian vai levar modelos de fronteira da OpenAI ao Rovo e aos seus agentes, com plugins que conectam ChatGPT e Codex ao contexto permissionado de projetos e exploração de integração mais profunda para atribuir tarefas do Jira a agentes. Mostra o agente como colega de equipe dentro da ferramenta de gestão de trabalho.

### 4.4 PwC e Cohere anunciam aliança global, começando pelo Canadá
**Fonte:** [PwC](https://www.pwc.com/gx/en/news-room/press-releases/2026/accelerate-secure-enterprise-ai-adoption.html) (semana de 09/10)

A aliança combina a plataforma North, da Cohere, com a expertise de risco e regulação da PwC, com opções de nuvem privada, local e isolada (air-gapped). Interessa a setores regulados e a governos que não podem enviar dados a nuvens públicas.

### 4.5 Workday: só 28% dos líderes esperam cortes de vagas por causa da IA
**Fonte:** [Enterprise Times](https://enterprisetimes.co.uk/2026/10/12/news-from-the-week-beginning-5th-october-2026) (05/10)

O relatório de outubro da Workday afirma que a IA reconfigura funções mais do que elimina e que a demanda por habilidades técnicas avançadas em IA subiu 51%. É pesquisa de fornecedor de RH, mas contrasta com a onda de cortes noticiada nas edições anteriores.

### 4.6 Cognizant cria a unidade Activate para empresas de médio porte
**Fonte:** [Solutions Review](https://solutionsreview.com/ai-news-for-the-week-of-october-9-updates-from-honeycomb-io-ninjatech-ai-oracle-more/) (08/10)

A unidade atende empresas com faturamento de US$ 1 bilhão a US$ 5 bilhões, com foco em serviços financeiros, saúde, manufatura e varejo, e um responsável único do início à entrega. Sinaliza que o mercado de IA corporativa busca o meio do mercado, onde faltam equipes próprias.
