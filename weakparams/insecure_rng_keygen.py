"""R7-13 RSA key generated from a NON-cryptographic, seeded random source -> predictable key."""
import random

from Crypto.PublicKey import RSA

rng = random.Random(1234)                      # fixed seed, Mersenne Twister


def predictable_bytes(n: int) -> bytes:
    return bytes(rng.getrandbits(8) for _ in range(n))


key = RSA.generate(2048, randfunc=predictable_bytes)
