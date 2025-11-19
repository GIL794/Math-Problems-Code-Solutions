# Goldbach Conjecture Verifier

This repository provides a solution in Python to verify Goldbach's Conjecture for even numbers.

## Problem Description

**Goldbach's Conjecture** is one of the oldest and most famous unsolved problems in number theory. Proposed by Christian Goldbach in 1742, it states:

> Every even integer greater than 2 can be expressed as the sum of two prime numbers.

For example:
- 4 = 2 + 2
- 6 = 3 + 3
- 8 = 3 + 5
- 10 = 3 + 7 = 5 + 5
- 100 = 3 + 97 = 11 + 89 = 17 + 83 = 29 + 71 = 41 + 59 = 47 + 53

## How It Works

The program implements several key functions:

1. **Prime Detection**: Uses efficient trial division to check if a number is prime
2. **Goldbach Pair Finding**: For any even number n, finds all pairs of primes (p, q) where p + q = n
3. **Range Verification**: Verifies the conjecture for ranges of even numbers
4. **Pattern Analysis**: Analyzes how many different ways numbers can be represented

### Algorithm Steps

1. For an even number n:
   - Iterate through all numbers from 2 to n/2
   - For each prime p, check if (n - p) is also prime
   - If both are prime, record the pair (p, n-p)

2. The conjecture is verified if at least one pair is found

3. Pattern analysis shows interesting trends:
   - Larger numbers typically have MORE representations
   - Some numbers have many pairs, others have few
   - All tested even numbers satisfy the conjecture

## Usage

Clone the repository and run:

```bash
python goldbach_verifier.py
```

The program will:

- Verify Goldbach's conjecture for several specific even numbers
- Show all Goldbach pairs for each number
- Analyze patterns across ranges of numbers
- Display interesting statistics about representations

## Example Output

```text
============================================================
Goldbach Verification for 28
============================================================
✓ Verified: 28 can be expressed as sum of two primes
   Number of representations: 4

   Goldbach pairs:
           5 +     23 = 28
          11 +     17 = 28
          17 +     11 = 28
          23 +      5 = 28
```

## Requirements

- Python 3.7+
- No external dependencies (uses only standard library)

## Mathematical Background

### Historical Context

- **1742**: Christian Goldbach wrote a letter to Leonhard Euler proposing the conjecture
- **Originally**: Goldbach's letter stated a different version involving odd numbers
- **Modern form**: Euler reformulated it to the version we know today
- **Status**: Remains UNPROVEN despite extensive verification

### Verification Progress

- Verified by computer up to **4 × 10^18** (4 quintillion)
- No counterexample has ever been found
- Most mathematicians believe it's true
- A proof remains elusive despite nearly 300 years of effort

### Related Results

- **Weak Goldbach Conjecture**: Every odd number > 5 can be expressed as sum of three primes
  - PROVEN in 2013 by Harald Helfgott
- **Goldbach's Comet**: A graph showing the number of representations forms a comet-like pattern
- **Vinogradov's Theorem**: Related result about sums of primes

### Why It's Hard to Prove

- Primes are multiplicatively defined but the conjecture is about addition
- Distribution of primes is irregular
- Requires deep understanding of prime gaps and density
- Involves subtle properties of prime numbers we don't fully understand

### Applications

While unproven, the conjecture has inspired:

- Development of new techniques in analytic number theory
- Research into prime distribution
- Studies of additive combinatorics
- Computational prime verification methods

## Interesting Observations

- **4 = 2 + 2**: The smallest case (using the same prime twice)
- **Smaller numbers**: Often have fewer representations
- **Larger numbers**: Tend to have many more representations
- **Even distribution**: Pairs are not evenly distributed
- **Computational verification**: Modern computers can verify billions of cases in seconds

## How to Contribute

Feel free to fork and send pull requests! Ideas for contributions:

- Optimize the prime checking algorithm
- Add visualization of Goldbach's Comet
- Implement parallel verification for large ranges
- Add more statistical analysis

---

## LICENSE

This project is licensed under the MIT License - see the LICENSE file for details.
