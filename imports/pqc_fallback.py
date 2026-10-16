"""R7-06 Graceful degradation: try PQC, silently fall back to RSA if the library is missing."""
try:
    import oqs

    def new_signer():
        return oqs.Signature("ML-DSA-65")
    MODE = "pqc"
except ImportError:                       # very common in real code
    from cryptography.hazmat.primitives.asymmetric import rsa

    def new_signer():
        return rsa.generate_private_key(public_exponent=65537, key_size=2048)
    MODE = "classical-fallback"

PREFERENCE = ["ML-DSA-65", "RSA-2048"]     # negotiation order, classical still accepted
