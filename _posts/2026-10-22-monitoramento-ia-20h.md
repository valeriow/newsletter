---
layout: post
title: "Radar IA — 22/10/2026, 20h"
date: 2026-10-22 20:00:00 -0300
categories: edicao
excerpt: "ServiceNow e Nvidia liberam o agente Arc para o uso geral; VAST e HPE vendem a infraestrutura governada para rodar agentes; Uber dá o ChatGPT Work a 30 mil funcionários; Volkswagen estende o Copilot a 330 mil pessoas; coordenadora de Flávio Bolsonaro propõe trocar servidores aposentados por IA; agentes de IA entram em finanças e em triagem de risco social."
---

*Janela pesquisada: 20/10 a 22/10/2026. Ficaram de fora, por já terem sido cobertos nas edições de 19, 20 e 21/10, o Muse Spark Open, o Gemini para serviços de governo, a Agent Knowledge Foundation da Nvidia, os Gemini Launchpads e o MiniMax M3.1 Flash. Itens sem confirmação em fonte primária foram descartados.*

## Destaques do dia

1. **Arc, o agente corporativo de longa duração, chega ao uso geral**: ServiceNow e Nvidia liberaram o Arc, que roda localmente com políticas aplicadas em tempo de execução pelo OpenShell; só há versão para Mac por enquanto. → 1.1
2. **A infraestrutura de governança de agentes vira produto**: VAST registra cada chamada de ferramenta em sandboxes OpenShell, a HPE adiciona APIs governadas e serviços MCP, e a WorkOS aponta as lacunas de identidade entre agentes. → 1.2, 1.3, 1.4
3. **Uber libera o ChatGPT Work para cerca de 30 mil funcionários**: um dos maiores desdobramentos conhecidos do produto, anunciado dias depois de relatos sobre falhas no monitoramento de modelos da OpenAI. → 4.1
4. **Volkswagen estende o Copilot a mais de 330 mil pessoas**: a Microsoft cita 300 mil usuários mensais e mais de 26 mil agentes ativos, números que são da própria fornecedora. → 4.2
5. **Trocar servidores aposentados por IA entra na campanha presidencial**: coordenadora de Flávio Bolsonaro propôs não repor vagas por concurso e transferir o trabalho a sistemas de IA, sem detalhar como. → 3.1
6. **Agentes de IA avançam em finanças e em triagem de risco social**: a Kognitos lança 61 "funcionários de IA" para finanças e uma organização australiana usa agentes para sinalizar clientes em risco. → 4.3, 4.4

## 1. Novidades de IA agêntica

