---
layout: post
title: "Radar IA — 02/11/2026, 20h"
date: 2026-11-02 20:33:00 -0300
categories: edicao
excerpt: "OpenAI e Anthropic alegam ter refutado a Hipótese do Tempo Exponencial; pesquisas novas medem agentes pela trajetória e não só pelo resultado final; Oracle e OpenAI lançam malha de segurança contra vulnerabilidades achadas por IA; FreeToken, AiSOC e os pesos prometidos do Kimi K3.1 movimentam o open source; Anthropic oferece 40% de desconto ao governo dos EUA via GSA enquanto a Casa Branca recusa divulgar seu marco de testes de IA; Aramco fecha a compra de 49% da HUMAIN e a OpenAI defende limites de velocidade para IA de fronteira."
---

*Janela pesquisada: 31/10 a 02/11/2026, com alguns itens de 26 a 30/10 que ainda não haviam sido cobertos. Excluídos por já constarem em edições anteriores: Super-Agent da DeepSeek, Mistral Large 4, S-1 da Anthropic, Apple com Qwen na China, padrão Microsoft–AFT para escolas e Segunda Semana de IA Serpro. Nesta edição vários sites primários estavam inacessíveis à execução automática; os itens apoiados em fontes secundárias estão indicados.*

## Destaques do dia

1. **OpenAI e Anthropic dizem ter refutado a Hipótese do Tempo Exponencial**: os dois laboratórios publicaram, com horas de diferença, algoritmos subexponenciais para o problema 3-SAT achados por modelos de IA, ainda sem validação externa. → 1.1
2. **Pesquisa de agentes passa a medir a trajetória, não só o resultado**: novos trabalhos tratam de executabilidade de prefixos, descrições de ferramentas para modelos pequenos e auto-evolução sem treinar pesos. → 1.2, 1.3, 1.4
3. **Oracle e OpenAI lançam malha de segurança, e Altman admite choque com o volume de falhas achadas por IA**: defesa cibernética vira o principal caso de uso corporativo de agentes. → 1.5
4. **Open source local e de segurança ganha ferramentas**: FreeToken roda MoEs gigantes em GPUs de consumo, AiSOC traz um SOC aberto com IA e o Kimi K3.1 Pro tem pesos prometidos até 4 de novembro. → 2.1, 2.2, 2.3
5. **Governo dos EUA compra Claude com 40% de desconto, mas esconde seu marco de testes de IA**: o acordo com a GSA estende preços a estados e municípios, enquanto a Casa Branca invoca segurança nacional para não divulgar o framework. → 3.1, 3.2
6. **Capital e política seguem a infraestrutura**: Aramco conclui a compra de 49% da HUMAIN e a OpenAI prepara campanha por "limites de velocidade" para IA de fronteira. → 4.1, 4.2

## 1. Novidades de IA agêntica

