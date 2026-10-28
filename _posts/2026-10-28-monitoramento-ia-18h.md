---
layout: post
title: "Radar IA — 28/10/2026, 18h"
date: 2026-10-28 18:00:00 -0300
categories: edicao
excerpt: "Google lança o Gemini 4 Carbon e lidera o índice da Artificial Analysis; GitHub libera o Copilot Fusion para orquestrar vários modelos; Anthropic mostra exploits encadeados de modelo inédito e viés de deferência em analistas; falhas críticas em MLflow e no MCP Toolbox expõem a infraestrutura de agentes; Nvidia, Mistral e Google abrem modelos de fala, séries temporais e embeddings; Delaware, FAR e eleições americanas colocam agentes de IA no centro do debate regulatório"
---

*Janela pesquisada: 26 a 28/10/2026. Excluídos por já terem sido cobertos nas edições anteriores: caso Qwen3.8 da Cohere, S-1 da Anthropic, Cursor Agent SDK, GPT-6.1 Terra, WISeR, AMD/World Labs e as promessas de Lula sobre IA brasileira e data centers.*

## Destaques do dia

1. **Google lança o Gemini 4 Carbon**: modelo de US$ 2/US$ 10 por milhão de tokens assume o primeiro lugar no índice da Artificial Analysis, com 59 pontos. → 1.1
2. **GitHub libera o Copilot Fusion**: camada que roteia e orquestra vários modelos por prompt chega à disponibilidade geral e promete desempenho próximo ao topo com metade do custo. → 1.2, 1.7
3. **Anthropic expõe riscos de modelos e de pessoas**: um modelo inédito encadeou falhas em cinco sistemas operacionais, e analistas adotaram 86% das inclinações sugeridas pela IA. → 1.3, 1.4
4. **Infraestrutura de agentes sob ataque**: falhas críticas no MLflow e no MCP Toolbox do Google, mais o sandbox da Akamai, mostram que a segurança de agentes virou problema de plataforma. → 1.5, 1.6
5. **Modelos abertos de fala, séries temporais e embeddings**: Nvidia, Mistral e Google liberam pesos que cobrem transcrição em 48 idiomas, previsão e busca multimodal. → 2.1, 2.2, 2.3
6. **Agentes de IA entram na agenda regulatória**: Delaware discute empresas geridas por agentes, o Conselho da FAR avalia padrões para compras públicas e as eleições americanas aceleram a pauta. → 3.1, 3.2, 3.3

## 1. Novidades de IA agêntica

