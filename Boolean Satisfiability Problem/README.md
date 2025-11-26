# Boolean Satisfiability Problem (SAT) Solver

This repository provides a comprehensive Python implementation of the Boolean Satisfiability Problem (SAT), the **first problem proven to be NP-complete** and one of the most fundamental problems in computer science, mathematics, and computational complexity theory.

## Problem Description

**The Boolean Satisfiability Problem (SAT)**: Given a Boolean formula in Conjunctive Normal Form (CNF), determine if there exists an assignment of truth values to variables that makes the formula true.

### Mathematical Formulation

A CNF formula is a conjunction (AND) of clauses, where each clause is a disjunction (OR) of literals:

```text
F = (x₁ ∨ x₂ ∨ ¬x₃) ∧ (¬x₁ ∨ x₂) ∧ (x₃ ∨ ¬x₂)
```

**Question**: Does there exist an assignment of {True, False} to variables {x₁, x₂, x₃, ...} such that F evaluates to True?

### Example

**Formula**: (x₁ OR x₂) AND (NOT x₁ OR x₂) AND (x₁ OR NOT x₂)

**Satisfying Assignment**: x₁ = True, x₂ = True

**Verification**:

- (True OR True) = True ✓
- (NOT True OR True) = True ✓
- (True OR NOT True) = True ✓

## Why SAT is the Most Difficult Problem

### 1. **NP-Completeness**

SAT was the **first problem proven to be NP-complete** by Stephen Cook in 1971 (Cook-Levin Theorem). This means:

- **Every problem in NP** can be reduced to SAT in polynomial time
- If SAT can be solved in polynomial time, then **P = NP** (worth $1,000,000 Millennium Prize)
- Solving SAT efficiently would solve **thousands of other problems** instantly

### 2. **Computational Complexity**

- **Time Complexity**: O(2ⁿ) in worst case (exponential)
- **Space Complexity**: O(n + m) where n = variables, m = clauses
- **Best Known**: No polynomial-time algorithm exists (unless P = NP)
- **Practical Limit**: Even with optimisations, instances with >1000 variables become intractable

### 3. **Theoretical Significance**

SAT sits at the heart of computational complexity theory:

- **Foundation of NP-completeness**: Proved that thousands of problems are equally hard
- **P vs NP Problem**: Central to the most important open question in computer science
- **Reduction Hub**: Most NP-complete proofs reduce problems to SAT

### 4. **Practical Difficulty**

- **Exponential Explosion**: 20 variables = 1 million assignments, 30 variables = 1 billion
- **No Efficient Algorithm**: Despite 50+ years of research, no polynomial algorithm found
- **Heuristic-Dependent**: Performance varies dramatically with problem structure
- **Industrial Challenge**: Real-world instances require sophisticated solvers

## Mathematical Significance

### Cook-Levin Theorem (1971)

**Statement**: SAT is NP-complete.

**Proof Sketch**:

1. SAT is in NP (easy to verify solutions)
2. Every problem in NP reduces to SAT
3. Therefore, SAT is NP-complete

**Impact**: This single theorem established the entire field of computational complexity and showed that thousands of seemingly different problems are fundamentally the same.

### Karp's 21 NP-Complete Problems (1972)

Richard Karp showed 21 classic problems are NP-complete by reducing them to SAT:

- Traveling Salesman Problem
- Graph Coloring
- Clique Problem
- Set Cover
- And 17 more...

All these reductions prove: **If you can solve SAT efficiently, you can solve all of them efficiently.**

### P vs NP Problem

**The Million-Dollar Question**: Is P = NP?

- **If P = NP**: SAT (and thousands of problems) have efficient solutions
- **If P ≠ NP**: SAT requires exponential time (current belief)
- **Status**: Unsolved, one of seven Millennium Prize Problems

## How It Works

### DPLL Algorithm

This implementation uses the **Davis-Putnam-Logemann-Loveland (DPLL)** algorithm:

1. **Unit Propagation**: If a clause has one unassigned literal, it must be true
2. **Pure Literal Elimination**: If a variable appears only positively (or only negatively), assign it accordingly
3. **Decision**: Choose an unassigned variable and try True
4. **Backtracking**: If conflict occurs, backtrack and try False
5. **Recursion**: Recursively solve simplified formula

### Algorithm Features

- **Complete**: Guaranteed to find solution if one exists
- **Sound**: Only returns valid satisfying assignments
- **Systematic**: Explores all possibilities through backtracking
- **Optimised**: Uses unit propagation and pure literal elimination

