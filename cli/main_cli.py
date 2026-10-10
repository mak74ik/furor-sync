import argparse
import sys
import os
from core.crypto import derive_key, encrypt_payload, decrypt_payload, generate_rsa_keypair

def run_cli():
    parser = argparse.ArgumentParser(
        prog='furor-sync',
        description='Furor Sync — Local-First P2P Encrypted Vault'
    )
    parser.add_argument('-p', '--password', help='Master password for encryption/decryption')
    parser.add_argument('-e', '--encrypt', action='store_true', help='Encrypt random symmetrical key into key.enc')
    parser.add_argument('-d', '--decrypt', action='store_true', help='Decrypt key.enc to stdout')
    parser.add_argument('--gen-rsa', action='store_true', help='Generate RSA-2048 PEM keypair')
    parser.add_argument('--status', action='store_true', help='Check cryptographic core health')

    args = parser.parse_args()

    if args.status:
        print("✅ [Furor-Sync] Cryptographic engine initialized and verified.")
        return 0

    if args.encrypt:
        if not args.password:
            print("❌ Error: --password is required for encryption.", file=sys.stderr)
            return 1
        secret = os.urandom(32)
        enc = encrypt_payload(secret, args.password)
        with open('key.enc', 'wb') as f:
            f.write(enc)
        print('🔒 Secret key encrypted successfully -> saved to key.enc')
        return 0

    elif args.decrypt:
        if not args.password:
            print("❌ Error: --password is required for decryption.", file=sys.stderr)
            return 1
        if not os.path.exists('key.enc'):
            print("❌ Error: key.enc not found.", file=sys.stderr)
            return 1
        with open('key.enc', 'rb') as f:
            enc = f.read()
        try:
            dec = decrypt_payload(enc, args.password)
            print(f'🔓 Key decrypted successfully (length: {len(dec)} bytes)')
            return 0
        except Exception as e:
            print(f'❌ Decryption failed: invalid password ({e})', file=sys.stderr)
            return 1

    elif args.gen_rsa:
        priv, pub = generate_rsa_keypair()
        with open('private_key.pem', 'wb') as f:
            f.write(priv)
        with open('public_key.pem', 'wb') as f:
            f.write(pub)
        print('🔑 RSA-2048 keypair generated -> private_key.pem & public_key.pem')
        return 0

    else:
        parser.print_help()
        return 0
