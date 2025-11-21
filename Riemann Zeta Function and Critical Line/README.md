# Riemann Zeta Function & Critical Line Explorer

This repository provides a comprehensive implementation of the Riemann Zeta Function and tools to explore one of mathematics' greatest mysteries: the Riemann Hypothesis.

## Problem Description

The Riemann Zeta Function ζ(s) is defined as:

```
ζ(s) = Σ(n=1 to ∞) 1/n^s  for Re(s) > 1
```

Through analytic continuation, it can be extended to all complex numbers except s = 1, where it has a simple pole.

**The Riemann Hypothesis** (one of the Millennium Prize Problems worth $1,000,000) conjectures that:
> All non-trivial zeros of ζ(s) lie on the critical line Re(s) = 1/2

This unsolved problem, formulated in 1859, is central to understanding the distribution of prime numbers.

## Mathematical Significance

The Riemann Zeta Function connects to:

1. **Prime Number Distribution**: Through the Euler product formula:
   ```
   ζ(s) = Π(p prime) 1/(1 - p^(-s))
   ```

2. **Prime Counting Function**: The explicit formula relates π(x) to the zeros of ζ(s)

3. **Number Theory**: Connections to divisor functions, perfect numbers, and more

4. **Quantum Physics**: Random matrix theory and energy levels

## Implementation Features

This implementation includes:

### 1. Zeta Function Computation
- **Dirichlet Series**: Direct summation for Re(s) > 1
- **Functional Equation**: Extends to Re(s) < 0
- **Riemann-Siegel Formula**: Efficient computation on the critical line
- **Complex Arithmetic**: Full support for complex inputs

### 2. Zero Finding
- **Critical Line Exploration**: Search for zeros at Re(s) = 1/2
- **Zero Verification**: Confirms zeros found
- **Gram Points**: Special points on the critical line
- **Zero Counting**: Estimates number of zeros in intervals

### 3. Analysis Tools
- **Argument Principle**: Counts zeros in regions
- **Euler Product**: Connection to primes
- **Zeta Values**: Special values (ζ(2), ζ(4), etc.)
- **Visualization Data**: Generates data for plotting

### 4. Special Values
- **ζ(2) = π²/6**: Basel problem solution
- **ζ(0) = -1/2**: Via analytic continuation
- **ζ(-1) = -1/12**: Famous paradoxical result
- **ζ(n) for even n**: Bernoulli number formulas

## How It Works

The program demonstrates:

1. **Basic Zeta Computation**: Calculate ζ(s) for various complex values
2. **Zero Finding**: Locate non-trivial zeros on the critical line
3. **Prime Connection**: Show Euler product convergence
4. **Special Values**: Compute and verify famous results
5. **Critical Strip**: Explore the region 0 < Re(s) < 1

## Algorithm Complexity

- **Dirichlet Series**: O(N) for N terms, accuracy ~10^(-log N)
- **Riemann-Siegel**: O(√t) for height t on critical line
- **Zero Finding**: O(N log N) using bisection with N evaluations

## Usage

Run the analyzer:

```bash
python riemann_zeta.py
```

The program will:
- Compute various zeta function values
- Find and verify zeros on the critical line
- Demonstrate the connection to prime numbers
- Calculate special values and identities

## Example Output

```text
Riemann Zeta Function Explorer
============================================================

Special Values:
ζ(2) = 1.6449340668 (π²/6 = 1.6449340668)
ζ(4) = 1.0823232337 (π⁴/90 = 1.0823232337)
ζ(-1) = -0.0833333333 (-1/12 = -0.0833333333)

Critical Line Zeros (Re(s) = 1/2):
Zero #1: 0.5000 + 14.1347i  |ζ| = 0.0000012
Zero #2: 0.5000 + 21.0220i  |ζ| = 0.0000008
Zero #3: 0.5000 + 25.0109i  |ζ| = 0.0000015

Euler Product Connection:
ζ(2) via Dirichlet Series:  1.6449340668
ζ(2) via Euler Product:     1.6449340667
Difference: 0.0000000001
```

## Requirements

- Python 3.7+
- No external dependencies (uses only standard library)
- Complex number arithmetic built-in

## Mathematical Background

### The Riemann Hypothesis

First 10 non-trivial zeros (on critical line Re(s) = 1/2):
- s = 0.5 + 14.134725i
- s = 0.5 + 21.022040i
- s = 0.5 + 25.010858i
- s = 0.5 + 30.424876i
- s = 0.5 + 32.935062i
- s = 0.5 + 37.586178i
- s = 0.5 + 40.918719i
- s = 0.5 + 43.327073i
- s = 0.5 + 48.005151i
- s = 0.5 + 49.773832i

Over 10 trillion zeros have been verified to lie on the critical line!

### Applications

1. **Cryptography**: Prime distribution affects RSA security
2. **Signal Processing**: Zeros relate to spectral analysis
3. **Quantum Chaos**: Energy level statistics
4. **Computer Science**: Randomness and pseudorandom generators

### Interesting Facts

- If the Riemann Hypothesis is true, it would improve prime counting algorithms
- The first zero was found by Riemann himself in 1859
- Computing zeros requires sophisticated numerical methods
- The zeros have connections to quantum mechanics and random matrices
- The zeta function appears in string theory and theoretical physics

## Limitations

This implementation:
- Uses approximations (not infinite series)
- Has numerical precision limits
- Cannot prove the Riemann Hypothesis (nobody can!)
- Is for educational purposes, not research-grade computation

## Further Reading

- Bernhard Riemann's original 1859 paper
- Harold Edwards: "Riemann's Zeta Function"
- The Clay Mathematics Institute's problem statement
- Andrew Odlyzko's computational work on zeros

---

## LICENSE

This project is licensed under the MIT License - see the LICENSE file for details.