### 1.1 Google lança o Gemini 4 Carbon e assume a liderança do índice da Artificial Analysis
**Fonte:** [Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/) (28/10) · [AIWeekly](https://aiweekly.co/alerts/google-ships-gemini-4-carbon-tops-aa-intelligence-index-at-59) (28/10)

O Gemini 4 Carbon custa US$ 2 por milhão de tokens de entrada e US$ 10 por milhão de saída e marca 59 pontos no Artificial Analysis Intelligence Index v5, o que o coloca em primeiro lugar. Para quem constrói agentes, o relevante é a combinação de preço e posição no ranking: um modelo de fronteira nessa faixa de custo muda a conta de sistemas que fazem muitas chamadas por tarefa. Os números de ranking são de um agregador terceiro e conviria reproduzi-los em tarefas próprias antes de migrar cargas de trabalho.

### 1.2 GitHub Copilot Fusion chega à disponibilidade geral
**Fonte:** [GitHub Changelog](https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion/) (28/10) · [AIWeekly](https://aiweekly.co/alerts/github-ships-copilot-fusion-as-commits-jump-5x-to-74b) (28/10)

O Fusion é uma opção de modelo do Copilot que, em vez de escolher um único modelo, roteia cada prompt e coordena vários deles em três padrões: simples, cascata (um modelo barato rascunha e uma verificação decide se escala) e crítica (um rascunha, outro revisa). Há três níveis de esforço (Standard, High e Max), controles de administração por modelo e cobrança pelo preço de cada modelo subjacente. O GitHub afirma que o Fusion Max ficou a dois pontos do Claude Code com Opus 5.5 Max no Coding Agent Index, com cerca de metade do custo e 40% menos tempo; são números do fornecedor. O ponto de fundo é a consolidação da orquestração multimodelo como produto padrão, não como experimento.

### 1.3 Anthropic diz que modelo inédito encadeou falhas em cinco sistemas operacionais
**Fonte:** [The Hacker News](https://thehackernews.com/2026/10/anthropics-unreleased-ai-model-chains.html) (28/10) · [AIWeekly](https://aiweekly.co/alerts/anthropics-frontier-red-team-says-unreleased-claude-chained-flaws-into-working) (28/10)

O Frontier Red Team da Anthropic relata que um modelo ainda não lançado montou cadeias de exploração funcionais em cinco sistemas operacionais, com todas as falhas comunicadas aos fornecedores antes da correção. Para a comunidade de segurança e para quem avalia agentes, o dado reforça que capacidades ofensivas autônomas estão avançando e que a avaliação de risco precisa acompanhar cada geração de modelos. É um relato do próprio laboratório, sem verificação independente nas fontes consultadas.

### 1.4 Estudo da Anthropic: analistas adotaram 86% das inclinações sugeridas pela IA, mas só 15% citaram a IA como origem
**Fonte:** [Anthropic](https://www.anthropic.com/research/agents-judgment-calls) (28/10) · [AIWeekly](https://aiweekly.co/alerts/anthropic-analysts-matched-claudes-random-lean-86-of-the-time) (28/10)

Em um experimento com 50 analistas, a posição induzida pelo modelo, escolhida ao acaso, foi reproduzida em 86% dos casos, e apenas 15% dos participantes reconheceram a IA como fonte da inclinação. Para quem projeta fluxos com humano no circuito, a lição é que revisão humana não basta como salvaguarda se o revisor absorve o viés sem perceber; vale desenhar auditorias que comparem decisões com e sem sugestão do agente.

### 1.5 Falhas críticas no MLflow e no MCP Toolbox do Google
**Fonte:** [The Hacker Wire](https://www.thehackerwire.com/vulnerability/CVE-2026-116692/) (27/10) · [Strix](https://www.strix.ai/cve/CVE-2026-93328) (26/10) · [AIWeekly](https://aiweekly.co/alerts/critical-cve-in-googles-mcp-toolbox-exfiltrates-host-files) (28/10)

O CVE-2026-116692 (CVSS 9,8) permite execução remota de código no MLflow entre as versões 3.12.0rc0 e 3.17.0, corrigido na 3.17.0. O CVE-2026-93328 (CVSS 9,3) é uma travessia de caminho no MCP Toolbox, do Google, nas versões 1.2.0 a 1.4.0, corrigido na 1.5.0, que expõe arquivos do host. Ambos atingem peças comuns de pipelines de ML e de agentes baseados em MCP; quem os usa deve atualizar e revisar quais servidores de ferramentas estão acessíveis.

### 1.6 Akamai lança sandbox para código escrito por agentes
**Fonte:** [Rio Rundown](https://riorundown.substack.com/p/ai-news-oct-28-2026-agentic-ai-risks) (28/10, citando a Akamai)

O Agent Sandbox executa código gerado por agentes em ambiente WebAssembly restrito, bloqueando por padrão o tráfego de saída, mas permitindo chamadas a ferramentas e servidores MCP. O serviço é construído sobre o projeto aberto Spin, está em beta e vem junto de uma oferta de inferência compatível com a API da OpenAI para 12 modelos abertos. O movimento segue a tendência de tratar o isolamento de execução como requisito de produção para agentes, em linha com as falhas do item anterior.

### 1.7 Benchmark Dayjob: Tax mostra agentes ainda longe de tarefas profissionais completas
**Fonte:** [Surge AI](https://surgehq.ai/blog/dayjob-tax) (27/10) · [AIWeekly](https://aiweekly.co/alerts/claude-sonnet-55-tops-new-tax-work-benchmark-at-just-108) (28/10)

O Dayjob: Tax reúne 50 ambientes de trabalho tributário; o melhor resultado, do Claude Sonnet 5.5, foi de apenas 10,8% de aprovação. O dado contrasta com os ganhos em benchmarks de código e é útil como lembrete de que avaliações realistas de trabalho de domínio ainda expõem grandes lacunas, especialmente para quem pretende automatizar processos fiscais e contábeis.

### 1.8 Agentes de navegador erram o clique por um problema de escala de coordenadas
**Fonte:** [Towards Data Science](https://towardsdatascience.com/i-broke-a-browser-agent-on-purpose-spotting-the-fault-was-not-the-same-as-fixing-it) (28/10, via Rio Rundown)

O autor mostra que modelos recebem capturas de tela redimensionadas, mas devolvem coordenadas na janela original, fazendo os cliques caírem a cerca de três quartos do alvo; as correções elevaram a pontuação de um concurso de 31,0 para 57,0. É um caso didático de falha de integração, não de capacidade do modelo, e serve de checklist para quem depura agentes de uso de computador.

### 1.9 Axiom Math formaliza a classificação dos grupos simples finitos em Lean 4 em 24 dias
**Fonte:** [Axiom Math](https://cfsg.axiommath.ai/) (27/10) · [AIWeekly](https://aiweekly.co/ai-news-today) (28/10)

Segundo a Axiom, agentes de IA produziram uma formalização completa em Lean 4 da classificação dos grupos simples finitos em 24 dias. Se confirmado por revisão independente, mostra o potencial de agentes com verificador formal, onde a correção é checada mecanicamente, como caminho promissor para matemática e verificação de software.

## 2. Ferramentas e modelos open source

### 2.1 Nvidia abre o Nemotron 3.5 Transcribe e o dataset Granary v2
**Fonte:** [SiliconANGLE](https://siliconangle.com/2026/10/28/nvidia-releases-all-in-one-adaptable-nemotron-3-5-audio-transcription-and-translation-model/) (28/10) · [AIWeekly](https://aiweekly.co/alerts/nvidia-opens-30b-nemotron-35-transcribe-and-463k-hour-granary-v2-speech-dataset) (28/10)

Modelo de fala de pesos abertos com 30 bilhões de parâmetros em arquitetura de mistura de especialistas, para transcrição e tradução, acompanhado do Granary v2, com 463.062 horas em 48 idiomas. A liberação de dados em escala é tão relevante quanto o modelo, pois permite ajuste fino e avaliação em línguas menos atendidas.

### 2.2 Mistral abre a família Timestral de previsão de séries temporais
**Fonte:** [Hugging Face](https://huggingface.co/mistralai/Timestral-209M) (27/10) · [AIWeekly](https://aiweekly.co/alerts/mistral-opens-timestral-family-from-5m-to-209m-parameters) (27/10)

São quatro modelos de pesos abertos de 5 milhões a 209 milhões de parâmetros, o primeiro movimento da Mistral em séries temporais. Os tamanhos pequenos rodam em hardware modesto, o que os torna candidatos para previsão de demanda e monitoramento em ambientes sem GPU.

### 2.3 Google lança o EmbeddingGemma 2, embedder multimodal aberto
**Fonte:** [Hugging Face](https://huggingface.co/google/embeddinggemma-2) (28/10) · [AIWeekly](https://aiweekly.co/alerts/google-ships-embeddinggemma-2-744m-unified-multimodal-embedder) (28/10)

Com 744 milhões de parâmetros, cobre texto, imagem, áudio e vídeo em um espaço único de vetores. Para sistemas de RAG multimodal, reduz a necessidade de manter um embedder por modalidade.

### 2.4 Hy-Nomas 8B: modelo de mundo em vídeo que roda em uma RTX 4090
**Fonte:** [Hugging Face Papers](https://huggingface.co/papers/2610.36729) (27/10) · [AIWeekly](https://aiweekly.co/alerts/hy-nomas-ships-8b-interactive-world-model-on-a-single-rtx-4090) (27/10)

Modelo de mundo com atenção sensível a ações, pesos e código liberados, executável em GPU de consumo. Facilita pesquisa acadêmica em simulação interativa e robótica sem depender de clusters.

### 2.5 LEANN: índice vetorial aberto que troca armazenamento por recomputação
**Fonte:** [MarkTechPost](https://www.marktechpost.com/2026/10/27/leann-vector-index-mlsys-2026) (27/10)

Do laboratório Sky Computing de Berkeley, com licença MIT e base no FAISS, o LEANN guarda um grafo podado e recalcula embeddings na consulta, reduzindo um índice de 60 milhões de trechos da Wikipédia de 201 GB para 6 GB. O custo é latência: consultas do HotpotQA chegaram a 44,8 segundos em um M1 Ultra. Útil para busca local em dispositivos com pouco disco.

### 2.6 Qwen3.5-4B-3D-Coder: ajuste fino Apache 2.0 para gerar cenas Three.js
**Fonte:** [Hugging Face](https://huggingface.co/ccore/Qwen3.5-4B-3D-Coder) (28/10)

Projeto individual que especializa o Qwen3.5-4B em cenas 3D interativas, com versões quantizadas de 2,71 GB e 4,48 GB. Exemplo de nicho em que um modelo pequeno ajustado roda localmente.

## 3. IA aplicada no setor público

*Brasil*

Sem novidades relevantes nas últimas 48 horas além do que já foi coberto na edição de 26/10 (anúncios de Lula sobre IA nacional e data centers, repercutidos em 27/10); a busca não encontrou ato normativo, edital ou iniciativa nova de governo no período.

*Internacional*

### 3.1 Delaware discute "empresas de IA" geridas por agentes e recebe questionamento no Congresso dos EUA
**Fonte:** [Ars Technica via Rio Rundown](https://riorundown.substack.com/p/ai-news-oct-28-2026-agentic-ai-risks) (28/10)

O deputado James Comer alertou o governador Matt Meyer de que o projeto de "Artificial Intelligence Companies" poderia blindar os donos de responsabilidade por danos causados por IA; o comitê de supervisão da Câmara pediu documentos. O rascunho permitiria que agentes gerissem negócios em um sandbox regulatório de 30 meses, com o setor bancário excluído. O caso é um teste de quem responde juridicamente por agentes autônomos.

### 3.2 Especialistas pedem à FAR padrões para IA em licitações federais
**Fonte:** [Federal News Network via Rio Rundown](https://riorundown.substack.com/p/ai-news-oct-28-2026-agentic-ai-risks) (28/10)

Após decisão judicial que exigiu incluir avaliações geradas por IA nos registros administrativos do Exército, especialistas defendem divulgação das ferramentas usadas e verificação independente, em consulta cujo prazo foi 19/10. Interessa a quem acompanha compras públicas no Brasil, onde a Lei 14.133 também exige motivação e rastreabilidade das decisões.

### 3.3 Eleições americanas aceleram a pauta de regulação e a OpenAI monta centro de operações eleitorais
**Fonte:** [CFO Dive via Rio Rundown](https://riorundown.substack.com/p/ai-news-oct-28-2026-agentic-ai-risks) (28/10) · [Politico](https://www.politico.com/news/2026/10/28/openai-election-war-room-interference-01137690) (28/10)

Pesquisas indicam maiorias bipartidárias favoráveis a maior supervisão de IA, o senador Mark Warner pediu salvaguardas após relatos de agentes acessando contas bancárias e Califórnia e Nova York avançam com regras próprias. A OpenAI abriu um centro de operações para as eleições de 3 de novembro. Mostra a regulação sendo puxada por incidentes com agentes, não só por modelos.

### 3.4 Hospital Geral de Singapura reduz em 20% o tempo de laudo de hemorragias cerebrais com IA
**Fonte:** [Healthcare IT News via Rio Rundown](https://riorundown.substack.com/p/ai-news-oct-28-2026-agentic-ai-risks) (28/10)

O sistema iScreen sinalizou suspeitas em 3.475 tomografias durante dois meses de validação, com 97,2% de acurácia e cerca de 3,8 minutos por resultado, reduzindo em 20% o tempo médio de laudo dos casos positivos. Números reportados pela própria instituição, mas um exemplo concreto de triagem por IA em hospital público.

## 4. IA aplicada em geral

### 4.1 Claude Enterprise ganha relatórios inteligentes, pesquisas internas e orçamentos compartilhados
**Fonte:** [Unite.AI](https://unite.ai/anthropic-adds-smart-reports-surveys-pooled-budgets-to-claude-enterprise) (28/10)

Os Smart Reports analisam como uma equipe usa o Claude e quanto isso custa, com até 28 dias de dados e 10 relatórios gratuitos por mês; as Surveys coletam feedback dentro do app; e os orçamentos agrupados criam um teto mensal por equipe, com alertas a 50%, 75%, 95% e 100%. É governança de adoção e de custo, tema que as empresas passam a cobrar à medida que o uso de agentes escala.

### 4.2 Oracle AI World: ChatGPT e Codex dentro dos aplicativos de negócio da Oracle
**Fonte:** [OpenAI](https://openai.com/index/oracle-apps-in-chatgpt) (28/10) · [CryptoBriefing](https://cryptobriefing.com/oracle-magouyrk-sam-altman-ai-world/) (27/10)

Aplicativos e dados da Oracle serão integrados ao ChatGPT; a Oracle diz ter 130 mil usuários ativos do ChatGPT e 95 mil do Codex, e a preparação de pesquisas de recrutamento caiu de dois a quatro dias para 15 a 20 minutos (dados da empresa). Sinaliza a migração dos agentes para dentro de sistemas corporativos de registro.

### 4.3 Lloyds amplia agentes de IA na investigação de fraude em cartões de débito
**Fonte:** [FStech via Rio Rundown](https://riorundown.substack.com/p/ai-news-oct-28-2026-agentic-ai-risks) (28/10)

Teste de 90 dias com mais de 10,6 mil casos atingiu mais de 90% de acurácia nas decisões após 50 refinamentos, e os especialistas passaram a acessar metade dos sistemas durante as ligações. Um caso de agente em processo regulado, com iteração sobre o desempenho.

### 4.4 Nvidia e Oracle levam o Vera Rubin à escala de vários gigawatts
**Fonte:** [Nvidia](https://nvidianews.nvidia.com/news/nvidia-and-oracle-expand-nvidia-vera-rubin-to-multi-gigawatt-scale-and-bring-nvidia-vera-cpu-to-oracle-cloud-infrastructure) (28/10)

A OCI oferecerá sistemas Vera Rubin e CPUs Vera, permitindo escalar treino em GPU e tarefas de agentes em CPU de forma independente. Reflete a demanda por infraestrutura voltada a cargas agênticas, que consomem mais CPU que o treino.

### 4.5 Dropbox corta cerca de 6% da equipe e CTO deixa a empresa
**Fonte:** [Reuters](https://www.reuters.com/business/world-at-work/dropbox-plans-9-workforce-cut-technology-chief-exit-2026-10-28/) (28/10)

Cerca de 200 vagas serão cortadas, e o CTO Ali Dasdan sai em 18/11. A fonte não vincula o corte diretamente à IA, mas o episódio entra no pano de fundo da reestruturação de empresas de software.

### 4.6 Cognition recebe ofertas que a avaliariam em US$ 70 a 80 bilhões
**Fonte:** [FourWeekMBA](https://fourweekmba.com/ai-cognition-gets-70b-80b-offers-weeks-after-a-48b-round/) (28/10)

Segundo a publicação, as conversas são iniciais e ocorrem sete semanas após uma rodada a US$ 48 bilhões, o que indica o apetite por empresas de agentes de programação. Informação não confirmada por fonte primária.

### 4.7 Property Finder corrige viés de avaliação com anotação de especialistas no Amazon Bedrock
**Fonte:** [AWS Machine Learning Blog](https://aws.amazon.com/blogs/machine-learning/fix-evaluation-bias-to-unlock-better-models-on-amazon-bedrock) (28/10)

A empresa descobriu que 96,8% dos rótulos de avaliação eram herdados do modelo incumbente, criando viés circular; com 256 imagens anotadas por especialistas e otimização evolutiva de prompts, relata mais acurácia com 86% menos custo. É um bom estudo de caso sobre a qualidade do conjunto de avaliação.
