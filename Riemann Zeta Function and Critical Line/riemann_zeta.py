"""
Riemann Zeta Function & Critical Line Explorer

A comprehensive implementation of the Riemann Zeta Function with tools
to explore the Riemann Hypothesis - one of mathematics' greatest unsolved problems.

This program computes ζ(s) for complex arguments, finds zeros on the critical line,
and demonstrates connections to prime number distribution.
"""

import math
import cmath


def zeta_dirichlet(s, terms=10000):
    """
    Compute the Riemann Zeta function using Dirichlet series.
    
    ζ(s) = Σ(n=1 to ∞) 1/n^s
    
    Converges for Re(s) > 1. For computational efficiency, uses finite sum.
    
    Args:
        s: Complex number or real number
        terms: Number of terms in the series
    
    Returns:
        Complex approximation of ζ(s)
    """
    if isinstance(s, (int, float)):
        s = complex(s, 0)
    
    # Handle special case s = 1 (pole)
    if abs(s - 1) < 1e-10:
        return complex(float('inf'), 0)
    
    result = 0
    for n in range(1, terms + 1):
        result += 1 / (n ** s)
    
    return result


def zeta_euler_product(s, num_primes=1000):
    """
    Compute zeta using Euler's product formula over primes.
    
    ζ(s) = Π(p prime) 1/(1 - p^(-s))
    
    This demonstrates the deep connection between ζ(s) and prime numbers.
    
    Args:
        s: Complex number or real number  
        num_primes: Number of primes to use in product
    
    Returns:
        Complex approximation of ζ(s)
    """
    if isinstance(s, (int, float)):
        s = complex(s, 0)
    
    primes = sieve_of_eratosthenes(num_primes)
    
    result = 1.0
    for p in primes:
        result *= 1 / (1 - p ** (-s))
    
    return result


def sieve_of_eratosthenes(limit):
    """Find all prime numbers up to limit."""
    if limit < 2:
        return []
    
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    
    return [i for i in range(2, limit + 1) if is_prime[i]]


def zeta_functional_equation(s, terms=1000):
    """
    Use functional equation to compute ζ(s) for Re(s) < 0.
    
    ζ(s) = 2^s π^(s-1) sin(πs/2) Γ(1-s) ζ(1-s)
    
    This extends the zeta function to the entire complex plane.
    
    Args:
        s: Complex number
        terms: Number of terms for computing ζ(1-s)
    
    Returns:
        Complex value of ζ(s)
    """
    if isinstance(s, (int, float)):
        s = complex(s, 0)
    
    # For Re(s) > 1, use direct computation
    if s.real > 1:
        return zeta_dirichlet(s, terms)
    
    # For Re(s) < 0, use functional equation
    if s.real < 0:
        # ζ(s) = 2^s π^(s-1) sin(πs/2) Γ(1-s) ζ(1-s)
        pi = math.pi
        
        # Compute each component
        one_minus_s = 1 - s
        zeta_1_minus_s = zeta_dirichlet(one_minus_s, terms)
        
        factor1 = 2 ** s
        factor2 = pi ** (s - 1)
        factor3 = cmath.sin(pi * s / 2)
        factor4 = gamma_stirling(one_minus_s)
        
        return factor1 * factor2 * factor3 * factor4 * zeta_1_minus_s
    
    # For 0 < Re(s) < 1, use alternating series (Dirichlet eta function)
    # η(s) = (1 - 2^(1-s)) ζ(s) = Σ (-1)^(n+1) / n^s
    eta = 0
    for n in range(1, terms + 1):
        eta += ((-1) ** (n + 1)) / (n ** s)
    
    zeta_s = eta / (1 - 2 ** (1 - s))
    return zeta_s


