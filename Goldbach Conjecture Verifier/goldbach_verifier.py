"""
Goldbach Conjecture Verifier

The Goldbach Conjecture states that every even integer greater than 2 can be
expressed as the sum of two prime numbers. This remains one of the oldest
unsolved problems in number theory (proposed in 1742).

This program verifies the conjecture for a range of even numbers and finds
all possible prime pair representations for each number.
"""

def sieve_of_eratosthenes(limit):
    """
    Find all prime numbers up to a given limit using the Sieve of Eratosthenes.
    
    Args:
        limit: Upper bound for finding primes
    
    Returns:
        List of prime numbers up to limit
    """
    if limit < 2:
        return []
    
    # Create a boolean array where True means the number is prime
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False
    
    # Sieve of Eratosthenes algorithm
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            # Mark all multiples of i as not prime
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    
    # Collect all primes
    primes = [i for i in range(2, limit + 1) if is_prime[i]]
    return primes


def is_prime(n):
    """
    Check if a number is prime using trial division.
    
    Args:
        n: Number to check
    
    Returns:
        True if n is prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check divisibility up to sqrt(n)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True


def find_goldbach_pairs(n, primes_set=None):
    """
    Find all pairs of primes that sum to n (Goldbach representations).
    
    Args:
        n: Even number to find prime pairs for
        primes_set: Set of primes up to n (computed if not provided)
    
    Returns:
        List of tuples (p1, p2) where p1 + p2 = n and p1 <= p2
    """
    if n <= 2 or n % 2 != 0:
        return []
    
    # Generate primes if not provided
    if primes_set is None:
        primes = sieve_of_eratosthenes(n)
        primes_set = set(primes)
    
    pairs = []
    
    # Find all pairs where p1 + p2 = n
    # We only need to check up to n/2 to avoid duplicates
    # Sort the set to iterate in order
    for p1 in sorted(primes_set):
        if p1 > n // 2:
            break
        p2 = n - p1
        if p2 in primes_set:
            pairs.append((p1, p2))
    
    return pairs


def verify_goldbach_range(start, end):
    """
    Verify Goldbach's conjecture for all even numbers in a range.
    
    Args:
        start: Starting even number
        end: Ending even number
    
    Returns:
        Dictionary mapping each even number to its Goldbach pairs
    """
    # Ensure start is even and >= 4
    if start < 4:
        start = 4
    if start % 2 != 0:
        start += 1
    
    # Ensure end is even
    if end % 2 != 0:
        end -= 1
    
    # Generate all primes up to end once
    primes = sieve_of_eratosthenes(end)
    primes_set = set(primes)
    
    results = {}
    
    for n in range(start, end + 1, 2):
        pairs = find_goldbach_pairs(n, primes_set)
        results[n] = pairs
    
    return results


def analyze_goldbach_representations(results):
    """
    Analyze patterns in Goldbach representations.
    
    Args:
        results: Dictionary from verify_goldbach_range
    
    Returns:
        Dictionary with analysis statistics
    """
    analysis = {
        'total_numbers': len(results),
        'verified': 0,
        'failed': [],
        'max_representations': 0,
        'min_representations': float('inf'),
        'numbers_with_max': [],
        'numbers_with_min': [],
        'avg_representations': 0
    }
    
    total_reps = 0
    
    for n, pairs in results.items():
        num_pairs = len(pairs)
        
        if num_pairs > 0:
            analysis['verified'] += 1
        else:
            analysis['failed'].append(n)
        
        total_reps += num_pairs
        
        if num_pairs > analysis['max_representations']:
            analysis['max_representations'] = num_pairs
            analysis['numbers_with_max'] = [n]
        elif num_pairs == analysis['max_representations']:
            analysis['numbers_with_max'].append(n)
        
        if num_pairs < analysis['min_representations']:
            analysis['min_representations'] = num_pairs
            analysis['numbers_with_min'] = [n]
        elif num_pairs == analysis['min_representations']:
            analysis['numbers_with_min'].append(n)
    
    if analysis['total_numbers'] > 0:
        analysis['avg_representations'] = total_reps / analysis['total_numbers']
    
    return analysis


def print_goldbach_results(results, show_all=False, max_display=20):
    """Print Goldbach verification results in a formatted way."""
    print(f"\n{'=' * 70}")
    print("Goldbach Conjecture Verification Results")
    print(f"{'=' * 70}")
    print(f"Range: {min(results.keys())} to {max(results.keys())}")
    print(f"Total even numbers verified: {len(results)}")
    
    # Count how many were successfully verified
    verified = sum(1 for pairs in results.values() if len(pairs) > 0)
    print(f"Successfully verified: {verified}/{len(results)}")
    
    if verified < len(results):
        failed = [n for n, pairs in results.items() if len(pairs) == 0]
        print(f"\n⚠️  Failed to verify: {failed}")
    else:
        print("\n✓ All numbers verified!")
    
    print(f"\n{'=' * 70}")
    print("Sample Goldbach Representations")
    print(f"{'=' * 70}")
    
    display_count = 0
    for n, pairs in sorted(results.items()):
        if not show_all and display_count >= max_display:
            remaining = len(results) - display_count
            print(f"\n... and {remaining} more even numbers")
            break
        
        print(f"\n{n} = ", end="")
        if len(pairs) == 0:
            print("NO REPRESENTATION FOUND!")
        elif len(pairs) == 1:
            p1, p2 = pairs[0]
            print(f"{p1} + {p2}")
        else:
            # Show first pair on same line
            p1, p2 = pairs[0]
            print(f"{p1} + {p2}")
            # Show remaining pairs indented
            for p1, p2 in pairs[1:]:
                print(f"{' ' * (len(str(n)) + 4)}{p1} + {p2}")
        
        display_count += 1
    
    print(f"\n{'=' * 70}")


def print_goldbach_analysis(analysis):
    """Print analysis of Goldbach representations."""
    print(f"\n{'=' * 70}")
    print("Goldbach Representations Analysis")
    print(f"{'=' * 70}")
    
    print(f"\nTotal even numbers analyzed: {analysis['total_numbers']}")
    print(f"Successfully verified: {analysis['verified']}")
    
    if analysis['failed']:
        print(f"Failed to verify: {len(analysis['failed'])}")
        print(f"  Numbers: {analysis['failed']}")
    else:
        print("✓ All numbers have at least one representation!")
    
    print(f"\nRepresentation Statistics:")
    print(f"  Average representations per number: {analysis['avg_representations']:.2f}")
    print(f"  Maximum representations: {analysis['max_representations']}")
    print(f"  Minimum representations: {analysis['min_representations']}")
    
    if analysis['numbers_with_max']:
        print(f"\n  Numbers with most representations ({analysis['max_representations']}):")
        for n in analysis['numbers_with_max'][:5]:
            print(f"    {n}")
        if len(analysis['numbers_with_max']) > 5:
            print(f"    ... and {len(analysis['numbers_with_max']) - 5} more")
    
    print(f"\n{'=' * 70}")


def find_weak_goldbach_partitions(n):
    """
    Find all ways to express an odd number as sum of three primes (Weak Goldbach).
    The weak Goldbach conjecture (now proven) states that every odd number > 5
    can be expressed as the sum of three odd primes.
    
    Args:
        n: Odd number to find prime triple for
    
    Returns:
        List of tuples (p1, p2, p3) where p1 + p2 + p3 = n
    """
    if n <= 5 or n % 2 == 0:
        return []
    
    primes = sieve_of_eratosthenes(n)
    primes_set = set(primes)
    triplets = []
    
    # Find all triplets where p1 + p2 + p3 = n
    for i, p1 in enumerate(primes):
        if p1 > n // 3:
            break
        for j in range(i, len(primes)):
            p2 = primes[j]
            if p1 + p2 > n - 2:
                break
            p3 = n - p1 - p2
            if p3 >= p2 and p3 in primes_set:
                triplets.append((p1, p2, p3))
    
    return triplets


def main():
    print("=" * 70)
    print("GOLDBACH CONJECTURE VERIFIER")
    print("=" * 70)
    print("\nThe Goldbach Conjecture (1742):")
    print("Every even integer greater than 2 can be expressed as the")
    print("sum of two prime numbers.")
    print("\nStatus: UNPROVEN (but verified for numbers up to 4 × 10¹⁸)")
    print("=" * 70)
    
    # Verify small range with detailed output
    print("\n" + "=" * 70)
    print("Verification for small even numbers (4 to 50)")
    print("=" * 70)
    
    results_small = verify_goldbach_range(4, 50)
    print_goldbach_results(results_small, show_all=True)
    
    analysis_small = analyze_goldbach_representations(results_small)
    print_goldbach_analysis(analysis_small)
    
    # Verify larger range with summary
    print("\n" + "=" * 70)
    print("Verification for larger range (4 to 200)")
    print("=" * 70)
    
    results_large = verify_goldbach_range(4, 200)
    print_goldbach_results(results_large, show_all=False, max_display=15)
    
    analysis_large = analyze_goldbach_representations(results_large)
    print_goldbach_analysis(analysis_large)
    
    # Show interesting specific cases
    print("\n" + "=" * 70)
    print("Interesting Observations")
    print("=" * 70)
    
    # Find numbers with many representations
    many_reps = [(n, len(pairs)) for n, pairs in results_large.items() if len(pairs) >= 10]
    many_reps.sort(key=lambda x: x[1], reverse=True)
    
    print("\nEven numbers with 10+ representations:")
    for n, count in many_reps[:10]:
        print(f"  {n}: {count} representations")
    
    # Demonstrate weak Goldbach (bonus)
    print("\n" + "=" * 70)
    print("BONUS: Weak Goldbach Conjecture (Proven in 2013)")
    print("=" * 70)
    print("Every odd number > 5 can be expressed as sum of three odd primes")
    
    odd_numbers = [7, 9, 15, 21, 27, 33]
    for n in odd_numbers:
        triplets = find_weak_goldbach_partitions(n)
        print(f"\n{n} has {len(triplets)} representation(s):")
        for i, (p1, p2, p3) in enumerate(triplets[:3]):
            print(f"  {p1} + {p2} + {p3}")
        if len(triplets) > 3:
            print(f"  ... and {len(triplets) - 3} more")
    
    print("\n" + "=" * 70)
    print("Mathematical Significance:")
    print("- Goldbach's conjecture is one of the oldest unsolved problems")
    print("- It has been verified computationally to extremely large numbers")
    print("- Related to the distribution of prime numbers")
    print("- Connects to cryptography and number theory")
    print("=" * 70)


if __name__ == "__main__":
    main()
