"""R7-14 AES-256-GCM with ONE fixed nonce reused for every message (breaks GCM)."""
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

KEY = AESGCM.generate_key(bit_length=256)
NONCE = b"\x00" * 12


def seal(msg: bytes) -> bytes:
    return AESGCM(KEY).encrypt(NONCE, msg, None)
