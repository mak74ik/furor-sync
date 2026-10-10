import argparse
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

def generate_key(password):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b'salt',
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

def encrypt_key(key, password):
    fernet = Fernet(generate_key(password))
    encrypted_key = fernet.encrypt(key)
    return encrypted_key

def decrypt_key(encrypted_key, password):
    fernet = Fernet(generate_key(password))
    decrypted_key = fernet.decrypt(encrypted_key)
    return decrypted_key

def generate_rsa_key():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_key = private_key.public_key()
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return private_pem, public_pem

def main():
    parser = argparse.ArgumentParser(description='Furor-sync')
    parser.add_argument('-p', '--password', help='password for encryption')
    parser.add_argument('-k', '--key', help='key file')
    parser.add_argument('-e', '--encrypt', action='store_true', help='encrypt key')
    parser.add_argument('-d', '--decrypt', action='store_true', help='decrypt key')
    args = parser.parse_args()

    if args.encrypt:
        key = os.urandom(32)
        encrypted_key = encrypt_key(key, args.password)
        with open('key.txt', 'wb') as f:
            f.write(encrypted_key)
        print('Key encrypted and saved to key.txt')

    elif args.decrypt:
        with open('key.txt', 'rb') as f:
            encrypted_key = f.read()
        decrypted_key = decrypt_key(encrypted_key, args.password)
        print('Key decrypted')

    elif args.password:
        private_pem, public_pem = generate_rsa_key()
        with open('private_key.pem', 'wb') as f:
            f.write(private_pem)
        with open('public_key.pem', 'wb') as f:
            f.write(public_pem)
        print('RSA keys generated and saved to private_key.pem and public_key.pem')

if __name__ == '__main__':
    main()