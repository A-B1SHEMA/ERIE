from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
import base64

PRIVATE_KEY = Ed25519PrivateKey.generate()
PUBLIC_KEY = PRIVATE_KEY.public_key()

def sign(data: bytes) -> str:
    return base64.b64encode(PRIVATE_KEY.sign(data)).decode()
