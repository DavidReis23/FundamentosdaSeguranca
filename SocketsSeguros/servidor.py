from socket import *
import hashlib
import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

KEY = b'0123456789abcdef0123456789abcdef'

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("Servidor seguro está pronto para receber...")

while True:
    data, clientAddress = serverSocket.recvfrom(4096)

    iv = data[:16]
    received_hash = data[16:48]
    ciphertext = data[48:]

    calculated_hash = hashlib.sha256(ciphertext).digest()

    if calculated_hash != received_hash:
        print("⚠️ Mensagem descartada! Integridade comprometida.")
        continue

    cipher = Cipher(algorithms.AES(KEY), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_message = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    message = unpadder.update(padded_message) + unpadder.finalize()

    print("Mensagem recebida (texto claro):", message.decode())