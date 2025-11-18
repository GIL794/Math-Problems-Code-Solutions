"""
Pythagorean Triples Finder

Finds all Pythagorean triples (a, b, c) where a^2 + b^2 = c^2
and a, b, c are positive integers up to a given limit.
"""

def find_pythagorean_triples(max_value):
    """
    Find all Pythagorean triples where a, b, c <= max_value.
    
    Args:
        max_value: Maximum value for any side of the triangle
    
    Returns:
        List of tuples (a, b, c) representing Pythagorean triples
    """
    triples = []
    
    # Generate all possible combinations
    for a in range(1, max_value + 1):
        for b in range(a, max_value + 1):  # Start from a to avoid duplicates
            c_squared = a**2 + b**2
            c = int(c_squared ** 0.5)
            
            # Check if c is an integer and within our limit
            if c * c == c_squared and c <= max_value:
                triples.append((a, b, c))
    
    return triples


def find_primitive_triples(max_value):
    """
    Find primitive Pythagorean triples (triples where gcd(a, b, c) = 1).
    
    Args:
        max_value: Maximum value for any side of the triangle
    
    Returns:
        List of tuples (a, b, c) representing primitive Pythagorean triples
    """
    def gcd(x, y):
        """Calculate greatest common divisor using Euclidean algorithm."""
        while y:
            x, y = y, x % y
        return x
    
    def gcd_three(a, b, c):
        """Calculate gcd of three numbers."""
        return gcd(gcd(a, b), c)
    
    all_triples = find_pythagorean_triples(max_value)
    primitive = []
    
    for triple in all_triples:
        a, b, c = triple
        if gcd_three(a, b, c) == 1:
            primitive.append(triple)
    
    return primitive


def print_triples(triples, title="Pythagorean Triples"):
    """Print triples in a formatted way."""
    print(f"\n{title}:")
    print(f"Total count: {len(triples)}\n")
    
    for idx, (a, b, c) in enumerate(triples, 1):
        print(f"{idx}. ({a}, {b}, {c}) - {a}² + {b}² = {c}² ({a**2} + {b**2} = {c**2})")


def main():
    print("=" * 60)
    print("Pythagorean Triples Finder")
    print("=" * 60)
    
    # Default limit
    max_value = 100
    
    print(f"\nFinding all Pythagorean triples with sides up to {max_value}...")
    
    # Find all triples
    all_triples = find_pythagorean_triples(max_value)
    print_triples(all_triples, "All Pythagorean Triples")
    
    # Find primitive triples
    primitive_triples = find_primitive_triples(max_value)
    print_triples(primitive_triples, "Primitive Pythagorean Triples")
    
    # Statistics
    print("\n" + "=" * 60)
    print("Statistics:")
    print(f"Total triples found: {len(all_triples)}")
    print(f"Primitive triples found: {len(primitive_triples)}")
    print("=" * 60)


if __name__ == "__main__":
    main()

