---
layout: post
title: "Radar IA — 04/10/2026, 18h"
date: 2026-10-04 18:00:00 -0300
categories: edicao
excerpt: "Google lança Skills no Gemini para automatizar tarefas entre aplicativos; Armadin levanta US$ 255,5 milhões para enxames de agentes que atacam redes para testá-las; Aleph Alpha abre o Kolibri de 78 bilhões de parâmetros e Bilibili abre um tradutor de 150 idiomas; Trump cria a Superintelligence Force com 120 dias para propor o papel do governo; MCTI marca para 8 de outubro as propostas do supercomputador de IA de R$ 959 milhões; Microsoft lança trio próprio de voz para agentes e reduz dependência de OpenAI e Anthropic."
---

*Janela pesquisada: 02/10 a 04/10/2026 (com itens de 01/10 ainda sem cobertura). Excluídos por já terem sido cobertos nas edições anteriores: Gemini 4 Argon, Strands Decider e Clef, Nvidia Open Agent Safety Platform, VigIA, investigação da FTC e processos sobre agentes invasores. O lançamento do agente Dots da OpenAI (29/09) também ficou de fora, por estar fora da janela.*

## Destaques do dia

1. **Gemini ganha Skills**: o Google transforma o assistente em agente que decompõe pedidos em etapas e age em Workspace e apps de terceiros, com autorização do usuário para ações sensíveis. → 1.1
2. **Enxames de 26 mil agentes atacam redes para testá-las**: a Armadin, de fundadores da Mandiant, levantou US$ 255,5 milhões com avaliação acima de US$ 2,5 bilhões. → 1.2
3. **Open source ganha um MoE europeu e um tradutor de 150 idiomas**: Kolibri (78 bilhões de parâmetros, Apache-2.0) e Index-Translate-35B-A3B chegam com pesos abertos. → 2.1, 2.2
4. **Trump cria a Superintelligence Force**: força-tarefa liderada por Jay Clayton terá 120 dias para propor o papel federal em IA, após acordo voluntário sem punições com big techs. → 3.1
5. **Brasil define data do supercomputador de IA**: propostas para o equipamento de R$ 959 milhões serão apresentadas em 8 de outubro, com exigência de transferência de tecnologia. → 3.2
6. **Microsoft monta pilha própria de voz para agentes**: MAI-Transcribe-2-Streaming e dois modelos de voz reduzem a dependência de OpenAI e Anthropic. → 4.1

## 1. Novidades de IA agêntica

