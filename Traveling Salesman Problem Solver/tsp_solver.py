"""
Traveling Salesman Problem (TSP) Solver

Implements multiple algorithms to solve the classic TSP - one of the most
famous NP-hard optimization problems. Compares exact, heuristic, and
metaheuristic approaches.

Demonstrates why some problems are computationally hard and how we can
still find good solutions in practice.
"""

import itertools
import math
import random
import time
from typing import List, Tuple


def euclidean_distance(city1: Tuple[float, float], 
                       city2: Tuple[float, float]) -> float:
    """
    Calculate Euclidean distance between two cities.
    
    Args:
        city1: (x, y) coordinates
        city2: (x, y) coordinates
    
    Returns:
        Distance between cities
    """
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def calculate_distance_matrix(cities: List[Tuple[float, float]]) -> List[List[float]]:
    """
    Pre-compute distances between all pairs of cities.
    
    Args:
        cities: List of (x, y) coordinates
    
    Returns:
        2D matrix where matrix[i][j] = distance from city i to city j
    """
    n = len(cities)
    distances = [[0.0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i != j:
                distances[i][j] = euclidean_distance(cities[i], cities[j])
    
    return distances


def tour_distance(tour: List[int], distances: List[List[float]]) -> float:
    """
    Calculate total distance of a tour.
    
    Args:
        tour: List of city indices in order
        distances: Distance matrix
    
    Returns:
        Total distance of the tour
    """
    total = 0.0
    n = len(tour)
    
    for i in range(n):
        total += distances[tour[i]][tour[(i + 1) % n]]
    
    return total


def brute_force_tsp(distances: List[List[float]]) -> Tuple[List[int], float]:
    """
    Solve TSP by checking all possible tours (exact solution).
    
    Enumerates all (n-1)!/2 possible tours and returns the shortest.
    Only practical for small n (≤ 10).
    
    Args:
        distances: Distance matrix
    
    Returns:
        (best_tour, best_distance) tuple
    """
    n = len(distances)
    cities = list(range(n))
    
    # Fix first city to reduce symmetry (all tours start from city 0)
    first_city = cities[0]
    remaining_cities = cities[1:]
    
    best_tour = None
    best_distance = float('inf')
    
    # Try all permutations
    for perm in itertools.permutations(remaining_cities):
        tour = [first_city] + list(perm)
        distance = tour_distance(tour, distances)
        
        if distance < best_distance:
            best_distance = distance
            best_tour = tour
    
    return best_tour, best_distance


def held_karp_tsp(distances: List[List[float]]) -> Tuple[List[int], float]:
    """
    Solve TSP using dynamic programming (Held-Karp algorithm).
    
    Uses memoization to avoid recomputing subproblems.
    Time: O(n² × 2ⁿ), Space: O(n × 2ⁿ)
    
    Optimal solution for n ≤ 20.
    
    Args:
        distances: Distance matrix
    
    Returns:
        (best_tour, best_distance) tuple
    """
    n = len(distances)
    
    # memo[subset][last] = (cost, prev) where:
    # - subset: bitmask of visited cities
    # - last: last city in the tour
    # - cost: minimum cost to reach this state
    # - prev: previous city in optimal path
    memo = {}
    
    # Base case: tours of length 1 starting from city 0
    for i in range(1, n):
        memo[(1 << i, i)] = (distances[0][i], 0)
    
    # Build up tours of increasing size
    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset_size):
            # Create bitmask for this subset
            bits = 0
            for bit in subset:
                bits |= 1 << bit
            
            # Try each city as the last in the tour
            for last in subset:
                prev_bits = bits & ~(1 << last)
                best = float('inf')
                best_prev = -1
                
                # Try each possible previous city
                for prev in subset:
                    if prev == last:
                        continue
                    if (prev_bits, prev) in memo:
                        cost = memo[(prev_bits, prev)][0] + distances[prev][last]
                        if cost < best:
                            best = cost
                            best_prev = prev
                
                if best < float('inf'):
                    memo[(bits, last)] = (best, best_prev)
    
    # Find the optimal tour
    all_bits = (1 << n) - 2  # All cities except 0
    best_distance = float('inf')
    best_last = -1
    
    for last in range(1, n):
        if (all_bits, last) in memo:
            cost = memo[(all_bits, last)][0] + distances[last][0]
            if cost < best_distance:
                best_distance = cost
                best_last = last
    
    # Reconstruct the tour
    tour = []
    bits = all_bits
    current = best_last
    
    while current != -1:
        tour.append(current)
        if (bits, current) in memo:
            prev = memo[(bits, current)][1]
            bits &= ~(1 << current)
            current = prev
        else:
            break
    
    tour.reverse()
    tour.insert(0, 0)
    
    return tour, best_distance


def nearest_neighbor_tsp(distances: List[List[float]], 
                         start: int = 0) -> Tuple[List[int], float]:
    """
    Solve TSP using nearest neighbor heuristic (greedy).
    
    Starting from a city, repeatedly visit the nearest unvisited city.
    Fast but not optimal - typically within 25% of optimal.
    
    Time: O(n²)
    
    Args:
        distances: Distance matrix
        start: Starting city (default 0)
    
    Returns:
        (tour, distance) tuple
    """
    n = len(distances)
    unvisited = set(range(n))
    tour = [start]
    unvisited.remove(start)
    
    current = start
    
    while unvisited:
        # Find nearest unvisited city
        nearest = min(unvisited, key=lambda city: distances[current][city])
        tour.append(nearest)
        unvisited.remove(nearest)
        current = nearest
    
    distance = tour_distance(tour, distances)
    return tour, distance


def two_opt_improve(tour: List[int], distances: List[List[float]], 
                    max_iterations: int = 1000) -> Tuple[List[int], float]:
    """
    Improve a tour using 2-opt local search.
    
    Repeatedly try swapping edges to reduce tour length.
    Continues until no improvement found (local optimum).
    
    Time: O(n²) per iteration
    
    Args:
        tour: Initial tour
        distances: Distance matrix
        max_iterations: Maximum iterations to prevent infinite loops
    
    Returns:
        (improved_tour, improved_distance) tuple
    """
    best_tour = tour[:]
    best_distance = tour_distance(best_tour, distances)
    improved = True
    iteration = 0
    
    while improved and iteration < max_iterations:
        improved = False
        iteration += 1
        
        for i in range(1, len(best_tour) - 2):
            for j in range(i + 1, len(best_tour)):
                if j - i == 1:
                    continue  # Adjacent edges, no improvement
                
                # Try reversing the segment [i:j]
                new_tour = best_tour[:]
                new_tour[i:j] = reversed(new_tour[i:j])
                new_distance = tour_distance(new_tour, distances)
                
                if new_distance < best_distance:
                    best_tour = new_tour
                    best_distance = new_distance
                    improved = True
                    break
            
            if improved:
                break
    
    return best_tour, best_distance


def simulated_annealing_tsp(distances: List[List[float]], 
                            initial_temp: float = 1000.0,
                            cooling_rate: float = 0.995,
                            min_temp: float = 1.0) -> Tuple[List[int], float]:
    """
    Solve TSP using simulated annealing metaheuristic.
    
    Inspired by metallurgical annealing - gradually "cool" the system
    to find good solutions. Accepts worse solutions probabilistically
    to escape local optima.
    
    Args:
        distances: Distance matrix
        initial_temp: Starting temperature
        cooling_rate: Temperature reduction factor (0 < rate < 1)
        min_temp: Stopping temperature
    
    Returns:
        (best_tour, best_distance) tuple
    """
    n = len(distances)
    
    # Start with random tour
    current_tour = list(range(n))
    random.shuffle(current_tour[1:])  # Keep first city fixed
    current_distance = tour_distance(current_tour, distances)
    
    best_tour = current_tour[:]
    best_distance = current_distance
    
    temperature = initial_temp
    
    while temperature > min_temp:
        # Generate neighbor by swapping two random cities
        new_tour = current_tour[:]
        i = random.randint(1, n - 1)
        j = random.randint(1, n - 1)
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
        
        new_distance = tour_distance(new_tour, distances)
        
        # Calculate acceptance probability
        delta = new_distance - current_distance
        
        if delta < 0:
            # Better solution - always accept
            current_tour = new_tour
            current_distance = new_distance
            
            if current_distance < best_distance:
                best_tour = current_tour[:]
                best_distance = current_distance
        else:
            # Worse solution - accept with probability exp(-delta/T)
            acceptance_prob = math.exp(-delta / temperature)
            if random.random() < acceptance_prob:
                current_tour = new_tour
                current_distance = new_distance
        
        # Cool down
        temperature *= cooling_rate
    
    return best_tour, best_distance


def generate_random_cities(n: int, max_coord: int = 100) -> List[Tuple[float, float]]:
    """
    Generate random city coordinates.
    
    Args:
        n: Number of cities
        max_coord: Maximum coordinate value
    
    Returns:
        List of (x, y) coordinate tuples
    """
    random.seed(42)  # For reproducibility
    cities = [(random.uniform(0, max_coord), random.uniform(0, max_coord)) 
              for _ in range(n)]
    return cities


def factorial(n: int) -> int:
    """Calculate factorial."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def main():
    """Demonstrate TSP solving with multiple algorithms."""
    
    print("=" * 70)
    print("Traveling Salesman Problem Solver")
    print("=" * 70)
    print("\nSolving one of computer science's most famous NP-hard problems!")
    
    # Generate problem instance
    num_cities = 10
    cities = generate_random_cities(num_cities)
    distances = calculate_distance_matrix(cities)
    
    print(f"\nProblem Size: {num_cities} cities")
    print(f"Possible tours: {factorial(num_cities - 1) // 2:,}")
    print(f"(That's {factorial(num_cities - 1) // 2} different routes to check!)")
    
    # Show sample cities
    print("\nSample Cities (x, y coordinates):")
    for i, city in enumerate(cities[:5]):
        print(f"  City {i}: ({city[0]:.2f}, {city[1]:.2f})")
    if num_cities > 5:
        print(f"  ... and {num_cities - 5} more cities")
    
    results = {}
    
    # Algorithm 1: Brute Force (only for small n)
    if num_cities <= 10:
        print("\n" + "=" * 70)
        print("Algorithm 1: Brute Force (Exact)")
        print("=" * 70)
        print("Checking all possible tours...")
        
        start_time = time.time()
        tour, distance = brute_force_tsp(distances)
        elapsed = time.time() - start_time
        
        print(f"\nTour: {' → '.join(map(str, tour))} → {tour[0]}")
        print(f"Distance: {distance:.2f}")
        print(f"Time: {elapsed:.3f} seconds")
        print("✓ OPTIMAL (guaranteed)")
        
        results['Brute Force'] = (tour, distance, elapsed)
    
    # Algorithm 2: Dynamic Programming (Held-Karp)
    if num_cities <= 15:
        print("\n" + "=" * 70)
        print("Algorithm 2: Dynamic Programming (Held-Karp)")
        print("=" * 70)
        print("Using memoization to avoid recomputing subproblems...")
        
        start_time = time.time()
        tour, distance = held_karp_tsp(distances)
        elapsed = time.time() - start_time
        
        print(f"\nTour: {' → '.join(map(str, tour))} → {tour[0]}")
        print(f"Distance: {distance:.2f}")
        print(f"Time: {elapsed:.3f} seconds")
        print("✓ OPTIMAL (guaranteed)")
        
        results['Dynamic Programming'] = (tour, distance, elapsed)
    
    # Algorithm 3: Nearest Neighbor
    print("\n" + "=" * 70)
    print("Algorithm 3: Nearest Neighbor (Greedy Heuristic)")
    print("=" * 70)
    print("Always choosing the nearest unvisited city...")
    
    start_time = time.time()
    tour, distance = nearest_neighbor_tsp(distances)
    elapsed = time.time() - start_time
    
    print(f"\nTour: {' → '.join(map(str, tour))} → {tour[0]}")
    print(f"Distance: {distance:.2f}")
    print(f"Time: {elapsed:.6f} seconds")
    
    # Compare to optimal if available
    if 'Brute Force' in results:
        optimal = results['Brute Force'][1]
        quality = (optimal / distance) * 100
        print(f"Quality: {quality:.1f}% of optimal")
    else:
        print("✓ Fast approximation")
    
    results['Nearest Neighbor'] = (tour, distance, elapsed)
    
    # Algorithm 4: 2-Opt Improvement
    print("\n" + "=" * 70)
    print("Algorithm 4: 2-Opt Local Search")
    print("=" * 70)
    print("Improving nearest neighbor solution by swapping edges...")
    
    initial_tour, initial_distance = nearest_neighbor_tsp(distances)
    
    start_time = time.time()
    tour, distance = two_opt_improve(initial_tour, distances)
    elapsed = time.time() - start_time
    
    print(f"\nInitial distance: {initial_distance:.2f}")
    print(f"Improved distance: {distance:.2f}")
    print(f"Improvement: {((initial_distance - distance) / initial_distance * 100):.1f}%")
    print(f"Time: {elapsed:.3f} seconds")
    
    if 'Brute Force' in results:
        optimal = results['Brute Force'][1]
        quality = (optimal / distance) * 100
        print(f"Quality: {quality:.1f}% of optimal")
    
    results['2-Opt'] = (tour, distance, elapsed)
    
    # Algorithm 5: Simulated Annealing
    print("\n" + "=" * 70)
    print("Algorithm 5: Simulated Annealing (Metaheuristic)")
    print("=" * 70)
    print("Probabilistically exploring the solution space...")
    
    start_time = time.time()
    tour, distance = simulated_annealing_tsp(distances)
    elapsed = time.time() - start_time
    
    print(f"\nTour: {' → '.join(map(str, tour))} → {tour[0]}")
    print(f"Distance: {distance:.2f}")
    print(f"Time: {elapsed:.3f} seconds")
    
    if 'Brute Force' in results:
        optimal = results['Brute Force'][1]
        quality = (optimal / distance) * 100
        print(f"Quality: {quality:.1f}% of optimal")
    else:
        print("✓ High-quality approximation")
    
    results['Simulated Annealing'] = (tour, distance, elapsed)
    
    # Summary
    print("\n" + "=" * 70)
    print("Performance Summary")
    print("=" * 70)
    
    print(f"\n{'Algorithm':<25} {'Distance':<15} {'Time (s)':<15} {'Quality'}")
    print("-" * 70)
    
    best_distance = min(result[1] for result in results.values())
    
    for name, (tour, distance, elapsed) in results.items():
        quality = (best_distance / distance) * 100
        print(f"{name:<25} {distance:<15.2f} {elapsed:<15.6f} {quality:.1f}%")
    
    # Complexity analysis
    print("\n" + "=" * 70)
    print("Computational Complexity")
    print("=" * 70)
    
    print(f"\nFor {num_cities} cities:")
    print(f"  Brute Force:       O(n!) = O({num_cities}!) = {factorial(num_cities):,} operations")
    print(f"  Dynamic Prog:      O(n²·2ⁿ) = O({num_cities}²·2^{num_cities}) ≈ {num_cities**2 * 2**num_cities:,} operations")
    print(f"  Nearest Neighbor:  O(n²) = O({num_cities}²) = {num_cities**2:,} operations")
    print(f"  2-Opt:             O(n²) per iteration")
    print(f"  Sim. Annealing:    O(n²) per iteration")
    
    # Real-world impact
    print("\n" + "=" * 70)
    print("Why This Matters")
    print("=" * 70)
    
    print("\nTSP optimization saves billions annually:")
    print("  ✓ UPS saves millions of gallons of fuel")
    print("  ✓ Circuit board manufacturing: faster production")
    print("  ✓ DNA sequencing: faster genome assembly")
    print("  ✓ Delivery services: reduced costs and emissions")
    
    print("\n" + "=" * 70)
    print("The P vs NP Question")
    print("=" * 70)
    
    print("\nTSP is NP-hard. If you find a polynomial-time algorithm,")
    print("you'll solve one of the Millennium Prize Problems and win")
    print("$1,000,000 from the Clay Mathematics Institute!")
    
    print("\nUntil then, we use these clever approximations and")
    print("heuristics to find good-enough solutions quickly.")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()
