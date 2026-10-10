import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

def derive_key(password: str, salt: bytes = b'furor_sync_salt_2026') -> bytes:
    """Derives a secure 32-byte Fernet key from password via PBKDF2-HMAC-SHA256."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt_payload(data: bytes, password: str) -> bytes:
    """Encrypts payload bytes using Fernet derived from master password."""
    fernet = Fernet(derive_key(password))
    return fernet.encrypt(data)

def decrypt_payload(encrypted_data: bytes, password: str) -> bytes:
    """Decrypts payload bytes using master password."""
    fernet = Fernet(derive_key(password))
    return fernet.decrypt(encrypted_data)

def generate_rsa_keypair():
    """Generates 2048-bit RSA public/private keypair in PEM format."""
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
    public_pem = private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return private_pem, public_pem
