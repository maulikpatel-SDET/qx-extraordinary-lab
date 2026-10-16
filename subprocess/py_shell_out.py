"""R7-15 Keys created by calling external tools from Python (no crypto library imported)."""
import os
import subprocess

subprocess.run(["openssl", "genrsa", "-out", "app.key", "2048"], check=True)
subprocess.run("openssl ecparam -name prime256v1 -genkey -noout -out ec.key", shell=True, check=True)
os.system("ssh-keygen -t rsa -b 2048 -N '' -f deploy_key")
subprocess.check_call(["gpg", "--batch", "--quick-generate-key", "ci@qx.example.com", "rsa3072", "sign", "1y"])
