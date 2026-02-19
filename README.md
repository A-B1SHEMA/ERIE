# ERIE — Dataset Usage Gating Demo

ERIE is a policy-aligned decision engine that controls whether datasets
can be used for analytics or AI — without accessing the data itself.

## What This Demo Shows
- Dataset usage request
- Risk/value evaluation
- Deterministic decision (approve / restrict / reject)
- Enforceable decision artifact with audit hash

## Run Locally

```bash
pip install -r requirements.txt
uvicorn erie_demo:app --reload
