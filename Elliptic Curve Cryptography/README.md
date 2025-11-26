# Elliptic Curve Cryptography (ECC)

This repository provides a complete implementation of Elliptic Curve Cryptography, demonstrating the mathematics behind modern secure communications used by billions daily.

## Problem Description

Elliptic Curve Cryptography is based on the algebraic structure of elliptic curves over finite fields. An elliptic curve is defined by the equation:

```text
y² = x³ + ax + b
```

Points on this curve, combined with a special "point at infinity" (O), form an abelian group under a geometric operation called "point addition."

**Why ECC matters:**

- **Smaller Keys**: 256-bit ECC provides security equivalent to 3072-bit RSA
- **Faster Operations**: More efficient computation
- **Lower Power**: Perfect for mobile and IoT devices
- **Modern Standard**: Used in Bitcoin, TLS 1.3, Signal, WhatsApp

## Mathematical Foundation

### Point Addition Rules

For points P = (x₁, y₁) and Q = (x₂, y₂) on the curve:

1. **Point at Infinity**: P + O = P (O is the identity element)

2. **Inverse**: P + (-P) = O where -P = (x₁, -y₁)

3. **Different Points** (P ≠ Q):

   ```text
   λ = (y₂ - y₁) / (x₂ - x₁)
   x₃ = λ² - x₁ - x₂
   y₃ = λ(x₁ - x₃) - y₁
   ```

4. **Point Doubling** (P = Q):

   ```text
   λ = (3x₁² + a) / (2y₁)
   x₃ = λ² - 2x₁
   y₃ = λ(x₁ - x₃) - y₁
   ```

### Scalar Multiplication

The most important operation in ECC:

```text
nP = P + P + ... + P (n times)
```

This is computed efficiently using the "double-and-add" algorithm in O(log n) time.

**The Discrete Logarithm Problem**: Given P and Q = nP, finding n is computationally infeasible for properly chosen curves. This is the foundation of ECC security.

## Implementation Features

### 1. Core Elliptic Curve Operations

- **Point Addition**: Add two points on the curve
- **Point Doubling**: Efficiently compute 2P
- **Scalar Multiplication**: Compute nP using double-and-add
- **Point Validation**: Verify points lie on the curve

### 2. ECDSA (Elliptic Curve Digital Signature Algorithm)

- **Key Generation**: Create public/private key pairs
- **Signature Generation**: Sign messages
- **Signature Verification**: Verify signatures
- **Hash Integration**: Uses SHA-256 for message hashing

### 3. ECDH (Elliptic Curve Diffie-Hellman)

- **Shared Secret**: Two parties establish common secret
- **Perfect Forward Secrecy**: Each session uses new keys
- **No Key Exchange**: Secret never transmitted

### 4. Popular Curves

- **secp256k1**: Used by Bitcoin, Ethereum
- **P-256 (secp256r1)**: NIST standard, used in TLS
- **Curve25519**: Modern, high-security curve

### 5. Security Features

- **Random Nonce Generation**: Critical for signature security
- **Point Compression**: Efficient storage (33 bytes vs 65 bytes)
- **Constant-Time Operations**: Resists timing attacks
- **Input Validation**: Prevents invalid curve attacks

## How It Works

The program demonstrates:

1. **Basic Curve Operations**: Point addition, doubling, scalar multiplication
2. **Key Generation**: Creating cryptographically secure keypairs
3. **Digital Signatures**: Sign and verify messages with ECDSA
4. **Key Exchange**: ECDH for shared secret establishment
5. **Real-World Curves**: Operations on secp256k1 and P-256

## Algorithm Complexity

- **Point Addition**: O(1) field operations
- **Scalar Multiplication**: O(log n) using double-and-add
- **Signature Generation**: O(log n) dominated by scalar multiplication
- **Signature Verification**: O(log n) with two scalar multiplications

## Usage

Run the demonstration:

```bash
python elliptic_curve_crypto.py
```

The program will:

- Demonstrate point operations on toy and real curves
- Generate ECDSA keypairs
- Sign and verify messages
- Perform ECDH key exchange
- Show why ECC is secure

## Example Output

```text
Elliptic Curve Cryptography
============================================================

Curve Parameters (secp256k1 - Bitcoin's curve):
p = 115792089237316195423570985008687907853269984665640564039457584007908834671663
a = 0
b = 7
G = Generator point
n = 115792089237316195423570985008687907852837564279074904382605163141518161494337

Point Operations Demo:
P = (x1, y1)
Q = (x2, y2)
P + Q = (x3, y3)
2P = (x4, y4)

ECDSA Digital Signature:
Private Key: 0x7a84b3c21f...
Public Key:  (0x8b3f7c2d..., 0x4e6a9f1b...)
Message: "Transfer 1 BTC to Alice"
Signature: (r, s)
Verification: ✓ Valid

ECDH Key Exchange:
Alice's Public Key: (0x1a2b3c..., 0x4d5e6f...)
Bob's Public Key:   (0x7g8h9i..., 0x0j1k2l...)
Shared Secret:      0x9d8f7e6c5b4a39281...
Both parties computed the same secret without transmitting it!
```

