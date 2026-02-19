def generate_explanation(risk, value):
    reasons = []
    if risk > 0.6:
        reasons.append("High privacy risk")
    if value > 0.7:
        reasons.append("High business value")
    return reasons or ["Balanced risk-value profile"]
