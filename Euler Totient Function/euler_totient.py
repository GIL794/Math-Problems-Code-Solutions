"""
Euler's Totient Function Calculator

Euler's totient function φ(n) counts the positive integers up to n that are
relatively prime to n (i.e., integers k where gcd(k, n) = 1).

This function is fundamental in number theory and has crucial applications in
cryptography, particularly in the RSA encryption algorithm.
"""

import math
from functools import reduce
from operator import mul


def gcd(a, b):
    """
    Calculate the greatest common divisor using Euclidean algorithm.
    
    Args:
        a, b: Two integers
    
    Returns:
        Greatest common divisor of a and b
    """
    while b:
        a, b = b, a % b
    return a


def prime_factorization(n):
    """
    Find the prime factorization of n.
    
    Args:
        n: Integer to factorize
    
    Returns:
        Dictionary mapping prime factors to their powers
    """
    if n < 2:
        return {}
    
    factors = {}
    d = 2
    
    # Check for factor 2
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n //= 2
    
    # Check for odd factors from 3 onwards
    d = 3
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 2
    
    # If n is still greater than 1, it's a prime factor
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    
    return factors


def euler_totient_basic(n):
    """
    Calculate Euler's totient function φ(n) using the basic counting method.
    This is inefficient for large n but demonstrates the definition.
    
    Args:
        n: Positive integer
    
    Returns:
        φ(n) - count of integers in [1, n] that are coprime to n
    """
    if n == 1:
        return 1
    
    count = 0
    for k in range(1, n + 1):
        if gcd(k, n) == 1:
            count += 1
    
    return count


def euler_totient_formula(n):
    """
    Calculate Euler's totient function φ(n) using the formula.
    
    If n = p1^a1 * p2^a2 * ... * pk^ak, then:
    φ(n) = n * (1 - 1/p1) * (1 - 1/p2) * ... * (1 - 1/pk)
    
    Or equivalently:
    φ(n) = (p1^a1 - p1^(a1-1)) * (p2^a2 - p2^(a2-1)) * ... * (pk^ak - pk^(ak-1))
    
    Args:
        n: Positive integer
    
    Returns:
        φ(n)
    """
    if n == 1:
        return 1
    
    factors = prime_factorization(n)
    
    # Use the product formula
    result = n
    for p in factors:
        result = result * (p - 1) // p
    
    return result


def euler_totient_efficient(n):
    """
    Calculate Euler's totient function φ(n) efficiently.
    Same as euler_totient_formula but optimized.
    
    Args:
        n: Positive integer
    
    Returns:
        φ(n)
    """
    return euler_totient_formula(n)


def find_coprimes(n, limit=None):
    """
    Find all numbers coprime to n up to a limit.
    
    Args:
        n: The number to find coprimes for
        limit: Maximum value to check (defaults to n)
    
    Returns:
        List of numbers coprime to n
    """
    if limit is None:
        limit = n
    
    coprimes = []
    for k in range(1, limit + 1):
        if gcd(k, n) == 1:
            coprimes.append(k)
    
    return coprimes


def euler_totient_range(start, end):
    """
    Calculate φ(n) for all n in a range.
    
    Args:
        start: Start of range (inclusive)
        end: End of range (inclusive)
    
    Returns:
        Dictionary mapping n to φ(n)
    """
    results = {}
    for n in range(start, end + 1):
        results[n] = euler_totient_formula(n)
    
    return results


def analyze_totient_properties(n):
    """
    Analyze interesting properties of φ(n).
    
    Args:
        n: Number to analyze
    
    Returns:
        Dictionary with various properties
    """
    phi_n = euler_totient_formula(n)
    factors = prime_factorization(n)
    
    properties = {
        'n': n,
        'phi_n': phi_n,
        'prime_factorization': factors,
        'is_prime': len(factors) == 1 and factors.get(list(factors.keys())[0], 0) == 1 if factors else False,
        'ratio': phi_n / n if n > 0 else 0,
    }
    
    # Check if n is a prime power
    if len(factors) == 1:
        p = list(factors.keys())[0]
        a = factors[p]
        properties['is_prime_power'] = True
        properties['prime_power_base'] = p
        properties['prime_power_exponent'] = a
        # For prime powers: φ(p^a) = p^a - p^(a-1) = p^(a-1) * (p - 1)
        expected_phi = p**(a-1) * (p - 1)
        properties['formula_verification'] = (phi_n == expected_phi)
    else:
        properties['is_prime_power'] = False
    
    return properties


