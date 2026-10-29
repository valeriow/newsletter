---
layout: post
title: "Radar IA — 29/10/2026, 18h"
date: 2026-10-29 18:00:00 -0300
categories: edicao
excerpt: "GitHub unifica sessões e automações do Copilot na nuvem; Snowflake dá controle de raciocínio e acesso a dados aos agentes de código; Microsoft revela 50 milhões de agentes registrados e novos contêineres de execução; Azure cresce 48% e a cobrança por consumo ganha espaço; Oracle e Google levam TPUs à OCI em 2027; AI Brasil Experience reúne 150 palestras sobre agentes e ROI em São Paulo"
---

*Janela pesquisada: 27 a 29/10/2026. Ficaram de fora o Gemini 4 Carbon, o Copilot Fusion, o sandbox da Akamai e os demais temas já cobertos nas edições de 26, 27 e 28/10. Edição enxuta: várias seções tiveram pouca novidade verificável nas últimas 48 horas, e preferimos dizer isso a preencher espaço.*

## Destaques do dia

1. **Copilot vira uma sessão contínua entre dispositivos**: o GitHub conecta a experiência de agente na nuvem entre web, celular, app, CLI e IDEs, com automações que aprendem com os resultados. → 1.1
2. **Agentes de dados ganham botões de controle**: o Snowflake adiciona esforço de raciocínio, instruções de sistema e montagem de stages nos agentes de código do Cortex. → 1.2
3. **Governar agentes é o novo produto**: a Microsoft diz ter mais de 50 milhões de agentes no Agent 365 e leva contêineres de execução ao Windows. → 1.3, 4.1
4. **Azure acelera e a cobrança muda**: Azure cresce 48%, Microsoft Cloud passa de US$ 63,9 bi no trimestre e o consumo começa a pesar mais que a assinatura por usuário. → 4.1
5. **TPUs saem do Google Cloud**: Oracle e Google anunciam TPUs na OCI a partir de 2027, abrindo alternativa às GPUs para agentes. → 4.2
6. **IA aplicada vira pauta de evento no Brasil**: a AI Brasil Experience reúne mais de 150 palestras em São Paulo sobre agentes, ROI e governança. → 4.3

## 1. Novidades de IA agêntica

