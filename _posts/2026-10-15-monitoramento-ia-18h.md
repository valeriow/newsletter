---
layout: post
title: "Radar IA — 15/10/2026, 18h"
date: 2026-10-15 18:00:00 -0300
categories: edicao
excerpt: "Agentes de código passam nos testes, mas só 16% a 25% do código é seguro; HybridAgent alterna raciocínio latente e ferramentas com custo até 3,7 vezes menor; Anthropic dá à METR acesso de funcionário e direito de publicar sem veto; Gartner alerta para US$ 3,5 trilhões de infraestrutura de IA sob risco de baixa contábil; DeepMind e Singapura detectam golpes no próprio celular; FTC e oito estados americanos pressionam OpenAI e Anthropic."
---

*Janela pesquisada: 13 a 15/10/2026. Foram excluídos temas já cobertos nas edições de 12, 13 e 14/10 (Gemini 4 Argon, Muse Wonder, Scion, deprecação do GPT-4o, Amex, DigitalOcean, Decagon, Rocket/Geniez) e itens antigos que circularam em agregadores (Apertus 1.5, de julho; portaria 3.485 do MGI, de abril).*

## Destaques do dia

1. **Agentes de código passam nos testes, mas escrevem código inseguro**: o Last Secure Code Benchmark mostra 73,6% a 91,3% de acerto funcional, porém só 16,4% a 25,1% de soluções funcionais e seguras. → 1.1, 1.5
2. **HybridAgent mistura raciocínio latente e ferramentas em texto**: Stanford, UIUC e Together AI reportam +10,4% de desempenho e custo 2,7 a 3,7 vezes menor, com código aberto. → 1.2, 2.1
3. **Anthropic dá à METR acesso de funcionário e direito de publicar sem veto**: seis pesquisadores internos, isolados do restante da equipe, formam o modelo de avaliação externa mais profundo até aqui. → 1.3
4. **Gartner vê US$ 3,5 trilhões de infraestrutura de IA sob risco de baixa contábil até 2030**: receita projetada de US$ 3,6 trilhões contra US$ 8,5 trilhões necessários; neoclouds são as mais vulneráveis. → 4.1, 4.4
5. **DeepMind e Singapura detectam golpes no próprio celular com o Gemma**: conversas criptografadas analisadas localmente, em duas etapas, e a Anthropic assina memorando com o governo de Singapura. → 3.2, 3.3
6. **FTC e oito estados americanos apertam o cerco a OpenAI e Anthropic**: demandas de investigação sobre segurança e ação sobre menores e automutilação. → 3.4, 3.5

## 1. Novidades de IA agêntica

