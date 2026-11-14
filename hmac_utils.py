"""HMAC-SHA256 creation and verification."""
import hmac
import hashlib
import secrets
import base64

def generate_key() -> bytes:
    return secrets.token_bytes(32)

def create_tag(message: bytes, key: bytes) -> str:
    tag = hmac.new(key, message, hashlib.sha256).digest()
    return base64.b64encode(tag).decode("ascii")

def verify_tag(message: bytes, key: bytes, supplied_tag_b64: str) -> bool:
    try:
        supplied = base64.b64decode(supplied_tag_b64, validate=True)
    except Exception:
        return False
    expected = hmac.new(key, message, hashlib.sha256).digest()
    return hmac.compare_digest(expected, supplied)

def main():
    key = generate_key()
    message = b"Authenticate this message"
    tag = create_tag(message, key)
    print("HMAC-SHA256 verification:", "PASS" if verify_tag(message, key, tag) else "FAIL")
    print("Tampered message rejected:", not verify_tag(message + b"!", key, tag))

if __name__ == "__main__":
    main()
