"""R7-01 Wildcard import: no 'rsa.' prefix anywhere at the call."""
from cryptography.hazmat.primitives.asymmetric.rsa import *  # noqa: F403

key = generate_private_key(public_exponent=65537, key_size=2048)  # noqa: F405
