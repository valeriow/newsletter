---
layout: post
title: "Radar IA — 05/11/2026, 17h"
date: 2026-11-05 17:05:00 -0300
categories: edicao
excerpt: "Relato de que o Google lançou o Agent Compute Engine, ainda sem confirmação oficial; Claude Duet segue só por lista de espera nos EUA; prazo de 4/11 para os pesos do Kimi K3.1 Pro venceu sem confirmação; Semana de IA do Serpro debate IA soberana até 6/11; roadshow do IPO da Anthropic é esperado a partir de 9–10/11; edição enxuta, com poucas novidades verificáveis"
---

*Janela pesquisada: 03/11 a 05/11/2026. Excluí o que já saiu nas edições de 03/11 e 04/11 (S-1/A da Anthropic, AT&T–Amdocs, Snowflake, Saab, CrowdStrike, Menlo Ventures, Fal etc.). Nota de transparência: a busca desta edição teve acesso limitado (alguns sites oficiais estavam bloqueados) e retornou pouco material datado das últimas 48 horas; por isso a edição é curta e marca o que não foi confirmado em fonte primária.*

## Destaques do dia

1. **Google teria lançado o Agent Compute Engine**: relato isolado descreve ambiente para rodar agentes, com Agent Registry e Agent Identity, mas sem confirmação oficial. → 1.1
2. **Claude Duet continua em lista de espera**: o agente pessoal da Anthropic segue restrito a assinantes Pro e Max nos EUA, sem data para abertura geral. → 1.2
3. **Pesos do Kimi K3.1 Pro: prazo venceu sem confirmação**: a Moonshot prometeu publicar até 4/11, e não achei prova de que isso aconteceu. → 2.1
4. **Semana de IA do Serpro discute IA soberana**: o evento vai de 4 a 6/11 e coloca o controle de dados e de nuvem no centro da agenda pública. → 3.1
5. **Roadshow do IPO da Anthropic perto**: a expectativa é de apresentações a investidores a partir de 9–10/11, ainda sem confirmação da empresa. → 4.1
6. **Dia de poucas novidades verificáveis**: vários assuntos são continuação de edições anteriores, e o Radar prefere dizer isso a encher a página. → 1.1, 2.1, 4.1

## 1. Novidades de IA agêntica