def gamma_stirling(s):
    """
    Approximate Gamma function using Stirling's formula.
    
    Γ(s) ≈ √(2π/s) * (s/e)^s
    
    Args:
        s: Complex number
    
    Returns:
        Complex approximation of Γ(s)
    """
    if isinstance(s, (int, float)):
        s = complex(s, 0)
    
    # Use reflection formula for Re(s) < 0.5
    if s.real < 0.5:
        # Γ(s)Γ(1-s) = π/sin(πs)
        return math.pi / (cmath.sin(math.pi * s) * gamma_stirling(1 - s))
    
    # Stirling's approximation
    e = math.e
    pi = math.pi
    
    result = cmath.sqrt(2 * pi / s) * ((s / e) ** s)
    return result


def find_zeros_critical_line(t_start, t_end, step=0.1):
    """
    Search for zeros of ζ(1/2 + it) on the critical line.
    
    Uses sign changes in Im(ζ(s)) to locate zeros.
    
    Args:
        t_start: Starting imaginary part
        t_end: Ending imaginary part
        step: Step size for search
    
    Returns:
        List of (t, |ζ(1/2 + it)|) tuples for potential zeros
    """
    zeros = []
    t = t_start
    prev_sign = None
    
    while t <= t_end:
        s = complex(0.5, t)
        zeta_val = zeta_functional_equation(s, terms=5000)
        
        # Check for sign change in imaginary part
        current_sign = 1 if zeta_val.imag > 0 else -1
        
        if prev_sign is not None and current_sign != prev_sign:
            # Refine the zero using bisection
            t_refined = bisection_zero(t - step, t, num_iterations=20)
            s_zero = complex(0.5, t_refined)
            zeta_at_zero = zeta_functional_equation(s_zero, terms=5000)
            magnitude = abs(zeta_at_zero)
            
            if magnitude < 0.01:  # Threshold for considering it a zero
                zeros.append((t_refined, magnitude))
        
        prev_sign = current_sign
        t += step
    
    return zeros


def bisection_zero(t_low, t_high, num_iterations=20):
    """
    Refine zero location using bisection on imaginary part of ζ(1/2 + it).
    
    Args:
        t_low: Lower bound
        t_high: Upper bound
        num_iterations: Number of bisection iterations
    
    Returns:
        Refined value of t
    """
    for _ in range(num_iterations):
        t_mid = (t_low + t_high) / 2
        s_mid = complex(0.5, t_mid)
        zeta_mid = zeta_functional_equation(s_mid, terms=5000)
        
        s_low = complex(0.5, t_low)
        zeta_low = zeta_functional_equation(s_low, terms=5000)
        
        if zeta_low.imag * zeta_mid.imag < 0:
            t_high = t_mid
        else:
            t_low = t_mid
    
    return (t_low + t_high) / 2


def special_zeta_values():
    """
    Compute special values of the zeta function with known closed forms.
    
    Returns:
        Dictionary of special values and their theoretical values
    """
    results = {}
    
    # ζ(2) = π²/6 (Basel problem)
    zeta_2_computed = zeta_dirichlet(2, terms=100000)
    zeta_2_exact = (math.pi ** 2) / 6
    results['zeta(2)'] = {
        'computed': zeta_2_computed.real,
        'exact': zeta_2_exact,
        'error': abs(zeta_2_computed.real - zeta_2_exact)
    }
    
    # ζ(4) = π⁴/90
    zeta_4_computed = zeta_dirichlet(4, terms=10000)
    zeta_4_exact = (math.pi ** 4) / 90
    results['zeta(4)'] = {
        'computed': zeta_4_computed.real,
        'exact': zeta_4_exact,
        'error': abs(zeta_4_computed.real - zeta_4_exact)
    }
    
    # ζ(0) = -1/2 (via analytic continuation)
    zeta_0_computed = zeta_functional_equation(0, terms=10000)
    zeta_0_exact = -0.5
    results['zeta(0)'] = {
        'computed': zeta_0_computed.real,
        'exact': zeta_0_exact,
        'error': abs(zeta_0_computed.real - zeta_0_exact)
    }
    
    # ζ(-1) = -1/12 (famous "paradoxical" result)
    zeta_neg1_computed = zeta_functional_equation(-1, terms=10000)
    zeta_neg1_exact = -1/12
    results['zeta(-1)'] = {
        'computed': zeta_neg1_computed.real,
        'exact': zeta_neg1_exact,
        'error': abs(zeta_neg1_computed.real - zeta_neg1_exact)
    }
    
    return results


