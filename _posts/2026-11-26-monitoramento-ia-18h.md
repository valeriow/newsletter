---
layout: post
title: "Radar IA — 26/11/2026, 18h"
date: 2026-11-26 18:00:00 -0300
categories: edicao
excerpt: "Relato sem confirmação de prova em Lean do girassol de Erdős–Rado; código Lean da alegada prova de Riemann é reproduzido, mas a revisão matemática mal começou; agentes sem novidade confirmada nas últimas 48 horas; modelos abertos sem lançamento datado; setor público e IA em geral sem notícia datada; coleta incompleta nesta edição"
---

*Janela pesquisada: 25 e 26/11 para os temas 1 a 4; 19 a 26/11 para o tema 5. Excluídos os itens já cobertos nas edições de 19 a 25/11 (prova de Riemann, disputa sobre Navier-Stokes, checagem dos artigos de matemática da OpenAI, entre outros). Esta é uma edição enxuta: a busca não encontrou novidades datadas e verificáveis nos temas 1 a 4.*

## Destaques do dia

1. **Relato sem confirmação de prova em Lean do girassol de Erdős–Rado**: uma newsletter diz que a OpenAI publicou preprint e formalização; não há página oficial nem revisão independente. → 5.1
2. **Código Lean da alegada prova de Riemann é reproduzido, mas a revisão matemática mal começou**: a certificação formal cobre o enunciado clássico, e isso não equivale a validar a ideia da prova. → 5.2
3. **Agentes de IA sem novidade confirmada nas últimas 48 horas**: as buscas só acharam lançamentos de semanas atrás, que ficaram de fora desta edição.
4. **Modelos abertos sem lançamento com data verificável**: as listas encontradas são de início de novembro ou não trazem data, e não foram usadas.
5. **Setor público e IA em geral sem notícia datada de 25 e 26/11**: a plataforma agêntica do governo federal, o Chat GOV.BR e o núcleo de Campinas seguem sem anúncio novo.
6. **Coleta incompleta nesta edição**: três domínios primários não puderam ser abertos nesta sessão, então os dados de algumas fontes vêm de trechos de busca e devem ser conferidos na origem.

## 1. Novidades de IA agêntica

*Nenhuma novidade confirmada nas últimas 24 a 48 horas. As buscas retornaram principalmente lançamentos de setembro a novembro de 2026, como a plataforma Imagine Enterprise, de IBM e Microsoft, anunciada em 10/11. Por estarem fora da janela, não entraram nesta edição.*

## 2. Ferramentas e modelos open source

*Nenhum modelo ou biblioteca aberta com data verificável nas últimas 48 horas. Listas de início de novembro (Kimi K3.1 Pro, Hy4, LongCat-2.5) e outras com Command A+, Mistral Medium 3.5 e Gemma 4 12B vieram sem data confirmada ou de fontes agregadoras. Como estão fora da janela ou não puderam ser checadas na página do Hugging Face, não foram incluídas.*

## 3. IA aplicada no setor público

*Sem notícia datada de 25 ou 26/11. Permanecem em acompanhamento, sem item: a plataforma agêntica planejada pelo governo federal, o Chat GOV.BR, citado em entrevista sem data de lançamento, e o núcleo de IA em Campinas, com investimento de R$ 60 milhões anunciado em maio e operação prevista para o fim de 2026.*

## 4. IA aplicada em geral

*Sem novidade confirmada nas últimas 48 horas. Os anúncios corporativos encontrados, como a plataforma de agentes da IBM com a Microsoft (10/11) e as novidades de agentes para atendimento e compras, são de datas anteriores à janela.*

## 5. Ciência e descobertas com IA

### 5.1 Relato sem confirmação: OpenAI diz ter provado em Lean uma versão do girassol de Erdős–Rado
**Fonte:** [Newsletter Singularity Unlocked (Substack)](https://patmcguinness.substack.com/p/singularity-unlocked) (24/11, relato não verificado)

O que foi afirmado: um preprint e uma formalização em Lean 4 de uma prova do teorema do girassol de Erdős–Rado na versão de número fixo de pétalas, isto é, que famílias suficientemente grandes de conjuntos de k elementos contêm um girassol. Segundo o relato, o Lean verifica a existência de uma constante, mas a fórmula explícita da dependência dos parâmetros não está formalizada, e o texto ainda não foi revisado por matemáticos externos. Quem afirma: o próprio relato atribui a afirmação à OpenAI, mas não encontrei página oficial da empresa nem o preprint em repositórios como arXiv ou no catálogo de preprints de matemática da OpenAI. Estado de verificação: nenhum; há só um relato de newsletter, de tom promocional. Papel da IA: não descrito com detalhe. O que continua em aberto: se o preprint existe, se a formalização prova exatamente o enunciado da conjectura, se a versão provada é a fraca ou a completa, e qual é o papel da IA na descoberta. Não confundir com o trabalho de Bucić, He e Lee sobre a conjectura de Erdős–Szemerédi, que tem formalização própria em Lean (arXiv:2610.26686), mas não é da OpenAI.

### 5.2 Código Lean da alegada prova de Riemann é reproduzido por terceiros; a revisão matemática mal começou
**Fonte:** [DEV Community, "The Lean Check"](https://dev.to/mihai_leanzero/claude-riemann-hypothesis-proof-the-lean-check-35m3) (25/11) · [riemannhypothesisclaude.org](https://riemannhypothesisclaude.org/) (atualização de 25/11, lida só por trecho de busca)

O que foi demonstrado, até aqui: segundo as fontes encontradas, Levent Alpöge, matemático da Anthropic, publicou em 20/11 uma nota dizendo que ele e o Claude tinham encontrado uma prova, liberada como código Lean, sem artigo. Em 21/11, a Lean FRO e a Mathlib Initiative certificaram que o código prova o enunciado clássico da hipótese de Riemann; a versão generalizada ficou de fora, como já comentado na edição de 24/11. Na atualização mais recente que encontrei, dezenas de pessoas teriam reproduzido o mesmo export bruto do código. Quem afirma: o autor da nota e o Claude, segundo ele; a certificação é da comunidade Lean. Estado de verificação: checagem formal por máquina do código, que compila; a explicação matemática das ideias da prova ainda não foi publicada em forma de artigo e a revisão por especialistas independentes, segundo a fonte, está apenas começando. Papel da IA: o relato diz que a prova foi feita com Claude, mas o grau de autonomia e a orientação humana não estão detalhados. O que continua em aberto: se o argumento está correto como matemática (o kernel do Lean confirma o código, não a ideia), se a formalização corresponde exatamente ao enunciado da hipótese de Riemann, e se o resultado sobrevive ao escrutínio de quem trabalha na área. Reproduzir o código mostra que ele compila; não mostra que a estratégia está certa.

## Encerramento

Este episódio cobre apenas uma parte pequena do que circula nesta semana, porque a busca de hoje não achou novidades datadas e confirmadas nos temas de agentes, modelos abertos, setor público e IA em empresas. A edição escrita, com fontes e links, está no site do Radar IA.
