---
layout: post
title: "Radar IA — 06/11/2026, 17h"
date: 2026-11-06 17:06:00 -0300
categories: edicao
excerpt: "Modelos da OpenAI e o Codex seguem em preview privado no Google Cloud; Kimi K3.1 Pro tem pesos reportados no Hugging Face, mas com relatos conflitantes; ERNIE 5.5 Flash Base sai com licença que exclui UE, Reino Unido e Coreia do Sul; Semana de IA do Serpro encerra o debate sobre IA soberana; Itália usa assistente multiagente no INPS; IPO da Anthropic ainda sem faixa de preço e com dúvidas de investidores."
---

*Janela pesquisada: 04 a 06/11/2026. Excluídos por já terem sido cobertos nas edições de 03, 04 e 05/11: marco legal da IA (PL 2338) parado na Câmara, contrato AT&T–Amdocs, Snowflake, Saab, CrowdStrike e demais itens daquelas edições. Esta edição teve poucas novidades primárias confirmadas; vários itens vêm de fontes secundárias e estão sinalizados.*

## Destaques do dia

1. **OpenAI e Codex seguem em preview privado no Google Cloud**: GPT-6 Astra, GPT-6.1 Sol e GPT-6 Luna estão no Model Garden só para clientes selecionados, com disponibilidade geral prometida "nas próximas semanas". → 1.1, 4.2
2. **Kimi K3.1 Pro: pesos reportados no Hugging Face, mas com relatos conflitantes**: o modelo agêntico de 2,8 tri de parâmetros teria sido publicado em 4 ou 5/11; outras fontes ainda não confirmam. → 2.1
3. **ERNIE 5.5 Flash Base chega com licença que exclui UE, Reino Unido e Coreia do Sul**: um "open weights" com restrição geográfica incomum. → 2.2
4. **Semana de IA do Serpro termina hoje com foco em IA soberana**: o debate é quem controla dados, tecnologia e poder de decisão no setor público. → 3.1
5. **Itália põe um assistente multiagente no INPS**: agentes restritos a fontes verificadas ajudam cidadãos a encontrar benefícios. → 3.2
6. **IPO da Anthropic: roadshow sem data firme e investidores resistem à avaliação**: ainda sem faixa de preço na SEC, com valores entre US$ 1 tri e US$ 2 tri em discussão. → 4.1

## 1. Novidades de IA agêntica

