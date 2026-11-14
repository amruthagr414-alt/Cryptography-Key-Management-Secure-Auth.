# Cryptography, Key Management & Secure Authentication

A defensive Python demonstration project covering authenticated encryption, asymmetric digital signatures, message authentication, password hashing, and key-management practices.

## Features
- AES-256-GCM authenticated encryption with a fresh random 96-bit nonce for each encryption.
- RSA 2048-bit key-pair generation and RSA-PSS/SHA-256 digital signatures.
- HMAC-SHA256 generation and constant-time verification.
- bcrypt password hashing with a configurable work factor.
- Key-storage, rotation, and operational security guidance.

## Requirements
- Python 3.10+
- Install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate        # macOS/Linux
pip install -r requirements.txt
```

## Run the demonstrations

```bash
python -m src.demo
```

The demo generates temporary keys and sample outputs locally. It does not contact a server or transmit secrets.

## Individual utilities

```bash
python -m src.aes_gcm
python -m src.rsa_sign
python -m src.hmac_utils
python -m src.passwords
```

## Important security notes
- The included demo uses generated local demonstration keys. Do not use these files or sample secrets in production.
- AES-GCM nonces must never be reused with the same key. This project generates a fresh random nonce for each encryption.
- Never commit private keys, `.env` files, passwords, production secrets, or real user data.
- For production, use a managed KMS/HSM or a secrets manager, access controls, audit logs, and a documented rotation process.
- Passwords are hashed with bcrypt, not encrypted. Never store plaintext passwords.
- HMAC keys must be random, secret, and separate from encryption keys.

## Evidence checklist
See [`evidence/README.md`](evidence/README.md). Run the scripts yourself and add genuine terminal screenshots or captured output before submitting.

## Repository structure

```text
.
├── src/
│   ├── aes_gcm.py
│   ├── rsa_sign.py
│   ├── hmac_utils.py
│   ├── passwords.py
│   └── demo.py
├── docs/
│   ├── SECURITY_BEST_PRACTICES.md
│   └── ALGORITHM_NOTES.md
├── keys/                  # generated key files are ignored by Git
├── evidence/
├── requirements.txt
├── .gitignore
└── README.md
```

## Disclaimer
For education and authorized defensive development only. This repository is a demonstration, not a production cryptographic library or a substitute for a security review.
