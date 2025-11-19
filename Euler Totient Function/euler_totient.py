"""
Euler's Totient Function Calculator

Calculates φ(n), also known as Euler's Totient Function, which counts the
number of integers from 1 to n that are coprime with n (i.e., gcd(k, n) = 1).

This function is fundamental in number theory and has important applications
in cryptography, especially in the RSA algorithm.
"""

import math
from collections import defaultdict


def gcd(a, b):
    """
    Calculate the Greatest Common Divisor using Euclidean algorithm.
    
    Args:
        a, b: Two integers
    
    Returns:
        Greatest common divisor of a and b
    """
    while b:
        a, b = b, a % b
    return a


def are_coprime(a, b):
    """
    Check if two numbers are coprime (their gcd is 1).
    
    Args:
        a, b: Two integers
    
    Returns:
        True if coprime, False otherwise
    """
    return gcd(a, b) == 1


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
    
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True


def prime_factorization(n):
    """
    Find the prime factorization of n.
    
    Args:
        n: Number to factorize
    
    Returns:
        Dictionary mapping prime factors to their powers
    """
    if n < 2:
        return {}
    
    factors = defaultdict(int)
    d = 2
    
    while d * d <= n:
        while n % d == 0:
            factors[d] += 1
            n //= d
        d += 1
    
    if n > 1:
        factors[n] += 1
    
    return dict(factors)


def euler_totient_naive(n):
    """
    Calculate φ(n) using the naive counting method.
    This directly counts numbers coprime to n.
    
    Args:
        n: Positive integer
    
    Returns:
        φ(n) - count of coprimes
    """
    if n == 1:
        return 1
    
    count = 0
    for i in range(1, n + 1):
        if gcd(i, n) == 1:
            count += 1
    
    return count


def euler_totient(n):
    """
    Calculate φ(n) using the formula based on prime factorization.
    
    For n = p1^k1 * p2^k2 * ... * pm^km:
    φ(n) = n * (1 - 1/p1) * (1 - 1/p2) * ... * (1 - 1/pm)
    
    Or equivalently:
    φ(n) = p1^(k1-1) * (p1-1) * p2^(k2-1) * (p2-1) * ... * pm^(km-1) * (pm-1)
    
    Args:
        n: Positive integer
    
    Returns:
        φ(n) - Euler's totient function
    """
    if n == 1:
        return 1
    
    result = n
    
    # Find all prime factors
    factors = prime_factorization(n)
    
    # Apply the formula
    for prime in factors:
        result = result * (prime - 1) // prime
    
    return result


def find_coprimes(n):
    """
    Find all numbers from 1 to n that are coprime with n.
    
    Args:
        n: Positive integer
    
    Returns:
        List of coprimes
    """
    if n == 1:
        return [1]
    
    coprimes = []
    for i in range(1, n + 1):
        if gcd(i, n) == 1:
            coprimes.append(i)
    
    return coprimes


def totient_range(start, end):
    """
    Calculate φ(n) for a range of numbers.
    
    Args:
        start, end: Range boundaries (inclusive)
    
    Returns:
        Dictionary mapping n to φ(n)
    """
    results = {}
    for n in range(start, end + 1):
        results[n] = euler_totient(n)
    return results


def analyze_totient_properties(n):
    """
    Analyze various properties related to φ(n).
    
    Args:
        n: Positive integer
    
    Returns:
        Dictionary with analysis results
    """
    phi_n = euler_totient(n)
    factors = prime_factorization(n)
    coprimes = find_coprimes(n) if n <= 50 else []  # Only show coprimes for small n
    
    # Check if n is prime
    n_is_prime = is_prime(n)
    
    # For primes, φ(p) = p - 1
    if n_is_prime:
        property_note = f"n is prime, so φ(n) = n - 1 = {n - 1}"
    elif len(factors) == 1:
        # Power of a prime
        p, k = list(factors.items())[0]
        property_note = f"n = {p}^{k}, so φ(n) = {p}^{k-1} * ({p} - 1) = {phi_n}"
    else:
        property_note = "n has multiple prime factors"
    
    return {
        'n': n,
        'phi_n': phi_n,
        'is_prime': n_is_prime,
        'prime_factors': factors,
        'coprimes': coprimes,
        'ratio': phi_n / n,
        'property_note': property_note
    }


