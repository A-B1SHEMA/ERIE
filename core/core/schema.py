from pydantic import BaseModel
from typing import List

class RiskSignals(BaseModel):
    pii_present: bool
    reidentification_score: float
    sensitivity_level: str

class DatasetUsageRequest(BaseModel):
    dataset_id: str
    intended_usage: str
    business_value: str
    risk_signals: RiskSignals
    policy_context: List[str]
