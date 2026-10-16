"""R7-21 Keys generated INSIDE an HSM through PKCS#11. The key never leaves the device."""
import pkcs11
from pkcs11 import KeyType, Mechanism

lib = pkcs11.lib("/usr/lib/softhsm/libsofthsm2.so")
token = lib.get_token(token_label="qx-test")

with token.open(user_pin="1234", rw=True) as session:
    pub, priv = session.generate_keypair(KeyType.RSA, 2048, label="qx-signing")
    signature = priv.sign(b"payload", mechanism=Mechanism.SHA256_RSA_PKCS)
    ec_pub, ec_priv = session.generate_keypair(KeyType.EC, 256, label="qx-ec")
