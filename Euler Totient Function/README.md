# Euler's Totient Function Calculator

This repository provides a comprehensive Python implementation of Euler's totient function φ(n), one of the most important functions in number theory and cryptography.

## Problem Description

**Euler's Totient Function** φ(n): The count of positive integers up to n that are relatively prime to n (i.e., have no common factors with n except 1).

For example:
- φ(1) = 1 (1 is coprime to itself)
- φ(2) = 1 (only 1 is coprime to 2)
- φ(6) = 2 (1 and 5 are coprime to 6)
- φ(9) = 6 (1, 2, 4, 5, 7, 8 are coprime to 9)
- φ(12) = 4 (1, 5, 7, 11 are coprime to 12)

## Mathematical Significance

Euler's totient function is fundamental to:

### Number Theory
- **Euler's Theorem**: If gcd(a, n) = 1, then a^φ(n) ≡ 1 (mod n)
- **Fermat's Little Theorem**: Special case where n is prime: a^(p-1) ≡ 1 (mod p)
- **Order of Elements**: φ(n) gives the maximum order of elements in the multiplicative group mod n

### Cryptography
- **RSA Encryption**: The private key exponent d is calculated using φ(n)
  - Choose primes p and q
  - Calculate n = p × q
  - Calculate φ(n) = (p-1)(q-1)
  - Find d such that e × d ≡ 1 (mod φ(n))
- **Key Generation**: Security depends on the difficulty of computing φ(n) without knowing the prime factors
- **Digital Signatures**: Relies on modular exponentiation with φ(n)

### Pure Mathematics
- Multiplicative function: φ(mn) = φ(m)φ(n) when gcd(m,n) = 1
- Sum property: Σ φ(d) = n, where the sum is over all divisors d of n
- Connection to Möbius function and other arithmetic functions

## How It Works

The program implements multiple algorithms:

### Basic Method (Demonstrative)
Count integers k where 1 ≤ k ≤ n and gcd(k, n) = 1
- Time complexity: O(n log n)
- Used only for small n to demonstrate the definition

### Formula Method (Efficient)
Use the prime factorization formula:

If n = p₁^a₁ × p₂^a₂ × ... × pₖ^aₖ, then:

φ(n) = n × (1 - 1/p₁) × (1 - 1/p₂) × ... × (1 - 1/pₖ)

Or equivalently:

φ(n) = (p₁^a₁ - p₁^(a₁-1)) × (p₂^a₂ - p₂^(a₂-1)) × ... × (pₖ^aₖ - pₖ^(aₖ-1))

- Time complexity: O(√n) for factorization
- Highly efficient even for large numbers

### Special Cases
- **Prime p**: φ(p) = p - 1
- **Prime power p^k**: φ(p^k) = p^k - p^(k-1) = p^(k-1)(p-1)
- **Product of coprimes**: φ(mn) = φ(m)φ(n) if gcd(m,n) = 1

## Features

The implementation includes:

1. **φ(n) Calculation**: Multiple methods (basic counting and efficient formula)
2. **Prime Factorization**: Finds prime factors needed for the formula
3. **Coprime Finding**: Lists all numbers coprime to n
4. **Range Calculation**: Computes φ(n) for ranges of numbers
5. **Totient Twins**: Finds pairs (n, m) where φ(n) = φ(m)
6. **Property Analysis**: Detailed analysis of φ(n) properties for any n
7. **RSA Connection**: Demonstrates how φ(n) is used in RSA cryptography

## Usage

Clone the repository and run:

```bash
python euler_totient.py
```

The program will:
- Display φ(n) values for n = 1 to 20
- Provide detailed analysis for specific interesting numbers
- Find and display "totient twins" (different numbers with same φ value)
- Show key mathematical properties with examples
- Demonstrate the connection to RSA cryptography

## Example Output

```text
EULER'S TOTIENT FUNCTION CALCULATOR
======================================================================

Euler's Totient Function φ(n) for n = 1 to 20
======================================================================

n=  1  n=  2  n=  3  n=  4  n=  5
φ=  1  φ=  1  φ=  2  φ=  2  φ=  4

n=  6  n=  7  n=  8  n=  9  n= 10
φ=  2  φ=  6  φ=  4  φ=  6  φ=  4

Detailed Analysis of φ(12)
======================================================================
Number: 12
φ(12) = 4
Ratio: φ(n)/n = 0.333333
Prime factorization: 2^2 × 3
Numbers coprime to 12: [1, 5, 7, 11]
```

## Requirements

- Python 3.7+
- No external dependencies (uses only standard library)

## Interesting Properties

### 1. Multiplicative Function
φ(mn) = φ(m) × φ(n) when gcd(m, n) = 1

Example: φ(15) = φ(3) × φ(5) = 2 × 4 = 8

### 2. Prime Numbers
For any prime p: φ(p) = p - 1

All numbers less than p are coprime to p since p has no factors.

### 3. Totient Twins
Different numbers can have the same φ value:
- φ(3) = φ(4) = φ(6) = 2
- φ(5) = φ(8) = φ(10) = φ(12) = 4
- φ(7) = φ(9) = φ(14) = φ(18) = 6

### 4. Never φ(n) = n-1 unless n is Prime
Only prime numbers satisfy φ(p) = p - 1

### 5. Ratio Bounds
For any n > 1: φ(n)/n ≥ 1/log(log(n)) (approximately)

The ratio approaches 0 as n increases, but very slowly.

## Applications in Computer Science

1. **RSA Cryptography**: Core component of key generation
2. **Cyclic Groups**: Determines the size of multiplicative groups
3. **Hash Functions**: Used in some cryptographic hash constructions
4. **Primality Testing**: Related to probabilistic primality tests
5. **Perfect Hash Functions**: Construction of minimal perfect hash functions
6. **Pseudo-random Generators**: Some PRNGs use totient function properties

## Performance

The efficient formula method can compute φ(n) for:
- Small numbers (< 10^6): Instantly
- Medium numbers (< 10^12): Milliseconds
- Large numbers (< 10^18): Seconds (limited by factorization)

The bottleneck is prime factorization, which is the same problem that makes RSA secure!

## How to Contribute

Feel free to fork and send pull requests! Some ideas:
- Add visualization of φ(n) growth patterns
- Implement sieve-based calculation for ranges
- Add more cryptographic applications
- Optimize factorization for very large numbers
- Add support for symbolic computation

---

## LICENSE

This project is licensed under the MIT License - see the LICENSE file for details.