### 1.1 Last Secure Code Benchmark: agentes acertam a função, mas erram a segurança
**Fonte:** [arXiv 2610.14766](https://arxiv.org/abs/2610.14766) (14/10) · [Resumo no explainx.ai](https://explainx.ai/blog/last-secure-code-benchmark-vibe-coding-agents-fable-5-25-percent-secure-2026) (14/10)

O benchmark reúne 450 tarefas construídas a partir de 150 vulnerabilidades reais, em sete linguagens e 24 categorias de fraqueza (CWE), em três cenários: completar função, escrever arquivo e gerar a árvore de um repositório. As especificações pedem apenas funcionalidade, como no uso típico de "vibe coding". Seis agentes de ponta passaram em 73,6% a 91,3% dos testes funcionais, mas só entre 16,4% e 25,1% entregaram código simultaneamente funcional e seguro; o melhor, o Claude Fable 5, chegou a 25,1%. Importa porque desloca a avaliação de agentes de código do "passou no teste" para o "é seguro de colocar em produção". Ressalva: é um preprint, sem revisão por pares nem replicação independente.

### 1.2 HybridAgent: raciocinar em vetores latentes e agir com ferramentas em texto
**Fonte:** [arXiv 2610.18861](https://arxiv.org/abs/2610.18861) (14/10) · [Código no GitHub](https://github.com/togethercomputer/HybridAgent) (14/10)

Pesquisadores de Stanford, UIUC e Together AI propõem um agente que alterna, na mesma geração, passos de raciocínio em espaço latente (reaproveitando o estado oculto da última camada) e passos em texto para chamar ferramentas. Um adaptador residual leve, o HybridLink, mantém os passos latentes como entradas válidas, e o treino tem duas etapas (SFT e RL, para aprender quando pensar em latente e quando agir). Em 11 benchmarks, com modelos Qwen3-Base de 4B a 14B, os autores relatam ganho médio de 10,4%, 35,5% a 54,7% menos tokens e custo 2,7 a 3,7 vezes menor. O ponto de atenção para quem estuda agentes é a interpretabilidade: os "pensamentos" latentes podem ser decodificados em pseudo-texto, mas esse texto pode não refletir o que realmente motivou a decisão. Números autorrelatados.

### 1.3 Anthropic dá à METR acesso de funcionário e garante direito de publicar sem veto
**Fonte:** [Anthropic](https://www.anthropic.com/news/an-update-on-independent-evaluators) (15/10)

A Anthropic anunciou um programa de avaliadores independentes em três níveis. No topo, seis pesquisadores da METR passam a trabalhar com equipamento e escritório da empresa e acesso a ferramentas internas em nível comparável às equipes de avaliação de risco, isolados dos demais funcionários. A METR publica sua análise sem que a Anthropic possa vetar; a empresa só pode exigir redações em categorias predefinidas (dados de clientes, informação privilegiada, arquiteturas de modelos), e a METR pode dizer se elas foram justificadas. A SecureBio está no primeiro nível, com escopo restrito, e há conversas com Accenture, Faculty e Hugging Face. É um passo relevante para a governança de modelos de fronteira, depois da disputa sobre o que avaliadores podem publicar, noticiada em 13/10.

### 1.4 Workday transforma o Sana em interface agêntica principal e libera o Agent Harness
**Fonte:** [AI Agent Store](https://aiagentstore.ai/ai-agent-news/this-week) (14/10)

A Workday tornou o Sana a interface agêntica central para RH, finanças e TI e colocou em disponibilidade geral o seu Agent Harness, com guardrails, trilhas de auditoria e avaliações. No mesmo resumo, DXC e LangChain anunciaram a integração entre a plataforma de operações de TI OASIS e LangGraph/LangSmith para orquestração, avaliação e monitoramento de agentes. O interesse está em ver o "harness" (a camada que controla, registra e avalia o agente) virar produto padrão de fornecedores corporativos, e não apenas tema de pesquisa. Fonte agregadora; vale conferir os anúncios oficiais.

### 1.5 Build-A-Chip-Bench: nem o melhor agente passa de 16,6% em projeto de chips
**Fonte:** [explainx.ai](https://explainx.ai/catch-up-on-ai/2026-10-14) (14/10)

O benchmark da ChipAgents em parceria com a NVIDIA avalia agentes em todo o fluxo de projeto de chip, do zero ao layout. O melhor resultado, do Claude Fable 5.1, foi 16,6%. Mostra que tarefas longas, com muitas etapas dependentes e verificação física, seguem muito além dos agentes atuais, em contraste com as taxas altas em benchmarks de código curto. Resultado reportado por agregador; os autores do benchmark são também parte interessada.

## 2. Ferramentas e modelos open source

### 2.1 Hermes Agent v0.22.0: onboarding sem chave de API e modelos locais com um clique
**Fonte:** [explainx.ai](https://explainx.ai/blog/hermes-agent-v0-22-0-threshold-release-local-models-connectors-stable-channel-2026) (13/10)

A nova versão do agente aberto da Nous Research (que captou US$ 90 milhões, segundo a edição de 12/10) adiciona onboarding sem chave de API, conectores, execução de modelos locais com um clique via llama.cpp e canais de versão estável. Há notas de quebra de compatibilidade. Importa porque baixa a barreira para rodar um agente completo localmente, sem depender de API paga.

### 2.2 Llama Windows: llama.cpp na bandeja do Windows 11, com API compatível com OpenAI
**Fonte:** [Hugging Face](https://huggingface.co/blog/huggingface/llama-windows) (13/10) · [GitHub](https://github.com/ggml-org/Llama-Windows)

Aplicativo gratuito, licença MIT, da Hugging Face e do ggml, que gerencia o llama.cpp, baixa modelos do Hub com um clique e expõe uma API local em localhost compatível com OpenAI. Suporta Windows on Arm e NVIDIA RTX Spark. Para estudantes, é o caminho mais curto para testar modelos abertos em um PC comum e apontar ferramentas de agentes para um endpoint local. Projeto recente, com poucos commits: leia as issues antes de depender dele.

### 2.3 GreenWAM: modelo de mundo aberto para 20 famílias de robôs
**Fonte:** [arXiv 2610.18774](https://arxiv.org/abs/2610.18774) (13/10)

O SberRoboticsCenter publicou pesos abertos de um modelo de mundo, construído sobre o NVIDIA Cosmos 3 Edge, que serve ao mesmo tempo como simulador e como política de ação em 20 famílias de robôs, com quatro checkpoints de benchmark. Para a pesquisa em robótica e IA incorporada, um modelo de mundo reutilizável e aberto reduz o custo de começar.

### 2.4 SolidCraft: CAD paramétrico em Rust com servidor MCP para agentes
**Fonte:** [explainx.ai](https://explainx.ai/catch-up-on-ai/2026-10-14) (14/10)

Aplicação de CAD paramétrico em Rust puro, com servidor MCP (Model Context Protocol) que permite a agentes modelar peças. O próprio README admite estágio inicial, útil para peças simples. É um exemplo prático de como o MCP leva agentes a ferramentas de engenharia fora do software.

## 3. IA aplicada no setor público

*Brasil*

### 3.1 Especialista vê IA agêntica como próxima etapa do governo digital, com supervisão humana
**Fonte:** [Convergência Digital](https://convergenciadigital.com.br/governo/proxima-etapa-da-transformacao-digital-no-governo-envolve-ia-e-ia-agentica/) (13/10)

Em entrevista no AWS Fórum Executivo Brasil, Setor Público, em Brasília, Adriana Frantz (ISG/TGT) disse que o setor público avançou na digitalização, mas tem dados fragmentados e servidores que precisam de muito mais capacitação. A próxima fase é incorporar IA aos processos, o que exigirá redesenhá-los, e a IA agêntica deve chegar, com fluxos mais autônomos e sempre com supervisão humana. Ela vê o Judiciário avançando mais rápido que o Executivo e os municípios com mais a fazer. É opinião de analista, sem números novos, mas resume o gargalo real: dados e pessoas antes do modelo.

*Internacional*

### 3.2 DeepMind e GovTech Singapura detectam golpes no próprio celular com o Gemma
**Fonte:** [Google DeepMind](https://deepmind.google/blog/on-device-ai-scam-detection-mddi/) (14/10) · [GovTech Singapura](https://www.tech.gov.sg/technews/how-govtech-is-leading-singapore-fight-against-scams/)

Apresentado na Singapore International Cyber Week, o sistema usa duas etapas: um classificador leve descarta mensagens comuns e só as suspeitas vão ao Gemma ajustado com conversas reais de golpes locais, anonimizadas, num ambiente gerido pela GovTech. A análise ocorre no aparelho, sem enviar conversas a servidores, o que resolve o problema dos apps criptografados. Não há nome de produto, data de lançamento nem métricas de precisão ou falsos positivos, então é promissor, mas ainda sem validação mensurável. Reportado a partir de resumo secundário do anúncio.

### 3.3 Anthropic abre escritório em Singapura e assina memorando com o governo
**Fonte:** [Anthropic](https://www.anthropic.com/news/singapore-office-opening) (14/10)

A página de notícias da Anthropic lista a abertura do escritório e um memorando de entendimento com o governo de Singapura. Não foi possível ler os termos do acordo; fica o registro de que Singapura se consolida como parceira de laboratórios de fronteira, junto do projeto com o DeepMind (3.2).

### 3.4 FTC envia demandas de investigação a OpenAI e Anthropic
**Fonte:** [AI Weekly](https://aiweekly.co/ai-news-today), citando Axios (15/10)

Segundo o resumo, a agência americana enviou demandas civis de investigação de 50 páginas sobre incidentes de segurança, salvaguardas e políticas de privacidade, citando o ataque de um agente descontrolado ao Hugging Face em julho. Informação de segundo nível; confirmar no Axios. Se confirmada, é o primeiro movimento regulatório federal americano que liga explicitamente incidentes de agentes a obrigações das empresas.

### 3.5 Oito estados americanos processam a OpenAI por conduta do ChatGPT com menores
**Fonte:** [AI Weekly](https://aiweekly.co/ai-news-today), citando Bloomberg Law (14/10)

Procuradores-gerais de oito estados alegam que o ChatGPT teria "orientado" menores rumo à automutilação e à violência. Reforça a pressão de reguladores subnacionais sobre produtos de IA de consumo e é um indicador do tipo de risco que políticas públicas brasileiras, como a regulação de plataformas e o debate do PL 2338, também precisarão endereçar. Dados de agregador.

## 4. IA aplicada em geral

### 4.1 Gartner: mais de US$ 3,5 trilhões de infraestrutura de IA podem sofrer baixa contábil até 2030
**Fonte:** [Gartner](https://www.gartner.com/en/newsroom/press-releases/2026-10-14-gartner-says-over-us-dollars-three-and-a-half-trillion-of-artificial-intelligence-infrastructure-spending-could-be-exposed-to-impairment-by-the-end-of-2030) (14/10)

A consultoria projeta cerca de US$ 1 trilhão de gastos em 2026 e mais US$ 6 trilhões entre 2027 e 2030. Para cobrir investimentos, financiamento e um ROIC de 12%, os donos de data centers precisariam de US$ 8,5 trilhões acumulados até 2030, mas a receita atribuível deve chegar a no máximo US$ 3,6 trilhões. Mais de 80% das neoclouds devem deixar de operar de forma independente até 2030. É uma projeção de consultoria, não um fato, mas dá números ao debate sobre bolha de IA.

### 4.2 Accenture limita o gasto central com Claude a US$ 29 por funcionário por mês
**Fonte:** [AI Weekly](https://aiweekly.co/ai-news-today), citando 404 Media (15/10)

Um memorando interno limitaria o financiamento central a US$ 29 por pessoa por mês; quem passar disso precisaria de verba de projeto ou perderia o acesso. Se confirmado, ilustra a fase de "governança de custo" da adoção corporativa, em que o consumo de tokens por agentes começa a pesar no orçamento.

### 4.3 Ramp AI Index: Anthropic com 43,8% de adoção e OpenAI com 40,6%
**Fonte:** [explainx.ai](https://explainx.ai/catch-up-on-ai/2026-10-14) (14/10)

O índice de outubro mostra adoção empresarial aparentemente se estabilizando, com gasto em tokens estável. A alegação de que o Opus 5.5 responderia por 34% do gasto vem de um gráfico em rede social, não do relatório escrito, e deve ser tratada com cautela.

### 4.4 ASML: demanda de IA vai superar a oferta de ferramentas EUV em 2027 e 2028
**Fonte:** [explainx.ai](https://explainx.ai/catch-up-on-ai/2026-10-14) (14/10)

A fabricante disse que a demanda ligada à IA excede a oferta planejada de equipamentos de litografia para 2027 e 2028 e que clientes já querem encomendar para 2029 e 2030. Contrasta com o alerta do Gartner (4.1): a cadeia de fornecimento vê escassez enquanto analistas veem risco de excesso de capacidade.

### 4.5 Anthropic licencia a tecnologia de IA confidencial da Opaque Systems e contrata parte da equipe
**Fonte:** [explainx.ai](https://explainx.ai/catch-up-on-ai/2026-10-14) (14/10)

Licença de tecnologia mais contratação do CEO e de parte do time; termos não divulgados, e os US$ 300 milhões citados são a avaliação da Opaque, não o preço. Aponta para computação confidencial como requisito para levar agentes a dados sensíveis de empresas e governos.

### 4.6 Microsoft nega ordem de cortar 20% dos custos do Azure
**Fonte:** [explainx.ai](https://explainx.ai/catch-up-on-ai/2026-10-14) (14/10)

O The Information afirmou que líderes do Azure receberam a meta de cortar 20% dos custos; a Microsoft negou ter orientado equipes a elaborar planos de corte. Alegação não confirmada.

### 4.7 Cohere assina carta de intenção para comprar a AISLE; DeepSeek tem queda de 4h52 e rodada em negociação
**Fonte:** [AI Weekly](https://aiweekly.co/ai-news-today) (14 e 15/10)

A Cohere teria firmado carta de intenção para adquirir a AISLE, startup de cibersegurança com IA que afirma ter achado mais de 500 CVEs inéditas. A DeepSeek ficou offline por cerca de 4h52 por falta de capacidade e promete créditos a clientes de API; a empresa também estaria perto de uma rodada de cerca de US$ 14 bilhões, com valuation próximo de US$ 75 bilhões. Tudo de fontes secundárias.
