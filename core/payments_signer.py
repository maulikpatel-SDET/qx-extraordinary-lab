"""R7-30 Own production code, but .gitattributes marks core/ as vendored."""
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec

key = ec.generate_private_key(ec.SECP256R1())
sig = key.sign(b"payment", ec.ECDSA(hashes.SHA256()))