### 1.1 ServiceNow e Nvidia tornam o agente Arc geralmente disponível
**Fonte:** [Let's Data Science](https://letsdatascience.com/news/servicenow-and-nvidia-make-arc-enterprise-ai-agent-generally-64c4e9d1) (21/10)

O Arc é um agente de longa duração para o trabalho rotineiro de funcionários: lê e-mails e notas de reunião, destaca ações pendentes e acumula memória e habilidades ao longo do tempo. Pode rodar localmente em um desktop ou em outro dispositivo dentro do OpenShell, o ambiente isolado da Nvidia, e envia tarefas complexas a modelos de fronteira apenas quando necessário. A governança fica com a Super Intelligence Control Tower, da ServiceNow, e o OpenShell aplica as políticas em tempo de execução. Há suporte para Mac; Windows e a integração do AI Passport (credencial de identidade para agentes) ainda estão por vir. Importa porque une, em um produto, a tendência de agentes que operam por horas ou dias e a exigência de que cada ação seja contida por política. As informações vêm de comunicados das empresas e não foram verificadas de forma independente; preço e suporte a outros equipamentos não foram esclarecidos.

### 1.2 VAST lança pilha de sandbox para agentes OpenShell com registro persistente
**Fonte:** [Let's Data Science](https://letsdatascience.com/news/vast-launches-agent-sandbox-foundation-stack-for-nvidia-open-934986d2) (22/10)

Anunciada em 21/10 no GTC Berlin, a pilha da VAST executa os agentes NemoClaw da Nvidia em sandboxes OpenShell sobre a plataforma da empresa e guarda um registro persistente de chamadas de ferramentas, prompts, tokens, custos e decisões. O ponto relevante é a auditabilidade: quando um agente age de forma inesperada, reconstruir o que ele fez e por quê depende desse tipo de trilha. É a mesma preocupação das edições anteriores sobre agentes que enfraquecem o próprio monitoramento, agora tratada como produto de infraestrutura. Trata-se de anúncio comercial, sem avaliação independente.

### 1.3 HPE amplia plataforma com Nvidia para IA agêntica governada
**Fonte:** [Let's Data Science](https://letsdatascience.com/news/hpe-expands-nvidia-backed-platform-for-governed-agentic-ai-0c3ba486) (21/10)

No GTC Berlin, a HPE atualizou o AI Factory com a Nvidia, acrescentando APIs governadas e serviços MCP (Model Context Protocol, o padrão que conecta agentes a ferramentas e dados) ao Private Cloud AI, além de suporte a GPUs heterogêneas. Para quem trabalha em órgãos ou empresas que precisam manter dados em ambiente próprio, a mensagem é que a camada de agentes está chegando também à nuvem privada, e não só aos serviços públicos de nuvem. Falta, nas informações disponíveis, qualquer dado de desempenho ou preço.

### 1.4 WorkOS descreve o SSO entre agentes e o que ainda falta
**Fonte:** [AI Agent Store](https://aiagentstore.ai/ai-agent-news/this-week) (20/10, resumo da publicação da WorkOS)

A WorkOS publicou uma análise sobre login único (SSO) e federação entre agentes de organizações diferentes, na esteira do impulso da Okta ao tema. Segundo o resumo, as lacunas estão em identidade, cadeias de delegação (quem autorizou quem a agir em nome de quem) e auditoria. Complementa o tema de identidade e passaporte de agentes tratado na edição de 19/10. A fonte é um agregador; o texto original da WorkOS não foi lido, então vale conferir antes de citar.

## 2. Ferramentas e modelos open source

*Sem novidades reais nas últimas 24 a 48 horas que pudessem ser confirmadas em fonte primária. Os lançamentos abertos recentes (Muse Spark Open, Beam, Timestral, Agent Knowledge Foundation) já foram cobertos em edições anteriores, e a abertura dos pesos do MiniMax M3.1 Flash, prevista para 23/10, será acompanhada na próxima edição.*

## 3. IA aplicada no setor público

*Brasil*

### 3.1 Coordenadora de Flávio Bolsonaro propõe trocar servidores aposentados por IA
**Fonte:** [Metrópoles, coluna de Matheus Leitão](https://metropoles.com/colunas/matheus-leitao/sonha-com-concurso-coordenadora-de-flavio-quer-trocar-servidor-por-ia) (22/10)

Segundo a coluna, Daniella Marques, apontada como coordenadora de Flávio Bolsonaro, disse no programa Pânico (19/10) que os servidores que se aposentarem deveriam ser substituídos por sistemas de IA em vez de novos concursos. Ela não informou quantos cargos, quais carreiras nem como os serviços continuariam. O colunista liga a ideia ao anúncio de Javier Milei de cortar mais 20 mil postos na Argentina e argumenta que deixar vagas sem preenchimento para depois extingui-las seria um atalho jurídico. Convém ler com cautela: é uma coluna de opinião, a conexão entre os três nomes é interpretação do autor e não há plano oficial de governo. Importa para a comunidade de IA porque coloca a IA no setor público como instrumento de corte de pessoal no debate eleitoral, o oposto da visão de reuso e apoio ao servidor defendida por técnicos de governo digital, e porque expõe a distância entre promessa e capacidade real dos sistemas.

*Internacional*

*Sem novidades novas nas últimas 48 horas além do Gemini para serviços de governo e dos Gemini Launchpads, já cobertos em edições anteriores.*

## 4. IA aplicada em geral

### 4.1 Uber libera o ChatGPT Work para cerca de 30 mil funcionários
**Fonte:** [The Tech Buzz](https://www.techbuzz.ai/articles/uber-rolls-out-chatgpt-work-to-all-30-000-employees) (22/10)

Depois de um piloto limitado, a Uber dará acesso ao ChatGPT Work, agente corporativo da OpenAI, a todos os cerca de 30 mil funcionários, em um dos maiores desdobramentos conhecidos do produto. A empresa não disse quais fluxos de trabalho visa nem o preço, e o veículo especula sobre desconto relevante. O anúncio vem dias depois de relatos sobre falhas no monitoramento de sistemas da OpenAI, o que sugere que as preocupações com segurança de agentes ainda não freiam a adoção em escala. Veículo menos consolidado que a imprensa tradicional; a OpenAI e a Uber não foram consultadas diretamente aqui.

### 4.2 Volkswagen estende o Copilot a mais de 330 mil funcionários
**Fonte:** [Let's Data Science](https://letsdatascience.com/news/microsoft-equips-330000-volkswagen-group-employees-with-copi-7d9d97f9) (21/10)

A Microsoft informou que o grupo Volkswagen deu acesso ao Copilot a mais de 330 mil pessoas, com mais de 300 mil usuários mensais do Copilot Chat e mais de 26 mil agentes ativos no mês anterior. O uso avançado, com o Work IQ, atinge engenharia, produção, compras e vendas. São números de uso fornecidos pela fabricante do software, sem ganhos de produtividade medidos de forma independente nem termos de licenciamento. Ainda assim, mostram em que escala as grandes empresas estão implantando agentes, e não só assistentes de conversa.

### 4.3 Kognitos lança 61 "funcionários de IA" para finanças
**Fonte:** [AI Agent Store](https://aiagentstore.ai/ai-agent-news/this-week) (22/10)

A Kognitos liberou funções de finanças baseadas em 515 procedimentos operacionais padrão (POPs) e um agente, o Quill, que redige POPs para aprovação humana. A ideia de ancorar o agente em procedimentos escritos e aprovados por pessoas é uma resposta direta ao medo de automações que improvisam. Informação vinda do próprio fabricante, via agregador.

### 4.4 Organização australiana usa agentes de IA para triar clientes em risco
**Fonte:** [Let's Data Science](https://letsdatascience.com/news/relationships-australia-sa-uses-ai-agents-to-screen-at-risk-231dd3ef) (22/10)

A Relationships Australia SA usa dois agentes na Nonprofit Cloud da Salesforce para avaliar o risco de clientes enquanto aguardam atendimento; sinais de risco elevado levam uma pessoa treinada a ligar. O desenho mantém o humano na decisão, o que é o modelo mais defensável para serviços sociais. Não é órgão público, mas é um caso próximo do que governos consideram.

### 4.5 ASI levanta US$ 325 milhões a US$ 3 bilhões de avaliação
**Fonte:** [Let's Data Science](https://letsdatascience.com/news/asi-raises-325-million-at-3-billion-valuation-for-infrastruc-c6aa10d5) (21/10)

A empresa de Boston, que faz software para controle de tráfego aéreo, redes de energia e operações militares, captou uma Série C de US$ 325 milhões e pretende expandir para energia, logística e defesa. Mostra capital fluindo para IA em infraestrutura crítica, setor em que erros custam mais caro.
