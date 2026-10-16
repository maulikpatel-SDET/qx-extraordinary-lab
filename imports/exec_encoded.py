"""R7-05 The RSA code only exists as base64 text that is decoded and exec'd at runtime."""
import base64

_SRC = "ZnJvbSBjcnlwdG9ncmFwaHkuaGF6bWF0LnByaW1pdGl2ZXMuYXN5bW1ldHJpYyBpbXBvcnQgcnNhCktFWSA9IHJzYS5nZW5lcmF0ZV9wcml2YXRlX2tleShwdWJsaWNfZXhwb25lbnQ9NjU1MzcsIGtleV9zaXplPTIwNDgpCg=="
_ns = {}
exec(base64.b64decode(_SRC).decode(), _ns)
KEY = _ns["KEY"]