### 1.1 Modelos GPT-6 e fluxos do Codex chegam ao Google Cloud, ainda em preview privado
**Fonte:** [TechEnclave](https://techenclave.com/news/items/openai-models-enter-google-cloud-private-preview-with-wider-access-planned) (21/10, atualizado até 27/10) · [Let's Data Science](https://letsdatascience.com/news/openai-brings-frontier-models-and-codex-to-google-cloud-ed6ecc1e)

O anúncio é de 21/10 e portanto não é novo, mas o status continua relevante: até onde encontrei, a disponibilidade geral ainda não foi confirmada. GPT-6 Astra (o modelo de topo), GPT-6.1 Sol (faixa de menor custo) e GPT-6 Luna (uso rápido em escala) estão no Model Garden do Google Cloud para clientes empresariais selecionados, e participantes do preview podem conectar o Codex CLI e o Codex Desktop à infraestrutura de inferência do Google. Para quem projeta arquiteturas agênticas, o ponto é a redução do aprisionamento a um único provedor de nuvem: modelos da OpenAI passam a poder ser comprados em Google Cloud, Azure e AWS. As fontes divergem sobre preços e faturamento, e não encontrei os comunicados oficiais, então trate os detalhes comerciais como não confirmados.

## 2. Ferramentas e modelos open source

### 2.1 Kimi K3.1 Pro: pesos aparecem em relatos, mas a confirmação é desigual
**Fonte:** [FourWeekMBA](https://fourweekmba.com/ai-kimi-k3-1-pro-weights-out-leads-opus-5-5-on-16-of-37-tests/) (05/11) · [KuCoin News](https://www.kucoin.com/news/flash/moonshot-ai-s-kimi-k3-1-pro-opens-on-hugging-face-tops-open-weight-model-rankings) (04–05/11) · [daily.dev](https://daily.dev/posts/kimi-ai-releases-kimi-k3-1-pro-model-weights-to-the-public-tw8jkno5e)

A Moonshot AI havia prometido os pesos do Kimi K3.1 Pro até 4/11, e as edições anteriores registraram que o prazo passou sem confirmação. Agora há relatos de que o modelo está no Hugging Face: arquitetura de mistura de especialistas (MoE) com 2,8 trilhões de parâmetros totais, cerca de 104 bilhões ativos por inferência, contexto de aproximadamente 1 milhão de tokens e cerca de 1,56 TB de pesos em 96 arquivos. Os mesmos relatos dizem que ele lidera os modelos de pesos abertos no Agent Arena. Ressalvas importantes: as datas divergem (4 ou 5/11), as fontes são secundárias, os números de desempenho são autodeclarados pela Moonshot, e outra busca não achou o model card nem a licença. Antes de usar ou citar, confira o repositório da organização moonshotai no Hugging Face. Para a pesquisa, o tamanho (1,5 TB) torna o uso local inviável sem infraestrutura séria; o interesse prático está em provedores de inferência.

### 2.2 ERNIE 5.5 Flash Base, da Baidu, sai com licença que exclui UE, Reino Unido e Coreia do Sul
**Fonte:** [Trending Topics EU](https://www.trendingtopics.eu/baidu-ernie-5-5-banned-europe-license/) (esta semana)

A Baidu publicou no Hugging Face o ERNIE 5.5 Flash Base, um modelo base de pesos abertos cuja licença cobre "todas as áreas geográficas do mundo, exceto a União Europeia, o Reino Unido e a Coreia do Sul". O caso é um bom lembrete de que "pesos abertos" não é sinônimo de "código aberto": a licença define quem pode usar, e restrições territoriais, possivelmente ligadas à regulação de IA nessas jurisdições, podem inviabilizar projetos acadêmicos e comerciais. Leia sempre a licença antes de adotar um modelo, em especial se a instituição tem parceiros ou usuários nessas regiões. Não encontrei a documentação oficial da Baidu, só a cobertura secundária.

## 3. IA aplicada no setor público

*Brasil*

### 3.1 II Semana de IA do Serpro termina hoje (6/11) com foco em IA soberana
**Fonte:** [Serpro](https://www.serpro.gov.br/menu/noticias/noticias-2026/segunda-semana-ia-serpro) · [Brasil Inovador](https://brasilinovador.com.br/segunda-semana-de-ia-serpro-discute-soberania-de-dados-e-poder-de-decisao-no-setor-publico/) (4 a 6/11)

O evento, de 4 a 6/11, em Brasília e online, tem o tema "IA Soberana: Dados, Tecnologia e Poder de Decisão", com painéis sobre infraestrutura de IA, indústria de semicondutores e a participação de MGI, MCTI, Receita Federal, RNP, Petrobras, LNCC e Tesouro Nacional. Já foi tratado nas edições de 04 e 05/11, então registro só o encerramento. O que importa para quem acompanha o setor público: o debate deixou de ser apenas "usar IA" e passou a ser "o que o Estado precisa controlar" (dados, modelos e capacidade de computação) para decidir com autonomia. Não encontrei, no material consultado, anúncios de produtos ou de contratos concretos decorrentes do evento; vale acompanhar a divulgação das conclusões pelo Serpro.

*Internacional*

### 3.2 Itália usa assistente multiagente no INPS para orientar cidadãos sobre benefícios
**Fonte:** [AI in Government: Policy Brief (semana de 2/11)](https://automatinggovernmentinsights.substack.com/p/ai-in-government-policy-brief-wc-975) (02/11)

Segundo o boletim de política pública, o INPS, a previdência social italiana, implantou um assistente generativo multiagente, construído sobre frameworks de código aberto e restrito a fontes verificadas pelo próprio instituto, no qual o cidadão descreve sua situação em linguagem simples e recebe indicação de benefícios. Não consegui abrir o boletim nem confirmar com o INPS, então os detalhes vêm do resumo da busca. Mesmo assim, o desenho é instrutivo: limitar o agente a uma base verificada é o padrão que reduz o risco de alucinação em serviços públicos, e é um modelo possível para casos brasileiros como previdência e assistência social.

## 4. IA aplicada em geral

### 4.1 IPO da Anthropic: roadshow sem data firme, sem faixa de preço e com dúvidas sobre a avaliação
**Fonte:** [Yahoo Finance](https://finance.yahoo.com/markets/article/anthropics-ipo-could-start-trading-as-soon-as-nov-16--heres-the-road-from-filing-to-first-trade-155405578.html) (05/11) · [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/1-5-trillion-too-much-051701570.html) · [FinanceFeeds](https://financefeeds.com/anthropic-ipo-roadshow-looms-with-no-price-range/)

Atualizando o item de ontem: a Anthropic abriu o S-1 (documento de registro na SEC) em 26/10, e a cobertura aponta o início do roadshow (as apresentações a investidores) entre 9 e 13/11, com estreia na Nasdaq, ticker ANT, possível entre 16 e 18/11. Até 5/11 não havia emenda com a faixa de preço. Segundo Reuters e WSJ, relatadas pela imprensa, parte dos investidores duvida de que dê tempo para uma listagem em novembro e pede avaliação menor que os cerca de US$ 1,5 tri em discussão; houve sugestão de algo perto de US$ 1 tri, enquanto outros veem US$ 1,8 a 2 tri. As datas conflitam entre veículos e são projeções, não anúncios. Para a área, o IPO é um termômetro de quanto o mercado paga por receita de IA em escala.

### 4.2 Mazda usa Codex com GPT-6 Astra em otimização aerodinâmica
**Fonte:** [Analytics India Magazine](https://analyticsindiamag.com/ai-news/openais-codex-helps-in-aerodynamic-engineering-for-mazda) (cerca de 4/11)

Segundo a cobertura, engenheiros da Mazda usam o Codex com o GPT-6 Astra para otimizar projetos de veículos por meio de simulações de fluxo de ar. É um caso de agente de código aplicado a engenharia física, não a software, o que amplia o campo de uso dessas ferramentas. Não consegui abrir a matéria nem encontrei a publicação original da OpenAI ou da Mazda; sem números de ganho ou detalhes do método, é um indício de adoção, não uma evidência de resultado.
