# Algorithm Notes

| Component | Configuration in this demo | Security purpose |
|---|---|---|
| AES | AES-256-GCM, 12-byte random nonce | Confidentiality and authenticated integrity |
| RSA | 2048-bit key, RSA-PSS, SHA-256 | Digital signatures and verification |
| HMAC | HMAC-SHA256, 32-byte random key | Message authentication/integrity |
| Password hashing | bcrypt, work factor 12 by default | Slow salted password verification |

## Important distinctions
- Encryption is reversible with the correct key; password hashing is intentionally one-way.
- HMAC uses a shared secret and proves message authenticity to parties holding that secret; it is not a public-key digital signature.
- A digital signature can be verified with a public key and is distinct from encryption.
- AES-GCM authentication failure must stop processing. Do not ignore invalid-tag errors.
- Nonces do not need to be secret, but uniqueness per AES-GCM key is critical.