### Time Complexity

- **Best Case**: O(n) with unit propagation
- **Average Case**: O(2^(n/4)) for random 3-SAT
- **Worst Case**: O(2ⁿ) exponential explosion

## Features

This implementation includes:

1. **Complete DPLL Algorithm**: Full backtracking search with optimisations
2. **CNF Representation**: Efficient clause and literal management
3. **Unit Propagation**: Automatic variable assignment from unit clauses
4. **Pure Literal Elimination**: Simplification through pure literals
5. **Multiple Examples**: Various satisfiable and unsatisfiable instances
6. **Pigeonhole Principle**: Demonstrates unsatisfiable formulas
7. **Random 3-SAT**: Generates difficult test instances

## Usage

Clone the repository and run:

```bash
python sat_solver.py
```

The program will:

- Solve multiple example CNF formulas
- Display formulas in human-readable format
- Show satisfying assignments or prove unsatisfiability
- Demonstrate different types of SAT instances

## Example Output

```text
======================================================================
Example 1: Simple Satisfiable
======================================================================
CNF Formula:
----------------------------------------------------------------------
(x1 OR x2) AND (NOT x1 OR x2) AND (x1 OR NOT x2)

Variables: 2, Clauses: 3

Result: SATISFIABLE

Satisfying Assignment:
----------------------------------------------------------------------
  x1 = True
  x2 = True
```

## Requirements

- Python 3.7+
- No external dependencies required - uses only Python standard library:
  - Standard library functions for Boolean operations
  - Data structures for CNF representation
  - Backtracking algorithm implementation

## Real-World Applications

### 1. Hardware Verification 🔌

- **Circuit Design**: Verify logic circuits are correct
- **Model Checking**: Ensure hardware meets specifications
- **Bug Detection**: Find design errors before manufacturing
- **Used By**: Intel, AMD, NVIDIA for chip verification

### 2. Software Verification 💻

- **Program Correctness**: Prove programs meet specifications
- **Static Analysis**: Find bugs without running code
- **Formal Methods**: Mathematical verification of software
- **Used By**: NASA, Microsoft, Google for critical systems

### 3. Artificial Intelligence 🤖

- **Automated Planning**: Generate plans for robots/AI
- **Constraint Satisfaction**: Solve CSP problems via SAT
- **Knowledge Representation**: Encode logical knowledge
- **Used By**: Planning systems, expert systems

### 4. Cryptography & Security 🔐

- **Cryptanalysis**: Break cryptographic systems
- **Key Recovery**: Find encryption keys
- **Security Analysis**: Verify security properties
- **Used By**: Security researchers, cryptanalysts

### 5. Scheduling & Optimisation 📅

- **Resource Allocation**: Assign resources optimally
- **Task Scheduling**: Schedule tasks with constraints
- **Route Planning**: Optimise delivery routes
- **Used By**: Airlines, logistics companies, cloud providers

### 6. Theorem Proving 📐

- **Automated Reasoning**: Prove mathematical theorems
- **Logic Puzzles**: Solve Sudoku, puzzles, games
- **Formal Verification**: Verify mathematical proofs
- **Used By**: Mathematicians, computer scientists

## Algorithm Complexity

### Time Complexity

| Algorithm | Best Case | Average Case | Worst Case |
|-----------|-----------|--------------|------------|
| **DPLL** | O(n) | O(2^(n/4)) | O(2ⁿ) |
| **CDCL** | O(n) | O(2^(n/5)) | O(2ⁿ) |
| **Brute Force** | O(2ⁿ) | O(2ⁿ) | O(2ⁿ) |

### Space Complexity

- **DPLL**: O(n + m) - linear in formula size
- **CDCL**: O(n + m + c) - includes learned clauses
- **Brute Force**: O(n) - just assignment storage

### Why Exponential?

For n variables, there are 2ⁿ possible assignments:

- n = 10: 1,024 assignments
- n = 20: 1,048,576 assignments
- n = 30: 1,073,741,824 assignments
- n = 50: 1,125,899,906,842,624 assignments

Even with optimisations, worst-case requires exponential time.

## Advanced Topics

### 1. Conflict-Driven Clause Learning (CDCL)

Modern SAT solvers use CDCL:

- **Learn from Conflicts**: When backtracking, learn new clauses
- **Non-Chronological Backtracking**: Jump back multiple levels
- **VSIDS Heuristic**: Variable State Independent Decaying Sum
- **Performance**: 100-1000x faster than basic DPLL

### 2. Random k-SAT

