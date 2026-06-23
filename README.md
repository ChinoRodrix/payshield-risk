# PayShield Risk

## Overview

PayShield Risk is the fraud‑risk analysis microservice of the PayShield Platform. It receives transaction details and returns a risk score (0‑100) along with an advised decision: `APPROVE`, `REVIEW` or `DECLINE`. The engine demonstrates key concepts of payment risk such as velocity checks (multiple attempts within a time window), anomaly detection based on transaction amount relative to a customer's historical average, country‑based risk and unusual time‑of‑day patterns. All data is simulated.

## Architecture / Arquitetura

```
Client
  |
  | POST /risk
  v
Risk Engine (FastAPI)
  |
  |---> In-memory store / MongoDB
  |
  +---> Rules (velocity, amount anomaly, country, time)
         |
         v
      Score & Decision
```

## OpenAPI / Swagger

This project uses FastAPI to automatically expose interactive API documentation. After running the service (`uvicorn main:app --reload`) you can open `http://localhost:8000/docs` to view the Swagger UI, test the `/risk` endpoint and inspect request/response schemas. Another OpenAPI document is available at `/openapi.json`.

## Use Cases

- **Simulation and learning** – send sample transactions to understand how fraud risk scores and decisions are calculated.
- **Integration testing** – integrate PayShield Core with PayShield Risk to simulate end-to-end payment and fraud analysis flows.
- **Experimentation** – extend the rule set or scoring algorithm to prototype anti-fraud ideas before applying them to real systems.

## Roadmap

- Persist past transactions in a MongoDB or PostgreSQL database for velocity checks.
- Add configurable rule thresholds and weights.
- Implement a simple machine learning model using Python libraries to augment rule-based scoring.
- Add authentication and rate limiting to protect the API.

## Screenshots

*To be added.* In future iterations we plan to include screenshots of the API documentation, sample requests and integration dashboards.

## Disclaimer

This repository is an educational project. It uses simulated data and naive algorithms purely for learning purposes. No real cardholder information is processed or stored. Do not use this code in production environments.

---

# PayShield Risk

## Visão Geral

O PayShield Risk é o microsserviço de análise de risco de fraude da PayShield Platform. Ele recebe detalhes de transações e retorna um score de risco (0‑100) junto com uma decisão recomendada: `APPROVE`, `REVIEW` ou `DECLINE`. O mecanismo demonstra conceitos chave de risco de pagamento como checagem de velocidade (várias tentativas em uma janela de tempo), detecção de anomalias baseada no valor da transação em relação à média histórica do cliente, risco por país e padrões de horários incomuns. Todos os dados são simulados.

## Arquitetura / Architecture

```
Cliente
  |
  | POST /risk
  v
Motor de Risco (FastAPI)
  |
  |---> Armazenamento em memória / MongoDB
  |
  +---> Regras (velocidade, anomalia de valor, país, horário)
         |
         v
      Score & Decisão
```

## OpenAPI / Swagger

O projeto utiliza FastAPI para expor automaticamente documentação interativa da API. Após executar o serviço (`uvicorn main:app --reload`) você pode abrir `http://localhost:8000/docs` para visualizar a interface Swagger, testar o endpoint `/risk` e inspecionar os esquemas de requisição/resposta. Outro documento OpenAPI está disponível em `/openapi.json`.

## Casos de Uso

- **Simulação e aprendizado** – envie transações de exemplo para entender como scores e decisões de risco de fraude são calculados.
- **Teste de integração** – integre o PayShield Core ao PayShield Risk para simular fluxos de pagamento e análise de fraude de ponta a ponta.
- **Experimentação** – estenda o conjunto de regras ou o algoritmo de score para prototipar ideias de antifraude antes de aplicá-las a sistemas reais.

## Roadmap

- Persistir transações passadas em um banco MongoDB ou PostgreSQL para verificação de velocidade.
- Adicionar limiares e pesos de regras configuráveis.
- Implementar um modelo de aprendizado de máquina simples usando bibliotecas Python para complementar a pontuação baseada em regras.
- Adicionar autenticação e rate limiting para proteger a API.

## Screenshots

*A serem adicionadas.* Em futuras iterações, planejamos incluir capturas de tela da documentação da API, requisições de exemplo e dashboards de integração.

## Aviso

Este repositório é um projeto educacional. Ele usa dados simulados e algoritmos ingênuos apenas para fins de aprendizado. Nenhuma informação real de portadores de cartão é processada ou armazenada. Não utilize este código em ambientes de produção.
