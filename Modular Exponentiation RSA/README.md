# Modular Exponentiation & RSA Demo

This repository provides a comprehensive implementation of fast modular exponentiation and demonstrates the fundamentals of RSA public-key cryptography.

## Problem Description

### Modular Exponentiation

Computing **(base^exponent) mod modulus** efficiently is a fundamental operation in cryptography. The naive approach of computing base^exponent first, then taking the modulus, becomes impractical for large exponents because intermediate results grow exponentially.

**Fast Modular Exponentiation** (also called binary exponentiation or square-and-multiply) solves this by:
- Taking the modulus at each step to keep numbers small
- Using binary representation of the exponent to reduce operations
- Achieving O(log n) complexity instead of O(n)

### RSA Cryptography

**RSA** (Rivest-Shamir-Adleman) is one of the first practical public-key cryptosystems and is widely used for secure data transmission. It's based on the mathematical difficulty of factoring large numbers.

## How It Works

### Modular Exponentiation Algorithm

The binary exponentiation method works by:

1. Converting the exponent to binary representation
2. Processing each bit from right to left
3. Squaring the base for each bit position
4. Multiplying by base when bit is 1
5. Taking modulus at each step to keep results manageable

**Example**: Computing 3^13 mod 7
```
13 in binary: 1101
Result = 1
- Bit 1: result = (1 × 3) mod 7 = 3
- Bit 0: base = (3 × 3) mod 7 = 2, skip multiply
- Bit 1: result = (3 × 2) mod 7 = 6, base = (2 × 2) mod 7 = 4
- Bit 1: result = (6 × 4) mod 7 = 3
Final: 3
```

### RSA Algorithm

