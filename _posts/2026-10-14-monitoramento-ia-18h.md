---
layout: post
title: "Radar IA — 14/10/2026, 18h"
date: 2026-10-14 18:00:00 -0300
categories: edicao
excerpt: "A Amex propõe um token de intenção para impedir compras indevidas feitas por agentes; a DigitalOcean lança serviços para agentes aprenderem com as próprias falhas; a OpenAI marca para 14/01/2027 o fim do GPT-4o e do GPT-4.1 na API; a startup Uvi ataca o custo de reensinar o contexto da empresa aos modelos; a Rocket Software compra a Geniez AI para agentes em mainframes; a Decagon teria conversado com a ServiceNow sobre uma venda."
---

*Janela pesquisada: 12 a 14/10/2026. Excluído por já ter sido coberto nas edições de 11, 12 e 13/10: Muse Wonder, Gemini 4 Argon, Mistral Large 4, Ling 3.1 Flash, Decreto 13.135 do SAC, Work IQ, Hermes/Nous e as demais notícias dessas edições. Dia de poucas novidades reais: os temas 2 e 3 não tiveram itens novos.*

## Destaques do dia

1. **Amex cria um "token de intenção" para compras de agentes**: o cliente aprova o que o agente pode comprar (loja, teto, preferências) e o pagamento só segue com essa prova, o que ajuda a barrar compras erradas e a resolver disputas. → 1.1
2. **DigitalOcean quer agentes que melhoram a cada execução**: registro de cada passo, detecção de sessões que travam e testes de correções com conversas simuladas, em preview público. → 1.2
3. **OpenAI aposenta o GPT-4o e o GPT-4.1 na API em 14/01/2027**: quem usa esses modelos, inclusive versões ajustadas (fine-tuned), precisa migrar, e a recomendação é o gpt-6-luna. → 1.3
4. **Contexto corporativo vira o gargalo dos agentes**: a israelense Uvi diz que empresas pagam repetidamente para reensinar às IAs de fronteira o que já sabem sobre as próprias operações. → 1.4, 4.3
5. **Rocket Software compra a Geniez AI por até US$ 100 milhões**: agentes que monitoram e diagnosticam mainframes, numa startup de seis funcionários, mostram o preço da modernização de legados. → 4.1
6. **Decagon teria sondado a ServiceNow para uma venda**: a startup de agentes de atendimento, que já estudaria uma venda de US$ 4,5 bilhões, mostra a consolidação do mercado de agentes corporativos. → 4.2

## 1. Novidades de IA agêntica

