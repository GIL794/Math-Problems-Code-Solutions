# Euler's Totient Function Calculator

This repository provides a comprehensive Python implementation of Euler's Totient Function (φ function) with analysis of coprime relationships.

## Problem Description

**Euler's Totient Function**, denoted as **φ(n)** (phi of n), is a fundamental function in number theory that counts how many positive integers up to n are **coprime** to n.

Two numbers are coprime (or relatively prime) if their greatest common divisor (GCD) is 1. In other words, they share no common factors other than 1.

### Examples

- **φ(1) = 1**: Only 1 is coprime to 1
- **φ(6) = 2**: Numbers 1 and 5 are coprime to 6
- **φ(12) = 4**: Numbers 1, 5, 7, 11 are coprime to 12
- **φ(17) = 16**: For any prime p, φ(p) = p - 1

### Formula

For a number with prime factorization n = p₁^k₁ × p₂^k₂ × ... × pₘ^kₘ:

```
φ(n) = n × (1 - 1/p₁) × (1 - 1/p₂) × ... × (1 - 1/pₘ)
```

Or equivalently:
```
φ(n) = p₁^(k₁-1) × (p₁-1) × p₂^(k₂-1) × (p₂-1) × ... × pₘ^(kₘ-1) × (pₘ-1)
```

### Special Cases

- **Prime numbers**: φ(p) = p - 1 (all numbers less than p are coprime to it)
- **Powers of primes**: φ(p^k) = p^(k-1) × (p - 1)
- **Product of coprimes**: φ(m × n) = φ(m) × φ(n) if gcd(m, n) = 1

## How It Works

The program implements multiple algorithms and analyses:

1. **GCD Calculation**: Uses the Euclidean algorithm
2. **Prime Factorization**: Breaks numbers into prime factors
3. **Naive Method**: Directly counts coprimes (educational)
4. **Efficient Method**: Uses the prime factorization formula
5. **Coprime Finding**: Lists all numbers coprime to n
6. **Property Analysis**: Demonstrates mathematical properties

### Algorithm Efficiency

- **Naive method**: O(n) - counts each number
- **Formula method**: O(√n) - only needs prime factorization
- For large n, the formula method is drastically faster

## Usage

Clone the repository and run:

```bash
python euler_totient.py
```

The program will:

- Calculate φ(n) for various test numbers
- Show coprime numbers for each n
- Compare totient values across a range
- Demonstrate the multiplicative property
- Display interesting mathematical facts

## Example Output

```text
============================================================
Euler's Totient Function: φ(12)
============================================================
φ(12) = 4
Ratio φ(n)/n = 0.3333

Prime factorization: 12 = 2^2 × 3
n has multiple prime factors

Numbers coprime to 12:
  [1, 5, 7, 11]

Properties:
  • 4 out of 12 numbers are coprime to 12
  • 8 numbers share a common factor with 12
```

## Requirements

- Python 3.7+
- No external dependencies (uses only standard library)

## Mathematical Background

### History

- **Leonhard Euler** (1707-1783) introduced this function
- Originally studied in the context of modular arithmetic
- Published in his work on Fermat's Little Theorem
- Named "totient" from the Latin "tot" meaning "so many"

### Key Properties

1. **Multiplicative Function**: If gcd(m, n) = 1, then φ(m·n) = φ(m)·φ(n)

2. **Sum of Divisors**: For any positive integer n:
   ```
   Σ φ(d) = n
   ```
   where the sum is over all divisors d of n

3. **Euler's Theorem**: If gcd(a, n) = 1, then:
   ```
   a^φ(n) ≡ 1 (mod n)
   ```

4. **Average Value**: As n approaches infinity:
   ```
   φ(n)/n → 6/π² ≈ 0.6079...
   ```

### Applications

#### Cryptography - RSA Algorithm

The totient function is **essential** to RSA encryption:

1. Choose two large primes p and q
2. Compute n = p × q
3. Calculate φ(n) = (p-1)(q-1)
4. Choose public exponent e coprime to φ(n)
5. Compute private exponent d where d·e ≡ 1 (mod φ(n))

The security relies on the difficulty of computing φ(n) without knowing the prime factors!

#### Other Applications

- **Cyclic Groups**: Orders of elements in modular arithmetic
- **Primitive Roots**: Finding generators of multiplicative groups
- **Finite Fields**: Structure of multiplicative groups
- **Generating Functions**: In analytic number theory
- **Möbius Inversion**: Connected to the Möbius function

### Connection to Other Functions

- **Möbius Function μ(n)**: Related through sum formulas
- **Carmichael Function λ(n)**: Always divides φ(n)
- **Jordan's Totient**: Generalization to higher dimensions
- **Dedekind Psi Function**: Similar multiplicative function

## Interesting Observations

### Prime Numbers
For primes, φ(p) = p - 1 because all numbers 1, 2, ..., p-1 are coprime to p.

### Powers of 2
- φ(2) = 1
- φ(4) = 2
- φ(8) = 4
- φ(16) = 8
- Pattern: φ(2^k) = 2^(k-1)

### Highly Composite Numbers
Numbers with many divisors often have lower φ(n)/n ratios because more numbers share factors with them.

### Perfect Numbers
For perfect numbers n (where sum of divisors = 2n), the relationship with φ(n) has special properties.

## Performance Considerations

The implementation uses the efficient formula-based method which:

- Computes prime factorization: O(√n)
- Applies formula: O(number of distinct prime factors)
- Overall: Much faster than O(n) naive counting

For very large numbers, optimizations include:
- Pollard's rho algorithm for factorization
- Precomputed prime tables
- Memoization for repeated calculations

## How to Contribute

Feel free to fork and send pull requests! Ideas for contributions:

- Add visualization of coprime patterns
- Implement Carmichael's function
- Add support for computing φ⁻¹(n) (inverse totient)
- Optimize factorization for very large numbers
- Add more number theory connections

---

## LICENSE

This project is licensed under the MIT License - see the LICENSE file for details.
