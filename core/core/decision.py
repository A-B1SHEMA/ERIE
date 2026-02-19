def map_decision(score, thresholds):
    if score < thresholds["approve"]:
        return "APPROVED"
    elif score < thresholds["restrict"]:
        return "RESTRICTED"
    return "REJECTED"
