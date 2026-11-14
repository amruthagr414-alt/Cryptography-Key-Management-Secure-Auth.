"""RSA-2048 key generation and RSA-PSS digital signatures."""
from pathlib import Path
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.exceptions import InvalidSignature

def generate_key_pair():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    return private_key, private_key.public_key()

def save_key_pair(private_key, private_path: str, public_path: str):
    Path(private_path).write_bytes(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(), # Demo only; protect file permissions.
    ))
    Path(public_path).write_bytes(private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    ))

def sign(message: bytes, private_key) -> bytes:
    return private_key.sign(
        message,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256(),
    )

def verify(message: bytes, signature: bytes, public_key) -> bool:
    try:
        public_key.verify(
            signature, message,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256(),
        )
        return True
    except InvalidSignature:
        return False

def main():
    private_key, public_key = generate_key_pair()
    message = b"Approved internship demonstration message"
    signature = sign(message, private_key)
    print("RSA key size:", private_key.key_size)
    print("Signature verification:", "PASS" if verify(message, signature, public_key) else "FAIL")
    print("Tampered message rejected:", not verify(message + b"!", signature, public_key))

if __name__ == "__main__":
    main()
