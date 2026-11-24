---
layout: post
title: "Radar IA — 24/11/2026, 18h"
date: 2026-11-24 18:00:00 -0300
categories: edicao
excerpt: "Claude Code recebe modo automático em provedores de nuvem, sem confirmação no changelog oficial; a certificação Lean da hipótese de Riemann cobre o enunciado clássico, e a versão generalizada ficou de fora; relato de 175 mil arquivos Lean compilados sem erro, com verificação independente do núcleo; compilar não basta, porque declarações com sorry também compilam; pesos abertos sem novidade verificada nas últimas 48 horas; setor público e empresas sem notícia datada no período"
---

*Janela pesquisada: 22 a 24/11/2026 (temas 1 a 4) e 17 a 24/11/2026 (tema 5). Ficaram de fora, por já terem sido cobertos nas edições anteriores, a certificação Lean da hipótese de Riemann (anúncio de 21/11, coberto em 23/11), a alegação de Navier-Stokes, o Nemotron for Science, o Claude Meetings, o computer use do Claude e a rodada da Sierra (23/11). Foi um dia de baixo volume: as buscas não trouxeram fontes primárias datadas nos temas 2, 3 e 4.*

## Destaques do dia

1. **Claude Code chega às versões 2.1.327 a 2.1.330 com modo automático em provedores de nuvem**: a ferramenta de programação com agentes ganha mais autonomia, mas a fonte ainda é agregadora e o changelog oficial não foi conferido. → 1.1
2. **Certificação Lean da hipótese de Riemann cobre o enunciado clássico**: a versão generalizada, que Alpöge também reivindica, não entrou na checagem pública, e as fontes divergem sobre o alcance. → 5.1
3. **Checagem mecânica em escala**: relato de 175 mil arquivos Lean compilados sem erro e de checagens independentes do núcleo, sem revisão humana publicada da demonstração. → 5.2
4. **Compilar não basta**: declarações marcadas com sorry também compilam, então a validade da prova depende de auditar as lacunas. → 5.2
5. **Pesos abertos sem novidade verificada**: a busca não achou lançamento datado nas últimas 48 horas, e as pistas (como o Kimi K3) ficaram sem data confirmada.
6. **Setor público e empresas sem notícia datada**: os temas 3 e 4 não trouxeram fonte primária no período; o que havia já saiu na edição de 23/11.

## 1. Novidades de IA agêntica