#### Key Generation
1. Choose two large prime numbers: **p** and **q**
2. Compute **n = p × q** (the modulus)
3. Compute **φ(n) = (p-1)(q-1)** (Euler's totient)
4. Choose **e** coprime to φ(n) (public exponent, often 65537)
5. Compute **d** where **d × e ≡ 1 (mod φ(n))** (private exponent)

**Public Key**: (e, n)  
**Private Key**: (d, n)

#### Encryption
```
ciphertext = plaintext^e mod n
```

#### Decryption
```
plaintext = ciphertext^d mod n
```

#### Why It Works
The correctness relies on **Euler's Theorem**:
```
If gcd(m, n) = 1, then m^φ(n) ≡ 1 (mod n)
```

Combined with the property that **e × d ≡ 1 (mod φ(n))**:
```
(m^e)^d = m^(ed) = m^(1 + k×φ(n)) = m × (m^φ(n))^k ≡ m × 1 ≡ m (mod n)
```

## Usage

Clone the repository and run:

```bash
python modular_exp_rsa.py
```

The program will:

- Demonstrate fast modular exponentiation with examples
- Compare naive vs. efficient algorithms
- Generate RSA key pairs
- Encrypt and decrypt messages
- Explain RSA security principles

## Example Output

```text
============================================================
Modular Exponentiation Demonstration
============================================================

(2^10) mod 1000 = 24
  Verification: ✓ (built-in pow: 24)

(3^100) mod 7 = 4
  Verification: ✓ (built-in pow: 4)

============================================================
RSA Encryption Demonstration
============================================================

Step 1: Generate RSA keys
------------------------------------------------------------
Public key:  (e=65537, n=...)
Private key: (d=..., n=...)
Key size: ~32 bits

Step 2: Encrypt and decrypt numeric messages
------------------------------------------------------------

  Original:   42
  Encrypted:  ...
  Decrypted:  42 ✓
```

## Requirements

- Python 3.7+
- No external dependencies (uses only standard library)

## Mathematical Background

### Historical Context

- **1977**: Ron Rivest, Adi Shamir, and Leonard Adleman published RSA
- **1973**: The UK's GCHQ had secretly developed equivalent system (not public)
- **Revolution**: First practical public-key cryptosystem
- **Impact**: Enabled secure communication without sharing secret keys

### Why RSA is Secure

**One-Way Function**: The security relies on the asymmetry between:

- **Easy**: Multiplying two large primes p × q = n (milliseconds)
- **Hard**: Factoring n back to find p and q (potentially millions of years)

For a 2048-bit RSA key:
- Generating the key: Seconds
- Factoring n (breaking the key): Estimated 6.4 quadrillion years with current technology

**Mathematical Foundation**:
- **Number Theory**: Prime numbers, modular arithmetic, Euler's theorem
- **Computational Complexity**: Integer factorization problem
- **One-way Functions**: Easy one direction, hard to reverse

### Efficiency of Binary Exponentiation

| Method | Time Complexity | Space | Example (2^1000 mod m) |
|--------|----------------|-------|----------------------|
| Naive multiply | O(n) | O(log result) | ~1000 multiplications |
| Binary exponentiation | O(log n) | O(1) | ~10 multiplications |

For encryption/decryption with large exponents, binary exponentiation is **essential**. Without it, RSA would be impractical.

## Applications

### RSA in the Real World

1. **HTTPS/SSL/TLS**: Secure web browsing
2. **Email Encryption**: PGP, S/MIME
3. **Digital Signatures**: Verify authenticity of messages
4. **Software Distribution**: Code signing
5. **VPN**: Secure remote connections
6. **Cryptocurrency**: Bitcoin, Ethereum (though mostly use ECDSA now)
7. **Secure Shell (SSH)**: Remote server access

### Other Uses of Modular Exponentiation

- **Diffie-Hellman Key Exchange**: Establishing shared secrets
- **ElGamal Encryption**: Another public-key system
- **Digital Signature Algorithm (DSA)**
- **Elliptic Curve Cryptography (ECC)**
- **Primality Testing**: Miller-Rabin algorithm
- **Cryptographic Hash Functions**

## Security Considerations

### This Implementation

⚠️ **WARNING**: This is an **educational implementation** only!

**Not suitable for production** because it lacks:
- Proper padding (OAEP, PSS)
- Timing attack protection
- Secure random number generation
- Large key sizes (uses small keys for demonstration)
- Side-channel attack protection

### Real-World RSA Requirements

1. **Key Size**: Minimum 2048 bits (4096 bits recommended)
2. **Padding**: OAEP for encryption, PSS for signatures
3. **Random Number Generator**: Cryptographically secure
4. **Implementation**: Use vetted libraries (OpenSSL, cryptography.io)
5. **Key Management**: Secure storage and distribution
6. **Constant-Time Operations**: Prevent timing attacks

### Modern Alternatives

While RSA is still widely used, newer alternatives are gaining adoption:

- **Elliptic Curve Cryptography (ECC)**: Smaller keys, equal security
- **Post-Quantum Cryptography**: Resistant to quantum computers
- **ChaCha20-Poly1305**: Fast symmetric encryption
- **EdDSA (Ed25519)**: Fast, secure signatures

### Quantum Computing Threat

⚠️ **Shor's Algorithm** (1994) can factor large numbers efficiently on quantum computers:
- Would break RSA, DSA, Diffie-Hellman, ECC
- Large-scale quantum computers don't exist yet (as of 2024)
- NIST is standardizing post-quantum algorithms
- Organisations should plan migration strategies

## Performance Analysis

### Algorithm Complexity

| Operation | Complexity |
|-----------|------------|
| Modular Exponentiation | O(log n) |
| RSA Key Generation | O(k²) for k-bit primes |
| RSA Encryption | O(log e) ≈ O(1) for small e |
| RSA Decryption | O(log n) |
| Prime Generation | O(k³) including primality testing |

### Practical Performance

For 2048-bit RSA (approximate times on modern hardware):
- Key generation: 100-500 ms
- Encryption: 0.1-1 ms (small public exponent)
- Decryption: 10-50 ms
- Signature verification: 0.1-1 ms
- Signature creation: 10-50 ms

## Interesting Facts

1. **Public Exponent**: 65537 (2^16 + 1) is commonly used because:
   - It's prime
   - Has only two 1-bits in binary (fast encryption)
   - Large enough to prevent small-exponent attacks

2. **Patent History**: RSA was patented in 1983, expired in 2000

3. **Export Restrictions**: US classified strong crypto as munitions until late 1990s

4. **Key Sizes**: Double the key size = 8x more security (not 2x!)

5. **Timing**: With 1970s technology, generating RSA keys took hours. Now: milliseconds

## How to Contribute

Feel free to fork and send pull requests! Ideas for contributions:

- Add Chinese Remainder Theorem optimization
- Implement proper padding schemes
- Add visualisation of the algorithm steps
- Demonstrate digital signatures
- Add more primality tests (Solovay-Strassen, AKS)

---

## LICENSE

This project is licensed under the MIT License - see the LICENSE file for details.
