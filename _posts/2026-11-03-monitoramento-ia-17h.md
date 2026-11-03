---
layout: post
title: "Radar IA — 03/11/2026, 17h"
date: 2026-11-03 17:06:00 -0300
categories: edicao
excerpt: "Anthropic admite no S-1/A que pode estar perto do limiar de auto-aperfeiçoamento recursivo; 50 agentes GPT-6.1 Sol em Minecraft mostram os limites da coordenação; novo estudo calcula quando um agente deve pedir ajuda humana; vercel-labs/agent-desktop dá ao agente acesso à acessibilidade do sistema operacional; o NCSC britânico prevê malware de IA contra infraestrutura crítica até 2028; Marvell compra a Lumentum por cerca de US$ 115 bi enquanto a Apollo vê pouco efeito da IA na produtividade."
---

*Janela pesquisada: 01/11 a 03/11/2026. Excluídos itens já cobertos nas edições anteriores (Kimi K3.1 Pro, Serpro, GSA, Aramco/HUMAIN, Hippo, Prefix Executability, DeepSeek Super-Agent, entre outros). Observação: parte das fontes primárias (TechCrunch, CNBC) não pôde ser aberta nesta execução; os itens abaixo se apoiam no AI Daily Digest nº 201 e nº 202 e nos links oficiais que ele cita, e isso é indicado quando relevante.*

## Destaques do dia

1. **Anthropic diz que pode estar perto do limiar de auto-aperfeiçoamento recursivo**: o S-1/A, emendado em 02/11, relata receita de cerca de US$ 17 bi no trimestre e admite ter lançado modelos cujos saltos de capacidade não reconheceu na hora. → 1.1, 4.1
2. **Cinquenta agentes em Minecraft, sem resolver a comida**: o experimento Civ50 criou papéis e permissões, mas teve 34 mortes, e o GPT-6.1 Sol bateu o Claude Opus 5.5 por 6 a 1 no Mindustry. → 1.2
3. **Quando o agente deve pedir ajuda humana**: novo paper reporta custo 18–31% menor que heurísticas comuns, e outro benchmark mostra que o melhor modelo acerta só 59,4% em documentos de trabalho. → 1.3, 1.4
4. **Agentes ganham acesso aberto ao sistema operacional**: o agent-desktop, da Vercel, expõe a árvore de acessibilidade a agentes, e o Nasiko controla custo e permissões do runtime. → 2.1, 2.2
5. **Alerta britânico sobre IA ofensiva**: o NCSC considera altamente provável malware com IA em ataque de ransomware à infraestrutura crítica do Reino Unido até 2028, enquanto a Coreia do Sul propõe ₩ 4,7 tri para modelos próprios. → 3.1, 3.2
6. **Dinheiro grande e dúvida sobre retorno**: a Marvell compra a Lumentum por cerca de US$ 115 bi, e a Apollo não vê efeito de IA nas margens do S&P 493. → 4.2, 4.3

## 1. Novidades de IA agêntica

