from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
import os

# Abrir o arquivo criptografado
file_name = "teste.txt.ransomwaretroll"
with open(file_name, "rb") as file:
    encrypted_data = file.read()

# Carregar a chave privada RSA
with open("private_key.pem", "rb") as private_key_file:
    private_key = serialization.load_pem_private_key(
        private_key_file.read(),
        password=None,
        backend=default_backend()
    )

# Descriptografar o arquivo com a chave privada RSA
decrypted_data = private_key.decrypt(
    encrypted_data,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Remover o arquivo criptografado
os.remove(file_name)

# Criar o arquivo descriptografado
new_file_name = "teste.txt"
with open(new_file_name, "wb") as new_file:
    new_file.write(decrypted_data)
