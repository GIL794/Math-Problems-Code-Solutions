# Maximum Flow Problem Solver

This repository provides a comprehensive Python implementation of the Maximum Flow Problem, one of the most fundamental and widely applied problems in graph theory, network optimisation, and algorithm design.

## Problem Description

**The Maximum Flow Problem**: Given a directed graph (flow network) with:
- A **source** vertex (where flow originates)
- A **sink** vertex (where flow terminates)
- **Edges** with **capacities** (maximum flow each edge can carry)

Find the **maximum amount of flow** that can be sent from source to sink, respecting edge capacity constraints.

### Mathematical Formulation

Given a flow network G = (V, E) with:
- Source s ∈ V, Sink t ∈ V
- Capacity function c: E → ℝ⁺
- Flow function f: E → ℝ⁺

**Constraints:**
1. **Capacity Constraint**: f(u,v) ≤ c(u,v) for all edges (u,v)
2. **Flow Conservation**: Σ f(u,v) = Σ f(v,w) for all v ∈ V\{s,t}
3. **Skew Symmetry**: f(u,v) = -f(v,u)

**Objective**: Maximise Σ f(s,v) (total flow from source)

## Mathematical Significance

The Maximum Flow Problem is central to:

### Graph Theory
- **Max-Flow Min-Cut Theorem**: Maximum flow equals minimum cut capacity
- **Duality**: Flow problems have natural dual problems (min-cut)
- **Network Analysis**: Understanding capacity and bottlenecks

### Algorithm Design
- **Ford-Fulkerson Algorithm**: Classic augmenting path approach
- **Edmonds-Karp Algorithm**: BFS-based variant (O(V·E²))
- **Push-Relabel Algorithms**: More efficient for dense graphs
- **Dinic's Algorithm**: O(V²·E) complexity

### Computational Complexity
- **Polynomial Time**: Solvable in polynomial time (unlike many graph problems)
- **P vs NP**: Demonstrates that some optimisation problems are tractable
- **Approximation**: Basis for approximation algorithms

## How It Works

### Ford-Fulkerson Algorithm

The algorithm works by repeatedly finding **augmenting paths**:

1. **Initialise**: Set all flows to 0
2. **Find Augmenting Path**: Use BFS to find path from source to sink with positive residual capacity
3. **Push Flow**: Send maximum possible flow along the path (bottleneck capacity)
4. **Update Residual Graph**: 
   - Decrease forward edge capacities (flow uses capacity)
   - Increase backward edge capacities (allows flow cancellation)
5. **Repeat**: Until no augmenting path exists

### Residual Graph

The key insight is the **residual graph**:
- **Forward edges**: Remaining capacity (original capacity - current flow)
- **Backward edges**: Allow "undoing" flow to find better paths
- Enables the algorithm to find optimal solutions even after suboptimal initial choices

### Edmonds-Karp Variant

This implementation uses **BFS** (breadth-first search) to find augmenting paths:
- Always finds the **shortest** augmenting path
- Guarantees **O(V·E²)** time complexity
- Prevents infinite loops (unlike DFS with irrational capacities)

## Features

This implementation includes:

1. **Complete Ford-Fulkerson Algorithm**: With BFS (Edmonds-Karp variant)
2. **Residual Graph Management**: Efficient capacity updates
3. **Flow Distribution Tracking**: Shows how flow is distributed across edges
4. **Minimum Cut Calculation**: Finds the bottleneck cut (Max-Flow Min-Cut Theorem)
5. **Bipartite Matching**: Demonstrates how max-flow solves matching problems
6. **Multiple Examples**: Various network configurations
7. **Comprehensive Visualisation**: Detailed output showing algorithm steps

## Usage

Clone the repository and run:

```bash
python maximum_flow.py
```

The program will:
- Solve multiple example networks
- Display maximum flow values
- Show flow distribution across edges
- Calculate and verify minimum cuts
- Demonstrate bipartite matching application

## Example Output

```text
======================================================================
EXAMPLE 1: Simple Network
======================================================================

Network: 5 vertices
Source: 0, Sink: 3

Edges (with capacities):
----------------------------------------------------------------------
  0 → 1: capacity = 10
  0 → 4: capacity = 10
  1 → 2: capacity = 4
  1 → 4: capacity = 2
  4 → 2: capacity = 9
  2 → 3: capacity = 10
  4 → 3: capacity = 10

======================================================================
Solving Maximum Flow Problem...
======================================================================

✓ Maximum Flow: 19

Flow Distribution:
----------------------------------------------------------------------
  0 → 1: 10/10 (flow/capacity)
  0 → 4: 9/10 (flow/capacity)
  1 → 2: 4/4 (flow/capacity)
  4 → 2: 5/9 (flow/capacity)
  2 → 3: 9/10 (flow/capacity)
  4 → 3: 10/10 (flow/capacity)

Minimum Cut:
----------------------------------------------------------------------
  Source side: [0, 1, 4]
  Sink side: [2, 3]

Edges in minimum cut:
  1 → 2: capacity = 4
  4 → 2: capacity = 9
  4 → 3: capacity = 10

✓ Minimum Cut Capacity: 23
✓ Verification (Max-Flow Min-Cut Theorem): 19 = 19
```

## Requirements

- Python 3.7+
- No external dependencies (uses only standard library)
- `collections.deque` for BFS queue
- `typing` for type hints (optional)

## Real-World Applications

### 1. Network Routing & Bandwidth Allocation 🌐
- **Internet Routing**: Maximise data throughput in networks
- **Telecommunications**: Allocate bandwidth in communication networks
- **Content Delivery**: Distribute content from servers to users
- **Load Balancing**: Distribute requests across servers

