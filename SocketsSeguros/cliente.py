from socket import *
import hashlib
import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

KEY = b'0123456789abcdef0123456789abcdef'

serverName = "127.0.0.1"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input("Digite uma mensagem: ").encode()

padder = padding.PKCS7(128).padder()
padded_data = padder.update(message) + padder.finalize()

iv = os.urandom(16)

cipher = Cipher(algorithms.AES(KEY), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded_data) + encryptor.finalize()

hash_value = hashlib.sha256(ciphertext).digest()

packet = iv + hash_value + ciphertext

clientSocket.sendto(packet, (serverName, serverPort))
print("Mensagem enviada com segurança!")

clientSocket.close()