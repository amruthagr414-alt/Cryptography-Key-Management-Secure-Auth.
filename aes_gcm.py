"""AES-256-GCM authenticated encryption helpers."""
import os
import base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

KEY_SIZE = 32       # 256 bits
NONCE_SIZE = 12     # 96 bits, recommended for GCM

def generate_key() -> bytes:
    """Generate a cryptographically secure 256-bit AES key."""
    return AESGCM.generate_key(bit_length=256)

def encrypt(plaintext: bytes, key: bytes, associated_data: bytes | None = None) -> dict:
    """Encrypt bytes; returns nonce and ciphertext (ciphertext includes GCM tag)."""
    if len(key) != KEY_SIZE:
        raise ValueError("AES-256 requires a 32-byte key")
    nonce = os.urandom(NONCE_SIZE)
    ciphertext = AESGCM(key).encrypt(nonce, plaintext, associated_data)
    return {
        "nonce_b64": base64.b64encode(nonce).decode("ascii"),
        "ciphertext_b64": base64.b64encode(ciphertext).decode("ascii"),
    }

def decrypt(envelope: dict, key: bytes, associated_data: bytes | None = None) -> bytes:
    """Decrypt and authenticate; raises InvalidTag if ciphertext/AAD is altered."""
    nonce = base64.b64decode(envelope["nonce_b64"], validate=True)
    ciphertext = base64.b64decode(envelope["ciphertext_b64"], validate=True)
    if len(nonce) != NONCE_SIZE:
        raise ValueError("Invalid AES-GCM nonce length")
    return AESGCM(key).decrypt(nonce, ciphertext, associated_data)

def main():
    key = generate_key()
    message = b"Cryptography internship demonstration"
    envelope = encrypt(message, key, associated_data=b"task4-demo")
    recovered = decrypt(envelope, key, associated_data=b"task4-demo")
    print("AES-256-GCM encryption/decryption: PASS")
    print("Recovered plaintext:", recovered.decode())

if __name__ == "__main__":
    main()
