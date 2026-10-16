"""R7-03 Module loaded with __import__(..., fromlist=...)."""
_rsa = __import__("cryptography.hazmat.primitives.asymmetric.rsa", fromlist=["generate_private_key"])
key = _rsa.generate_private_key(public_exponent=65537, key_size=2048)
