# furor-sync

A local-first encrypted file vault and cryptographic key manager using Fernet (AES-128-CBC with HMAC-SHA256 authentication), PBKDF2-HMAC-SHA256 key derivation, and RSA-2048 asymmetric key generation.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python: 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Cryptography: Fernet / RSA](https://img.shields.io/badge/crypto-Fernet%20%7C%20RSA--2048-green.svg)](#)

---

## Features

- **Fernet Payload Encryption**: Symmetrical encryption using 128-bit AES in CBC mode with PKCS7 padding and HMAC-SHA256 for integrity verification.
- **PBKDF2 Key Derivation**: Derives strong 32-byte encryption keys from user passwords with 100,000 SHA-256 iterations.
- **RSA-2048 Keypair Generation**: Generates standard PKCS#8 private and SubjectPublicKeyInfo public keys in PEM format for asymmetric key agreement.
- **Zero Cloud Footprint**: Operates entirely offline on the local filesystem.

---

## Quickstart

### 1. Requirements
```bash
pip install cryptography
```

### 2. Check Engine Health
```bash
python3 main.py --status
```

### 3. Encrypt a Symmetric Secret
```bash
python3 main.py -e -p "your-master-passphrase"
```
Output:
```text
🔒 Secret key encrypted successfully -> saved to key.enc
```

### 4. Decrypt the Secret
```bash
python3 main.py -d -p "your-master-passphrase"
```

### 5. Generate RSA-2048 Keypair
```bash
python3 main.py --gen-rsa
```
Creates `private_key.pem` and `public_key.pem`.

---

## Testing

Run unit tests:
```bash
python3 -m unittest discover -s tests
```

---

## License

[MIT License](LICENSE)
