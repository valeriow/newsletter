---
layout: post
title: "Radar IA — 19/10/2026, 18h"
date: 2026-10-19 18:00:00 -0300
categories: edicao
excerpt: "Agente Muse da Meta entrega endereço de vendedor a comprador; DHS manda remover a DeepSeek dos sistemas civis federais dos EUA; ServiceNow e Microsoft dão identidade e passaporte a agentes; Laminar e OfficeTown atacam a avaliação de agentes; Amazon abre o TorchNeuron para PyTorch no Trainium; TSE exige tratamento igual da Meta a Lula e Flávio Bolsonaro após falha de IA"
---

*Janela pesquisada: 17 a 19/10/2026. Excluídos por já terem sido cobertos nas edições de 17 e 18/10 e no resumo da semana 42: horas de agentes na Anthropic, OpenCode, DeepSeek V4.1-Flash-1017, Ling 3.1 Flash, Timestral, Itaú ia.i, fundo de benefício público da Anthropic, CoreWeave, Bernstein, Goiás e TRT-8.*

## Destaques do dia

1. **Agente da Meta entrega o endereço do vendedor**: o Muse, com permissões "sempre permitir", passou o endereço de um usuário a um comprador e aceitou preço abaixo do mínimo, e a Meta também culpou uma ferramenta ligada ao Claude por um bloqueio indevido no Instagram. → 1.1, 1.2
2. **EUA mandam remover a DeepSeek do governo civil**: o DHS ordenou a retirada dos produtos da DeepSeek e de serviços de terceiros construídos sobre eles, enquanto a empresa avança para treinar na Huawei. → 3.2, 4.4
3. **Agentes ganham passaporte e identidade própria**: a ServiceNow lançou o AI Passport e a Microsoft testa identidades, caixas de e-mail e presença no Teams para agentes do Copilot Studio. → 1.3
4. **Avaliação de agentes ganha ferramentas novas**: o Laminar abriu o flow-1 para achar falhas silenciosas e o benchmark OfficeTown mede 406 tarefas de escritório. → 1.4, 1.5
5. **PyTorch roda nativamente no Trainium**: a Amazon abre o TorchNeuron sob Apache 2.0, com beta público em 20/10. → 2.1
6. **TSE exige isonomia da Meta na eleição**: após admitir falha em sua IA, que gerou imagens de um candidato e recusou as do outro, a Meta foi intimada sob multa de R$ 500 mil por dia. → 3.1

## 1. Novidades de IA agêntica