### 1.1 GitHub conecta sessões do Copilot na nuvem entre dispositivos e lança Automations
**Fonte:** [AI Agent Store, resumo do anúncio do GitHub](https://aiagentstore.ai/ai-agent-news/this-week) (29/10)

O GitHub começou a liberar, em 28/10, uma experiência "conectada" do agente de nuvem do Copilot: a sessão persiste entre web, celular, app, CLI e IDEs, de modo que o desenvolvedor pode iniciar uma tarefa em um lugar e retomá-la em outro. Junto vêm as Copilot Automations, rotinas que rodam na nuvem, aprendem com os resultados e sugerem melhorias que a equipe aprova ou rejeita. Importa porque desloca o agente de "ferramenta que roda na minha máquina" para "serviço persistente com memória e ciclo de melhoria", o que traz perguntas de pesquisa abertas para quem estuda agentes: como avaliar uma automação que muda ao longo do tempo e como auditar o que ela aprendeu. Observação: a fonte é um agregador que resume o anúncio; vale conferir o post original do GitHub antes de citar detalhes de disponibilidade por plano.

### 1.2 Snowflake adiciona controle de raciocínio, instruções de sistema e stage mounts aos agentes de código do Cortex
**Fonte:** [AI Agent Store, citando a documentação do Snowflake](https://aiagentstore.ai/ai-agent-news/this-week) (29/10; documentação atualizada em 28/10)

A API de agentes de código do Cortex ganhou três controles: `thinking_effort`, para ajustar a profundidade do raciocínio; `instructions.system`, para somar instruções de nível de sistema; e `stage_mounts`, que dá ao sandbox do agente acesso a stages versionados do Snowflake sem copiar arquivos. É um exemplo concreto de uma tendência que vale acompanhar: provedores expondo o orçamento de raciocínio como parâmetro de produção, para equilibrar custo, latência e qualidade, e aproximando o agente dos dados em vez de movê-los. Para quem projeta sistemas agênticos, é um bom caso de estudo sobre onde colocar a fronteira entre agente, dados e permissões.

### 1.3 Microsoft: Agent 365 passa de 50 milhões de agentes e contêineres de execução chegam ao Windows
**Fonte:** [PYMNTS](https://www.pymnts.com/earnings/2026/microsoft-sees-enterprise-ai-adoption-accelerate-as-copilot-usage-grows/) (28/10)

Na divulgação de resultados, a Microsoft informou que o registro Agent 365 tem mais de 50 milhões de agentes (alta de mais de 30% no trimestre), que clientes auditaram mais de 7,6 bilhões de atividades de agentes com o Purview e que agentes já abrem mais de um terço dos pull requests no GitHub, com um aumento de 6 vezes em seis meses. A empresa também disse que o Microsoft Execution Containers passa a governar agentes no Windows, com adoção citada por OpenAI (Codex), Anthropic (Claude Code) e Meta. Para quem acompanha o campo, o sinal é que identidade, registro, auditoria e isolamento de agentes estão virando infraestrutura padrão de plataforma, e que a disputa deixou de ser só sobre capacidade do modelo. Os números são autodeclarados pela empresa e não há metodologia pública para o que conta como "agente".

## 2. Ferramentas e modelos open source

*Sem novidades verificáveis nas últimas 24 a 48 horas. Os lançamentos abertos recentes que encontramos (como o DeepSeek V4.1-Flash-1017, de 17/10, e os modelos em alta no Hugging Face na semana passada) são anteriores à janela ou já foram cobertos nas edições anteriores.*

## 3. IA aplicada no setor público

*Brasil*

*Sem novidades verificáveis nas últimas 24 a 48 horas. As matérias localizadas sobre governança de IA no governo federal (portaria do MGI, levantamento de 52 órgãos com IA) são de abril e junho de 2026 e não foram repetidas aqui.*

*Internacional*

*Sem novidades verificáveis nas últimas 24 a 48 horas. O lançamento mais recente que encontramos, o Gemini for Government Services, do Google Public Sector, é de 20/10 e está fora da janela.*

## 4. IA aplicada em geral

### 4.1 Microsoft: Azure cresce 48% e a cobrança por consumo ganha espaço
**Fonte:** [PYMNTS](https://www.pymnts.com/earnings/2026/microsoft-sees-enterprise-ai-adoption-accelerate-as-copilot-usage-grows/) (28/10)

No primeiro trimestre fiscal, a Microsoft reportou receita de US$ 92,3 bilhões (alta de 19%), Microsoft Cloud de US$ 63,9 bilhões (alta de 30%) e crescimento de 48% no Azure. O número de usuários diários do Copilot cresceu quase 50% sobre o trimestre anterior e mais de 5 vezes sobre um ano antes; clientes com mais de 50 mil assentos cresceram mais de 8 vezes. Satya Nadella citou Unilever, Rolls-Royce e Raiffeisen como casos de IA aplicada a processos operacionais e disse que o foco agora é confiabilidade, custo e segurança. A CFO Amy Hood previu que a cobrança por consumo para agentes crescerá mais devagar fora do desenvolvimento de software. Importa porque mostra a migração do modelo de assinatura por usuário para o pagamento por tarefa executada, algo que muda a conta de quem planeja adotar agentes em escala.

### 4.2 Oracle e Google levam TPUs à Oracle Cloud a partir de 2027
**Fonte:** [AI Agent Store, citando o anúncio conjunto](https://aiagentstore.ai/ai-agent-news/daily/2026-10-28) (28/10)

Durante o Oracle AI World, as duas empresas disseram que os TPUs do Google estarão disponíveis na Oracle Cloud Infrastructure a partir de 2027, com ênfase em cargas agênticas, de contexto longo e de raciocínio em várias etapas. Para o mercado, é uma opção de hardware que não é GPU Nvidia, o que pode pressionar o custo de rodar agentes em escala e reduzir dependência de um único fornecedor. Os detalhes de regiões, preços e capacidade ainda não foram divulgados, então a análise de custo fica para quando houver números.

### 4.3 AI Brasil Experience reúne mais de 150 palestras sobre agentes, ROI e governança em São Paulo
**Fonte:** [Tudo sobre CDP](https://www.tudosobrecdp.com.br/ia/ai-brasil-experience-2026-programacao-destaques/) (28 e 29/10)

O evento acontece nos dias 28 e 29/10, no Distrito Anhembi, com cinco arenas e mais de 150 palestras, além de uma Arena Hands-on e um Laboratório de Experiências Práticas; a programação destaca agentes de IA, retorno sobre investimento, CRM, governança e futuro do trabalho. A edição anterior reuniu mais de 12 mil participantes. É um termômetro do momento do mercado brasileiro: a conversa corporativa saiu de "o que a IA pode fazer" para "qual o retorno e como governar". A fonte descreve a programação, não resultados do evento, e a página consultada não lista palestrantes nem conteúdos voltados ao setor público.