**Phase Transition**: At clause/variable ratio ≈ 4.26, problems transition from easy to hard:

- **Below threshold**: Mostly satisfiable, easy to solve
- **At threshold**: Hardest instances (50% satisfiable)
- **Above threshold**: Mostly unsatisfiable, easier to prove

### 3. Approximation Algorithms

While exact SAT is hard, approximations exist:

- **MAX-SAT**: Maximise number of satisfied clauses
- **Approximation Ratios**: Can achieve 3/4 of optimal
- **Practical Use**: When exact solution not needed

### 4. Special Cases

Some SAT variants are polynomial-time:

- **2-SAT**: Clauses with 2 literals (O(n + m))
- **Horn SAT**: Special clause structure (O(n + m))
- **XOR-SAT**: Linear algebra approach

### 5. Quantum Algorithms

**Grover's Algorithm**: Quantum search can solve SAT in O(√2ⁿ) time

- **Quadratic Speedup**: Still exponential, but faster
- **Requires**: Large-scale quantum computers (not yet available)
- **Future**: May provide practical speedup for SAT

## Limitations of This Implementation

1. **Educational Purpose**: Basic DPLL, not production-grade
2. **No CDCL**: Doesn't use modern conflict-driven learning
3. **Simple Heuristics**: Uses first unassigned variable (not VSIDS)
4. **No Parallelisation**: Sequential implementation
5. **Memory**: Could be optimised for very large instances

**For Production Use**: Consider libraries like:

- **PySAT** (Python)
- **MiniSAT** (C++)
- **Glucose** (C++)
- **Z3** (Microsoft's SMT solver)

## Interesting Facts

1. **Historical**: First NP-complete proof (Cook, 1971)
2. **Millennium Prize**: Solving SAT efficiently = $1,000,000
3. **Industrial Impact**: Used to verify billions of dollars of hardware
4. **Competitions**: Annual SAT competitions with thousands of instances
5. **Records**: Modern solvers can handle millions of variables
6. **Reductions**: Thousands of problems reduce to SAT
7. **Theoretical**: Central to computational complexity theory

## Mathematical Theorems

### Cook-Levin Theorem (1971)

**Every problem in NP reduces to SAT in polynomial time.**

This single theorem:

- Established NP-completeness as a concept
- Showed thousands of problems are equally hard
- Created the foundation of complexity theory
- Won Stephen Cook the Turing Award (1982)

### Karp's Reductions (1972)

Richard Karp showed 21 problems are NP-complete by reducing to SAT:

- Proved fundamental equivalence of diverse problems
- Established reduction as proof technique
- Won Richard Karp the Turing Award (1985)

### PCP Theorem (1990s)

**Probabilistically Checkable Proofs**: Relates SAT to approximation hardness

- Shows even approximating SAT is hard
- Fundamental to modern complexity theory
- Won multiple researchers major awards

## Performance Characteristics

### Small Instances (n < 20)

- Solves instantly
- Can enumerate all assignments
- Useful for verification

### Medium Instances (n < 50)

- Solves in seconds to minutes
- Requires backtracking
- Practical for many applications

### Large Instances (n < 100)

- May take hours or days
- Requires sophisticated heuristics
- Used in industrial verification

### Very Large Instances (n > 100)

- May be intractable
- Requires modern CDCL solvers
- Used in research and competitions

## How to Contribute

Feel free to fork and send pull requests! Some ideas:

- Implement CDCL (Conflict-Driven Clause Learning)
- Add VSIDS heuristic for variable selection
- Implement clause learning and non-chronological backtracking
- Add DIMACS CNF file parser
- Implement 2-SAT polynomial algorithm
- Add MAX-SAT approximation
- Implement parallel SAT solving
- Add visualisation of search tree
- Optimise for large instances

## Further Reading

### Textbooks

- "Computational Complexity" by Arora & Barak
- "Introduction to Algorithms" (CLRS) - Chapter on NP-completeness
- "The Complexity of Boolean Functions" by Wegener

### Research Papers

- Cook (1971): "The Complexity of Theorem-Proving Procedures"
- Karp (1972): "Reducibility Among Combinatorial Problems"
- Marques-Silva & Sakallah (1999): "GRASP: A Search Algorithm for Propositional Satisfiability"

### Online Resources

- Wikipedia: Boolean Satisfiability Problem
- SAT Competition: Annual competition website
- Complexity Zoo: Complexity class definitions

---

## LICENSE

This project is licensed under the MIT License - see the LICENSE file for details.
