# GCD and LCM Calculator

This repository provides a comprehensive solution in Python to calculate the Greatest Common Divisor (GCD) and Least Common Multiple (LCM) of numbers.

## Problem Description

The **Greatest Common Divisor (GCD)** of two integers is the largest positive integer that divides both numbers without a remainder. The **Least Common Multiple (LCM)** is the smallest positive integer that is divisible by both numbers.

### Examples:

**GCD Examples:**
- **GCD(12, 18) = 6** - The largest number that divides both 12 and 18
- **GCD(48, 180) = 12** - Common divisors are 1, 2, 3, 4, 6, 12
- **GCD(17, 19) = 1** - Coprime numbers (no common divisors except 1)

**LCM Examples:**
- **LCM(12, 18) = 36** - The smallest number divisible by both 12 and 18
- **LCM(4, 6) = 12** - Multiples of 4: 4, 8, 12... Multiples of 6: 6, 12...
- **LCM(5, 7) = 35** - For coprime numbers, LCM = a × b

**Mathematical Relationship:**
- For any two numbers a and b: **GCD(a, b) × LCM(a, b) = a × b**

## How It Works

The program implements multiple algorithms:

### 1. **Euclidean Algorithm** (for GCD)
The most efficient method, discovered by Euclid around 300 BCE:
- Repeatedly replace the larger number with the remainder of division
- Continue until the remainder is 0
- Example: GCD(48, 180)
  - 180 = 48 × 3 + 36
  - 48 = 36 × 1 + 12
  - 36 = 12 × 3 + 0
  - Result: GCD = 12

### 2. **LCM Calculation**
Uses the relationship: **LCM(a, b) = (a × b) / GCD(a, b)**

### 3. **Extended Euclidean Algorithm**
Finds integers x and y such that: **a × x + b × y = GCD(a, b)**
- Essential for modular arithmetic and cryptography
- Used in RSA key generation

### 4. **Multiple Numbers**
Extends GCD and LCM to work with more than two numbers:
- GCD: Apply repeatedly: GCD(a, b, c) = GCD(GCD(a, b), c)
- LCM: Apply repeatedly: LCM(a, b, c) = LCM(LCM(a, b), c)

## Features

- ✅ Calculate GCD using the efficient Euclidean algorithm
- ✅ Calculate LCM using the GCD relationship
- ✅ Extended GCD for finding Bézout coefficients
- ✅ Handle multiple numbers (3 or more)
- ✅ Check if numbers are coprime (relatively prime)
- ✅ Find all common divisors of two numbers
- ✅ Step-by-step visualisation of the Euclidean algorithm
- ✅ Demonstrate mathematical properties and relationships

## Usage

Clone the repository and run:

```bash
python gcd_lcm_calculator.py
```

The program will:
- Calculate GCD and LCM for various number pairs
- Show step-by-step calculation process
- Demonstrate the Extended Euclidean Algorithm
- Find GCD and LCM of multiple numbers
- Verify mathematical properties

## Example Output

```text
============================================================
Analysis of 12 and 18
============================================================
GCD(12, 18) = 6
LCM(12, 18) = 36
Product: 12 × 18 = 216
GCD × LCM = 6 × 36 = 216
Coprime: No

Extended GCD: 12 × (-1) + 18 × 1 = 6

Divisors of 12: [1, 2, 3, 4, 6, 12]
Divisors of 18: [1, 2, 3, 6, 9, 18]
Common divisors: [1, 2, 3, 6]
Greatest common divisor: 6

============================================================
Step-by-Step GCD Calculation: GCD(48, 180)
============================================================
Step 1: 180 = 48 × 3 + 36
Step 2: 48 = 36 × 1 + 12
Step 3: 36 = 12 × 3 + 0

Result: GCD(48, 180) = 12
```

## Requirements

- Python 3.7+
- No external dependencies (uses only standard library)

## Mathematical Background

### Historical Significance
- **Euclid's Algorithm** (300 BCE) - One of the oldest algorithms still in use
- Appears in Euclid's "Elements" - Book VII, Propositions 1-2
- One of the most efficient algorithms ever devised

### Properties of GCD
1. **Commutative**: GCD(a, b) = GCD(b, a)
2. **Associative**: GCD(a, GCD(b, c)) = GCD(GCD(a, b), c)
3. **Identity**: GCD(a, 0) = a
4. **GCD and LCM relationship**: GCD(a, b) × LCM(a, b) = a × b

### Coprime Numbers
Two numbers are **coprime** (or relatively prime) if GCD(a, b) = 1:
- 8 and 15 are coprime (no common factors except 1)
- Consecutive integers are always coprime
- Coprime numbers are important in cryptography (RSA encryption)

## Real-World Applications

### 1. **Fraction Simplification** 🔢
Reduce fractions to lowest terms:
- 12/18 → divide by GCD(12, 18) = 6 → 2/3

### 2. **Cryptography** 🔐
- **RSA Encryption**: Requires coprime numbers for key generation
- **Extended GCD**: Finds modular multiplicative inverses
- Modern internet security relies on these algorithms

### 3. **Scheduling Problems** 📅
- Two buses arrive every 12 and 18 minutes
- They coincide every LCM(12, 18) = 36 minutes
- Used in task scheduling, traffic light synchronization

### 4. **Music Theory** 🎵
- Harmonic frequencies are related by simple ratios
- GCD helps find common harmonics
- LCM determines when waveforms repeat

### 5. **Gear Ratios** ⚙️
- Design mechanical systems with specific gear ratios
- Determine when gears return to starting position
- LCM calculates rotation cycles

### 6. **Computer Graphics** 🎨
- Pixel spacing and pattern generation
- Tiling and tessellation algorithms
- Screen resolution calculations

### 7. **Number Theory Research** 🔬
- Fundamental to many proofs and algorithms
- Connection to prime factorization
- Basis for advanced mathematical concepts

## Time Complexity

- **Euclidean Algorithm**: O(log(min(a, b))) - Very efficient!
- **LCM Calculation**: O(log(min(a, b))) - Same as GCD
- **Extended GCD**: O(log(min(a, b))) - Same complexity
- For n numbers: O(n × log(min(numbers)))

The Euclidean algorithm is remarkably efficient - even for very large numbers, it completes in just a few steps!

## How to Contribute

Feel free to fork and send pull requests! Suggestions for improvements:
- Implement binary GCD algorithm (Stein's algorithm)
- Add visualisation of the Euclidean algorithm
- Include more real-world examples
- Add interactive input mode

---

## LICENSE

This project is licensed under the MIT License - see the LICENSE file for details.
