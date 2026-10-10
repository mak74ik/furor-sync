import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import unittest
import os
from core.crypto import derive_key, encrypt_payload, decrypt_payload, generate_rsa_keypair

class TestFurorCrypto(unittest.TestCase):
    def test_encryption_roundtrip(self):
        password = "SuperSecret2026!"
        original = b"Sample P2P local file data packet"
        encrypted = encrypt_payload(original, password)
        self.assertNotEqual(original, encrypted)

        decrypted = decrypt_payload(encrypted, password)
        self.assertEqual(original, decrypted)

    def test_rsa_keypair_generation(self):
        priv, pub = generate_rsa_keypair()
        self.assertTrue(priv.startswith(b'-----BEGIN PRIVATE KEY-----'))
        self.assertTrue(pub.startswith(b'-----BEGIN PUBLIC KEY-----'))

if __name__ == '__main__':
    unittest.main()