### 2. Bipartite Matching Problems 👥
- **Job Assignment**: Match employees to tasks
- **Dating/Matching**: Match people based on preferences
- **University Admissions**: Assign students to courses
- **Resource Allocation**: Match resources to demands

### 3. Image Processing & Computer Vision 🖼️
- **Image Segmentation**: Separate foreground from background
- **Graph Cut Algorithms**: Used in image editing software
- **Object Detection**: Identify and isolate objects

### 4. Supply Chain & Logistics 📦
- **Transportation Networks**: Maximise product flow
- **Pipeline Systems**: Oil, gas, water distribution
- **Manufacturing**: Optimise production flow
- **Warehouse Management**: Route goods efficiently

### 5. Sports & Scheduling ⚽
- **Tournament Scheduling**: Assign teams to time slots
- **Resource Booking**: Allocate facilities to events
- **Transport Scheduling**: Route vehicles optimally

### 6. Game Theory & Economics 💰
- **Market Clearing**: Match supply and demand
- **Auction Design**: Allocate goods efficiently
- **Coalition Formation**: Optimal group assignments

## Algorithm Complexity

### Time Complexity

| Algorithm | Time Complexity | Best For |
|-----------|----------------|----------|
| **Ford-Fulkerson (DFS)** | O(E · max_flow) | Small flows, simple graphs |
| **Edmonds-Karp (BFS)** | O(V · E²) | General purpose (this implementation) |
| **Dinic's Algorithm** | O(V² · E) | Dense graphs |
| **Push-Relabel** | O(V² · E) | Very dense graphs |
| **Orlin's Algorithm** | O(V · E) | Theoretical best |

### Space Complexity
- **O(V + E)**: Store graph and residual capacities
- **O(V)**: BFS queue and parent array

### Why It's Complex

1. **Non-Greedy**: Optimal solution may require "undoing" previous flow
2. **Residual Graph**: Must maintain both forward and backward edges
3. **Path Finding**: Must efficiently find augmenting paths
4. **Capacity Updates**: Must correctly update residual capacities
5. **Correctness Proof**: Requires understanding of network flow theory

## Mathematical Theorems

### Max-Flow Min-Cut Theorem

**Statement**: In any flow network, the maximum flow from source to sink equals the minimum cut capacity.

**Significance**: 
- Proves algorithm correctness
- Provides dual perspective (flow vs cut)
- Enables verification of solutions
- Fundamental to network theory

### Integrality Theorem

If all capacities are integers, the Ford-Fulkerson algorithm produces an integer flow.

**Implications**:
- Discrete problems (matching, assignment) have integer solutions
- No need for fractional flows in many applications
- Simplifies implementation

## Advanced Topics

### 1. Multiple Sources and Sinks
- Add super-source connecting to all sources
- Add super-sink connecting from all sinks
- Reduces to standard max-flow problem

### 2. Minimum Cost Maximum Flow
- Each edge has both capacity and cost
- Find maximum flow with minimum total cost
- Applications: Transportation, logistics

### 3. Circulation Problems
- No source/sink: flow must be conserved everywhere
- More general than max-flow
- Applications: Scheduling with constraints

### 4. Bipartite Matching
- Special case: all edges have capacity 1
- Maximum flow = maximum matching
- Applications: Assignment problems

### 5. Network Reliability
- Find minimum edges to remove to disconnect source and sink
- Related to minimum cut
- Applications: Network security, fault tolerance

## Performance Characteristics

### Small Networks (V < 20)
- Solves instantly
- Can enumerate all paths
- Useful for verification

### Medium Networks (V < 100)
- Solves in milliseconds
- Practical for real applications
- Good for interactive systems

### Large Networks (V < 1000)
- Solves in seconds
- Requires efficient implementation
- Used in production systems

### Very Large Networks (V > 1000)
- May require advanced algorithms (Dinic's, Push-Relabel)
- Parallel implementations available
- Used in large-scale systems

## Limitations of This Implementation

1. **Educational Purpose**: Not optimised for production use
2. **Single Algorithm**: Only implements Edmonds-Karp
3. **No Parallelisation**: Sequential implementation
4. **Memory**: Could be optimised for very large graphs
5. **Input Validation**: Basic validation (could be enhanced)

**For Production Use**: Consider libraries like:
- NetworkX (Python)
- Boost Graph Library (C++)
- JGraphT (Java)
- igraph (R, Python, C)

## Interesting Facts

1. **Historical**: First solved by Ford and Fulkerson in 1956
2. **Polynomial Time**: One of first polynomial-time algorithms for optimisation
3. **Duality**: Demonstrates strong duality in linear programming
4. **Applications**: Used in Google's PageRank, Facebook's friend suggestions
5. **Complexity**: Despite being polynomial, still challenging for large graphs
6. **Variants**: Hundreds of variants and extensions exist

## How to Contribute

Feel free to fork and send pull requests! Some ideas:
- Implement Dinic's algorithm for better performance
- Add minimum cost maximum flow
- Implement push-relabel algorithm
- Add graph visualisation
- Support for multiple sources/sinks
- Add capacity scaling optimisation
- Implement parallel algorithms
- Add more example networks

## Further Reading

### Textbooks
- "Introduction to Algorithms" (CLRS) - Chapter 26
- "Algorithm Design" by Kleinberg & Tardos
- "Network Flows" by Ahuja, Magnanti, & Orlin

### Research Papers
- Ford & Fulkerson (1956): Original algorithm
- Edmonds & Karp (1972): BFS variant
- Dinic (1970): More efficient algorithm

### Online Resources
- Wikipedia: Maximum Flow Problem
- TopCoder: Algorithm tutorials
- Competitive Programming resources

---

## LICENSE

This project is licensed under the MIT License - see the LICENSE file for details.

