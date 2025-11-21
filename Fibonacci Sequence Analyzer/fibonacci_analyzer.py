"""
Fibonacci Sequence Analyzer

Generates and analyzes the Fibonacci sequence, where each number is the sum
of the two preceding ones: F(n) = F(n-1) + F(n-2), with F(0) = 0, F(1) = 1.

The sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
"""

def fibonacci_iterative(n):
    """
    Generate Fibonacci sequence up to n terms using iteration.
    
    Args:
        n: Number of terms to generate
    
    Returns:
        List of Fibonacci numbers
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    
    return fib


def fibonacci_nth(n):
    """
    Calculate the nth Fibonacci number (0-indexed).
    
    Args:
        n: Index of Fibonacci number (0-based)
    
    Returns:
        The nth Fibonacci number
    """
    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b


def fibonacci_recursive(n):
    """
    Calculate the nth Fibonacci number using recursion (inefficient for large n).
    
    Args:
        n: Index of Fibonacci number (0-based)
    
    Returns:
        The nth Fibonacci number
    """
    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_golden_ratio(n):
    """
    Calculate Fibonacci numbers using Binet's formula (approximation).
    Uses the golden ratio: φ = (1 + √5) / 2
    
    Args:
        n: Index of Fibonacci number (0-based)
    
    Returns:
        Approximate nth Fibonacci number
    """
    import math
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    return int((phi**n - psi**n) / math.sqrt(5))


def analyze_fibonacci_properties(sequence):
    """Analyze interesting properties of the Fibonacci sequence."""
    print(f"\n{'=' * 60}")
    print("Fibonacci Sequence Properties")
    print(f"{'=' * 60}")
    
    if len(sequence) < 2:
        return
    
    # Check if numbers are even or odd
    even_count = sum(1 for x in sequence if x % 2 == 0)
    odd_count = len(sequence) - even_count
    print(f"\nEven numbers: {even_count}")
    print(f"Odd numbers: {odd_count}")
    
    # Find ratio between consecutive terms (approaching golden ratio)
    if len(sequence) >= 2:
        print(f"\nRatio between consecutive terms (approaching φ ≈ 1.618...):")
        for i in range(1, min(len(sequence), 11)):
            if sequence[i - 1] != 0:
                ratio = sequence[i] / sequence[i - 1]
                print(f"  F({i})/F({i-1}) = {sequence[i]}/{sequence[i-1]} = {ratio:.6f}")
    
    # Check for prime Fibonacci numbers
    def is_prime_simple(n):
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
    
    prime_fibs = [x for x in sequence if is_prime_simple(x) and x > 1]
    if prime_fibs:
        print(f"\nPrime Fibonacci numbers found: {prime_fibs}")
    
    # Sum of first n Fibonacci numbers
    total_sum = sum(sequence)
    print(f"\nSum of first {len(sequence)} Fibonacci numbers: {total_sum}")
    print(f"  (Note: Sum of first n Fibonacci numbers = F(n+2) - 1)")


def print_fibonacci_sequence(sequence, max_display=30):
    """Print Fibonacci sequence in a formatted way."""
    print(f"\n{'=' * 60}")
    print(f"Fibonacci Sequence (first {len(sequence)} terms)")
    print(f"{'=' * 60}")
    
    if len(sequence) <= max_display:
        # Print in columns
        cols = 8
        for i in range(0, len(sequence), cols):
            row = sequence[i:i + cols]
            indices = [f"F({i+j})" for j in range(len(row))]
            print("  ".join(f"{idx:>8}" for idx in indices))
            print("  ".join(f"{num:>8}" for num in row))
            print()
    else:
        # Show first and last terms
        print("First 20 terms:")
        cols = 8
        for i in range(0, min(20, len(sequence)), cols):
            row = sequence[i:i + cols]
            indices = [f"F({i+j})" for j in range(len(row))]
            print("  ".join(f"{idx:>8}" for idx in indices))
            print("  ".join(f"{num:>8}" for num in row))
            print()
        
        print(f"... (showing last 10 terms)")
        last_10 = sequence[-10:]
        start_idx = len(sequence) - 10
        indices = [f"F({start_idx+j})" for j in range(len(last_10))]
        print("  ".join(f"{idx:>12}" for idx in indices))
        print("  ".join(f"{num:>12}" for num in last_10))


def main():
    print("=" * 60)
    print("Fibonacci Sequence Analyzer")
    print("=" * 60)
    
    # Generate sequences of different lengths
    lengths = [20, 30]
    
    for length in lengths:
        sequence = fibonacci_iterative(length)
        print_fibonacci_sequence(sequence)
        analyze_fibonacci_properties(sequence)
    
    # Calculate specific Fibonacci numbers
    print(f"\n{'=' * 60}")
    print("Specific Fibonacci Numbers")
    print(f"{'=' * 60}")
    
    test_indices = [10, 20, 30, 40, 50]
    
    for idx in test_indices:
        fib_value = fibonacci_nth(idx)
        print(f"F({idx}) = {fib_value}")
    
    # Compare methods for accuracy
    print(f"\n{'=' * 60}")
    print("Method Comparison (for F(20))")
    print(f"{'=' * 60}")
    
    n = 20
    iterative = fibonacci_nth(n)
    golden = fibonacci_golden_ratio(n)
    print(f"Iterative method: F({n}) = {iterative}")
    print(f"Golden ratio (Binet's formula): F({n}) = {golden}")
    print(f"Difference: {abs(iterative - golden)}")
    
    print(f"\n{'=' * 60}")
    print("Mathematical Note:")
    print("The ratio of consecutive Fibonacci numbers approaches")
    print("the golden ratio φ = (1 + √5) / 2 ≈ 1.618033988749...")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()

