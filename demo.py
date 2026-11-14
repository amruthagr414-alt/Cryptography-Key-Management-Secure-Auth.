"""Run all cryptographic utility demonstrations."""
from src.aes_gcm import main as aes_main
from src.rsa_sign import main as rsa_main
from src.hmac_utils import main as hmac_main
from src.passwords import main as password_main

if __name__ == "__main__":
    print("\\n=== AES-256-GCM ===")
    aes_main()
    print("\\n=== RSA-2048 / Digital Signature ===")
    rsa_main()
    print("\\n=== HMAC-SHA256 ===")
    hmac_main()
    print("\\n=== bcrypt Password Hashing ===")
    password_main()
