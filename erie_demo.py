from crypto import generate_keypair, sign

PRIVATE_KEY, PUBLIC_KEY = generate_keypair()

def make_artifact(payload):
    payload["timestamp"] = int(time.time())
    raw = json.dumps(payload, sort_keys=True).encode()
    payload["hash"] = hashlib.sha256(raw).hexdigest()
    payload["signature"] = sign(PRIVATE_KEY, raw)
    return payload