### 1.1 Claude Code chega às versões 2.1.327 a 2.1.330 com modo automático em provedores de nuvem
**Fonte:** [Releasebot — Anthropic (notas de versão)](https://releasebot.io/updates/anthropic) (22 a 23/11) · [ClaudeLog — notícias](https://claudelog.com/claude-news/) (22 a 23/11)

O Claude Code é o agente de programação da Anthropic, que roda no terminal, edita arquivos e executa comandos. As versões 2.1.327 a 2.1.330, publicadas entre 22 e 23 de novembro segundo os agregadores, trazem o modo automático em grandes provedores de nuvem e o login corporativo para planos Enterprise. O modo automático é relevante para quem estuda agentes porque mexe no ponto em que a supervisão humana costuma estar: em vez de confirmar cada ação, o usuário delega a decisão à ferramenta, dentro de regras de permissão. Isso aproxima o agente de uma execução com menos pontos de controle, o que torna mais importante a política de permissões e o registro das ações. O que não está claro é o escopo exato de quais ações são liberadas automaticamente, e as duas fontes são agregadoras que repetem as notas de versão. Vale conferir o changelog oficial da Anthropic antes de tratar o recurso como estável.

*Os demais lançamentos agênticos de 22 a 24/11 que apareceram nas buscas ou eram repetições de notícias já cobertas, ou vinham de fontes sem data verificável. Não foi possível localizar um artigo novo, dentro da janela, sobre orquestração multiagente ou avaliação de sistemas agênticos com fonte primária. Os artigos de arXiv encontrados são de julho e agosto de 2026.*

## 2. Ferramentas e modelos open source

*Nenhuma novidade verificada nas últimas 48 horas. As buscas encontraram pistas sem data confirmada: um relato da OfficeChai diz que a Moonshot publicou os pesos do Kimi K3 com crescimento recorde no Hugging Face, sem data no texto, e um rastreador cita um "Kimi K3.1 Pro" em 4 a 5 de novembro, fora da janela. Antes de citar qualquer um dos dois, confirme a data e a licença diretamente no Hugging Face da Moonshot.*

## 3. IA aplicada no setor público

*Brasil*

*Nenhuma notícia nova verificada nas últimas 48 horas. O que havia de mais relevante (a proposta de transformar o Ministério das Comunicações em pasta digital e o registro de modelos no Reino Unido) saiu na edição de 23/11. As buscas por novidades de 23 e 24/11 em portais de governo não retornaram nada datado.*

*Internacional*

*Nenhuma notícia nova verificada no período. Os casos de IA no setor público que apareceram nas buscas são de meses atrás ou são páginas de referência, sem novidade de 24 horas.*

## 4. IA aplicada em geral

*Nenhuma notícia nova verificada nas últimas 48 horas. As buscas por anúncios empresariais de 24/11 retornaram apenas páginas institucionais sem data, balanços de adoção sem fonte primária e parcerias já cobertas, como a Copilotforce e a Emerson com a Databricks. Não incluímos nenhum deles para não preencher a edição com conteúdo fraco.*

## 5. Ciência e descobertas com IA

*Janela de 7 dias. Foram buscados matemática, prova formal, física, biologia, química e materiais. Em matemática, o desdobramento de verificação da alegação sobre a hipótese de Riemann é o único com fonte datada no período. Em física, química, materiais e biologia, as buscas acharam só preprints e textos de divulgação sem data dentro da janela, e não entraram.*

### 5.1 Certificação Lean da hipótese de Riemann cobre o enunciado clássico; a versão generalizada ficou de fora
**Fonte:** [Neoteo — Lean FRO e Mathlib certificam a prova de Alpöge](https://www.neoteo.com/en/lean-fro-and-mathlib-initiative-certify-levent-alpoges-riemann-hypothesis-proof) (21/11) · [Wikipedia — Alpöge's proof of the Riemann hypothesis](https://en.wikipedia.org/wiki/Alp%C3%B6ge's_proof_of_the_Riemann_hypothesis) (consulta em 24/11) · [Espelho do repositório no GitHub](https://github.com/JGalego/riemann) (21/11)

Este item é um desdobramento da certificação de 21/11, já coberta em 23/11: o que muda é o alcance. Segundo as fontes, a comunidade Lean checou por máquina que o enunciado formalizado corresponde à hipótese de Riemann tal como definida no Mathlib, usando ferramentas de comparação de enunciados (comparator e con-leche). O ponto em aberto é a ampliação: Levent Alpöge afirma que o método também alcança a hipótese de Riemann generalizada, que é uma família de hipóteses mais forte, e a declaração pública não certifica essa ampliação. As fontes divergem sobre o que a formalização de fato prova. Uma delas diz que Elliot Glazer afirmou em 20/11 que a proposição formalizada seria a generalizada; a página de Andrew Sutherland, do MIT, é mais cautelosa e diz que o teorema principal é a hipótese de Riemann como definida no Mathlib.

Quem afirma é Levent Alpöge, pesquisador da Anthropic, que usou o Claude para escrever a formalização. O estado de verificação é este: checagem mecânica no Lean, com comparação de enunciado; ainda não há revisão publicada por especialistas independentes, e matemáticos afirmam que não entendem a demonstração. O papel da IA, segundo as fontes, foi o de ferramenta de escrita da formalização, sem detalhe público sobre quanto da ideia matemática veio do modelo. Por isso o título fala do enunciado certificado, e não da prova da hipótese. Segue em aberto, para fins de conferência independente, se a formalização corresponde à versão generalizada e qual é a argumentação matemática. A fonte primária (anúncio da Lean FRO e da Mathlib Initiative) não foi consultada diretamente nesta edição.

### 5.2 Checagem mecânica em escala: 175 mil arquivos compilam sem erro, mas compilar não basta
**Fonte:** [CASRAI — Anthropic, Alpöge e a alegação sobre a hipótese de Riemann em Lean](https://casrai.org/news/anthropic-levent-alpoge-claude-lean-riemann-hypothesis-claim-2026) (21 a 22/11, data aproximada) · [arXiv 2606.13925 — "Sorries Are Not the Hard Part"](https://arxiv.org/pdf/2606.13925) (preprint de junho, usado como referência metodológica)

Segundo o registro de verificação atribuído a Andrew Sutherland, do MIT, todos os 175.187 módulos do arquivo compilaram sem erro, e a demonstração passou por mais de uma checagem independente do núcleo do Lean. O arquivo é fixado na versão 4.33.1 do Lean e num commit específico do Mathlib. As estimativas de tamanho divergem (17 e 17,4 milhões de linhas, conforme a fonte). Isso é uma verificação forte de que o código é aceito pelo sistema, mas há um limite que o próprio campo conhece: o Lean aceita declarações fechadas com `sorry`, a marcação de lacuna, e um arquivo que compila pode conter teoremas incompletos. O preprint de junho sobre formalização semiautônoma mostra que o trabalho difícil costuma ser justamente auditar essas lacunas, e não o ato de compilar. Por isso a afirmação correta hoje é que o código compila e o enunciado principal confere com o do Mathlib, mas a auditoria completa de lacunas e a leitura humana da demonstração ainda não foram publicadas.

Quem afirma é a comunidade de verificação formal, a partir do registro de Sutherland, e a alegação original é de Alpöge. O estado é de verificação mecânica, sem artigo revisado por pares nem revisão por especialistas independentes publicada. O papel da IA é de ferramenta de formalização e escrita, sem informação pública de quanto do argumento matemático foi gerado pelo modelo. Em aberto: a leitura do argumento pelos especialistas, a auditoria das lacunas e a submissão a periódicos.
