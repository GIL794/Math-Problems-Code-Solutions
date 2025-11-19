"""
Goldbach Conjecture Verifier

Verifies Goldbach's Conjecture: Every even integer greater than 2 can be
expressed as the sum of two prime numbers.

This famous unsolved problem was proposed by Christian Goldbach in 1742.
While it has been verified for extremely large numbers, it remains unproven
in the general case.
"""

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
    is_prime_array = [True] * (limit + 1)
    is_prime_array[0] = False
    is_prime_array[1] = False
    
    # Sieve of Eratosthenes algorithm
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime_array[i]:
            # Mark all multiples of i as not prime
            for j in range(i * i, limit + 1, i):
                is_prime_array[j] = False
    
    # Collect all primes
    primes = [i for i in range(2, limit + 1) if is_prime_array[i]]
    return primes


def find_goldbach_pairs(n):
    """
    Find all pairs of primes that sum to n (Goldbach pairs).
    
    Args:
        n: Even integer greater than 2
    
    Returns:
        List of tuples (p, q) where p and q are primes and p + q = n
    """
    if n <= 2 or n % 2 != 0:
        return []
    
    pairs = []
    
    # We only need to check up to n/2 to avoid duplicates
    for p in range(2, n // 2 + 1):
        if is_prime(p):
            q = n - p
            if is_prime(q):
                pairs.append((p, q))
    
    return pairs


def verify_goldbach(n):
    """
    Verify that a specific even number can be expressed as sum of two primes.
    
    Args:
        n: Even integer greater than 2
    
    Returns:
        Tuple (success, pairs) where success is True if verification passed
    """
    if n <= 2:
        return False, []
    
    if n % 2 != 0:
        return False, []
    
    pairs = find_goldbach_pairs(n)
    return len(pairs) > 0, pairs


def verify_goldbach_range(start, end):
    """
    Verify Goldbach's conjecture for a range of even numbers.
    
    Args:
        start: Starting even number
        end: Ending even number (inclusive)
    
    Returns:
        Dictionary with results for each number
    """
    results = {}
    
    # Ensure start is even
    if start % 2 != 0:
        start += 1
    
    # Ensure start is at least 4
    start = max(start, 4)
    
    for n in range(start, end + 1, 2):
        success, pairs = verify_goldbach(n)
        results[n] = {
            'verified': success,
            'pair_count': len(pairs),
            'first_pair': pairs[0] if pairs else None
        }
    
    return results


def count_representations(n, max_n=None):
    """
    Count how many ways an even number can be represented as sum of two primes.
    
    Args:
        n: Even integer to analyze
        max_n: Optional maximum to analyze a range
    
    Returns:
        Dictionary or single count
    """
    if max_n is None:
        pairs = find_goldbach_pairs(n)
        return len(pairs)
    else:
        counts = {}
        for num in range(4, max_n + 1, 2):
            pairs = find_goldbach_pairs(num)
            counts[num] = len(pairs)
        return counts


def print_goldbach_verification(n, pairs):
    """Print Goldbach verification results in a formatted way."""
    print(f"\n{'=' * 60}")
    print(f"Goldbach Verification for {n}")
    print(f"{'=' * 60}")
    
    if not pairs:
        print(f"✗ Could not verify: {n} cannot be expressed as sum of two primes")
        print("   (This would disprove Goldbach's Conjecture!)")
    else:
        print(f"✓ Verified: {n} can be expressed as sum of two primes")
        print(f"   Number of representations: {len(pairs)}")
        print(f"\n   Goldbach pairs:")
        
        # Show up to 10 pairs
        display_pairs = pairs[:10]
        for p, q in display_pairs:
            print(f"      {p:>6} + {q:<6} = {n}")
        
        if len(pairs) > 10:
            print(f"      ... and {len(pairs) - 10} more pairs")


def analyze_goldbach_pattern(start, end):
    """Analyze patterns in Goldbach representations."""
    print(f"\n{'=' * 60}")
    print(f"Goldbach Pattern Analysis ({start} to {end})")
    print(f"{'=' * 60}")
    
    results = verify_goldbach_range(start, end)
    
    all_verified = all(r['verified'] for r in results.values())
    
    if all_verified:
        print(f"\n✓ All {len(results)} even numbers verified!")
        
        # Find number with most representations
        max_reps = max(r['pair_count'] for r in results.values())
        max_nums = [n for n, r in results.items() if r['pair_count'] == max_reps]
        
        print(f"\n   Most representations: {max_reps}")
        print(f"   Number(s) with most representations: {max_nums}")
        
        # Find number with fewest representations
        min_reps = min(r['pair_count'] for r in results.values())
        min_nums = [n for n, r in results.items() if r['pair_count'] == min_reps]
        
        print(f"\n   Fewest representations: {min_reps}")
        print(f"   Number(s) with fewest representations: {min_nums}")
        
        # Show some examples
        print(f"\n   Sample representations:")
        sample_nums = list(results.keys())[:5]
        for n in sample_nums:
            r = results[n]
            if r['first_pair']:
                p, q = r['first_pair']
                print(f"      {n} = {p} + {q}  ({r['pair_count']} total pairs)")
    else:
        print("\n✗ CONJECTURE DISPROVED!")
        failed = [n for n, r in results.items() if not r['verified']]
        print(f"   Failed for: {failed}")


def main():
    print("=" * 60)
    print("Goldbach Conjecture Verifier")
    print("=" * 60)
    print("\nGoldbach's Conjecture (1742):")
    print("Every even integer greater than 2 can be expressed as")
    print("the sum of two prime numbers.")
    print("\nStatus: UNPROVEN (but verified for numbers up to 4 × 10^18)")
    
    # Test specific even numbers
    test_numbers = [4, 6, 10, 28, 100, 200, 1000]
    
    for n in test_numbers:
        success, pairs = verify_goldbach(n)
        print_goldbach_verification(n, pairs)
    
    # Analyze patterns in different ranges
    ranges = [(4, 50), (100, 150)]
    
    for start, end in ranges:
        analyze_goldbach_pattern(start, end)
    
    # Show interesting facts
    print(f"\n{'=' * 60}")
    print("Interesting Facts")
    print(f"{'=' * 60}")
    
    print("\n• 4 = 2 + 2 is the smallest even number in the conjecture")
    print("• As numbers grow larger, they typically have MORE Goldbach pairs")
    print("• The conjecture has been verified by computer for extremely large numbers")
    print("• Despite extensive verification, no mathematical proof exists")
    print("• A related 'weak' Goldbach conjecture (for odd numbers) was proven in 2013")
    
    print(f"\n{'=' * 60}")


if __name__ == "__main__":
    main()
