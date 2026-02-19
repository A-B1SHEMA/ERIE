from fastapi import FastAPI
from core.schema import DatasetUsageRequest
from core.normalize import *
from core.risk import compute_risk
from core.policy import load_policy
from core.hamiltonian import compute_hamiltonian
from core.decision import map_decision
from core.explain import generate_explanation
from core.artifact import create_artifact

app = FastAPI(title="ERIE")

@app.post("/check_dataset_usage")
def check_dataset(req: DatasetUsageRequest):

    reid = norm_reid(req.risk_signals.reidentification_score)
    sens = norm_sensitivity(req.risk_signals.sensitivity_level)
    value = norm_value(req.business_value)

    risk = compute_risk(reid, sens, req.risk_signals.pii_present)
    control_cost = 0.2

    policy = load_policy(req.policy_context[0])
    score = compute_hamiltonian(risk, value, control_cost, policy)
    decision = map_decision(score, policy["thresholds"])

    artifact = create_artifact({
        "dataset_id": req.dataset_id,
        "decision": decision,
        "risk": round(risk,2),
        "value": round(value,2),
        "score": round(score,2),
        "conditions": ["NO_EXPORT"] if decision == "RESTRICTED" else []
    })

    return artifact
