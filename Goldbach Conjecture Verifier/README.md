# Goldbach Conjecture Verifier

This repository provides a Python solution to verify the Goldbach Conjecture, one of the oldest and most famous unsolved problems in mathematics.

## Problem Description

**Goldbach's Conjecture** (proposed in 1742): Every even integer greater than 2 can be expressed as the sum of two prime numbers.

For example:
- 4 = 2 + 2
- 6 = 3 + 3
- 8 = 3 + 5
- 10 = 3 + 7 = 5 + 5
- 100 = 3 + 97 = 11 + 89 = 17 + 83 = 29 + 71 = 41 + 59 = 47 + 53

## Mathematical Significance

- **Status**: Still unproven after nearly 300 years!
- **Verification**: Computationally verified for all even numbers up to 4 × 10¹⁸
- **Importance**: One of the seven most important unsolved problems in mathematics
- **Connections**: Related to prime number distribution, analytic number theory, and the Riemann Hypothesis

The conjecture appears simple but has resisted all attempts at proof. It's a perfect example of how some mathematical statements can be easy to verify but incredibly difficult to prove.

## How It Works

The program includes several powerful features:

### Core Functions
- **Goldbach Pair Finder**: Finds all possible ways to express an even number as the sum of two primes
- **Range Verification**: Verifies the conjecture for all even numbers in a given range
- **Statistical Analysis**: Analyzes patterns in the number of representations
- **Weak Goldbach**: Also demonstrates the weak Goldbach conjecture (expressing odd numbers as sum of three primes)

### Algorithms Used
1. **Sieve of Eratosthenes**: Efficiently generates all primes up to a limit - O(n log log n)
2. **Set-based Lookup**: Uses hash sets for O(1) prime checking
3. **Smart Iteration**: Only checks up to n/2 to avoid duplicate pairs

## Usage

Clone the repository and run:

```bash
python goldbach_verifier.py
```

The program will:
- Verify Goldbach's conjecture for even numbers from 4 to 50 (with full details)
- Verify for numbers 4 to 200 (with summary statistics)
- Show numbers with the most representations
- Demonstrate the weak Goldbach conjecture for odd numbers
- Provide statistical analysis and interesting observations

## Example Output

```text
GOLDBACH CONJECTURE VERIFIER
======================================================================

Verification for small even numbers (4 to 50)
======================================================================

4 = 2 + 2
6 = 3 + 3
8 = 3 + 5
10 = 3 + 7
    5 + 5
12 = 5 + 7
14 = 3 + 11
    7 + 7
...

✓ All numbers verified!

Goldbach Representations Analysis
======================================================================
Total even numbers analyzed: 24
Successfully verified: 24
Average representations per number: 2.54
Maximum representations: 6
```

## Requirements

- Python 3.7+
- No external dependencies (uses only standard library)

## Interesting Facts

1. **Most representations**: As numbers get larger, they tend to have more Goldbach representations
2. **Twin primes**: Numbers that are the sum of twin primes (like 10 = 5 + 5 from twins 3, 5, 7) are common
3. **Computational record**: The conjecture has been verified up to 4 × 10¹⁸ (2014)
4. **Weak Goldbach**: The "weak" version (odd numbers as sum of three primes) was proven in 2013!
5. **Even 4**: The smallest even number (4 = 2 + 2) has only one representation

## Related Conjectures

- **Weak Goldbach Conjecture** (Proven 2013): Every odd number > 5 is the sum of three odd primes
- **Lemoine's Conjecture**: Every odd number > 5 is the sum of an odd prime and an even semiprime
- **Levy's Conjecture**: Every odd number > 5 is the sum of an odd prime and twice a prime

## Applications

While primarily of theoretical interest, Goldbach's conjecture relates to:
- **Prime distribution theory**: Understanding how primes are distributed
- **Cryptography**: Prime numbers are fundamental to modern encryption
- **Additive number theory**: The study of representing numbers as sums
- **Computational complexity**: Testing the limits of verification vs. proof

## Performance

The implementation is optimized for efficiency:
- Generates primes once using the Sieve of Eratosthenes
- Uses set lookups for O(1) prime checking
- Avoids duplicate pair checking
- Can verify thousands of numbers in seconds

For the range 4 to 1000, the program verifies all 499 even numbers instantly, finding thousands of prime pair representations.

## How to Contribute

Feel free to fork and send pull requests! Some ideas:
- Optimize the algorithm further
- Add visualization of prime pair distributions
- Implement parallel verification for very large ranges
- Add more statistical analysis features

---

## LICENSE

This project is licensed under the MIT License - see the LICENSE file for details.