### 1.1 Relato aponta Agent Compute Engine do Google Cloud, sem confirmação oficial
**Fonte:** [SecurityBrief Asia](https://securitybrief.asia/story/google-cloud-launches-ai-agent-engine-governance) (06/11, data inconsistente) · [Google Cloud — Agent Identity](https://cloud.google.com/blog/products/identity-security/whats-new-in-iam-security-governance-and-runtime-defense)

Uma reportagem descreve o lançamento de um "Agent Compute Engine", infraestrutura baseada na usada para rodar o Gemini em tarefas de trabalho, acompanhada de ferramentas de governança como Agent Registry e Agent Identity. A data da matéria (06/11) é posterior a hoje, então trate o relato com cautela e confirme nas notas de versão do Google Cloud. O que já é documentado pelo Google, desde o Cloud Next de abril, é o Agent Identity: cada agente recebe uma identidade criptográfica própria, baseada no padrão aberto SPIFFE, o que torna suas ações auditáveis e ligadas a políticas de autorização. Para quem estuda ou opera agentes, o ponto relevante é a tendência: identidade, registro e auditoria de agentes estão virando camada obrigatória de plataforma, não detalhe.

### 1.2 Claude Duet segue em pré-visualização restrita
**Fonte:** [Let's Data Science](https://letsdatascience.com/news/anthropic-opens-claude-duet-research-preview-for-proactive-a-16522f5d) (21/10, atualizações recentes) · [Runtime Wire](https://runtimewire.com/article/anthropic-claude-duet-waitlist-access)

Lançado como pré-visualização em 21/10, o Claude Duet é um agente pessoal proativo que trabalha em contas conectadas e continua tarefas enquanto o usuário está ausente, pedindo aprovação antes de enviar mensagens, pagar, assinar ou apagar. O acesso continua limitado a assinantes Pro e Max nos EUA, por convites em ondas, e um mercado de previsão dá cerca de 29% de chance de abertura sem fila até 30/11. Não é notícia nova, mas é útil como status: o desenho de "aprovação para ações irreversíveis" é um padrão de segurança que merece ser copiado em agentes próprios.

## 2. Ferramentas e modelos open source

### 2.1 Kimi K3.1 Pro: prazo de 4/11 para os pesos passou sem confirmação
**Fonte:** [Let's Data Science](https://letsdatascience.com/news/moonshot-releases-kimi-k31-pro-api-open-weights-due-nov-4-786e160c) (23/10) · [Coders Era](https://codersera.com/blog/kimi-k3-1-pro-complete-guide-2026/amp/)

A Moonshot liberou o Kimi K3.1 Pro pela API em 23/10 (US$ 2 e US$ 10 por milhão de tokens) e prometeu publicar os pesos até 4/11. Na busca de hoje, todas as fontes são anteriores ao prazo e nenhuma confirma o repositório no Hugging Face; um guia notava que o repositório ainda não existia. Sem verificação direta, não dá para afirmar que foi cumprido nem que foi descumprido. Vale conferir a organização oficial da Moonshot antes de planejar qualquer uso local: o modelo exige algo como 1,6 TB de disco, segundo guias de hardware.

*Sem outras novidades de código aberto confirmadas nas últimas 48 horas.*

## 3. IA aplicada no setor público

*Brasil*

### 3.1 II Semana de IA do Serpro (4 a 6/11) debate "IA Soberana: dados, tecnologia e poder de decisão"
**Fonte:** [Serpro](https://www.serpro.gov.br/menu/noticias/noticias-2026/segunda-semana-ia-serpro) (05/11) · [MobileTime](https://www.mobiletime.com.br/noticias/07/08/2026/serpro-ia-soberana/)

O evento acontece em Brasília e online (inscrição gratuita; presencial esgotado), das 9h às 17h, e pergunta o que as instituições públicas precisam dominar para manter autonomia sobre sistemas de IA que já participam da entrega de serviços. Há painéis sobre critérios de segurança e controle de dados e da operação de nuvem com fornecedores globais, e sobre como redes de ciência, energia e pesquisa podem construir infraestrutura soberana. A agenda inclui a Plataforma IA do Brasil e experiências do Tesouro Nacional. O contexto é a oferta de IA soberana do Serpro lançada no Febraban Tech, que busca competir em preço de token. Importa porque define o vocabulário (soberania, controle de nuvem) que deve orientar compras públicas de IA.

*Internacional: sem novidades confirmadas nas últimas 48 horas. Sobre o marco legal (PL 2338), não encontrei andamento novo além do que a edição de 04/11 já registrou.*

## 4. IA aplicada em geral

### 4.1 IPO da Anthropic: apresentações a investidores esperadas a partir de 9–10/11
**Fonte:** [Crypto Briefing](https://cryptobriefing.com/anthropic-targets-november-ipo-delay/) · [Parameter](https://parameter.io/claude-creator-prepares-100-billion-public-offering-ahead-of-thanksgiving/)

Reportagens secundárias citam a Bloomberg: a empresa deve iniciar apresentações formais a investidores já na semana de 9/11, com início mais cedo possível em 10/11, depois de adiar de outubro para ter o balanço do terceiro trimestre completo. Estimativas falam em avaliação entre US$ 1 tri e US$ 2 tri e cerca de US$ 100 bi de captação, mas a Anthropic não confirmou datas e cronogramas de IPO costumam mudar. É continuação do assunto da edição de 03/11 e 04/11; o dado novo é apenas a janela do roadshow. Para o mercado, uma oferta desse tamanho vira termômetro do apetite por IA.
