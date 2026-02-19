def compute_risk(reid, sens, pii):
    return min(0.6 * reid + 0.4 * sens + (0.2 if pii else 0), 1.0)
