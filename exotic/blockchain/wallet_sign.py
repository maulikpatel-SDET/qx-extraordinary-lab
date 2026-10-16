"""R7-20 Off-chain side: Ethereum account (secp256k1) signs the order the contract verifies."""
from eth_account import Account
from eth_account.messages import encode_defunct

acct = Account.create()                                   # secp256k1 private key
signed = acct.sign_message(encode_defunct(text="order-123"))