## Requirements

- Python 3.7+
- No external dependencies (uses only standard library)
- `hashlib` for SHA-256 hashing
- `secrets` for cryptographically secure random numbers

## Real-World Applications

### Bitcoin & Cryptocurrency

- **secp256k1 curve**: All Bitcoin transactions use ECDSA
- **Address Generation**: Public key → Bitcoin address
- **Transaction Signing**: Proves ownership of funds
- **Schnorr Signatures**: New upgrade to Bitcoin

### TLS/SSL (HTTPS)

- **P-256 curve**: Most common for web security
- **ECDHE**: Elliptic Curve Diffie-Hellman Ephemeral
- **Perfect Forward Secrecy**: Past communications stay secure
- **Certificate Signatures**: CA signs certificates with ECDSA

### Messaging Apps (Signal, WhatsApp)

- **X25519**: Key exchange (based on Curve25519)
- **Ed25519**: Digital signatures
- **End-to-End Encryption**: Only sender and recipient can decrypt
- **Double Ratchet**: Uses ECC for key derivation

### IoT & Embedded Systems

- **Low Power**: ECC requires less computation than RSA
- **Small Keys**: Fits in constrained memory
- **Fast**: Critical for real-time systems
- **Smart Cards**: ECDSA fits in small chips

## Security Considerations

### Why ECC is Secure

1. **Discrete Logarithm Problem**: No efficient algorithm exists for general curves
2. **Key Size**: 256-bit ECC ≈ 3072-bit RSA ≈ 128-bit security level
3. **Mathematical Structure**: Group operations on curves are one-way functions

### Common Vulnerabilities (and how to avoid them)

1. **Weak Random Numbers**: Use `secrets` module, never pseudo-random
2. **Nonce Reuse**: Each signature needs unique k (Sony PS3 hack!)
3. **Invalid Curve Attacks**: Always validate points are on the curve
4. **Timing Attacks**: Use constant-time implementations in production
5. **Small Subgroup Attacks**: Verify curve parameters

### Curves to Avoid

- **Small Fields**: p < 2²⁵⁶ is too small
- **Singular Curves**: Must satisfy 4a³ + 27b² ≠ 0
- **Unknown Parameters**: Only use standardized curves

## Comparison with RSA

| Property | ECC (256-bit) | RSA (3072-bit) |
|----------|---------------|----------------|
| Security Level | 128-bit | 128-bit |
| Key Size | 256 bits | 3072 bits |
| Signature Size | 512 bits | 3072 bits |
| Key Generation | Fast | Slow |
| Signing | Fast | Slow |
| Verification | Medium | Fast |

**Verdict**: ECC is faster, uses less bandwidth, and is more future-proof.

## Mathematical Depth

### Why Elliptic Curves?

1. **Abelian Group**: Satisfies closure, associativity, identity, inverse
2. **Smooth Curves**: No cusps or self-intersections (discriminant ≠ 0)
3. **Finite Field**: Operations modulo prime p for computational efficiency
4. **Point Counting**: Group order determined by Schoof's algorithm

### Advanced Topics (not implemented here)

- **Pairing-Based Cryptography**: BLS signatures, zk-SNARKs
- **Edwards Curves**: Faster, complete addition formulas
- **Isogeny-Based Crypto**: Potential post-quantum security
- **Elliptic Curve Factorization**: Uses curves to factor integers

## Limitations of This Implementation

- **Educational Purpose**: Not production-hardened
- **Timing Attacks**: Not constant-time (leaks info via timing)
- **Side Channels**: Doesn't protect against power analysis
- **Limited Curves**: Only demonstrates a few curves
- **No Assembly**: Production code uses optimized field arithmetic

**For Production Use**: Use established libraries like:

- `cryptography` (Python)
- OpenSSL
- libsodium
- BoringSSL

## Further Reading

- **Standards**: NIST FIPS 186-4, SEC 2
- **Books**: "Guide to Elliptic Curve Cryptography" by Hankerson et al.
- **Papers**: Original Koblitz and Miller papers (1985)
- **SafeCurves**: https://safecurves.cr.yp.to/

---

## LICENSE

This project is licensed under the MIT License - see the LICENSE file for details.
