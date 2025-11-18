# Pythagorean Triples Finder

This repository provides a solution in Python to find all Pythagorean triples up to a given limit.

## Problem Description

A Pythagorean triple consists of three positive integers (a, b, c) such that:

- a² + b² = c²
- a, b, c are positive integers

The most famous example is (3, 4, 5) since 3² + 4² = 5² (9 + 16 = 25).

A primitive Pythagorean triple is one where the greatest common divisor (gcd) of a, b, and c is 1.

## How It Works

The program:

1. Generates all possible combinations of (a, b) where a ≤ b ≤ max_value
2. Calculates c = √(a² + b²)
3. Checks if c is an integer and within the limit
4. Identifies primitive triples by checking if gcd(a, b, c) = 1

## Usage

Clone the repository and run:

```bash
python pythagorean_triples.py
```

The program will find and display all Pythagorean triples with sides up to 100, including:

- All triples found
- Primitive triples only
- Statistics about the results

## Example Output

```text
Pythagorean Triples:
Total count: 52

1. (3, 4, 5) - 3² + 4² = 5² (9 + 16 = 25)
2. (5, 12, 13) - 5² + 12² = 13² (25 + 144 = 169)
...
```

## Requirements

- Python 3.7+
- No external dependencies (uses only standard library)

## Mathematical Background

Pythagorean triples have been studied since ancient times. Euclid's formula can generate all primitive triples:

- a = m² - n²
- b = 2mn
- c = m² + n²

where m > n > 0, m and n are coprime, and one of them is even.

## How to Contribute

Feel free to fork and send pull requests!

---

## LICENSE

This project is licensed under the MIT License.
