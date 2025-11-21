# Traveling Salesman Problem (TSP) Solver

This repository provides multiple algorithms to solve the classic Traveling Salesman Problem - one of the most famous NP-hard optimization problems in computer science and operations research.

## Problem Description

**The Traveling Salesman Problem**: Given a list of cities and the distances between each pair, find the shortest possible route that visits each city exactly once and returns to the starting city.

**Mathematical Formulation**:
- Input: Complete graph with n vertices (cities) and weighted edges (distances)
- Output: Hamiltonian cycle with minimum total weight
- Objective: Minimize Σ d(ci, ci+1) for all cities in the tour

**Complexity**: The TSP is NP-hard, meaning:
- No known polynomial-time algorithm exists
- Brute force requires checking (n-1)!/2 possible tours
- For 20 cities: 60,822,550,204,416,000 possible tours!

## Why TSP Matters

The TSP is not just an academic curiosity - it has countless real-world applications:

### Logistics & Transportation
- **Package Delivery**: FedEx, UPS route optimization
- **School Bus Routes**: Efficient student pickup/dropoff
- **Garbage Collection**: Municipal waste management
- **Airline Routes**: Flight scheduling and connections

### Manufacturing
- **Circuit Board Drilling**: Minimize drill movement
- **DNA Sequencing**: Overlap fragment assembly
- **Robotic Welding**: Optimize welding arm path
- **3D Printing**: Layer-by-layer path planning

### Computer Science
- **Network Design**: Fiber optic cable routing
- **Data Analysis**: Clustering and visualization
- **VLSI Design**: Wire routing on chips
- **Compiler Optimization**: Register allocation

## Implementation Features

This solver includes five different approaches, from exact to approximate:

### 1. Brute Force (Exact)
- **Method**: Enumerate all possible tours
- **Complexity**: O(n!)
- **Best For**: Small problems (n ≤ 10)
- **Guarantee**: Optimal solution
- **Note**: Becomes impractical quickly

### 2. Dynamic Programming (Held-Karp Algorithm)
- **Method**: Break problem into subproblems, use memoization
- **Complexity**: O(n² × 2ⁿ)
- **Best For**: Medium problems (n ≤ 20)
- **Guarantee**: Optimal solution
- **Memory**: Exponential space requirement

### 3. Nearest Neighbor Heuristic
- **Method**: Greedy - always visit closest unvisited city
- **Complexity**: O(n²)
- **Best For**: Quick approximations, large problems
- **Guarantee**: Within ~25% of optimal (on average)
- **Advantage**: Fast and simple

### 4. 2-Opt Local Search
- **Method**: Iteratively improve tour by swapping edges
- **Complexity**: O(n²) per iteration
- **Best For**: Improving existing tours
- **Guarantee**: Local optimum (not global)
- **Quality**: Often within 5% of optimal

### 5. Simulated Annealing (Metaheuristic)
- **Method**: Probabilistic technique inspired by metallurgy
- **Complexity**: O(n² × iterations)
- **Best For**: Large problems, good quality solutions
- **Guarantee**: Probabilistically good solutions
- **Flexibility**: Escapes local optima

## Mathematical Background

### NP-Hardness

TSP belongs to the class of NP-hard problems, which means:
1. **No Polynomial Algorithm Known**: Best known exact algorithms are exponential
2. **Easy to Verify**: Given a tour, easy to check its length
3. **Hard to Solve**: Finding optimal tour is computationally expensive
4. **Equivalent Problems**: If you solve TSP in P time, you solve all NP problems

### The P vs NP Question

TSP is related to one of the Millennium Prize Problems:
- **P**: Problems solvable in polynomial time
- **NP**: Problems verifiable in polynomial time
- **Question**: Is P = NP?
- **TSP**: If TSP ∈ P, then P = NP (win $1,000,000!)

### Approximation Algorithms

For practical purposes, we use approximation algorithms:

**Christofides Algorithm** (not implemented here):
- Guarantees at most 1.5× optimal for metric TSP
- Uses minimum spanning tree + matching
- Best known approximation ratio for general metric TSP

**Nearest Neighbor**:
- No worst-case guarantee for general TSP
- Can be O(log n)-approximate for some instances

## Algorithm Comparison

| Algorithm | Time | Space | Optimal | Quality | Best For |
|-----------|------|-------|---------|---------|----------|
| Brute Force | O(n!) | O(n) | Yes | 100% | n ≤ 10 |
| Dynamic Programming | O(n²2ⁿ) | O(n2ⁿ) | Yes | 100% | n ≤ 20 |
| Nearest Neighbor | O(n²) | O(n) | No | ~75% | Quick estimate |
| 2-Opt | O(n²k) | O(n) | No | ~95% | Improvement |
| Simulated Annealing | O(n²k) | O(n) | No | ~90-95% | Large n |

Where k is the number of iterations for iterative algorithms.

## How It Works

The program demonstrates:

