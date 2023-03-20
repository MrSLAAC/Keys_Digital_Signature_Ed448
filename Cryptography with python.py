from cryptography.hazmat.primitives.asymmetric.ed448 import (
    Ed448PrivateKey,
    Ed448PublicKey,
)
from cryptography.hazmat.primitives import serialization


private_key = Ed448PrivateKey.generate()
public_key = private_key.public_key()


private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.Raw,
    format=serialization.PrivateFormat.Raw,
    encryption_algorithm=serialization.NoEncryption()
)

with open('private_key.pem', 'wb') as f:
    f.write(private_pem)

public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.Raw,
    format=serialization.PublicFormat.Raw,
)
with open('public_key.pem', 'wb') as f:
    f.write(public_pem)


with open("private_key.pem", "rb") as key_file:
    private_key = Ed448PrivateKey.from_private_bytes(key_file.read())

with open("public_key.pem", "rb") as key_file:
    public_key = Ed448PublicKey.from_public_bytes(key_file.read())
