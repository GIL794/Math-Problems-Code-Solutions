# Fibonacci Sequence Analyzer

This repository provides a solution in Python to generate and analyze the Fibonacci sequence.

## Problem Description

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones:

- F(0) = 0
- F(1) = 1
- F(n) = F(n-1) + F(n-2) for n > 1

The sequence begins: **0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...**

## How It Works

The program includes multiple methods to generate Fibonacci numbers:

1. **Iterative method**: Efficient O(n) time complexity
2. **Recursive method**: Simple but inefficient for large n
3. **Binet's formula**: Uses the golden ratio for direct calculation

The program also analyzes:
- Ratio between consecutive terms (approaching the golden ratio)
- Prime Fibonacci numbers
- Even/odd distribution
- Sum properties

## Usage

Clone the repository and run:

```bash
python fibonacci_analyzer.py
```

The program will:
- Generate Fibonacci sequences of various lengths
- Analyze mathematical properties
- Calculate specific Fibonacci numbers
- Compare different calculation methods

## Example Output

```text
Fibonacci Sequence (first 20 terms)
============================================================
  F(0)     F(1)     F(2)     F(3)     F(4)     F(5)     F(6)     F(7)
       0        1        1        2        3        5        8       13
```

## Requirements

- Python 3.7+
- No external dependencies (uses only standard library)

## Mathematical Background

The Fibonacci sequence appears throughout nature and mathematics:

- **Golden Ratio**: The ratio of consecutive Fibonacci numbers approaches φ = (1 + √5) / 2 ≈ 1.618
- **Nature**: Found in flower petals, pinecones, shells (spiral patterns)
- **Binet's Formula**: F(n) = (φⁿ - ψⁿ) / √5, where ψ = (1 - √5) / 2
- **Properties**:
  - Sum of first n Fibonacci numbers = F(n+2) - 1
  - Every 3rd Fibonacci number is even
  - F(n) is prime for n = 3, 4, 5, 7, 11, 13, 17, 23, 29, 43, 47, ...

Applications:
- Computer algorithms (dynamic programming, graph theory)
- Financial modeling
- Art and design (golden ratio)
- Cryptography

## How to Contribute

Feel free to fork and send pull requests!

---

## LICENSE

This project is licensed under the MIT License - see the LICENSE file for details.

