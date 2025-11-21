"""
GCD and LCM Calculator

Calculates the Greatest Common Divisor (GCD) and Least Common Multiple (LCM)
of two or more numbers using the Euclidean algorithm and mathematical relationships.

Example: GCD(12, 18) = 6 and LCM(12, 18) = 36
"""

def gcd(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) of two numbers using
    the Euclidean algorithm.
    
    Args:
        a: First positive integer
        b: Second positive integer
    
    Returns:
        GCD of a and b
    """
    # Ensure positive integers
    a, b = abs(a), abs(b)
    
    # Euclidean algorithm
    while b:
        a, b = b, a % b
    
    return a


def lcm(a, b):
    """
    Calculate the Least Common Multiple (LCM) of two numbers.
    Uses the relationship: LCM(a, b) = |a * b| / GCD(a, b)
    
    Args:
        a: First positive integer
        b: Second positive integer
    
    Returns:
        LCM of a and b
    """
    if a == 0 or b == 0:
        return 0
    
    return abs(a * b) // gcd(a, b)


def gcd_multiple(numbers):
    """
    Calculate the GCD of multiple numbers.
    
    Args:
        numbers: List of positive integers
    
    Returns:
        GCD of all numbers in the list
    """
    if not numbers:
        return 0
    
    result = numbers[0]
    for num in numbers[1:]:
        result = gcd(result, num)
    
    return result


def lcm_multiple(numbers):
    """
    Calculate the LCM of multiple numbers.
    
    Args:
        numbers: List of positive integers
    
    Returns:
        LCM of all numbers in the list
    """
    if not numbers:
        return 0
    
    result = numbers[0]
    for num in numbers[1:]:
        result = lcm(result, num)
    
    return result


def extended_gcd(a, b):
    """
    Extended Euclidean Algorithm.
    Finds integers x and y such that: a*x + b*y = gcd(a, b)
    
    Args:
        a: First positive integer
        b: Second positive integer
    
    Returns:
        Tuple (gcd, x, y) where a*x + b*y = gcd
    """
    if b == 0:
        return a, 1, 0
    
    gcd_val, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    
    return gcd_val, x, y


def are_coprime(a, b):
    """
    Check if two numbers are coprime (relatively prime).
    Two numbers are coprime if their GCD is 1.
    
    Args:
        a: First positive integer
        b: Second positive integer
    
    Returns:
        True if a and b are coprime, False otherwise
    """
    return gcd(a, b) == 1


def get_all_divisors(n):
    """
    Get all divisors of a number.
    
    Args:
        n: Positive integer
    
    Returns:
        List of all divisors of n
    """
    n = abs(n)
    if n == 0:
        return []
    
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    
    return sorted(divisors)


def analyze_pair(a, b):
    """
    Provide detailed analysis of two numbers including GCD, LCM,
    and their relationship.
    
    Args:
        a: First positive integer
        b: Second positive integer
    """
    gcd_val = gcd(a, b)
    lcm_val = lcm(a, b)
    coprime = are_coprime(a, b)
    
    print(f"\n{'=' * 60}")
    print(f"Analysis of {a} and {b}")
    print(f"{'=' * 60}")
    print(f"GCD({a}, {b}) = {gcd_val}")
    print(f"LCM({a}, {b}) = {lcm_val}")
    print(f"Product: {a} × {b} = {a * b}")
    print(f"GCD × LCM = {gcd_val} × {lcm_val} = {gcd_val * lcm_val}")
    print(f"Coprime: {'Yes' if coprime else 'No'}")
    
    # Extended GCD
    gcd_ext, x, y = extended_gcd(a, b)
    print(f"\nExtended GCD: {a} × {x} + {b} × {y} = {gcd_ext}")
    
    # Divisors
    divisors_a = get_all_divisors(a)
    divisors_b = get_all_divisors(b)
    common_divisors = sorted(set(divisors_a) & set(divisors_b))
    
    print(f"\nDivisors of {a}: {divisors_a}")
    print(f"Divisors of {b}: {divisors_b}")
    print(f"Common divisors: {common_divisors}")
    print(f"Greatest common divisor: {max(common_divisors)}")


def demonstrate_gcd_steps(a, b):
    """
    Show step-by-step calculation of GCD using Euclidean algorithm.
    
    Args:
        a: First positive integer
        b: Second positive integer
    """
    print(f"\n{'=' * 60}")
    print(f"Step-by-Step GCD Calculation: GCD({a}, {b})")
    print(f"{'=' * 60}")
    
    original_a, original_b = a, b
    step = 1
    
    while b:
        quotient = a // b
        remainder = a % b
        print(f"Step {step}: {a} = {b} × {quotient} + {remainder}")
        a, b = b, remainder
        step += 1
    
    print(f"\nResult: GCD({original_a}, {original_b}) = {a}")


def main():
    print("=" * 60)
    print("GCD and LCM Calculator")
    print("=" * 60)
    
    # Example 1: Simple pair
    print("\n### Example 1: Basic Calculation")
    a, b = 12, 18
    analyze_pair(a, b)
    
    # Example 2: Larger numbers
    print("\n### Example 2: Larger Numbers")
    a, b = 48, 180
    analyze_pair(a, b)
    
    # Example 3: Step-by-step demonstration
    demonstrate_gcd_steps(48, 180)
    
    # Example 4: Coprime numbers
    print("\n### Example 3: Coprime Numbers")
    a, b = 17, 19
    analyze_pair(a, b)
    
    # Example 5: Multiple numbers
    print(f"\n{'=' * 60}")
    print("GCD and LCM of Multiple Numbers")
    print(f"{'=' * 60}")
    
    numbers = [12, 18, 24, 30]
    print(f"\nNumbers: {numbers}")
    print(f"GCD: {gcd_multiple(numbers)}")
    print(f"LCM: {lcm_multiple(numbers)}")
    
    numbers = [15, 25, 35, 45]
    print(f"\nNumbers: {numbers}")
    print(f"GCD: {gcd_multiple(numbers)}")
    print(f"LCM: {lcm_multiple(numbers)}")
    
    # Mathematical properties
    print(f"\n{'=' * 60}")
    print("Mathematical Properties")
    print(f"{'=' * 60}")
    
    print("\n1. GCD × LCM = Product of two numbers")
    a, b = 12, 18
    print(f"   {a} and {b}: GCD({a},{b}) × LCM({a},{b}) = {gcd(a,b)} × {lcm(a,b)} = {gcd(a,b) * lcm(a,b)}")
    print(f"   Product: {a} × {b} = {a * b}")
    print(f"   Property verified: {gcd(a,b) * lcm(a,b) == a * b}")
    
    print("\n2. Coprime numbers have GCD = 1")
    pairs = [(7, 11), (15, 28), (21, 35)]
    for a, b in pairs:
        print(f"   GCD({a}, {b}) = {gcd(a, b)} - {'Coprime' if are_coprime(a, b) else 'Not coprime'}")
    
    print("\n3. GCD is distributive")
    a, b, c = 12, 18, 24
    print(f"   GCD({a}, GCD({b}, {c})) = GCD({a}, {gcd(b, c)}) = {gcd(a, gcd(b, c))}")
    print(f"   GCD(GCD({a}, {b}), {c}) = GCD({gcd(a, b)}, {c}) = {gcd(gcd(a, b), c)}")
    
    print(f"\n{'=' * 60}")
    print("Applications:")
    print("• Fraction simplification: Reduce numerator and denominator by their GCD")
    print("• Modular arithmetic: Finding multiplicative inverses")
    print("• Cryptography: RSA key generation uses coprime numbers")
    print("• Scheduling: LCM finds when periodic events coincide")
    print("• Music theory: Finding harmonic frequencies")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
