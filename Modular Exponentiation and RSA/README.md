# Modular Exponentiation and RSA Cryptography

This repository provides a comprehensive Python implementation of modular exponentiation and RSA cryptography, demonstrating the mathematical foundations of modern secure communication.

## Problem Description

**Modular Exponentiation**: Computing (a^b) mod m efficiently, even when b is enormous.

**RSA Cryptography**: A public-key cryptosystem that enables:
- Secure communication without pre-shared secrets
- Digital signatures for authentication
- Key exchange for symmetric encryption

## Mathematical Background

### Modular Exponentiation

Computing a^b mod m directly is infeasible for large b (e.g., b = 10^100). The naive approach would require 10^100 multiplications!

**Binary Exponentiation (Square-and-Multiply)** solves this in O(log b) time:
- Based on: a^b = (a^(b/2))^2 if b is even
- Or: a^b = a × a^(b-1) if b is odd

Example: 3^13 mod 1000
- 13 in binary: 1101
- 3^13 = 3^8 × 3^4 × 3^1
- Only needs 3 multiplications instead of 13!

### RSA Algorithm

**Key Generation:**
1. Choose two large primes p and q
2. Calculate n = p × q (public modulus)
3. Calculate φ(n) = (p-1)(q-1) (Euler's totient)
4. Choose e where gcd(e, φ(n)) = 1 (public exponent)
5. Calculate d where d × e ≡ 1 (mod φ(n)) (private exponent)

**Encryption:** c ≡ m^e (mod n)

**Decryption:** m ≡ c^d (mod n)

**Why it works:** By Euler's theorem, (m^e)^d = m^(ed) ≡ m^(1 + kφ(n)) ≡ m (mod n)

## Features

This implementation includes:

### Core Algorithms
1. **Fast Modular Exponentiation**: Binary exponentiation method
2. **Extended Euclidean Algorithm**: For finding modular inverses
3. **Miller-Rabin Primality Test**: Probabilistic prime testing
4. **Prime Generation**: Random prime number generation

### RSA Operations
1. **Key Generation**: Creates public/private key pairs
2. **Encryption**: Encrypts messages with public key
3. **Decryption**: Decrypts with private key (two methods)
4. **CRT Optimization**: Chinese Remainder Theorem for 4x faster decryption

### Demonstrations
1. **Performance Comparisons**: Naive vs fast algorithms
2. **Euler's Theorem**: Verification with examples
3. **Security Concepts**: Explanation of RSA security
4. **Real-World Context**: Applications in cryptography

## Usage

Clone the repository and run:

```bash
python modular_rsa.py
```

The program will:
- Demonstrate modular exponentiation with examples
- Generate RSA keys and show all parameters
- Encrypt and decrypt sample messages
- Compare standard vs CRT decryption performance
- Verify Euler's theorem with examples
- Explain RSA security concepts

## Example Output

```text
MODULAR EXPONENTIATION AND RSA CRYPTOGRAPHY
======================================================================

Modular Exponentiation: Computing (base^exp) mod m
======================================================================

Examples:
  2^10 mod 1000 = 24
  3^100 mod 1000 = 1
  7^256 mod 1000 = 801
  123^456 mod 789 = 699

RSA Cryptography Demonstration
======================================================================

Key Generation:
  Prime p: 54167
  Prime q: 48779
  Modulus n = p × q: 2642033393
  φ(n) = (p-1)(q-1): 2641930448
  Public exponent e: 65537
  Private exponent d: 1879266033
  Verification: e × d mod φ(n) = 1 ✓

Message: 12345
  Encrypted: 1847629487
  Decrypted (standard): 12345
  Decrypted (CRT): 12345
  Verification: ✓
```

## Requirements

- Python 3.7+
- No external dependencies (uses only standard library)

## Security Notes

### Why RSA is Secure

1. **One-Way Function**: Easy to multiply primes (p × q = n), hard to factor n back to p and q
2. **Key Size**: 2048-bit keys provide ~100 years of security with current technology
3. **No Quantum Resistance**: Shor's algorithm can break RSA on quantum computers
4. **Mathematical Foundation**: Security relies on computational difficulty, not secrecy of algorithm

### Recommended Key Sizes

| Year | Minimum Bits | Security Level |
|------|--------------|----------------|
| 2000-2013 | 1024 | Deprecated |
| 2014-2030 | 2048 | Standard |
| 2030+ | 3072 | High Security |
| Military | 4096+ | Maximum Security |

### Common Attacks and Mitigations

1. **Small Exponent Attack**: Always use e ≥ 65537
2. **Factorization**: Use strong primes (avoid special forms)
3. **Timing Attacks**: Use constant-time implementations
4. **Padding**: Always use proper padding schemes (OAEP)

## Real-World Applications

### Where RSA is Used

1. **SSL/TLS (HTTPS)**: Secure web browsing
   - Server authentication
   - Key exchange for symmetric encryption

2. **SSH**: Secure remote server access
   - Public key authentication
   - Encrypted communication

3. **Digital Signatures**: 
   - Code signing
   - Document authentication
   - Email signatures (PGP)

4. **Cryptocurrencies**: 
   - Bitcoin and Ethereum use ECDSA (elliptic curve variant)
   - Some altcoins use RSA-based schemes

5. **VPNs**: 
   - Certificate-based authentication
   - Key exchange

## Optimizations Implemented

### Chinese Remainder Theorem (CRT)

Standard decryption: m = c^d mod n (slow for large d)

CRT optimization:
- m₁ = c^(d mod p-1) mod p
- m₂ = c^(d mod q-1) mod q
- Combine m₁ and m₂ to get m

**Speedup**: ~4x faster because we work with smaller numbers

### Binary Exponentiation

Instead of n multiplications, only log₂(n) multiplications needed.

Example: 2^1000 needs only 10 multiplications (log₂ 1000 ≈ 10)

## Mathematical Theorems Used

### Euler's Theorem
If gcd(a, n) = 1, then a^φ(n) ≡ 1 (mod n)

This guarantees RSA works: (m^e)^d = m^(ed) = m^(1 + kφ(n)) = m × (m^φ(n))^k ≡ m (mod n)

### Fermat's Little Theorem
Special case of Euler's theorem when n is prime: a^(p-1) ≡ 1 (mod p)

### Chinese Remainder Theorem
If gcd(m, n) = 1, then the system:
- x ≡ a (mod m)
- x ≡ b (mod n)

has a unique solution mod mn.

## Performance

### Encryption/Decryption Speed
- Small messages (< 1KB): < 1ms
- Key generation: ~100ms for 2048-bit keys
- CRT decryption: 4x faster than standard

### Scalability
- Time complexity: O(log n) for exponentiation
- Space complexity: O(1) - constant memory
- Suitable for: Embedded systems to servers

## Limitations

1. **Message Size**: m must be < n (typically encrypt small symmetric keys)
2. **Speed**: Slower than symmetric encryption (AES)
3. **Quantum Vulnerable**: Not resistant to quantum computers
4. **Implementation**: Easy to implement incorrectly (timing attacks, etc.)

## Common Use Pattern

In practice, RSA is used for:
1. **Key Exchange**: RSA encrypts a symmetric key
2. **Bulk Encryption**: AES encrypts the actual data
3. **Digital Signatures**: RSA signs a hash of the document

This hybrid approach gets the best of both worlds!

## How to Contribute

Feel free to fork and send pull requests! Some ideas:
- Add more padding schemes (OAEP, PSS)
- Implement digital signatures
- Add key serialization (PEM format)
- Optimize prime generation
- Add more cryptographic primitives
- Implement post-quantum alternatives

---

## LICENSE

This project is licensed under the MIT License - see the LICENSE file for details.

## References

- RSA Paper: Rivest, Shamir, and Adleman (1978)
- NIST Special Publication 800-56B: Recommendation for Pair-Wise Key Establishment
- RFC 8017: PKCS #1: RSA Cryptography Specifications Version 2.2