### 1.1 Google lança Skills no Gemini para automatizar tarefas repetitivas entre aplicativos
**Fonte:** [Emergent](https://emergent.sh/news/gemini-skills-launch-automate-repetitive) (01/10)

O Google lançou o recurso Skills no Gemini, que interpreta instruções em linguagem natural, divide pedidos complexos em etapas executáveis e coordena ações no Google Workspace e em integrações de terceiros, em tarefas como entrada de dados, geração de relatórios e gestão de agenda. O ponto de projeto relevante é que operações que alteram dados ou enviam comunicações continuam exigindo autorização do usuário, isto é, o modelo de supervisão humana nos passos sensíveis. Para quem estuda agentes, o lançamento mostra a convergência dos assistentes de consumo para o padrão "skills" (instruções e rotinas reutilizáveis) já comum em ferramentas de desenvolvimento, e coloca o Google em competição direta com ChatGPT e Claude no terreno da automação de trabalho. A fonte é um veículo secundário e não detalha disponibilidade por plano ou região; vale confirmar no blog oficial do Google.

### 1.2 Armadin levanta US$ 255,5 milhões para enxames de agentes que simulam ataques
**Fonte:** [Tech Funding News](https://techfundingnews.com/mandiant-founders-ai-hacking-startup-armadin-raises-255-5m-from-a16z-and-accel-at-a-2-5b-valuation) (01/10) · [AI Agents Directory](https://aiagentsdirectory.com/news/ai-agents-news-brief-october-2-2026) (02/10)

A Armadin, fundada por Kevin Mandia e outros ex-Mandiant, fechou uma Series B de US$ 255,5 milhões liderada por a16z e Accel, com avaliação acima de US$ 2,5 bilhões e total captado de US$ 445 milhões em 13 meses de existência. A empresa implanta enxames de agentes especializados que encadeiam vulnerabilidades para testar as defesas de uma organização; em um teste de agosto, 26 mil agentes identificaram 238 achados de segurança em uma rede institucional real. O caso é um exemplo concreto de orquestração multiagente em larga escala saindo do laboratório, e mostra que a segurança ofensiva automatizada virou a categoria de agentes que mais atrai capital, em linha com a tendência de acesso restrito a modelos de ciberdefesa vista nesta semana. Os números de achados vêm da própria empresa e não foram auditados de forma independente.

## 2. Ferramentas e modelos open source

### 2.1 Aleph Alpha abre o Kolibri: MoE de 78 bilhões de parâmetros, foco em alemão e inglês, Apache-2.0
**Fonte:** [OrcaRouter](https://www.orcarouter.ai/blog/kolibri-release-explained) (03/10)

A Aleph Alpha liberou o Kolibri, um modelo de mistura de especialistas com 78,1 bilhões de parâmetros totais e apenas 3,46 bilhões ativos por token, janela de contexto validada de cerca de 1 milhão de tokens e licença Apache-2.0. Foi treinado com 20 trilhões de tokens em 768 GPUs Nvidia B200 por 21 dias, com cerca de 20% de dados em alemão, parte deles sintéticos (aproximadamente 1 trilhão de tokens gerados por reescrita). Os pesos estão no Hugging Face, sem API de fornecedor, e exigem ao menos duas GPUs A100 de 80 GB. Segundo a análise da fonte, os resultados são mistos: o Qwen3.8 de 27 bilhões supera o Kolibri em várias métricas, mas a esparsidade agressiva dá vantagem de eficiência. Importa como caso de soberania de dados e idiomas na Europa e como referência de receita de dados para línguas com menos corpus público, um desafio comum ao português.

### 2.2 Bilibili libera o Index-Translate-35B-A3B-preview, tradutor para 150 idiomas
**Fonte:** [Digital Applied](https://www.digitalapplied.com/blog/ai-model-releases-october-2026-tracker) (02/10)

A equipe Index, da Bilibili, publicou em versão preliminar um modelo de tradução com 35 bilhões de parâmetros totais e 3 bilhões ativos (MoE), cobrindo 150 idiomas de texto, sob Apache-2.0, disponível no Hugging Face e no ModelScope. Com poucos parâmetros ativos, o modelo é barato de servir e adequado a pipelines de tradução em lote ou a agentes que precisam de tradução como ferramenta. A fonte é um rastreador agregador; não encontrei relatório técnico nem benchmarks, então a qualidade, sobretudo em português, precisa ser testada antes de adoção.

## 3. IA aplicada no setor público

*Internacional*

### 3.1 Trump cria a "Superintelligence Force" e dá 120 dias para propor o papel do governo federal
**Fonte:** [Observador](https://observador.pt/2026/10/04/trump-cria-forca-da-superinteligencia-para-coordenar-o-desenvolvimento-de-ia/) (04/10) · [O Tempo](https://www.otempo.com.br/mundo/2026/10/4/trump-nomeia-chefe-de-inteligencia-para-liderar-forca-tarefa-sobre-ia) (04/10)

O presidente americano anunciou uma unidade de coordenação na Casa Branca, chefiada pelo diretor de Inteligência Nacional, Jay Clayton, que responde diretamente a ele e à chefe de gabinete Susie Wiles. Em 120 dias, a força deve avaliar riscos e oportunidades da IA, propor o papel do governo federal, reforçar a resposta a incidentes de IA e coordenar a relação com consumidores, empresas e organizações. O anúncio vem após uma diretriz para trocar "inteligência artificial" por "superinteligência" na comunicação oficial e um almoço com executivos de Google, xAI, Anthropic, Meta, Nvidia e OpenAI, que resultou em compromissos voluntários (auditorias independentes e controles internos), sem punição por descumprimento. Importa porque coloca a coordenação de IA sob a área de inteligência, em vez de um órgão regulador, o que sinaliza abordagem de segurança nacional e competição com a China, e não de regulação ampla. Não há reações documentadas nas fontes consultadas.

*Brasil*

### 3.2 MCTI marca para 8 de outubro as propostas do supercomputador de IA de R$ 959 milhões
**Fonte:** [É Notícia](https://enoticiapr.com.br/governo-federal-define-data-para-recebimento-de-propostas-do-novo-supercomputador-de-ia/) (data da publicação não informada; audiência em 08/10)

O Ministério da Ciência, Tecnologia e Inovação marcou para 8 de outubro uma audiência presencial em que empresas apresentarão propostas técnicas e de preço para um novo supercomputador de IA, com investimento de R$ 959.040.959,04. O equipamento será instalado no Rio Grande do Norte, com o Laboratório Nacional de Computação Científica (LNCC), em Petrópolis, como sede do projeto, e é voltado a desenvolvimento, treinamento e inferência de modelos avançados, com ênfase em LLMs, para o setor público, a comunidade científica e o ecossistema de inovação. As propostas vencedoras devem incluir transferência de tecnologia, capacitação de especialistas brasileiros e codesenvolvimento de infraestrutura de software nacional, o que reflete a agenda de soberania tecnológica do Plano Brasileiro de IA. A fonte é um veículo regional e não informa a data da notícia; o resultado da audiência é o próximo marco a acompanhar.

## 4. IA aplicada em geral

### 4.1 Microsoft lança modelo de transcrição em streaming e duas vozes próprias para agentes de voz
**Fonte:** [SiliconANGLE](https://siliconangle.com/2026/10/01/microsoft-targets-ultra-realistic-voice-agents-with-its-first-streaming-transcription-model) (01/10) · [AI Agents Directory](https://aiagentsdirectory.com/news/ai-agents-news-brief-october-2-2026) (02/10)

A Microsoft apresentou o MAI-Transcribe-2-Streaming, seu primeiro modelo de transcrição em tempo real via WebSocket, com primeira transcrição em cerca de 320 ms, mais de 60 idiomas e preço de US$ 0,54 por hora de áudio, além do MAI-Voice-2.1 (US$ 22 por milhão de caracteres) e do MAI-Voice-2.1-Flash (US$ 15 por milhão), ambos em 23 idiomas. Com o modelo de raciocínio Mai-Thinking-1, os três formam uma pilha completa de agente de voz sem depender de provedores externos, em linha com a orientação de Mustafa Suleyman de reduzir a dependência de OpenAI e Anthropic. Para empresas, o movimento pressiona preços de voz em tempo real e reforça a tendência de grandes fornecedores verticalizarem toda a cadeia de agentes. Os modelos são proprietários.
