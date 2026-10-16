"""R7-07 FALSE-POSITIVE TRAP: RSA types imported only for type hints. No crypto runs."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey


def describe(key: RSAPrivateKey) -> str:
    return f"key of {key.key_size} bits"