### 1.1 Amex propõe o "Intent Intelligence Framework" para evitar compras indevidas feitas por agentes
**Fonte:** [TechCrunch](https://techcrunch.com/2026/10/13/amex-introduces-a-framework-to-prevent-ai-agents-from-making-unauthorized-purchases/) (13/10)

A American Express apresentou uma estrutura que confirma a intenção de compra do cliente antes que um agente conclua a transação. Uma API de criação de intenção registra as instruções e as restrições (loja, orçamento máximo, preferências); o cliente se autentica e aprova; o sistema gera um ID de intenção e um token de prova de intenção, usado para obter uma credencial de pagamento digital que o agente utiliza no checkout no lugar do número do cartão. No exemplo da empresa, se o usuário pede um tênis Nike branco e o agente tenta comprar um Adidas, a transação pode ser bloqueada. Importa porque o comércio feito por agentes depende de uma resposta ao problema da não determinância dos LLMs: o registro do que foi autorizado, por qual agente e quando também serve a prevenção de fraude e a resolução de disputas. A Amex diz que ainda não viu aumento de disputas e conversa com parceiros do ecossistema de pagamentos para que o modelo vire padrão, o que é uma intenção, não uma adoção confirmada. Segue a linha das edições anteriores sobre identidade e permissão de agentes.

### 1.2 DigitalOcean lança serviços para agentes aprenderem com as próprias execuções
**Fonte:** [Business Wire, via FinancialContent](https://www.financialcontent.com/article/bizwire-2026-10-12-digitalocean-launches-agent-learning-and-data-services-for-recursively-self-improving-ai-agents) (12/10)

O pacote Agent Learning Services tem três partes: Insights, que registra cada passo do agente; Signals, que sinaliza sessões em que o agente trava, entra em laço, perde o usuário ou falha; e Evaluations & Simulations, que testa correções propostas com conversas realistas construídas a partir das sessões sinalizadas antes de chegarem a usuários reais. Junto vem o Agent Data Services, uma camada de dados gerenciada que processa vídeo, áudio, documentos, logs e sessões e os torna pesquisáveis por significado, com catálogo por cliente e controle de acesso. O Inference Router também foi ampliado para escolher o modelo de melhor desempenho por tarefa, reexecutando avaliações quando saem novos modelos. Insights, Signals e Evaluations estão em preview público; o otimizador do roteador e o Data Services estão em preview privado, sem suporte para produção, segundo a própria empresa. Para quem estuda avaliação de sistemas agênticos, o ponto é o ciclo fechado de observar, diagnosticar, simular e só então publicar a mudança, com aprovação humana mantida. É um comunicado de fornecedor: a Amplitude é citada como cliente, mas não há dados independentes de resultado.

### 1.3 OpenAI deprecia GPT-4o, GPT-4o mini, GPT-4.1 e GPT-4.1 mini na API
**Fonte:** [Releasebot (notas de versão da OpenAI)](https://releasebot.io/updates/openai) (14/10)

Segundo o agregador de notas de versão, a OpenAI notificou desenvolvedores de que gpt-4o (versões de 08/2024 e 11/2024), gpt-4o-mini, gpt-4.1 e gpt-4.1-mini serão removidos da API em 14/01/2027, com o gpt-6-luna indicado como substituto. Versões ajustadas (fine-tuned) seguem o mesmo calendário dos modelos-base. Importa porque muitos sistemas em produção, avaliações e pipelines de ajuste fino ainda estão presos a essas famílias: a migração muda custo, latência e comportamento, e exige reexecutar suítes de avaliação e, no caso de fine-tunes, retreinar sobre o novo modelo. Registre-se a limitação: a informação vem de um agregador, e vale confirmar a data e a lista no aviso oficial da OpenAI antes de planejar.

### 1.4 Uvi: reduzir o custo de reensinar o contexto da empresa aos modelos
**Fonte:** [Blocks and Files](https://blocksandfiles.com/ai-ml/2026/10/14/uvi-gives-ai-agents-enterprise-context/5302514) (14/10)

A startup israelense Uvi, segundo o Blocks and Files, parte da tese de que as empresas pagam aos fornecedores de modelos de fronteira, repetidamente, para reensinar o que já sabem sobre as próprias operações, e propõe dar contexto corporativo aos agentes. A página acessível traz apenas o resumo, sem detalhes de produto, clientes ou preços, e o texto menciona o armazenamento de objetos MinIO como tema relacionado. Por isso o item vale mais como sinal do que como análise de produto: a camada de contexto (dados, memória, permissões) segue sendo o terreno de disputa dos agentes corporativos, o mesmo que motivou os anúncios de Work IQ e de "context engines" nos últimos dias.

## 2. Ferramentas e modelos open source

*Sem novidades reais nas últimas 24-48 horas. O rastreador llm-stats não registrou lançamentos de pesos abertos no período, e os lançamentos abertos recentes (Mistral Large 4, Ling 3.1 Flash, Gemma Transcribe) já foram cobertos em edições anteriores.*

## 3. IA aplicada no setor público

*Sem novidades reais nas últimas 24-48 horas. A única notícia brasileira recente, o decreto do SAC com IA e atendimento humano garantido, já foi coberta na edição de 13/10; os demais casos internacionais mapeados no período (Itália, Alemanha, Reino Unido e EUA) são de dias anteriores e não foram repetidos aqui.*

## 4. IA aplicada em geral

### 4.1 Rocket Software compra a Geniez AI, de agentes para mainframes, por até US$ 100 milhões
**Fonte:** [Calcalist Tech](https://www.calcalistech.com/ctechnews/article/996lzw73e) (13/10)

A Rocket Software, empresa de software corporativo controlada pelo fundo Bain Capital, adquiriu a startup israelense Geniez AI por valor estimado de até US$ 100 milhões; a startup tinha seis funcionários. A Geniez constrói ferramentas de IA generativa para operar e modernizar mainframes, com agentes que atuam diretamente nesses sistemas para monitorá-los, diagnosticar incidentes e executar tarefas a partir de instruções em linguagem natural. O valor é estimado pela imprensa, não confirmado pelas partes. Importa porque sistemas legados de bancos, seguradoras e governos concentram décadas de lógica de negócio, e a modernização assistida por agentes virou um dos casos de uso com compra rápida e preço alto por funcionário.

### 4.2 Decagon teria conversado com a ServiceNow sobre uma venda
**Fonte:** [Business Insider](https://www.businessinsider.com/ai-agent-company-decagon-hired-investment-bank-acquisition-interest-2026-10) (13/10, conforme resumo do AI Agents Directory; página de origem não pôde ser aberta por esta rotina)

A startup de agentes de atendimento Decagon teria mantido conversas iniciais de fusão ou aquisição com a ServiceNow e outras empresas, depois de contratar um banco de investimento. A edição de ontem registrou que a empresa estudaria uma venda por cerca de US$ 4,5 bilhões; a novidade é o nome de um possível comprador. Trata-se de informação baseada em fontes, sem confirmação oficial. Importa porque mostra a consolidação do atendimento por agentes em plataformas de fluxo de trabalho corporativo.

### 4.3 Outros movimentos corporativos citados no resumo do dia
**Fonte:** [AI Agents Directory](https://aiagentsdirectory.com/news/ai-agents-drive-enterprise-modernization-and-manda-activity) (13/10)

O mesmo resumo menciona o lançamento do Deputy Agent da Cresta, para automatizar tarefas de retaguarda de atendimento, e uma parceria entre a DXC Technology e a LangChain para escalar agentes governados. Não foi possível confirmar nenhum dos dois em fonte primária nesta rodada, então ficam como registro, sem análise: acompanhe os comunicados oficiais antes de citar. O padrão, porém, é coerente com o restante do dia: integradoras e plataformas se reposicionando em torno de agentes com governança.
