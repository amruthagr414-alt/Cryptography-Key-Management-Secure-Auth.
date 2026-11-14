# Cryptography, Key Management & Secure Authentication — Project Report

## Objective
Demonstrate common defensive cryptographic building blocks in Python: authenticated symmetric encryption, public-key digital signatures, message authentication, and secure password hashing.

## Implementation
- AES-256-GCM: random 12-byte nonce, ciphertext with authentication tag, optional associated authenticated data.
- RSA-2048: generated key pair and RSA-PSS/SHA-256 signature verification.
- HMAC-SHA256: message tag generation and constant-time comparison.
- bcrypt: per-password salt and work factor 12 by default.

## Validation plan
Run `python -m src.demo`. Confirm that valid ciphertext/signatures/tags/passwords are accepted and tampered or incorrect inputs are rejected. Record actual outputs and screenshots in `evidence/`.

## Key-management controls
The security guide recommends KMS/HSM or secrets manager storage, least privilege, key separation, rotation, audit logging, and incident response.

## Results
Not yet recorded. Populate this section only after running the code and observing the actual results. Attach genuine evidence in `evidence/`.

## Limitations
This is an educational implementation using established Python libraries. It is not a production key-management service and does not implement a KMS, certificate authority, user database, rate limiter, MFA, or a full key-rotation service.
