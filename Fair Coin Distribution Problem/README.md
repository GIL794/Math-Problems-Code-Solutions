# Fair Coin Distribution Problem Solver

This repository provides a solution in Python to the following combinatorial optimisation problem:

## Problem Description

> A father has 7 children and 49 coins, where each coin weighs 1g more than the previous (i.e., coins weigh from 1g to 49g). Each child should receive a maximum of 7 coins, and the **sum of the weights** must be the same for each child. No one gets more or fewer coins or any difference in total weight.

This is a classic fair distribution problem that demonstrates:
- Combinatorial optimisation
- Constraint satisfaction
- Fair resource allocation algorithms
- Mathematical problem-solving with code

## Mathematical Analysis

**Given:**
- 49 coins with weights: 1g, 2g, 3g, ..., 49g
- Total weight: 1 + 2 + 3 + ... + 49 = 49 × 50 / 2 = 1,225g
- 7 children
- Each child gets at most 7 coins
- Each child must receive the same total weight

**Constraints:**
- If each child gets exactly 7 coins: 7 × 7 = 49 coins (all coins used)
- Target weight per child: 1,225g / 7 = 175g
- Each child must receive exactly 175g worth of coins

## How It Works

The code computes valid distributions (if possible) matching the conditions above using:
- Combinatorial search algorithms
- Constraint satisfaction techniques
- Backtracking or exhaustive search methods

## Usage

Clone the repository and run:

```bash
python coin_distributor.py
```

The program will print the solution or state if there is none.

## Requirements

- Python 3.7+
- No external dependencies required - uses only Python standard library:
  - Standard library functions for combinatorial operations
  - Coin distribution algorithm implementation

## Applications

This type of problem has real-world applications in:
- **Resource Allocation**: Distributing resources fairly among multiple parties
- **Scheduling**: Assigning tasks with constraints
- **Combinatorial Optimisation**: Finding optimal distributions
- **Fair Division**: Ensuring equitable resource sharing

## Mathematical Significance

This problem demonstrates:
- **Combinatorial Mathematics**: Finding valid combinations under constraints
- **Optimisation Theory**: Maximising fairness while satisfying constraints
- **Algorithm Design**: Efficient search strategies for constraint satisfaction
- **Fair Division**: Principles of equitable distribution

## How to Contribute

Feel free to fork and send pull requests!

---

## LICENSE

This project is licensed under the MIT License - see the LICENSE file for details.
