import json, time, hashlib, os
from security.crypto import sign
from blockchain.anchor import anchor_hash

def create_artifact(payload):
    payload["timestamp"] = int(time.time())
    raw = json.dumps(payload, sort_keys=True).encode()
    payload["hash"] = hashlib.sha256(raw).hexdigest()
    payload["signature"] = sign(raw)

    try:
        payload["chain_tx"] = anchor_hash(
            payload["hash"],
            os.getenv("CHAIN_ACCOUNT"),
            os.getenv("CHAIN_PRIVATE_KEY")
        )
    except Exception:
        payload["chain_tx"] = None

    return payload
