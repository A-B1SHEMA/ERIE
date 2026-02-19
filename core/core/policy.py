import yaml

def load_policy(name: str):
    with open(f"policies/{name.lower()}.yaml") as f:
        return yaml.safe_load(f)