### 1.1 OpenAI e Anthropic anunciam, com horas de diferença, refutações da Hipótese do Tempo Exponencial
**Fonte:** [Science](https://www.science.org/content/article/ai-cracks-27-year-old-pillar-computer-science-openai-and-anthropic-claim) (28/10) · [Runtime Wire](https://runtimewire.com/article/anthropic-posts-its-own-eth-refutation-hours-after-openai-as-lance-fortnow-says-) (27/10) · [OfficeChai](https://officechai.com/ai/anthropic-says-claude-too-independently-disproved-exponential-time-hypothesis-on-the-same-day-as-openai/) (27/10)

A OpenAI afirma que um modelo interno ainda não lançado produziu um algoritmo de tempo subexponencial para o 3-SAT, o que refutaria a Hipótese do Tempo Exponencial (ETH, na sigla em inglês), uma conjectura de 1999 que sustenta boa parte da teoria de complexidade. O manuscrito de 67 páginas e uma prova em Lean estão no GitHub. Horas depois, a Anthropic publicou um artigo de 49 páginas atribuído ao Claude, dizendo que o algoritmo central foi encontrado em 16/10 com 14 milhões de tokens de saída e sem intervenção humana, e que o resultado também atingiria a versão forte da hipótese. Nenhuma das duas alegações foi revisada por pares; Lance Fortnow disse que a abordagem "parece promissora", mas não pôde atestá-la ainda, e a própria Anthropic ressalva que o resultado nada diz sobre resolver fórmulas na prática nem sobre P versus NP. Para quem trabalha com agentes, o ponto é a escala de autonomia: horas de raciocínio sem humano gerando artefatos verificáveis por prova formal. Se resistir à verificação, será o exemplo mais forte até hoje de IA produzindo matemática nova. Datas divergem entre as fontes (16 a 27/10), por isso o caso entra aqui como alegação pendente.

### 1.2 Hippo: auto-evolução de agentes por "repetição hipocampal", sem treinar pesos
**Fonte:** [arXiv 2610.24453](https://arxiv.org/abs/2610.24453) (fim de outubro; via [AI Daily Digest nº 201](https://github.com/diclogic/ai-daily-digest/issues/201), 02/11)

O trabalho propõe que um agente melhore reprocessando episódios passados, inspirado no papel do hipocampo na consolidação de memória, em vez de atualizar pesos do modelo. A promessa é aprendizado contínuo barato, aplicável a modelos fechados acessados por API. Não consegui acessar o artigo, então os resultados quantitativos não foram verificados. Vale acompanhar porque memória e auto-aperfeiçoamento sem fine-tuning são hoje a fronteira prática de harnesses de agentes.

### 1.3 Prefix Executability: avaliar se trajetórias parciais de agentes continuam executáveis
**Fonte:** [arXiv 2610.40444](https://arxiv.org/abs/2610.40444) (via [AI Daily Digest nº 201](https://github.com/diclogic/ai-daily-digest/issues/201), 02/11)

A proposta é pontuar se os prefixos de uma trajetória de agente (a sequência de ações até certo ponto) ainda podem ser executados, e não apenas se o resultado final foi correto. Isso expõe agentes que acertam por acaso ou que acumulam estados inconsistentes no meio do caminho, um ponto cego de benchmarks que só olham o sucesso final. Resumo baseado na descrição do digest; o artigo não pôde ser lido.

### 1.4 Agentes pequenos dependem da qualidade das descrições das ferramentas
**Fonte:** [arXiv 2610.35981](https://arxiv.org/abs/2610.35981) (via [AI Daily Digest nº 201](https://github.com/diclogic/ai-daily-digest/issues/201), 02/11)

O estudo examina como a redação das descrições de ferramentas afeta a escolha e o uso correto por modelos pequenos. A implicação prática é direta para quem monta servidores MCP e catálogos de ferramentas: descrições ruins custam mais em modelos pequenos, justamente os preferidos para rodar localmente. Detalhes numéricos não verificados.

### 1.5 Oracle lança malha de segurança com a OpenAI; Altman diz estar "chocado" com o volume de falhas encontradas por IA
**Fonte:** [Computer Weekly](https://www.computerweekly.com/news/366652912/OpenAIs-Altman-Only-way-out-of-patch-apocalypse-is-through) (27/10) · [AI Daily Digest nº 201](https://github.com/diclogic/ai-daily-digest/issues/201) (02/11)

No Oracle AI World, a Oracle anunciou o AI Security Mesh, construído com a OpenAI para detecção de vulnerabilidades. Na mesma ocasião, Sam Altman disse estar "chocado com quantas vulnerabilidades esses sistemas de IA estão encontrando" e defendeu que a única saída para o que chamou de "apocalipse de patches" é seguir adiante com a mesma tecnologia, ou seja, usar IA também para corrigir. O tema conversa com a edição de 30/10 (agentes que acham zero-days) e mostra que a segurança ofensiva e defensiva com agentes se tornou o caso de uso corporativo mais concreto, com um gargalo novo: a capacidade humana de aplicar correções.

## 2. Ferramentas e modelos open source

### 2.1 Kimi K3.1 Pro: pesos abertos prometidos até 4 de novembro, ainda não publicados
**Fonte:** [AI Daily Digest nº 201](https://github.com/diclogic/ai-daily-digest/issues/201) (02/11)

O modelo foi lançado em 23/10 por app e API, com pontuação autodeclarada de 65,7 no Terminal-Bench 4.0. A Moonshot prometeu abrir os pesos até 4/11, mas até 02/11 não havia publicação nem licença anunciada. Complementa a edição de 01/11, quando a empresa encerrou novas contas do Kimi K2. Cuidado: a pontuação é autodeclarada e a data é uma promessa, não um fato.

### 2.2 FreeToken: motor aberto para servir MoEs gigantes em GPUs de consumo
**Fonte:** [GitHub FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) (02/11)

Projeto em Apache-2.0, com cerca de 15,5 mil estrelas, que promete rodar modelos de mistura de especialistas (MoE) de mais de 290 bilhões de parâmetros em PCs gamer, combinando execução CPU-GPU, cache de especialistas e realocação de VRAM entre cache de especialistas e memória de KV. Expõe endpoints compatíveis com Anthropic e OpenAI, para uso com Claude Code, Codex e OpenCode, e suporta DeepSeek-V4-Flash, Qwen3.6-35B-A3B e GLM-5.2. Exige GPU NVIDIA RTX 30/40/50 em Windows ou Linux. O README não traz números de desempenho (cita um paper, arXiv:2608.16157), então a alegação central precisa de teste independente.

### 2.3 AiSOC: centro de operações de segurança aberto, com agentes que exigem aprovação humana
**Fonte:** [GitHub beenuar/AiSOC](https://github.com/beenuar/AiSOC) (02/11)

Licença MIT, financiado pela Cyble. Ingere telemetria, correlaciona alertas em incidentes e usa agentes para investigar, registrando prompts, chamadas de ferramentas e veredictos em um "Investigation Ledger"; ações de resposta exigem aprovação humana por padrão. Traz milhares de regras de detecção, 91 conectores, exportação de evidências em OCSF e um servidor MCP. O README admite que nenhum provedor de LLM hospedado foi testado e que o modelo local embutido não é de fronteira. Útil como referência de arquitetura de agentes auditáveis para segurança.

### 2.4 hex: ditado por voz local, de código aberto, para macOS
**Fonte:** [GitHub anomalyco/hex](https://github.com/anomalyco/hex) (02/11, via [AI Daily Digest nº 201](https://github.com/diclogic/ai-daily-digest/issues/201))

Ferramenta MIT de ditado "aperte para falar" que transcreve no próprio dispositivo, apenas em Apple silicon, com cerca de 3,5 mil estrelas e alta de 1.179 no dia; não aceita pull requests. Importa pela tendência de voz local e privada, sem depender de nuvem.

### 2.5 Qwen4 ainda não saiu; só a variante de 27B deve ter pesos abertos
**Fonte:** [Yotta Labs](https://www.yottalabs.ai/post/qwen-4-27b-release-date-specs-hardware-what-is-known-2026) (23/09) · [Manifold](https://manifold.markets/Terminator2/will-alibaba-publish-open-weights-f) (24/10)

Atualização da edição de 30/10: segundo fontes secundárias, a Alibaba anunciou a família em 22/09 (Max, Flash, Plus e 27B), disse que o 27B terá pesos abertos, mas não publicou data nem licença; o boato de "próxima semana" não foi confirmado por fonte oficial. Tratar como incerto até aparecer no repositório oficial da Qwen.

## 3. IA aplicada no setor público

*Brasil*

Sem novidades reais nas últimas 48 horas: a Segunda Semana de IA Serpro ("IA Soberana"), de 4 a 6 de novembro, já foi coberta na edição anterior e só começa na quarta-feira; o PL 2338/2023 segue na Câmara sem votação confirmada nas fontes consultadas.

*Internacional*

### 3.1 Anthropic e a GSA: 40% de desconto para todos os níveis de governo dos EUA
**Fonte:** [Anthropic](https://www.anthropic.com/news/expanding-partnership-gsa) (27/10)

Novo acordo no programa OneGov dá 40% de desconto no Claude Enterprise, Claude for Government e na API, sem gasto mínimo, estendido a governos estaduais, locais, tribais e territoriais; a Anthropic estima economia de cerca de US$ 1 bilhão. A empresa diz que cerca de 500 organizações públicas dos EUA usam o Claude e que o uso em agências civis federais cresceu cerca de 20 vezes em um ano. Casos citados: Utah deu Claude Code a 34 desenvolvedores de 10 agências, com 71% relatando economia de 20 horas ou mais em quatro semanas, e um órgão estadual respondeu a um ransomware em 8 minutos contra os habituais 2 a 3 dias. Os números são da própria empresa. O Claude for Government opera em FedRAMP High e o Claude Enterprise está em processo para FedRAMP Moderate. Importa como modelo de compra centralizada: preço negociado em nível federal que os entes subnacionais podem usar, algo comparável a atas de registro de preços no Brasil.

### 3.2 Casa Branca se recusa a divulgar seu framework de testes de modelos de IA
**Fonte:** [CBS News](https://www.cbsnews.com/news/ai-model-framework-white-house/) (30/10) · [The Information](https://www.theinformation.com/briefings/trump-administration-refuses-release-information-ai-testing-framework) (30/10)

Em resposta a uma ação de acesso à informação da Protect Democracy, o Escritório do Diretor Nacional de Cibersegurança invocou exceções de segurança nacional e de sigilo comercial para não divulgar o framework de testes de modelos de IA. Importa para a governança: o governo testa modelos de fronteira, mas a sociedade não consegue auditar critérios. Detalhes além do resumo do digest não foram verificados (página principal inacessível).

## 4. IA aplicada em geral

### 4.1 Aramco conclui a compra de 49% da HUMAIN
**Fonte:** [Aramco](https://www.aramco.com/en/news-media/news/2026/pif-and-aramco-close-humain-transaction-to-accelerate-humains-global-growth) (01/11) · [Arabian Business](https://www.arabianbusiness.com/business/technology/saudi-aramco-acquires-49-stake-in-humain-in-2-6bn-ai-deal-with-pif)

A Aramco pagará cerca de 9,9 bilhões de riais sauditas (aprox. US$ 2,6 bilhões) em dinheiro em 2026, mais ativos de IA, enquanto o PIF mantém 51% da HUMAIN. Mostra petrolíferas e fundos soberanos virando acionistas diretos de plataformas de IA e infraestrutura no Golfo, em linha com a corrida por IA soberana.

### 4.2 OpenAI prepara campanha por "limites de velocidade" e por chamar data centers de "compute campuses"
**Fonte:** [Implicator.ai](https://www.implicator.ai/openai-plans-post-midterms-policy-pr-blitz-pushing-mandatory/) (01/11, citando Axios)

Segundo o Axios, após as eleições de meio de mandato a OpenAI pretende defender limites de velocidade obrigatórios para sistemas de fronteira e rebatizar data centers; um porta-voz disse que "compute campuses descreve melhor a escala e o papel da infraestrutura". Reportagem de segunda mão, não confirmada em fonte da empresa. Importa porque sinaliza regulação defendida pelo próprio líder do setor e uma disputa de narrativa sobre a oposição local a data centers.

### 4.3 Dream levanta US$ 17 milhões em rodada seed para "modelos de mundo construído"
**Fonte:** [TNW](https://thenextweb.com/news/dream-17m-seed-ai-building-design) (29/10)

Startup fundada por ex-executivos da Palantir que aplica modelos de mundo a projetos de construção em edificações licenciadas nos EUA; teria 10 projetos no Texas e na Califórnia. Dado de imprensa, sem validação independente de resultados. Exemplo de IA vertical em setor físico tradicional.

### 4.4 Investimento em IA incorporada na China chega a 93,5 bilhões de yuans no 1º semestre
**Fonte:** [Crypto Briefing](https://cryptobriefing.com/chinese-robot-makers-raise-13b-ai-robotics/) (02/11, dados da ITjuzi)

Foram 322 negócios, com o dinheiro migrando para software de robôs. É um indicador de onde a IA física está atraindo capital, mas vem de consultoria de dados citada por veículo secundário.
