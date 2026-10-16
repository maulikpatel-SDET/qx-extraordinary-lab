"""R7-02 The function itself is imported under a neutral name."""
from cryptography.hazmat.primitives.asymmetric.rsa import generate_private_key as make_key

key = make_key(public_exponent=65537, key_size=2048)
