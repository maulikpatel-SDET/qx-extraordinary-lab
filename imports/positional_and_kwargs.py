"""R7-08 Key size passed positionally and via a **kwargs dict (no 'key_size=' keyword at the call)."""
from cryptography.hazmat.primitives.asymmetric import rsa

positional = rsa.generate_private_key(65537, 1024)          # 2nd positional arg = key_size (weak)
PARAMS = {"public_exponent": 65537, "key_size": 3072}
from_dict = rsa.generate_private_key(**PARAMS)