def demonstrate_euler_product():
    """
    Demonstrate the connection between ζ(s) and prime numbers.
    
    Shows that Dirichlet series and Euler product give same result.
    """
    print("\n" + "=" * 60)
    print("Euler Product Formula: ζ(s) = Π(p prime) 1/(1 - p^(-s))")
    print("=" * 60)
    
    test_values = [2, 3, 4, 5]
    
    for s in test_values:
        zeta_dirichlet_val = zeta_dirichlet(s, terms=10000)
        zeta_euler_val = zeta_euler_product(s, num_primes=1000)
        
        print(f"\nζ({s}):")
        print(f"  Dirichlet Series: {zeta_dirichlet_val.real:.10f}")
        print(f"  Euler Product:    {zeta_euler_val.real:.10f}")
        print(f"  Difference:       {abs(zeta_dirichlet_val - zeta_euler_val):.2e}")


def main():
    """Main function demonstrating the Riemann Zeta Function."""
    
    print("=" * 70)
    print("Riemann Zeta Function & Critical Line Explorer")
    print("=" * 70)
    print("\nExploring one of mathematics' greatest mysteries:")
    print("The Riemann Hypothesis - Are all non-trivial zeros on Re(s) = 1/2?")
    
    # Special Values
    print("\n" + "=" * 70)
    print("Special Zeta Values (with closed forms)")
    print("=" * 70)
    
    special_vals = special_zeta_values()
    for name, data in special_vals.items():
        print(f"\n{name}:")
        print(f"  Computed: {data['computed']:.10f}")
        print(f"  Exact:    {data['exact']:.10f}")
        print(f"  Error:    {data['error']:.2e}")
    
    # Euler Product
    demonstrate_euler_product()
    
    # Find zeros on critical line
    print("\n" + "=" * 70)
    print("Searching for Zeros on Critical Line (Re(s) = 1/2)")
    print("=" * 70)
    print("\nThis may take a moment...")
    
    zeros = find_zeros_critical_line(10, 30, step=0.5)
    
    print(f"\nFound {len(zeros)} zeros in the range Im(s) ∈ [10, 30]:")
    print("\n{:^20} | {:^20}".format("s = 1/2 + it", "|ζ(s)|"))
    print("-" * 45)
    
    for i, (t, magnitude) in enumerate(zeros[:10], 1):
        print(f"Zero #{i:2d}: 0.5 + {t:8.4f}i | {magnitude:.2e}")
    
    # Complex values
    print("\n" + "=" * 70)
    print("Zeta Function at Complex Points")
    print("=" * 70)
    
    test_points = [
        complex(2, 0),
        complex(0.5, 14.135),  # Near first zero
        complex(3, 5),
        complex(-1, 0),
    ]
    
    print("\n{:^20} | {:^30}".format("s", "ζ(s)"))
    print("-" * 52)
    
    for s in test_points:
        zeta_val = zeta_functional_equation(s, terms=5000)
        print(f"{s.real:6.2f} + {s.imag:6.2f}i | "
              f"{zeta_val.real:10.6f} + {zeta_val.imag:10.6f}i")
    
    print("\n" + "=" * 70)
    print("The Riemann Hypothesis")
    print("=" * 70)
    print("\nAll zeros found lie on the critical line Re(s) = 1/2!")
    print("Over 10 trillion zeros have been verified computationally.")
    print("But a general proof remains one of mathematics' greatest challenges.")
    print("\nProve it and win $1,000,000 from the Clay Mathematics Institute!")
    print("=" * 70)


if __name__ == "__main__":
    main()
