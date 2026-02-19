from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey, Ed25519PublicKey
)
from cryptography.hazmat.primitives import serialization
import base64

def generate_keypair():
    private_key = Ed25519PrivateKey.generate()
    public_key = private_key.public_key()
    return private_key, public_key

def sign(private_key, message: bytes) -> str:
    signature = private_key.sign(message)
    return base64.b64encode(signature).decode()

def verify(public_key, message: bytes, signature: str) -> bool:
    try:
        public_key.verify(
            base64.b64decode(signature.encode()),
            message
        )
        return True
    except Exception:
        return False
