---
layout: post
title: "Radar IA — 28/11/2026, 18h"
date: 2026-11-28 18:00:00 -0300
categories: edicao
excerpt: "Dia fraco em novidades verificadas: nenhum anúncio de 24 a 48 horas nos temas de agentes e setor público; GLM-5.2 e Kimi K2.7 Code, abertos em junho, ainda sem cobertura aqui; Anthropic amplia alianças com DXC e TCS; preprint aponta descasamento entre a prova Lean e o texto da OpenAI sobre Navier–Stokes"
---

*Janela pesquisada: 24 a 28/11/2026 para os temas 1 a 4 e 21 a 28/11/2026 para o tema 5. Nos temas 1 e 3 não houve novidade verificada nas últimas 48 horas. Os itens 2.1, 2.2 e 4.1 são de junho, e o 5.1 é de outubro: entraram porque ainda não tinham sido publicados nesta newsletter, e a data de cada um aparece no texto. Excluídos por já terem sido cobertos: o preprint de Alpöge e Buckmaster sobre Navier–Stokes (20/11), a alegada prova de Riemann, o Gemma 4 12B, a Semana de IA do Serpro e o Microsoft Agent Framework. Excluídos por estarem fora da janela de 7 dias: o contraexemplo da conjectura de Jacobian (julho), a formalização de Fermat pela Anthropic (setembro) e o anúncio original da OpenAI sobre Navier–Stokes (setembro).*

## Destaques do dia

1. **Dia fraco em novidades verificadas**: as buscas dos temas 1 a 4 não encontraram anúncio datado das últimas 48 horas com fonte primária; os itens abaixo são de junho e de outubro e estão datados. → 2.1, 2.2, 4.1
2. **GLM-5.2 abre pesos de um modelo de código com contexto de 1 milhão de tokens**: licença MIT e pesos no Hugging Face, mas os números de benchmark são autodeclarados. → 2.1
3. **Kimi K2.7 Code traz um modelo aberto de código com 1 trilhão de parâmetros**: a Moonshot diz usar 30% menos tokens de raciocínio que o K2.6, e a checagem independente ainda é limitada. → 2.2
4. **Anthropic fecha alianças com DXC e TCS para levar Claude a setores regulados**: as parcerias incluem produtos de serviços de TI e acesso antecipado a novos modelos. → 4.1
5. **Preprint aponta descasamento entre a prova Lean e o texto da OpenAI sobre Navier–Stokes**: os autores dizem que a versão formal não corresponde fielmente ao artigo, mas não concluem que a prova esteja errada. → 5.1
6. **Tema 5 não tem nada novo na janela de 7 dias**: o único item é uma verificação de outubro, e os anúncios de julho e setembro seguem sem checagem independente concluída. → 5.1

## 1. Novidades de IA agêntica

*Nenhuma novidade verificada nas últimas 24 a 48 horas. A única notícia datada de novembro encontrada, sobre uma plataforma de orquestração de agentes da Red Hat (12/11), aparece em um único site de notícias, sem o anúncio oficial. Por isso não foi incluída; vale checar o comunicado da empresa antes de tratá-la como fato.*

## 2. Ferramentas e modelos open source

