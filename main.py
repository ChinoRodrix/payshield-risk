"""PayShield Risk Engine

This module defines a simple fraud‑risk engine using FastAPI. It
exposes a `/risk` endpoint that accepts transaction details and
returns a risk score and a decision. The logic here is deliberately
naïve to illustrate common fraud detection concepts such as velocity
checks, anomalous ticket values, country risk and unusual purchase
times.

This project is for educational purposes only. Do not use this in
production.
"""

from datetime import datetime, timedelta, time
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, Field, validator


class Transaction(BaseModel):
    """Represents a single payment transaction for risk analysis."""
    customer_id: str = Field(..., description="Unique identifier for the customer")
    card_number: str = Field(..., description="Tokenised or masked card number")
    amount: float = Field(..., ge=0.0, description="Transaction amount")
    country: str = Field(..., min_length=2, max_length=2, description="ISO country code")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Timestamp of the transaction")

    @validator("country")
    def uppercase_country(cls, v: str) -> str:
        return v.upper()


class RiskResponse(BaseModel):
    risk_score: int = Field(..., ge=0, le=100, description="Calculated risk score")
    decision: str = Field(..., description="Recommended decision: APPROVE/REVIEW/DECLINE")


app = FastAPI(
    title="PayShield Risk Engine",
    description="Educational fraud risk engine for payment transactions",
    version="0.1.0",
)

# In‑memory transaction history for velocity checks and ticket averages.
_transactions: List[Transaction] = []


@app.post("/risk", response_model=RiskResponse)
def calculate_risk(tx: Transaction) -> RiskResponse:
    """Calculate a simple fraud risk score based on transaction details.

    The logic here uses the following heuristics:

    * Velocity: count transactions with the same card in the last 2 minutes. High velocity increases risk.
    * High ticket: compare against average ticket for the same customer. Large deviations increase risk.
    * Country risk: transactions from countries other than the customer's presumed country (e.g. 'BR') increase risk.
    * Time risk: transactions occurring in the early morning hours are more suspicious.

    Returns a score between 0 and 100 and a recommended decision.
    """
    now = datetime.utcnow()
    # Keep only recent history (last 24h) to prevent memory blow‑up
    cutoff = now - timedelta(hours=24)
    global _transactions
    _transactions = [t for t in _transactions if t.timestamp >= cutoff]

    # Calculate velocity: number of transactions for this card in last 2 minutes
    velocity_count = sum(
        1
        for t in _transactions
        if t.card_number == tx.card_number and (now - t.timestamp) < timedelta(minutes=2)
    )

    # Calculate average ticket for customer
    customer_txs = [t for t in _transactions if t.customer_id == tx.customer_id]
    avg_ticket = (
        sum(t.amount for t in customer_txs) / len(customer_txs)
        if customer_txs
        else tx.amount
    )

    # Build risk score
    risk_score = 0
    # Velocity rule: more than 5 tx in 2 minutes adds risk
    if velocity_count >= 5:
        risk_score += 30
    elif velocity_count >= 3:
        risk_score += 15

    # High ticket rule: if amount significantly exceeds average ticket
    if tx.amount > avg_ticket * 5:
        risk_score += 25
    elif tx.amount > avg_ticket * 2:
        risk_score += 10

    # Country risk: treat non‑domestic purchases as higher risk
    # For simplicity, assume the customer's country is the first transaction's country or BR
    customer_country = customer_txs[0].country if customer_txs else "BR"
    if tx.country != customer_country:
        risk_score += 20

    # Time risk: transactions between 0:00 and 05:00 UTC are more suspicious
    tx_time = tx.timestamp.time()
    if time(0, 0) <= tx_time <= time(5, 0):
        risk_score += 15

    # Clamp score to [0, 100]
    risk_score = min(100, risk_score)

    # Persist transaction
    _transactions.append(tx)

    # Decision thresholds
    if risk_score >= 70:
        decision = "DECLINE"
    elif risk_score >= 40:
        decision = "REVIEW"
    else:
        decision = "APPROVE"

    return RiskResponse(risk_score=risk_score, decision=decision)


@app.get("/health")
def health() -> dict:
    """Health‑check endpoint to verify service availability."""
    return {"status": "ok"}
