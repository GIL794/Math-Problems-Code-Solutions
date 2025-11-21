"""
Prime Number Sieve

Implements the Sieve of Eratosthenes algorithm to find all prime numbers
up to a given limit. Also includes methods to check if a number is prime
and to find prime factors of a number.
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


def prime_factors(n):
    """
    Find all prime factors of a number.
    
    Args:
        n: Number to factorize
    
    Returns:
        List of prime factors (with repetition)
    """
    if n < 2:
        return []
    
    factors = []
    d = 2
    
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    
    if n > 1:
        factors.append(n)
    
    return factors


def prime_factors_unique(n):
    """
    Find unique prime factors of a number.
    
    Args:
        n: Number to factorize
    
    Returns:
        Set of unique prime factors
    """
    return set(prime_factors(n))


def count_primes_up_to(limit):
    """
    Count the number of primes up to a given limit.
    
    Args:
        limit: Upper bound
    
    Returns:
        Number of primes
    """
    primes = sieve_of_eratosthenes(limit)
    return len(primes)


def print_primes(primes, limit, max_display=50):
    """Print primes in a formatted way."""
    print(f"\n{'=' * 60}")
    print(f"Prime Numbers up to {limit}")
    print(f"{'=' * 60}")
    print(f"Total count: {len(primes)}")
    
    if len(primes) <= max_display:
        print(f"\nAll primes:")
        # Print in columns for better readability
        cols = 10
        for i in range(0, len(primes), cols):
            row = primes[i:i + cols]
            print("  ".join(f"{p:>6}" for p in row))
    else:
        print(f"\nFirst {max_display} primes:")
        cols = 10
        for i in range(0, min(max_display, len(primes)), cols):
            row = primes[i:i + cols]
            print("  ".join(f"{p:>6}" for p in row))
        print(f"\n... and {len(primes) - max_display} more")


def analyze_prime_distribution(primes):
    """Analyze the distribution of primes."""
    if len(primes) < 2:
        return
    
    print(f"\n{'=' * 60}")
    print("Prime Distribution Analysis")
    print(f"{'=' * 60}")
    
    # Find twin primes (primes that differ by 2)
    twin_primes = []
    for i in range(len(primes) - 1):
        if primes[i + 1] - primes[i] == 2:
            twin_primes.append((primes[i], primes[i + 1]))
    
    if twin_primes:
        print(f"\nTwin primes found: {len(twin_primes)}")
        if len(twin_primes) <= 10:
            for p1, p2 in twin_primes:
                print(f"  ({p1}, {p2})")
        else:
            print("  First 5:")
            for p1, p2 in twin_primes[:5]:
                print(f"  ({p1}, {p2})")
            print(f"  ... and {len(twin_primes) - 5} more")
    
    # Find largest gap between consecutive primes
    if len(primes) > 1:
        gaps = [primes[i + 1] - primes[i] for i in range(len(primes) - 1)]
        max_gap = max(gaps)
        max_gap_index = gaps.index(max_gap)
        print(f"\nLargest gap between consecutive primes: {max_gap}")
        print(f"  Between {primes[max_gap_index]} and {primes[max_gap_index + 1]}")


def main():
    print("=" * 60)
    print("Prime Number Sieve - Sieve of Eratosthenes")
    print("=" * 60)
    
    # Find primes up to different limits
    limits = [100, 1000]
    
    for limit in limits:
        print(f"\nFinding primes up to {limit}...")
        primes = sieve_of_eratosthenes(limit)
        print_primes(primes, limit)
        analyze_prime_distribution(primes)
    
    # Test prime factorization
    print(f"\n{'=' * 60}")
    print("Prime Factorization Examples")
    print(f"{'=' * 60}")
    
    test_numbers = [12, 100, 1234, 10000, 97]
    
    for num in test_numbers:
        factors = prime_factors(num)
        unique_factors = prime_factors_unique(num)
        print(f"\n{num} = {' × '.join(map(str, factors))}")
        print(f"  Unique prime factors: {sorted(unique_factors)}")
    
    # Check individual numbers
    print(f"\n{'=' * 60}")
    print("Prime Number Checks")
    print(f"{'=' * 60}")
    
    check_numbers = [17, 25, 97, 100, 101, 997]
    
    for num in check_numbers:
        result = is_prime(num)
        status = "✓ Prime" if result else "✗ Not Prime"
        print(f"{num:>6}: {status}")
    
    print(f"\n{'=' * 60}")


if __name__ == "__main__":
    main()

