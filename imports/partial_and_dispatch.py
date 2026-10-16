"""R7-04 functools.partial pre-binds the key size; the callable is stored in a dict and called later."""
import functools

from cryptography.hazmat.primitives.asymmetric import ec, rsa

FACTORIES = {
    "rsa2048": functools.partial(rsa.generate_private_key, 65537, 2048),
    "p384": functools.partial(ec.generate_private_key, ec.SECP384R1()),
}


def build(name: str):
    return FACTORIES[name]()
