# PayShield Risk

**English**

PayShield Risk is a simple fraud‑risk engine built with FastAPI. It demonstrates core concepts of payment
risk analysis such as velocity checks, anomaly detection based on transaction value, country‑based risk and
time‑of‑day patterns. The project exposes a single `/risk` endpoint that receives transaction details and
returns a risk score (0–100) along with a recommended decision (`APPROVE`, `REVIEW` or `DECLINE`).

This repository is part of the **PayShield Platform**, which simulates a complete payment ecosystem for
educational purposes. No real cardholder data is processed or stored.

**Disclaimer**: This is an educational project. The engine uses naive rules and in‑memory storage for
learning purposes only. Do not use this code in production environments.

---

**Português**

PayShield Risk é um mecanismo simples de avaliação de risco de fraude construído com FastAPI. Ele demonstra
conceitos centrais de análise de risco em pagamentos, como checagem de velocidade (muitas tentativas em
pouco tempo), detecção de anomalias pelo valor da transação, risco baseado em país de origem e padrão de
horário de uso. O projeto expõe um único endpoint `/risk` que recebe os dados da transação e retorna um
score de risco (0–100) juntamente com uma decisão recomendada (`APPROVE`, `REVIEW` ou `DECLINE`).

Este repositório faz parte da **Plataforma PayShield**, que simula um ecossistema completo de pagamentos
para fins educacionais. Nenhum dado real de portadores de cartão é processado ou armazenado.

**Aviso**: Este é um projeto educacional. O mecanismo utiliza regras ingênuas e armazenamento em memória
apenas para fins de aprendizagem. Não utilize este código em ambientes de produção.
