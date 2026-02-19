def compute_hamiltonian(risk, value, cost, p):
    return p["alpha"] * risk - p["beta"] * value + p["gamma"] * cost
