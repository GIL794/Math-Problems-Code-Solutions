# Perfect Numbers Finder

This repository provides a solution in Python to find and analyze perfect numbers.

## Problem Description

A perfect number is a positive integer that is equal to the sum of its proper positive divisors (excluding the number itself).

Examples:

- **6** = 1 + 2 + 3 (divisors: 1, 2, 3)
- **28** = 1 + 2 + 4 + 7 + 14 (divisors: 1, 2, 4, 7, 14)
- **496** = 1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248

## How It Works

The program includes two methods:

1. **Brute Force Method**: Checks each number by finding all divisors
2. **Euclid's Formula**: Uses the mathematical relationship between Mersenne primes and perfect numbers
   - If 2^p - 1 is prime (Mersenne prime), then (2^p - 1) × 2^(p-1) is perfect

The program also:

- Classifies numbers as perfect, abundant, or deficient
- Analyzes divisor properties
- Verifies perfect numbers mathematically

## Usage

Clone the repository and run:

```bash
python perfect_numbers.py
```

The program will:

- Find perfect numbers up to 10,000 using both methods
- Analyze known perfect numbers in detail
- Classify numbers as perfect, abundant, or deficient
- Search for perfect numbers up to 100,000,000 using Euclid's formula

## Example Output

```text
Perfect Numbers Found
============================================================
Total count: 4

6:
  Divisors: [1, 2, 3]
  Verification: 1 + 2 + 3 = 6 = 6

28:
  Divisors: [1, 2, 4, 7, 14]
  Verification: 1 + 2 + 4 + 7 + 14 = 28 = 28
```

## Requirements

- Python 3.7+
- No external dependencies (uses only standard library)

## Mathematical Background

Perfect numbers have fascinated mathematicians since ancient times:

- **Euclid's Discovery**: Around 300 BCE, Euclid proved that if 2^p - 1 is prime, then (2^p - 1) × 2^(p-1) is perfect
- **Euler's Proof**: In the 18th century, Euler proved that all even perfect numbers follow this form
- **Odd Perfect Numbers**: It is unknown whether any odd perfect numbers exist (none have been found)
- **Mersenne Primes**: Perfect numbers are closely related to Mersenne primes (primes of form 2^p - 1)

Known perfect numbers:
- 6, 28, 496, 8,128, 33,550,336, 8,589,869,056, ...
- As of 2023, 51 perfect numbers are known (all even)
- The largest known perfect number has over 49 million digits

Related concepts:
- **Abundant numbers**: Sum of proper divisors > number (e.g., 12)
- **Deficient numbers**: Sum of proper divisors < number (e.g., 16)

## How to Contribute

Feel free to fork and send pull requests!

---

## LICENSE

This project is licensed under the MIT License - see the LICENSE file for details.