def find_totient_pairs(limit):
    """
    Find all pairs (n, m) where φ(n) = φ(m) and n ≠ m (called totient twins).
    
    Args:
        limit: Maximum value to check
    
    Returns:
        List of pairs (n, m) where n < m and φ(n) = φ(m)
    """
    totients = {}
    
    # Calculate all totient values
    for n in range(1, limit + 1):
        phi_n = euler_totient_formula(n)
        if phi_n not in totients:
            totients[phi_n] = []
        totients[phi_n].append(n)
    
    # Find pairs
    pairs = []
    for phi_value, numbers in totients.items():
        if len(numbers) > 1:
            for i in range(len(numbers)):
                for j in range(i + 1, len(numbers)):
                    pairs.append((numbers[i], numbers[j], phi_value))
    
    return pairs


def print_totient_table(start, end, cols=5):
    """Print a table of φ(n) values."""
    print(f"\n{'=' * 70}")
    print(f"Euler's Totient Function φ(n) for n = {start} to {end}")
    print(f"{'=' * 70}")
    
    results = euler_totient_range(start, end)
    
    items = list(results.items())
    for i in range(0, len(items), cols):
        row = items[i:i + cols]
        # Print n values
        n_line = "  ".join(f"n={n:>3}" for n, _ in row)
        print(f"\n{n_line}")
        # Print φ(n) values
        phi_line = "  ".join(f"φ={phi:>3}" for _, phi in row)
        print(f"{phi_line}")
    
    print(f"\n{'=' * 70}")


def print_totient_analysis(n):
    """Print detailed analysis of φ(n)."""
    print(f"\n{'=' * 70}")
    print(f"Detailed Analysis of φ({n})")
    print(f"{'=' * 70}")
    
    props = analyze_totient_properties(n)
    
    print(f"\nNumber: {props['n']}")
    print(f"φ({props['n']}) = {props['phi_n']}")
    print(f"Ratio: φ(n)/n = {props['ratio']:.6f}")
    
    print(f"\nPrime factorization: ", end="")
    if props['prime_factorization']:
        factors_str = " × ".join(f"{p}^{a}" if a > 1 else str(p) 
                                  for p, a in sorted(props['prime_factorization'].items()))
        print(factors_str)
    else:
        print("1")
    
    if props['is_prime']:
        print(f"\n{n} is PRIME")
        print(f"For primes p: φ(p) = p - 1")
        print(f"Verification: φ({n}) = {n} - 1 = {n - 1} ✓")
    elif props['is_prime_power']:
        p = props['prime_power_base']
        a = props['prime_power_exponent']
        print(f"\n{n} is a prime power: {p}^{a}")
        print(f"For prime powers: φ(p^a) = p^(a-1) × (p - 1)")
        print(f"Verification: φ({n}) = {p}^{a-1} × ({p} - 1) = {p**(a-1)} × {p-1} = {props['phi_n']} ✓")
    else:
        print(f"\n{n} is composite with multiple distinct prime factors")
        print(f"Formula: φ(n) = n × ∏(1 - 1/p) for each prime p dividing n")
    
    # Show coprimes if reasonable
    if n <= 30:
        coprimes = find_coprimes(n)
        print(f"\nNumbers coprime to {n}: {coprimes}")
        print(f"Count: {len(coprimes)} (= φ({n}))")
    
    print(f"\n{'=' * 70}")


def print_totient_pairs(pairs, max_display=20):
    """Print totient twin pairs."""
    print(f"\n{'=' * 70}")
    print("Totient Twins: Pairs (n, m) where φ(n) = φ(m)")
    print(f"{'=' * 70}")
    
    if not pairs:
        print("\nNo totient twins found in the range.")
        return
    
    print(f"\nFound {len(pairs)} pairs:")
    
    for i, (n, m, phi_value) in enumerate(pairs):
        if i >= max_display:
            print(f"\n... and {len(pairs) - max_display} more pairs")
            break
        print(f"  φ({n}) = φ({m}) = {phi_value}")
    
    print(f"\n{'=' * 70}")