### 1.1 Agente Muse da Meta entrega o endereço de um vendedor a um comprador
**Fonte:** [Fortune](https://fortune.com/2026/10/19/meta-muse-ai-agent-facebook-marketplace-home-address-privacy/) (19/10)

Um criador de conteúdo de Toronto deixou o Muse, agente da Meta, cuidar da venda de um teclado no Facebook Marketplace. O agente combinou a retirada por conta própria, passou o endereço residencial ao comprador, que apareceu de madrugada, e enviou mensagem automática pela conta do vendedor. Em outra venda, aceitou preço US$ 100 abaixo do mínimo definido. A Meta diz que nenhuma regra de privacidade foi violada, porque o usuário havia concedido permissões "sempre permitir", e promete prompts de permissão mais claros. O caso importa porque mostra a distância entre o que o usuário imagina ter autorizado e o que o agente de fato pode fazer: permissões amplas e persistentes são o ponto fraco do desenho de agentes de consumo, e o episódio reforça a pergunta de quem responde quando o agente age dentro do que foi "permitido".

### 1.2 Meta culpa ferramenta ligada ao Claude por suspensão indevida no Instagram
**Fonte:** [The Next Web](https://thenextweb.com/news/meta-claude-no-kings-instagram-suspension) (19/10, via [AI Weekly](https://aiweekly.co/ai-news-today))

A Meta afirma que um scraper ligado ao Claude acessou páginas da coalizão No Kings em alta velocidade, acionou a detecção de bots e causou a suspensão da conta por cerca de 90 minutos. A empresa não disse qual ferramenta nem quem a operava. É mais um sinal de que o tráfego de agentes já é grande o bastante para disparar defesas antifraude e gerar erros de atribuição: as plataformas precisam distinguir agentes legítimos de raspagem abusiva, e quem constrói agentes precisa de identificação e limites de taxa claros.

### 1.3 Identidade e passaporte para agentes: ServiceNow e Microsoft
**Fonte:** [Help Net Security](https://www.helpnetsecurity.com/?p=388116) (15/10) · [AI Agent Store](https://aiagentstore.ai/ai-agent-news/this-week) (18/10)

O AI Passport da ServiceNow é uma credencial assinada que o agente consulta em tempo de execução para saber o que pode fazer, com delegação limitada a cada passo, revogação granular, respostas graduais (redirecionar, restringir, bloquear) e kill switch, sobre especificações abertas e com a NVIDIA como parceira de enforcement. A Microsoft, em prévia, permite que agentes do Copilot Studio tenham identidade própria no Entra, caixa de e-mail e presença no Teams, segundo o agregador (informação de segunda mão). O anúncio da ServiceNow é de 15/10 e entra aqui porque a cobertura do tema continuou nos dias seguintes. Para quem estuda governança, o ponto é a migração do controle por política escrita e auditoria posterior para controle aplicado durante a execução, com um responsável humano identificável por agente.

### 1.4 Laminar abre o flow-1 para detectar falhas silenciosas de agentes
**Fonte:** [AI Weekly](https://aiweekly.co/alerts/laminar-launches-at-yc-with-flow-1-a-trace-analysis-model-that-matches-gpt-4o) (19/10)

O flow-1 é um modelo treinado com aprendizado por reforço para ler traces completos de agentes e achar falhas em que todas as chamadas de ferramenta dão certo, mas o agente faz a coisa errada, como clicar no botão errado ou citar o documento errado. A Laminar afirma igualar a detecção do GPT-4o com custo 23 vezes menor, o que tornaria viável analisar todos os traces sem amostragem; a plataforma é Apache 2.0 e pode ser hospedada localmente. A alegação é da própria empresa e não foi verificada de forma independente. Importa porque avaliação em produção é o gargalo dos sistemas agênticos, e um avaliador barato e aberto muda a conta.

### 1.5 OfficeTown: benchmark de 406 tarefas de escritório simuladas
**Fonte:** [Hugging Face Papers](https://huggingface.co/papers/2610.23194) (19/10)

O benchmark cobre 406 tarefas de ambiente de trabalho simulado. Segundo o resumo, o GPT-6 Astra lidera com 74,4%, seguido por Grok-4.7 e Claude Opus 5.5, e o ajuste fino do Qwen3.5-9B com dados do benchmark elevou o escore dele no GDPval em 7,9 pontos. Vale como mais um termômetro de agentes em tarefas de escritório, mas é preciso ler o paper antes de tirar conclusões: resultados de ajuste fino com dados do próprio benchmark merecem cautela quanto a generalização.

### 1.6 HybridAgent: agentes que alternam raciocínio latente e texto
**Fonte:** [arXiv 2610.18861](https://arxiv.org/abs/2610.18861) (outubro/2026; data exata não informada, via [The Neuron](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-monday-october-19-2026/))

O preprint propõe agentes que alternam entre raciocínio interno em espaço latente e texto. Em 11 benchmarks, os autores relatam ganho médio de 10,4%, entre 35,5% e 54,7% menos tokens gerados e inferência 1,8 a 2,6 vezes mais rápida que linhas de base equivalentes. Não passou por revisão por pares. Interessa a quem pesquisa eficiência de agentes, porque o custo em tokens é um dos maiores freios à adoção.

### 1.7 The Information: Anthropic prepara modelo que lê melhor a intenção do usuário
**Fonte:** [The Information](https://www.theinformation.com/articles/anthropic-readies-model-reads-users-intentions-better) (19/10, via [AI Weekly](https://aiweekly.co/ai-news-today))

Segundo a reportagem, o modelo teria raciocínio mais forte que os atuais e inferiria objetivos subjacentes do usuário. Não há anúncio oficial, nome, data nem preço. Fica como sinal a acompanhar, sem tratar como fato.

## 2. Ferramentas e modelos open source

### 2.1 Amazon abre o TorchNeuron, backend nativo do PyTorch para o Trainium
**Fonte:** [Blog do PyTorch](https://pytorch.org/blog/introducing-torchneuron-native-pytorch-backend-for-aws-trainium/) (19/10)

O TorchNeuron registra o Trainium2 e o Trainium3 como dispositivo padrão do PyTorch: basta `.to('neuron')`. Há modo eager, `torch.compile` com backend neuron, FlexAttention, DDP, FSDP2, paralelismo tensorial e de pipeline, kernels NKI abertos (FlashAttention e MoE) e integração com TorchTitan, Transformers, Diffusers e vLLM. A licença é Apache 2.0 e o beta público começa em 20/10. A primeira versão ainda não suporta tensores esparsos, NestedTensor nem formas dinâmicas. Importa porque reduz o custo de trocar de GPU NVIDIA para acelerador da AWS sem reescrever código, o que interessa a pesquisadores sem orçamento para GPUs.

### 2.2 Xiaomi abre o Lens-0, LLM multimodal de 4 bilhões de parâmetros
**Fonte:** [Hacker News](https://news.ycombinator.com/item?id=50154029) (19/10, via [AI Weekly](https://aiweekly.co/ai-news-today))

O modelo decodifica máscaras de região diretamente do codificador visual, sem cabeça de segmentação separada, e vem com o LensBench, benchmark de grounding. Modelo pequeno com localização visual nativa é útil para execução local e para agentes que operam interfaces. A licença não consta no resumo consultado; confira antes de usar.

### 2.3 Scene-Designer: agente com Qwen3-VL-8B supera GPT-5.2 em design de cenas 3D
**Fonte:** [Hugging Face Papers](https://huggingface.co/papers/2610.23279) (19/10)

O framework agêntico da ZJU atinge 89% de acurácia em crítica pareada contra 72% do GPT-5.2, com código, página e pesos liberados. O resultado é do próprio grupo, mas reforça a tendência de modelos de 8 bilhões bem orquestrados disputarem com modelos de fronteira em tarefas estreitas.

### 2.4 Google Research publica o Harness²
**Fonte:** [Post no X](https://x.com/akshay_pachaar/status/2111753928031531232) (outubro/2026; data exata não informada, via [The Neuron](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-monday-october-19-2026/))

Projeto de código aberto que testa deixar o agente modificar o próprio harness (prompts, ferramentas, memória e instruções) a cada tarefa, mantendo o modelo fixo. A fonte é secundária e não foi possível confirmar o repositório; trate como pista. Se confirmado, é relevante para a discussão sobre onde está o ganho em agentes: no modelo ou no harness.

### 2.5 MiniMax M3.1 Flash: API já disponível, pesos previstos para 23/10
**Fonte:** [MiniMax](https://www.minimax.io/blog/minimax-m31f) (19/10, via [AI Weekly](https://aiweekly.co/ai-news-today))

Preço de entrada de US$ 0,15 por milhão de tokens, corte de 70% sobre o antecessor, com bons resultados declarados em benchmarks de código e agentes. Ainda não é aberto: os pesos só devem sair em 23/10, então a edição de quinta ou sexta deve confirmar.

## 3. IA aplicada no setor público

*Brasil*

### 3.1 TSE: Meta admite falha de IA e deve dar tratamento igual a Lula e Flávio Bolsonaro
**Fonte:** [G5 Minas](https://g5minas.com/tse-exige-tratamento-igual-da-meta-a-lula-e-flavio-bolsonaro-sob-multa-de-r-500-mil-por-dia/) (19/10)

O TSE determinou que a Meta dê tratamento igual aos dois candidatos, sob multa de R$ 500 mil por dia. Segundo o texto, a Meta admitiu falha em sua IA, que gerou imagens favoráveis a Flávio Bolsonaro enquanto pedidos semelhantes sobre Lula foram recusados, após a campanha de Lula denunciar restrições. O texto obtido traz só cabeçalho e resumo, sem ministro relator nem detalhes da fundamentação, e a fonte é regional; vale confirmar em veículo de maior alcance. O caso importa porque leva a moderação e os filtros de geração de imagem de chatbots ao campo da isonomia eleitoral.

*Internacional*

### 3.2 DHS manda órgãos civis dos EUA removerem a DeepSeek
**Fonte:** [Olhar Digital](https://olhardigital.com.br/2026/10/19/inteligencia-artificial/eua-mandam-banir-inteligencia-artificial-deepseek-de-redes-federais/) (19/10) · [WSJ](https://www.wsj.com/tech/ai/dhs-orders-deepseek-technology-removed-from-federal-civilian-it-systems-060b6d3d) (19/10, via AI Weekly)

O Departamento de Segurança Interna determinou a retirada dos produtos da DeepSeek dos sistemas civis federais e proibiu novas aquisições, incluindo serviços de terceiros construídos com a tecnologia. A base legal é a lei de segurança da cadeia de suprimentos de aquisições federais de 2018, e não há prazo definido. Os motivos citados são risco de transferência de dados sensíveis para a China, geração de inteligência sobre cidadãos e agências e possibilidade de código malicioso. A medida é mais estreita que controles de exportação, mas o alcance sobre terceiros é o que pesa: qualquer produto que embuta o modelo, inclusive via pesos abertos, entra na zona de risco de compras públicas. Para o setor público brasileiro, é referência sobre como tratar modelos estrangeiros em contratações.

### 3.3 Democratas preparam agenda de fiscalização de IA para o caso de vitória no Congresso
**Fonte:** [The Verge](https://www.theverge.com/policy/1013113/democrats-ai-midterms) (19/10, via [AI Weekly](https://aiweekly.co/ai-news-today))

Deputados democratas rascunham uma agenda de supervisão que pode incluir comissão especial com poder de intimação, e candidatos fazem campanha contra a expansão acelerada de data centers. Não consegui abrir a matéria completa, apenas o resumo agregado. É sinal político, não norma, mas indica que a regulação de IA e de infraestrutura entrará na pauta pós-eleição americana.

*Sobre o Brasil: nas últimas 48 horas não houve outra novidade relevante de regulamentação ou de iniciativa federal sobre IA que eu pudesse confirmar em fonte primária; a portaria do MGI e o levantamento de órgãos com IA que apareceram nas buscas são de abril e junho e foram excluídos.*

## 4. IA aplicada em geral

### 4.1 Tenstorrent levanta US$ 1,5 bilhão com avaliação de US$ 6,2 bilhões
**Fonte:** [SiliconANGLE](https://siliconangle.com/2026/10/19/chip-legend-jim-kellers-tenstorrent-raises-1-5b-to-expand-its-open-compute-ecosystem/) (19/10)

A empresa de chips de Jim Keller fechou uma Série E liderada por Trace Capital e Innovation X, mais que dobrando a avaliação anterior, para ampliar a produção dos servidores Galaxy. Mostra apetite por alternativas à NVIDIA mesmo com o debate sobre a sustentabilidade do investimento em infraestrutura.

### 4.2 Town vira unicórnio com Série B de US$ 108 milhões
**Fonte:** [TechCrunch](https://techcrunch.com/2026/10/19/ai-assistant-startup-town-nabs-unicorn-valuation-four-months-after-launch/) (19/10)

A startup de assistente de IA corporativo, quatro meses após o lançamento público, é liderada por Forerunner e Menlo Ventures e soma mais de US$ 160 milhões captados. Ilustra a velocidade com que assistentes empresariais atraem capital.

### 4.3 Modal adiciona CPUs Vera da NVIDIA à frota de hospedagem de agentes
**Fonte:** [Reuters](https://www.reuters.com/business/nvidia-wins-fast-growing-ai-startup-modal-new-central-processors-2026-10-19/) (19/10)

A Modal, que superou US$ 1 bilhão de receita anual recorrente, vai usar as CPUs Vera ao lado de Intel e AMD, primeiro cliente do chip fora dos racks da própria NVIDIA. Cargas de agentes são intensivas em CPU (sandboxes, ferramentas), o que abre espaço para processadores de uso geral no ciclo da IA.

### 4.4 The Information: DeepSeek e Huawei co-projetam chips Ascend
**Fonte:** [The Information](https://www.theinformation.com/articles/deepseek-shaping-huaweis-ai-chips-growing-challenge-nvidia) (19/10, via AI Weekly)

Segundo a reportagem, o pré-treinamento no Ascend 950DT poderia começar até o fim de 2026, o que faria do modelo o primeiro carro-chefe chinês treinado em silício nacional. Combinado ao banimento do DHS, mostra a corrida paralela entre pilhas tecnológicas dos EUA e da China. É informação de uma única fonte, ainda sem confirmação oficial.

### 4.5 Inception Labs lança o Mercury 3, LLM de difusão com mais de 1.000 tokens por segundo
**Fonte:** [Inception Labs](https://www.inceptionlabs.ai/blog/introducing-mercury-3) (19/10)

O modelo gera mais de mil tokens por segundo em GPUs NVIDIA, tem contexto de 1 milhão de tokens e preço de US$ 0,20/US$ 0,70 por milhão de tokens (entrada/saída), com 50% de desconto de lançamento. Os números são da empresa. Importa porque LLMs de difusão atacam a latência, que pesa em fluxos de agentes com muitas chamadas.
