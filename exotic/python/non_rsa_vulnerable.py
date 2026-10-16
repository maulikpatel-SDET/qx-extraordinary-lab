"""R7-19 Quantum-vulnerable algorithms that are NOT RSA/ECC by name:
Paillier (factoring, like RSA), BLS signatures (pairing-based), ElGamal and classic DSA (discrete log)."""
from Crypto.PublicKey import ElGamal
from Crypto.Random import get_random_bytes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa
from phe import paillier
from py_ecc.bls import G2ProofOfPossession as bls

pub, priv = paillier.generate_paillier_keypair(n_length=2048)        # Paillier homomorphic encryption
enc_total = pub.encrypt(42)

bls_sk = bls.KeyGen(b"\x01" * 32)                                     # BLS12-381 signature
bls_sig = bls.Sign(bls_sk, b"block-123")

elg = ElGamal.generate(2048, get_random_bytes)                        # ElGamal

dsa_key = dsa.generate_private_key(key_size=2048)                     # classic finite-field DSA
dsa_sig = dsa_key.sign(b"x", hashes.SHA256())
