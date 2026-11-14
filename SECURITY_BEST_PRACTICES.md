# Secure Key, Secret and Password Management

## 1. Secret storage
- Prefer a managed Key Management Service (KMS), Hardware Security Module (HSM), or reputable secrets manager.
- Restrict access using least privilege, workload identity, and role-based access controls.
- Do not hard-code secrets or place them in source control, chat messages, logs, screenshots, or client-side code.
- For local development, use environment variables or a local secret store; keep `.env` out of Git and restrict file permissions.
- Encrypt backups and limit who can restore them.

## 2. Key separation and purpose
- Use independent random keys for AES encryption and HMAC authentication.
- Do not reuse an AES-GCM key as an HMAC key.
- Keep private signing keys private; distribute public keys through an authenticated channel and validate their fingerprints.
- Prefer envelope encryption: data-encryption keys protect data and a KMS-managed key-encryption key protects the data keys.

## 3. Rotation
1. Maintain an inventory of keys, owners, purpose, creation date, and expiry/review date.
2. Define rotation intervals based on risk, policy, and applicable standards.
3. Create a new key in the KMS/secret manager and grant only required services access.
4. Update applications to use the new key; version key identifiers with encrypted data where appropriate.
5. For decryption, retain old key versions only as long as required to decrypt existing data.
6. Re-encrypt or re-wrap stored data where required, then disable and securely retire old keys.
7. Record approvals, timestamps, access, and completion in an audit log.
8. Rotate immediately after suspected exposure; investigate scope and revoke compromised credentials.

## 4. AES-GCM
- Use AES-256-GCM through a vetted cryptographic library.
- Generate a fresh, unpredictable 96-bit nonce for every encryption under a given key. Never reuse a nonce with the same key.
- Store the nonce alongside ciphertext; it is not secret.
- Use associated data (AAD) for metadata that must be authenticated but not encrypted.
- Treat authentication failure as a hard failure; never use unauthenticated plaintext.

## 5. RSA signatures
- This project uses RSA-2048 with RSA-PSS and SHA-256.
- Protect private keys with KMS/HSM where possible and restrict access.
- Verify signatures with a trusted public key and a well-defined key-distribution process.
- Plan cryptographic agility: key sizes and algorithms should be reviewed against current organizational policy.

## 6. Passwords
- Store salted bcrypt hashes, never plaintext passwords or reversible encrypted passwords.
- Choose a work factor that is as high as practical while keeping authentication latency acceptable; benchmark on deployment hardware and review periodically.
- Use rate limiting, MFA, secure password reset, and breach monitoring alongside password hashing.
- Do not log passwords, hashes, reset tokens, or authentication secrets.
- bcrypt has input-length constraints; applications should follow the library's current guidance and avoid unsafe ad-hoc pre-hashing.

## 7. Incident response
- Revoke or disable exposed keys and tokens.
- Rotate affected credentials and assess logs for unauthorized use.
- Determine which data may have been exposed and notify the responsible security owner.
- Document the incident, root cause, remediation, and lessons learned.