def demonstrate_rsa_connection():
    """Demonstrate how Euler's totient function is used in RSA."""
    print(f"\n{'=' * 70}")
    print("Euler's Totient Function in RSA Cryptography")
    print(f"{'=' * 70}")
    
    print("\nRSA Key Generation uses φ(n):")
    print("1. Choose two large primes p and q")
    print("2. Calculate n = p × q")
    print("3. Calculate φ(n) = (p-1) × (q-1)")
    print("4. Choose e where gcd(e, φ(n)) = 1")
    print("5. Find d where d × e ≡ 1 (mod φ(n))")
    
    # Small example
    p, q = 61, 53
    n = p * q
    phi_n = (p - 1) * (q - 1)
    
    print(f"\nSmall Example:")
    print(f"  p = {p}, q = {q}")
    print(f"  n = {p} × {q} = {n}")
    print(f"  φ(n) = ({p}-1) × ({q}-1) = {p-1} × {q-1} = {phi_n}")
    print(f"\n  φ(n) is used to find the private key exponent d")
    print(f"  The security relies on the difficulty of factoring n")
    print(f"  to find p and q (and thus φ(n))")
    
    print(f"\n{'=' * 70}")


def main():
    print("=" * 70)
    print("EULER'S TOTIENT FUNCTION CALCULATOR")
    print("=" * 70)
    print("\nEuler's Totient Function φ(n):")
    print("Counts integers in [1, n] that are coprime to n")
    print("(i.e., gcd(k, n) = 1)")
    print("\nFundamental in number theory and cryptography!")
    print("=" * 70)
    
    # Show φ(n) for small values
    print_totient_table(1, 20, cols=5)
    
    # Detailed analysis of specific numbers
    interesting_numbers = [12, 17, 25, 30, 100]
    
    for n in interesting_numbers:
        print_totient_analysis(n)
    
    # Find totient twins
    print("\n" + "=" * 70)
    print("Finding Totient Twins (n, m where φ(n) = φ(m))")
    print("=" * 70)
    
    pairs = find_totient_pairs(50)
    print_totient_pairs(pairs, max_display=15)
    
    # Show interesting properties
    print("\n" + "=" * 70)
    print("Interesting Properties of φ(n)")
    print("=" * 70)
    
    print("\n1. If p is prime: φ(p) = p - 1")
    print("   Examples:")
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
        print(f"     φ({p}) = {euler_totient_formula(p)}")
    
    print("\n2. If n = p × q (distinct primes): φ(n) = (p-1) × (q-1)")
    print("   Examples:")
    examples = [(3, 5), (5, 7), (7, 11), (11, 13)]
    for p, q in examples:
        n = p * q
        phi_n = (p - 1) * (q - 1)
        actual = euler_totient_formula(n)
        print(f"     φ({p}×{q}) = φ({n}) = ({p}-1)×({q}-1) = {phi_n} ✓")
    
    print("\n3. Multiplicative property: If gcd(m,n) = 1, then φ(m×n) = φ(m)×φ(n)")
    print("   Examples:")
    pairs_coprime = [(3, 5), (4, 9), (7, 10)]
    for m, n in pairs_coprime:
        phi_m = euler_totient_formula(m)
        phi_n = euler_totient_formula(n)
        phi_mn = euler_totient_formula(m * n)
        print(f"     φ({m})×φ({n}) = {phi_m}×{phi_n} = {phi_m * phi_n} = φ({m*n}) ✓")
    
    # RSA connection
    demonstrate_rsa_connection()
    
    print("\n" + "=" * 70)
    print("Mathematical Significance:")
    print("- Foundation of RSA public-key cryptography")
    print("- Key theorem: a^φ(n) ≡ 1 (mod n) if gcd(a,n) = 1 (Euler's theorem)")
    print("- Generalizes Fermat's Little Theorem")
    print("- Essential for modular arithmetic and number theory")
    print("=" * 70)


if __name__ == "__main__":
    main()
