"""R7-12 RSA with public exponent 3 (weak parameter, allowed by the library)."""
from cryptography.hazmat.primitives.asymmetric import rsa

key = rsa.generate_private_key(public_exponent=3, key_size=2048)