### 1.1 Anthropic admite em emenda ao S-1 que pode estar perto do limiar de auto-aperfeiçoamento recursivo
**Fonte:** [TechCrunch](https://techcrunch.com/2026/11/02/anthropic-warns-that-its-very-close-to-rsi-capability-aka-self-building-ai/) (02/11) · [Gizmodo](https://gizmodo.com/anthropic-claims-to-be-closing-in-on-recursive-self-improvement-2000834175) (03/11) · [CNBC](https://www.cnbc.com/2026/11/02/anthropic-ant-s-1-quarter-financials.html) (02/11)

A emenda ao formulário S-1 acrescenta que a empresa pode em breve atingir o limiar de auto-aperfeiçoamento recursivo (RSI) previsto na sua Política de Escalonamento Responsável, e que já lançou modelos cujos saltos de capacidade não foi capaz de reconhecer no momento. Nenhum modelo atual foi designado como acima do limiar. É relevante porque a frase aparece num documento regulatório sujeito a responsabilização legal, não num blog de pesquisa: para quem estuda avaliação de sistemas agênticos, indica que a medição de capacidade em tempo real continua sendo o ponto fraco. A cobertura é secundária, via digest; vale ler o texto original da SEC.

### 1.2 Civ50: cinquenta agentes GPT-6.1 Sol em Minecraft criam papéis e permissões, mas não resolvem a comida
**Fonte:** [Y Combinator no X](https://x.com/ycombinator/status/2115904922017579275) · [Hacker News](https://news.ycombinator.com/item?id=50296486) (02/11)

O YC Labs e a Olam Labs soltaram cinquenta agentes num mundo de sobrevivência por três horas: houve cerca de 5.900 mensagens, 34 mortes e uma divisão de papéis com emissão de permissões, mas a produção de alimentos não foi resolvida. Em sete partidas de Mindustry, enxames de GPT-6.1 Sol venceram enxames de Claude Opus 5.5 por 6 a 1, e o GPT também levou uma série de Bed Wars (6 a 3). O interesse está na coordenação emergente e em seus limites: comunicação abundante não garantiu planejamento coletivo. O harness seria aberto (yc-software/minecraft-agent-harness), mas o link não foi confirmado; um veículo falou em "centenas" de agentes, número que as demais fontes não sustentam.

### 1.3 "When Should AI Agents Ask?": quando escalar para um humano
**Fonte:** [arXiv 2610.41129](https://arxiv.org/abs/2610.41129) (02/11)

O artigo trata da decisão de um agente pedir ajuda em vez de seguir sozinho. Num benchmark sintético, reporta distância média de 0,07% para o custo ótimo e redução de custo de 18% a 31% frente a três heurísticas comuns. Como o ambiente é sintético, a transferência para tarefas reais é incerta, mas o enquadramento (custo de perguntar versus custo de errar) é útil para desenhar pontos de aprovação humana em sistemas agênticos.

### 1.4 Novos benchmarks: AGORA para documentos de trabalho e testes de agentes que reescrevem o próprio estado
**Fonte:** [arXiv 2606.24526](https://arxiv.org/abs/2606.24526) · [arXiv 2610.41905](https://arxiv.org/abs/2610.41905) · [arXiv 2610.40940](https://arxiv.org/abs/2610.40940) (02/11, via [AI Daily Digest nº 202](https://github.com/diclogic/ai-daily-digest/issues/202))

O AGORA reúne 362 perguntas sobre 9.664 documentos em oito coleções, e o melhor de oito modelos avaliados chega a 59,4% de acerto. Na mesma leva vieram um estudo sobre custo e completude de estruturas de recuperação para pedidos que exigem várias ferramentas, uma avaliação retrospectiva de agentes de previsão e um teste de agentes que reescrevem estado persistente para inferir regras nunca declaradas. Em conjunto, reforçam que a avaliação saiu do "passou ou falhou" para medir custo, trajetória e raciocínio sobre documentos reais.

### 1.5 Framework de "sono" do Google segue em debate: resultados só em modelos pequenos
**Fonte:** [arXiv 2606.03979](https://arxiv.org/abs/2606.03979) (discussão no Hacker News em 02/11)

O trabalho de Behrouz e Mirrokni propõe uma fase de consolidação inspirada no sono para aprendizado contínuo, mas os resultados aparecem apenas em modelos Llama e Qwen pequenos. Críticos apontam custo computacional alto e ausência de ganho de velocidade quantificado frente ao ajuste fino supervisionado comum. É um bom exemplo de ideia promissora ainda sem evidência de escala.

### 1.6 GPT-6.2 "Astra" aparece em relatórios de uso do Codex, sem anúncio da OpenAI
**Fonte:** [TestingCatalog](https://www.testingcatalog.com/gpt-6-2-astra-appears-codex-usage/) (02/11)

Uma entrada "gpt-6.2-astra" surgiu em detalhamentos de uso do Codex; a OpenAI não anunciou nada e ao menos uma tentativa de seleção retornou erro. Trate como indício, não como lançamento: serve apenas para acompanhar se um novo modelo chega nos próximos dias.

## 2. Ferramentas e modelos open source

### 2.1 vercel-labs/agent-desktop: CLI aberta para agentes operarem aplicativos pela árvore de acessibilidade
**Fonte:** [GitHub](https://github.com/vercel-labs/agent-desktop) (03/11)

Projeto em Rust sob Apache-2.0, com cerca de 10,5 mil estrelas (+2.275 no dia), que devolve ao agente referências a elementos da interface em vez de depender de casamento de pixels. Opera sem tela por padrão. O README avisa que os instantâneos podem capturar conteúdo privado e que alguns recursos variam por sistema operacional. Importa porque a acessibilidade é um caminho mais barato e determinístico que captura de tela para uso de computador por agentes.

### 2.2 Nasiko: runtime aberto que mede custo por harness e modelo e filtra permissões em MCP
**Fonte:** [GitHub Nasiko-Labs/nasiko](https://github.com/Nasiko-Labs/nasiko) (03/11)

Apache-2.0, em Rust, com cerca de 11,5 mil estrelas. Hospeda agentes A2A, oferece um gateway MCP com filtro de permissões e limites em cascata. Está na versão 0.1.0 e, ao conectar um agente, edita arquivos globais de configuração do usuário, o que pede cautela em ambientes compartilhados. Interessa a quem precisa de governança e contabilidade de custos em orquestração multiagente.

### 2.3 Heretic 2.0 troca a ablação clássica por ablação de posto arbitrário
**Fonte:** [GitHub, release v2.0.0](https://github.com/p-e-w/heretic/releases/tag/v2.0.0) · [Hacker News](https://news.ycombinator.com/item?id=50328567) (01/11)

A versão 2.0 dispensa localizar uma única direção de recusa e amplia o escopo, do "descensuramento" para reduzir bajulação, linguagem de enchimento e ajustar alinhamento emocional. As configurações da série 1.x deixam de funcionar. A licença é AGPL-3.0, e não MIT como um texto afirmou. Vale como ferramenta de pesquisa em interpretabilidade, com o lembrete de que remover recusas de modelos tem implicações de segurança.

### 2.4 Codync e doop: agentes de código no celular e canvas de design multiagente
**Fonte:** [GitHub leepokai/Codync](https://github.com/leepokai/Codync) · [GitHub kgoedecke/doop](https://github.com/kgoedecke/doop) (03/11)

O Codync permite conversar com agentes de código locais pelo iPhone ou terminal, via relé com criptografia ponta a ponta (instalador de Windows sem assinatura, login obrigatório). O doop é um canvas colaborativo em que humanos e agentes editam as mesmas pranchas por um servidor MCP com 42 ferramentas (AGPL-3.0; o README alerta que usar assinatura do ChatGPT por servidor de terceiros pode violar os termos da OpenAI). São sinais de que a interface do agente está migrando para fora do terminal.

## 3. IA aplicada no setor público

*Brasil*

Sem novidades reais nas últimas 24–48 horas além do que já foi coberto: a II Semana de IA Serpro ("IA Soberana"), que começa amanhã, 04/11, foi tratada na edição de 01/11, e o PL 2338/2023 continua em tramitação na Câmara, sem votação de plenário identificada nesta busca.

*Internacional*

### 3.1 NCSC britânico projeta malware com IA em ataque de ransomware à infraestrutura crítica até 2028
**Fonte:** [NCSC, avaliação "AI to 2027"](https://www.ncsc.gov.uk/report/impact-ai-cyber-threat-now-2027) (03/11)

O relatório State of the Cyber Nation julga altamente provável que malware com IA seja usado num ataque de ransomware à infraestrutura nacional crítica do Reino Unido até 2028, aponta a China como o desafio cibernético mais sofisticado e espera uso rotineiro de IA por Rússia e China. A avaliação complementar diz que o risco de curto prazo é sobretudo a aceleração de táticas existentes. Para gestores públicos, a mensagem prática é priorizar higiene básica e velocidade de correção. O relatório principal não foi acessado; a fonte linkada é a avaliação de apoio.

### 3.2 Coreia do Sul propõe orçamento recorde de ₩ 820,9 tri com ₩ 4,7 tri para modelos de linguagem nacionais
**Fonte:** [AI Daily Digest nº 202](https://github.com/diclogic/ai-daily-digest/issues/202) (02/11; sem fonte primária localizada)

A proposta para 2027 inclui ₩ 21,3 tri (cerca de US$ 16 bi) para semicondutores, IA física e data centers de IA, e ₩ 4,7 tri para modelos de linguagem domésticos; ainda depende do Legislativo. Para o debate brasileiro de IA soberana, é um parâmetro de escala do investimento estatal em modelos próprios.

### 3.3 OpenAI contrata o ex-secretário do Exército Dan Driscoll para "modernização de segurança nacional"
**Fonte:** [CNBC](https://www.cnbc.com/2026/11/03/openai-hires-dan-driscoll-national-security.html) · [Bloomberg](https://www.bloomberg.com/news/articles/2026-11-03/openai-says-former-army-secretary-dan-driscoll-to-join-company) (03/11)

Driscoll assume o cargo novo de conselheiro sênior para modernização de segurança nacional. As fontes divergem sobre quando ele deixou o Pentágono. O movimento mostra a porta giratória entre governo e laboratórios de IA, relevante para quem acompanha contratos e regulação de IA em defesa.

## 4. IA aplicada em geral

### 4.1 S-1/A da Anthropic: receita de cerca de US$ 17 bi no trimestre e compromissos de compute de ~US$ 895 bi
**Fonte:** [CNBC](https://www.cnbc.com/2026/11/02/anthropic-ant-s-1-quarter-financials.html) (02/11) · [AI Daily Digest nº 202](https://github.com/diclogic/ai-daily-digest/issues/202)

A emenda aponta prejuízo operacional de cerca de US$ 567 milhões no trimestre e cerca de US$ 895,4 bi em compromissos agregados de compute. Há ainda relato de que a abertura de capital ocorreria na semana de 16/11 e uma carta da Controladoria de Nova York pedindo adiamento por questões de segurança e governança. Os números são do digest; confirme no documento original.

### 4.2 Marvell compra a Lumentum por cerca de US$ 115 bi em ações
**Fonte:** [ServeTheHome](https://servethehome.com/marvell-to-acquire-lumentum-115-billion-optical-ai-connectivity) · [Quartz](https://qz.com/marvell-lumentum-acquisition-115-billion-all-stock-110226) · [SEC Form 425](https://www.sec.gov/Archives/edgar/data/0001835632/000119312526442723/d81187d425.htm) (02/11)

São 4,5 ações da Marvell por ação da Lumentum, com prêmio de 23,9%; o foco é interconexão óptica e lasers, reportados como esgotados até 2029. Fechamento esperado no primeiro semestre de 2028. O gargalo da IA continua migrando do chip para a conexão entre chips.

### 4.3 Apollo: sem efeito visível da IA em margens e receita por funcionário no S&P 493
**Fonte:** [AI Daily Digest nº 202](https://github.com/diclogic/ai-daily-digest/issues/202) (02/11, citando TechCrunch) · [SigNoz](https://newsletter.signoz.io/p/ai-isnt-replacing-sres-its-deskilling)

O economista-chefe da Apollo encontrou margens e receita por trabalhador estáveis fora das gigantes de tecnologia. Em paralelo, um texto defende que a IA "deprecia habilidades" de engenheiros de confiabilidade em vez de substituí-los. Contrasta com o ritmo de investimento e alimenta o debate sobre retorno.

### 4.4 Altman no ADIPEC: IA já supera cientistas na maior parte, mas humanos devem manter o controle
**Fonte:** [The National](https://www.thenationalnews.com/future/technology/2026/11/02/no-room-for-debate-over-human-control-of-ai-says-sam-altman/) (02/11)

Altman repetiu a alegação de ter resolvido um problema do Milênio, referente a um resultado de Navier-Stokes de setembro que é contestado; o matemático Tristan Buckmaster acusa fraude acadêmica e o Instituto Clay não concluiu a avaliação. Leia a declaração com esse contexto.

### 4.5 42AI sai do anonimato com US$ 62,5 mi para um modelo de mundo do comportamento humano
**Fonte:** [Unite.ai](https://www.unite.ai/42ai-secures-62-5m-in-seed-funding-for-behavioral-world-model/) · [Startup Fortune](https://startupfortune.com/israeli-startup-42ai-says-its-world-model-can-predict-human-behavior/) (02/11)

A startup israelense, em operação em 10 corretoras, afirma 98% de acerto, mas o número se refere a fluxos agregados; o F1 por direção fica entre 0,80 e 0,85. Boa parte do aporte veio de fundadores e investidor relacionado.

### 4.6 Rodadas e cortes: Salience Labs (US$ 125 mi), Marble Cognition (€ 3,35 mi) e demissões na Front
**Fonte:** [AI Daily Digest nº 202](https://github.com/diclogic/ai-daily-digest/issues/202) (02–03/11; sem fontes primárias)

A Salience, de chaveadores ópticos para clusters de GPU, levantou Série B liderada pela Bullhound; a Marble, de Munique, capta para agentes que aprendem como funcionários executam tarefas antes de automatizá-las; a Front, de atendimento com IA, corta vagas em número não divulgado. Dados sem confirmação primária.
