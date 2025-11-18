# Prime Number Sieve

This repository provides a solution in Python to find prime numbers using the Sieve of Eratosthenes algorithm.

## Problem Description

A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The Sieve of Eratosthenes is an ancient algorithm for finding all prime numbers up to a given limit.

The algorithm works by:

1. Creating a list of numbers from 2 to the limit
2. Starting with the first prime number (2)
3. Marking all multiples of that prime as composite
4. Moving to the next unmarked number (which is prime)
5. Repeating until all numbers are processed

## How It Works

The program includes:

- **Sieve of Eratosthenes**: Efficiently finds all primes up to a limit
- **Prime checking**: Determines if a specific number is prime
- **Prime factorization**: Finds all prime factors of a number
- **Distribution analysis**: Analyzes patterns like twin primes and gaps

## Usage

Clone the repository and run:

```bash
python prime_sieve.py
```

The program will:

- Find all primes up to 100 and 1000
- Analyze prime distribution (twin primes, gaps)
- Demonstrate prime factorization
- Check if specific numbers are prime

## Example Output

```text
Prime Numbers up to 100
============================================================
Total count: 25

All primes:
     2      3      5      7     11     13     17     19     23     29
    31     37     41     43     47     53     59     61     67     71
    73     79     83     89     97
```

## Requirements

- Python 3.7+
- No external dependencies (uses only standard library)

## Mathematical Background

Prime numbers are fundamental in number theory and have applications in:

- Cryptography (RSA encryption)
- Hash functions
- Random number generation
- Computer science algorithms

The Sieve of Eratosthenes has a time complexity of O(n log log n), making it one of the most efficient algorithms for finding primes.

Interesting facts:

- There are infinitely many prime numbers (proven by Euclid)
- Twin primes are pairs of primes that differ by 2 (e.g., 3 and 5, 11 and 13)
- The largest known prime as of 2023 has over 24 million digits

## How to Contribute

Feel free to fork and send pull requests!

---

## LICENSE

This project is licensed under the MIT License - see the LICENSE file for details.