### 2.1 GLM-5.2, da Z.ai: modelo aberto para código e agentes de longa duração
**Fonte:** [Modelo no Hugging Face (zai-org/GLM-5.2)](https://huggingface.co/zai-org/GLM-5.2) (16/06) · [VentureBeat](https://venturebeat.com/technology/z-ais-open-weights-glm-5-2-beats-gpt-5-5-on-multiple-long-horizon-coding-benchmarks-for-1-6th-the-cost) (junho)

O GLM-5.2 é um modelo de pesos abertos da Z.ai, voltado a programação e a tarefas de agentes que rodam por muito tempo. Segundo a cobertura da época, ele tem cerca de 744 a 753 bilhões de parâmetros (as fontes divergem), contexto de 1 milhão de tokens e licença MIT, que permite uso comercial. A API é citada a US$ 1,40 por milhão de tokens de entrada e US$ 4,40 por milhão de saída. Por que importa: para quem estuda agentes de código, é um modelo grande que pode ser baixado, avaliado e comparado com sistemas fechados. Em aberto: os resultados de benchmark vêm do próprio laboratório, e a data de lançamento aparece como 13, 16 ou 17 de junho conforme a fonte. Não consegui abrir o cartão do modelo nesta execução; os números devem ser confirmados nele antes de uso acadêmico.

### 2.2 Kimi K2.7 Code: modelo aberto de programação com 1 trilhão de parâmetros
**Fonte:** [The Decoder](https://the-decoder.com/moonshots-open-model-kimi-k2-7-code-undercuts-gpt-5-5-and-claude-by-up-to-12x-on-price-per-token/) (12/06) · [GIGAZINE](https://www.gigazine.net/gsc_news/en/20260615-kimi-k2-7-code) (15/06)

A Moonshot AI publicou o Kimi K2.7 Code como modelo aberto de programação, com pesos no Hugging Face. É um MoE de 1 trilhão de parâmetros, com cerca de 32 bilhões ativos por token e janela de contexto de 256 mil tokens. A empresa diz que o modelo gasta 30% menos tokens de raciocínio que o K2.6, que continua sendo o modelo geral da linha. Os ganhos de benchmark, como +21,8% no Kimi Code Bench v2, são da própria empresa; em 15/06, o modelo ainda não tinha sido submetido às suítes públicas padrão. Por que importa: é um exemplo de modelo aberto que compete em custo por tarefa de programação, o que interessa a quem roda agentes localmente ou em infraestrutura própria. Em aberto: a verificação independente.

## 3. IA aplicada no setor público

*Nenhuma novidade verificada nas últimas 24 a 48 horas. As buscas sobre IA no governo brasileiro trouxeram a II Semana de IA do Serpro (4 a 6/11), o simpósio no Ceará (9 e 10/11) e o curso gratuito do Serpro (aulas a partir de 17/11), todos já cobertos em edições anteriores, além da pesquisa do Cetic.br de julho. Nenhum deles é novidade de regulação ou de contratação.*

## 4. IA aplicada em geral

### 4.1 Anthropic fecha alianças com DXC e TCS para IA em setores regulados
**Fonte:** [Anthropic: aliança com a DXC](https://anthropic.com/news/dxc-anthropic-alliance) (11/06) · [Anthropic: parceria com a TCS](https://anthropic.com/news/tcs-anthropic-partnership) (11/06) · [TechCrunch](https://techcrunch.com/2026/06/11/anthropic-taps-tcs-to-scale-its-enterprise-ai-deployments/) (11/06)

A Anthropic anunciou duas alianças plurianuais com grandes empresas de serviços de TI, a DXC Technology e a Tata Consultancy Services (TCS). A DXC vai integrar o Claude à plataforma OASIS, que ela lançou em abril para serviços gerenciados. A TCS criará uma unidade de negócio dedicada a serviços por setor, com acesso antecipado a novos modelos da família Claude. As duas empresas citam setores regulados, como seguros, bancos e saúde, como motivo principal. Por que importa: a disputa agora se dá menos pelo modelo e mais por quem o implanta dentro de grandes empresas, e essas alianças mostram a rota de distribuição. Em aberto: os resultados em clientes ainda não foram publicados. Por se tratar de anúncio de empresas, a leitura deve separar o que é compromisso comercial do que foi demonstrado em uso real. A data é de junho, e o item entrou porque não tinha sido coberto antes.

## 5. Ciência e descobertas com IA

### 5.1 Preprint de Cambridge e King's College aponta descasamento entre a prova Lean e o texto da OpenAI sobre Navier–Stokes
**Fonte:** [arXiv:2610.08144](https://arxiv.org/abs/2610.08144), preprint de 06/10 · [King's College London](https://www.kcl.ac.uk/news/openais-navier-stokes-proof-called-into-question) (data da nota não confirmada)

Este item é um desdobramento de verificação do anúncio da OpenAI de uma prova de Navier–Stokes, feito em setembro, e fica fora da janela de 7 dias, por isso aparece aqui como contexto e não como novidade do dia. O que foi demonstrado: Alexander Bastounis (King's College London), Fabian Circelli e Anders C. Hansen (Cambridge) compararam a formalização em Lean, gerada com IA, com o artigo em linguagem natural e encontraram pontos em que as duas versões fazem afirmações diferentes, com o Lema 8.6 como exemplo. A conclusão deles é que a formalização não corresponde fielmente ao texto. O que continua em aberto: eles não afirmam que a prova em linguagem natural esteja errada nem que o teorema seja falso. Estado de verificação: preprint, sem revisão por pares. O papel da IA foi o de gerar tanto a prova quanto a formalização, e a checagem humana do texto ainda é a parte pendente. Crítica de Terence Tao ao método, citada pela imprensa, vai na mesma direção. Por que importa: compilar em Lean não basta se o enunciado formal não é o do texto.