1. **Problem Generation**: Create random city distributions
2. **Distance Calculation**: Compute all pairwise distances
3. **Algorithm Execution**: Run each solver
4. **Performance Comparison**: Time and quality metrics
5. **Visualization Data**: Output for plotting tours

## Usage

Run the solver:

```bash
python tsp_solver.py
```

The program will:
- Generate a random set of cities
- Solve using multiple algorithms
- Compare solution quality and runtime
- Display the best tour found
- Show performance statistics

## Example Output

```text
Traveling Salesman Problem Solver
============================================================

Problem: 10 cities
Total possible tours: 181,440

Distance Matrix:
     0    1    2    3    4    5    6    7    8    9
0    0   34   48   23   56   78   45   12   67   89
1   34    0   29   45   67   23   56   78   34   45
...

Solving with Multiple Algorithms:
============================================================

1. Brute Force (Exact):
   Tour: 0 → 3 → 7 → 1 → 2 → 5 → 4 → 8 → 6 → 9 → 0
   Distance: 245
   Time: 2.34 seconds

2. Dynamic Programming (Exact):
   Tour: 0 → 3 → 7 → 1 → 2 → 5 → 4 → 8 → 6 → 9 → 0
   Distance: 245
   Time: 0.18 seconds

3. Nearest Neighbor (Heuristic):
   Tour: 0 → 3 → 1 → 2 → 5 → 7 → 8 → 4 → 6 → 9 → 0
   Distance: 267
   Quality: 91.8% of optimal
   Time: 0.001 seconds

4. 2-Opt Improvement:
   Initial: 267 → Improved: 249
   Quality: 98.4% of optimal
   Time: 0.023 seconds

5. Simulated Annealing:
   Tour: 0 → 7 → 3 → 1 → 2 → 5 → 4 → 8 → 6 → 9 → 0
   Distance: 247
   Quality: 99.2% of optimal
   Time: 0.156 seconds

Best Solution Found: 245 (Brute Force & Dynamic Programming)
```

## Requirements

- Python 3.7+
- No external dependencies (uses only standard library)
- `random` for test case generation
- `itertools` for permutations
- `math` for distance calculations
- `time` for performance measurement

## Advanced Topics

### Variants of TSP

1. **Asymmetric TSP**: Distance from A to B ≠ B to A (one-way streets)
2. **Multiple TSP**: Multiple salesmen, partition cities
3. **TSP with Time Windows**: Visit cities within time constraints
4. **Prize-Collecting TSP**: Optional cities with rewards
5. **Generalized TSP**: Visit one city from each cluster

### Cutting-Edge Algorithms

- **Concorde**: Best exact TSP solver, solved 85,900-city problem
- **LKH (Lin-Kernighan-Helsgaun)**: State-of-the-art heuristic
- **Genetic Algorithms**: Evolutionary approach
- **Ant Colony Optimization**: Swarm intelligence
- **Neural Networks**: Learning-based approaches

### Complexity Theory Connections

**Hamiltonian Cycle**: Decision version of TSP
- Is there a tour with distance ≤ k?
- NP-complete

**TSP Optimization**: Find minimum tour
- NP-hard

**Approximation Hardness**:
- No polynomial-time approximation scheme for general TSP
- Unless P = NP, no polynomial algorithm guarantees any ratio

## Practical Considerations

### When to Use Each Algorithm

**Exact Algorithms** (Brute Force, DP):
- Small problems (n < 20)
- When optimality is crucial
- When you have time to wait

**Heuristics** (Nearest Neighbor):
- Large problems (n > 100)
- Need quick answer
- Approximation acceptable

**Metaheuristics** (Simulated Annealing, 2-Opt):
- Medium to large problems
- Good balance of quality and speed
- When near-optimal is sufficient

### Real-World Enhancements

1. **Caching**: Store distance computations
2. **Parallel Processing**: Run multiple algorithms
3. **Geographic Constraints**: Use lat/long coordinates
4. **Capacity Constraints**: Limited vehicle capacity
5. **Multi-Objective**: Minimize time AND distance

## Interesting Facts

- **Largest TSP Solved**: 85,900 cities (circuit board drilling)
- **Complexity**: 50-city problem has ~10⁶⁴ possible tours
- **First Study**: 1930s by Karl Menger
- **Economic Impact**: Billions saved annually through TSP optimization
- **Still Active Research**: Papers published weekly on TSP variants

## Limitations of This Implementation

- Uses Euclidean distance (easily adaptable)
- Simulated annealing parameters not optimized
- No visualization (generates data for external plotting)
- Not parallelized (could use multiprocessing)
- Educational purpose, not production-grade

## Further Reading

- **Books**: 
  - "The Traveling Salesman Problem" by Applegate et al.
  - "In Pursuit of the Traveling Salesman" by Cook
- **Software**: Concorde TSP Solver, LKH
- **Website**: www.math.uwaterloo.ca/tsp/
- **Competitions**: TSPLIB benchmark instances

---

## LICENSE

This project is licensed under the MIT License - see the LICENSE file for details.