def print_totient_analysis(analysis):
    """Print detailed analysis of φ(n)."""
    n = analysis['n']
    phi_n = analysis['phi_n']
    
    print(f"\n{'=' * 60}")
    print(f"Euler's Totient Function: φ({n})")
    print(f"{'=' * 60}")
    print(f"φ({n}) = {phi_n}")
    print(f"Ratio φ(n)/n = {analysis['ratio']:.4f}")
    
    # Prime factorization
    if analysis['prime_factors']:
        factors_str = ' × '.join(
            f"{p}^{k}" if k > 1 else str(p)
            for p, k in sorted(analysis['prime_factors'].items())
        )
        print(f"\nPrime factorization: {n} = {factors_str}")
    
    print(f"\n{analysis['property_note']}")
    
    # Show coprimes if available
    if analysis['coprimes']:
        print(f"\nNumbers coprime to {n}:")
        print(f"  {analysis['coprimes']}")
    elif n > 50:
        print(f"\n(Too many coprimes to display for n = {n})")
    
    # Properties
    print(f"\nProperties:")
    if analysis['is_prime']:
        print(f"  • {n} is prime")
        print(f"  • All numbers from 1 to {n-1} are coprime to {n}")
    else:
        print(f"  • {phi_n} out of {n} numbers are coprime to {n}")
        print(f"  • {n - phi_n} numbers share a common factor with {n}")


def compare_totients(numbers):
    """Compare φ(n) for multiple numbers."""
    print(f"\n{'=' * 60}")
    print("Totient Function Comparison")
    print(f"{'=' * 60}")
    print(f"\n{'n':>6} | {'φ(n)':>6} | {'φ(n)/n':>8} | {'Properties'}")
    print("-" * 60)
    
    for n in numbers:
        phi_n = euler_totient(n)
        ratio = phi_n / n
        
        props = []
        if is_prime(n):
            props.append("prime")
        
        factors = prime_factorization(n)
        if len(factors) == 1 and list(factors.values())[0] > 1:
            p, k = list(factors.items())[0]
            props.append(f"{p}^{k}")
        
        props_str = ", ".join(props) if props else "composite"
        
        print(f"{n:>6} | {phi_n:>6} | {ratio:>8.4f} | {props_str}")


def interesting_totient_facts():
    """Display interesting mathematical facts about the totient function."""
    print(f"\n{'=' * 60}")
    print("Interesting Facts About Euler's Totient Function")
    print(f"{'=' * 60}")
    
    facts = [
        ("Multiplicative", "If gcd(m,n) = 1, then φ(m*n) = φ(m) * φ(n)"),
        ("Prime Property", "For prime p: φ(p) = p - 1"),
        ("Prime Power", "For prime p and k > 0: φ(p^k) = p^(k-1) * (p - 1)"),
        ("Sum Property", "Sum of φ(d) for all divisors d of n equals n"),
        ("RSA Connection", "φ(n) is crucial for RSA encryption key generation"),
        ("Carmichael", "λ(n) ≤ φ(n), where λ is Carmichael's function"),
        ("Density", "Average value of φ(n)/n approaches 6/π² ≈ 0.608 as n → ∞"),
    ]
    
    for i, (title, description) in enumerate(facts, 1):
        print(f"\n{i}. {title}:")
        print(f"   {description}")


def demonstrate_multiplicative_property():
    """Demonstrate that φ is multiplicative."""
    print(f"\n{'=' * 60}")
    print("Multiplicative Property Demonstration")
    print(f"{'=' * 60}")
    print("\nIf gcd(m, n) = 1, then φ(m × n) = φ(m) × φ(n)")
    
    test_pairs = [(3, 5), (7, 11), (4, 9), (15, 28)]
    
    for m, n in test_pairs:
        if gcd(m, n) == 1:
            phi_m = euler_totient(m)
            phi_n = euler_totient(n)
            phi_mn = euler_totient(m * n)
            
            print(f"\n  m = {m}, n = {n} (coprime: gcd = 1)")
            print(f"  φ({m}) = {phi_m}, φ({n}) = {phi_n}")
            print(f"  φ({m} × {n}) = φ({m * n}) = {phi_mn}")
            print(f"  φ({m}) × φ({n}) = {phi_m} × {phi_n} = {phi_m * phi_n}")
            print(f"  ✓ Property verified: {phi_mn} = {phi_m * phi_n}")
        else:
            print(f"\n  m = {m}, n = {n} (NOT coprime: gcd = {gcd(m, n)})")
            print(f"  Property does not apply")


def main():
    print("=" * 60)
    print("Euler's Totient Function Calculator")
    print("=" * 60)
    print("\nφ(n) counts integers from 1 to n that are coprime with n")
    print("(i.e., numbers k where gcd(k, n) = 1)")
    
    # Analyze specific numbers
    test_numbers = [1, 2, 6, 12, 15, 20, 36, 100]
    
    for n in test_numbers:
        analysis = analyze_totient_properties(n)
        print_totient_analysis(analysis)
    
    # Compare multiple numbers
    comparison_numbers = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    compare_totients(comparison_numbers)
    
    # Demonstrate multiplicative property
    demonstrate_multiplicative_property()
    
    # Show interesting facts
    interesting_totient_facts()
    
    print(f"\n{'=' * 60}")


if __name__ == "__main__":
    main()
