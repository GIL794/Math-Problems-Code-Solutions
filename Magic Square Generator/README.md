# Magic Square Generator

This repository provides a solution in Python to generate magic squares of various sizes.

## Problem Description

A magic square is an n×n grid filled with distinct positive integers from 1 to n² such that:

- The sum of numbers in each **row** is the same
- The sum of numbers in each **column** is the same
- The sum of numbers in both **main diagonals** is the same

The magic constant (the sum) for an n×n magic square is:
**M = n(n² + 1) / 2**

For example, a 3×3 magic square has a magic constant of 15:

```text
8  1  6
3  5  7
4  9  2
```

## How It Works

The program uses different algorithms depending on the size:

1. **Odd-sized squares** (3, 5, 7, ...): Uses the **Siamese method** (also called De la Loubère's method)
   - Start in the middle of the top row
   - Move diagonally up-right
   - If position is occupied, move down instead
   - Wrap around edges

2. **Doubly even-sized squares** (4, 8, 12, ...): Uses a pattern-based method
   - Fill sequentially, then swap elements in specific positions

3. **Singly even-sized squares** (6, 10, 14, ...): Uses the **LUX method**
   - Divides into four quadrants based on an odd magic square
   - Swaps elements to achieve the magic property

## Usage

Clone the repository and run:

```bash
python magic_square.py
```

The program will generate and display magic squares of sizes 3, 4, 5, and 7, along with verification that they are valid magic squares.

## Example Output

```text
Magic Square of size 3×3
Magic Constant: 15
============================================================

   8    1    6

   3    5    7

   4    9    2

Verification: Valid magic square
Expected magic constant: 15
============================================================
```

## Requirements

- Python 3.7+
- NumPy (for array operations, though the code can work without it)

Note: The current implementation uses basic Python lists. NumPy is imported but not strictly required for the core functionality.

## Mathematical Background

Magic squares have fascinated mathematicians for thousands of years. They appear in:

- Ancient Chinese mathematics (Lo Shu square)
- Islamic art and architecture
- Renaissance mathematics
- Modern recreational mathematics

The number of distinct magic squares increases rapidly with size:

- 3×3: 1 unique magic square (up to rotation/reflection)
- 4×4: 880 distinct magic squares
- 5×5: 275,305,224 distinct magic squares

## How to Contribute

Feel free to fork and send pull requests!

---

## LICENSE

This project is licensed under the MIT License.
