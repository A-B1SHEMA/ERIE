import requests

res = requests.post(
    "http://127.0.0.1:8000/check_dataset_usage",
    json={
        "dataset_id": "healthcare_2024",
        "intended_usage": "analytics",
        "business_value": "high",
        "risk_signals": {
            "pii_present": True,
            "reidentification_score": 55,
            "sensitivity_level": "moderate"
        },
        "policy_context": ["HIPAA"]
    }
).json()

if res["decision"] == "REJECTED":
    raise Exception("❌ BLOCKED")

print("✅ JOB ALLOWED:", res["decision"])
