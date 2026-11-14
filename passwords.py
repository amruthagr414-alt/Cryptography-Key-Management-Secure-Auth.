"""bcrypt password hashing and verification."""
import bcrypt

DEFAULT_ROUNDS = 12

def hash_password(password: str, rounds: int = DEFAULT_ROUNDS) -> bytes:
    if not isinstance(password, str) or not password:
        raise ValueError("Password must be a non-empty string")
    if not 4 <= rounds <= 16:
        raise ValueError("Demo work factor must be between 4 and 16")
    salt = bcrypt.gensalt(rounds=rounds)
    return bcrypt.hashpw(password.encode("utf-8"), salt)

def verify_password(password: str, stored_hash: bytes) -> bool:
    try:
        return bcrypt.checkpw(password.encode("utf-8"), stored_hash)
    except (ValueError, TypeError):
        return False

def main():
    sample_password = "Example-Only-Password-Change-Me"
    stored = hash_password(sample_password)
    print("bcrypt work factor:", stored.decode().split("$")[2])
    print("Correct password accepted:", verify_password(sample_password, stored))
    print("Incorrect password rejected:", not verify_password("wrong-password", stored))

if __name__ == "__main__":
    main()
