"""R7-01 Wildcard import: no 'rsa.' prefix anywhere at the call."""
from cryptography.hazmat.primitives.asymmetric.rsa import *  # noqa: F403

key = test
