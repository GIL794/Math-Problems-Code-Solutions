"""
Perfect Numbers Finder

Finds perfect numbers and analyzes their properties. A perfect number is a
positive integer that is equal to the sum of its proper positive divisors
(excluding the number itself).

Example: 6 = 1 + 2 + 3 (divisors: 1, 2, 3)
"""

def get_divisors(n):
    """
    Get all divisors of a number.
    
    Args:
        n: Positive integer
    
    Returns:
        List of divisors
    """
    if n < 1:
        return []
    
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i and i != n:
                divisors.append(n // i)
    
    return sorted(divisors)


def get_proper_divisors(n):
    """
    Get proper divisors of a number (excluding the number itself).
    
    Args:
        n: Positive integer
    
    Returns:
        List of proper divisors
    """
    divisors = get_divisors(n)
    return [d for d in divisors if d != n]


def is_perfect(n):
    """
    Check if a number is perfect.
    
    Args:
        n: Positive integer
    
    Returns:
        True if n is perfect, False otherwise
    """
    if n < 2:
        return False
    
    proper_divisors = get_proper_divisors(n)
    return sum(proper_divisors) == n


def classify_number(n):
    """
    Classify a number as perfect, abundant, or deficient.
    
    - Perfect: sum of proper divisors = n
    - Abundant: sum of proper divisors > n
    - Deficient: sum of proper divisors < n
    
    Args:
        n: Positive integer
    
    Returns:
        String classification
    """
    if n < 2:
        return "Invalid"
    
    proper_divisors = get_proper_divisors(n)
    divisor_sum = sum(proper_divisors)
    
    if divisor_sum == n:
        return "Perfect"
    elif divisor_sum > n:
        return "Abundant"
    else:
        return "Deficient"


def find_perfect_numbers(limit):
    """
    Find all perfect numbers up to a given limit.
    
    Args:
        limit: Upper bound for search
    
    Returns:
        List of perfect numbers
    """
    perfect_numbers = []
    
    for n in range(2, limit + 1):
        if is_perfect(n):
            perfect_numbers.append(n)
    
    return perfect_numbers


def find_perfect_numbers_euclid(limit):
    """
    Find perfect numbers using Euclid's formula.
    Euclid proved that if 2^p - 1 is prime (Mersenne prime),
    then (2^p - 1) * 2^(p-1) is a perfect number.
    
    Args:
        limit: Upper bound for search
    
    Returns:
        List of perfect numbers found using this method
    """
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    perfect_numbers = []
    p = 2
    
    while True:
        mersenne = (2 ** p) - 1
        if mersenne > limit:
            break
        
        if is_prime(mersenne):
            perfect = mersenne * (2 ** (p - 1))
            if perfect <= limit:
                perfect_numbers.append(perfect)
            else:
                break
        
        p += 1
    
    return perfect_numbers


def analyze_number(n):
    """Analyze a number and display its properties."""
    divisors = get_divisors(n)
    proper_divisors = get_proper_divisors(n)
    divisor_sum = sum(proper_divisors)
    classification = classify_number(n)
    
    print(f"\n{'=' * 60}")
    print(f"Analysis of {n}")
    print(f"{'=' * 60}")
    print(f"All divisors: {divisors}")
    print(f"Proper divisors: {proper_divisors}")
    print(f"Sum of proper divisors: {divisor_sum}")
    print(f"Classification: {classification}")
    
    if is_perfect(n):
        print(f"✓ {n} is a PERFECT NUMBER!")
        print(f"  {n} = {' + '.join(map(str, proper_divisors))}")


def print_perfect_numbers(perfect_numbers, method=""):
    """Print perfect numbers in a formatted way."""
    print(f"\n{'=' * 60}")
    if method:
        print(f"Perfect Numbers Found ({method})")
    else:
        print("Perfect Numbers Found")
    print(f"{'=' * 60}")
    
    if not perfect_numbers:
        print("No perfect numbers found in the given range.")
        return
    
    print(f"Total count: {len(perfect_numbers)}\n")
    
    for num in perfect_numbers:
        proper_divisors = get_proper_divisors(num)
        print(f"{num}:")
        print(f"  Divisors: {proper_divisors}")
        print(f"  Verification: {' + '.join(map(str, proper_divisors))} = {sum(proper_divisors)} = {num}")
        print()


def main():
    print("=" * 60)
    print("Perfect Numbers Finder")
    print("=" * 60)
    
    # Find perfect numbers using brute force
    print("\nSearching for perfect numbers up to 10,000...")
    perfect_numbers = find_perfect_numbers(10000)
    print_perfect_numbers(perfect_numbers, "Brute Force Method")
    
    # Find perfect numbers using Euclid's formula
    print("\nSearching using Euclid's formula (up to 10,000)...")
    perfect_euclid = find_perfect_numbers_euclid(10000)
    print_perfect_numbers(perfect_euclid, "Euclid's Formula")
    
    # Analyze known perfect numbers
    print(f"\n{'=' * 60}")
    print("Detailed Analysis of Known Perfect Numbers")
    print(f"{'=' * 60}")
    
    known_perfect = [6, 28, 496, 8128]
    
    for num in known_perfect:
        analyze_number(num)
    
    # Classify a range of numbers
    print(f"\n{'=' * 60}")
    print("Number Classification (Perfect, Abundant, or Deficient)")
    print(f"{'=' * 60}")
    
    test_numbers = [6, 12, 16, 28, 100, 496]
    
    for num in test_numbers:
        classification = classify_number(num)
        proper_divisors = get_proper_divisors(num)
        divisor_sum = sum(proper_divisors)
        print(f"{num:>6}: {classification:>10} (sum of proper divisors = {divisor_sum})")
    
    # Find all perfect numbers up to a larger limit using Euclid's method
    print(f"\n{'=' * 60}")
    print("Perfect Numbers up to 100,000,000 (using Euclid's formula)")
    print(f"{'=' * 60}")
    
    large_perfect = find_perfect_numbers_euclid(100000000)
    if large_perfect:
        print(f"\nFound {len(large_perfect)} perfect numbers:")
        for num in large_perfect:
            print(f"  {num:,}")
    else:
        print("\nNo additional perfect numbers found in this range.")
    
    print(f"\n{'=' * 60}")
    print("Mathematical Note:")
    print("All known perfect numbers are even. It is unknown whether")
    print("any odd perfect numbers exist. As of 2023, 51 perfect numbers")
    print("have been discovered, all using Mersenne primes.")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()

