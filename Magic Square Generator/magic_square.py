"""
Magic Square Generator

Generates magic squares of different sizes. A magic square is an n×n grid
filled with distinct positive integers from 1 to n² such that the sum of
the numbers in each row, column, and both main diagonals is the same.

The magic constant (sum) for an n×n magic square is: M = n(n² + 1) / 2
"""

def generate_odd_magic_square(n):
    """
    Generate a magic square for odd n using the Siamese method.
    
    Args:
        n: Size of the magic square (must be odd)
    
    Returns:
        2D list representing the magic square
    """
    if n % 2 == 0:
        raise ValueError("This method only works for odd-sized magic squares")
    
    # Initialize empty square
    square = [[0] * n for _ in range(n)]
    
    # Start position: middle of top row
    i, j = 0, n // 2
    num = 1
    
    while num <= n * n:
        square[i][j] = num
        num += 1
        
        # Move diagonally up-right
        new_i = (i - 1) % n
        new_j = (j + 1) % n
        
        # If the new position is occupied, move down instead
        if square[new_i][new_j] != 0:
            i = (i + 1) % n
        else:
            i, j = new_i, new_j
    
    return square


def generate_doubly_even_magic_square(n):
    """
    Generate a magic square for doubly even n (divisible by 4).
    
    Args:
        n: Size of the magic square (must be divisible by 4)
    
    Returns:
        2D list representing the magic square
    """
    if n % 4 != 0:
        raise ValueError("This method only works for doubly even-sized magic squares (divisible by 4)")
    
    # Initialize with numbers 1 to n²
    square = [[0] * n for _ in range(n)]
    num = 1
    
    # Fill the square sequentially
    for i in range(n):
        for j in range(n):
            square[i][j] = num
            num += 1
    
    # Invert pattern for doubly even magic square
    # For positions that should be inverted: swap with complement
    for i in range(n):
        for j in range(n):
            # Check if this position should be inverted
            # Pattern: invert if NOT in the corners of 4x4 blocks
            i_mod = i % 4
            j_mod = j % 4
            
            # Invert if in the middle cross pattern of each 4x4 block
            if (i_mod == 0 or i_mod == 3) and (j_mod == 0 or j_mod == 3):
                continue  # Keep as is (corners)
            elif (i_mod == 1 or i_mod == 2) and (j_mod == 1 or j_mod == 2):
                continue  # Keep as is (center)
            else:
                # Invert this position
                square[i][j] = n * n + 1 - square[i][j]
    
    return square


def generate_singly_even_magic_square(n):
    """
    Generate a magic square for singly even n (even but not divisible by 4).
    Uses the LUX method.
    
    Args:
        n: Size of the magic square (must be singly even)
    
    Returns:
        2D list representing the magic square
    """
    if n % 2 != 0 or n % 4 == 0:
        raise ValueError("This method only works for singly even-sized magic squares")
    
    # This is more complex - simplified version
    # For simplicity, we'll use a basic approach
    m = n // 2
    A = generate_odd_magic_square(m)
    
    # Create four quadrants
    square = [[0] * n for _ in range(n)]
    
    # Fill quadrants
    for i in range(m):
        for j in range(m):
            square[i][j] = A[i][j]  # Top-left
            square[i + m][j + m] = A[i][j] + m * m  # Bottom-right
            square[i][j + m] = A[i][j] + 2 * m * m  # Top-right
            square[i + m][j] = A[i][j] + 3 * m * m  # Bottom-left
    
    # Swap some elements to fix the magic property
    k = (m - 1) // 2
    for i in range(m):
        for j in range(k):
            if i == k and j == 0:
                continue
            square[i][j], square[i + m][j] = square[i + m][j], square[i][j]
    
    for i in range(m):
        for j in range(n - k + 1, n):
            square[i][j], square[i + m][j] = square[i + m][j], square[i][j]
    
    return square


def generate_magic_square(n):
    """
    Generate a magic square of size n.
    
    Args:
        n: Size of the magic square
    
    Returns:
        2D list representing the magic square
    """
    if n < 3:
        raise ValueError("Magic square must be at least 3x3")
    
    if n % 2 == 1:
        return generate_odd_magic_square(n)
    elif n % 4 == 0:
        return generate_doubly_even_magic_square(n)
    else:
        return generate_singly_even_magic_square(n)


def verify_magic_square(square):
    """
    Verify that a square is indeed a magic square.
    
    Args:
        square: 2D list representing the square
    
    Returns:
        Tuple (is_magic, magic_constant, details)
    """
    n = len(square)
    magic_constant = n * (n * n + 1) // 2
    
    # Check rows
    row_sums = [sum(row) for row in square]
    if not all(s == magic_constant for s in row_sums):
        return False, magic_constant, "Row sums don't match"
    
    # Check columns
    col_sums = [sum(square[i][j] for i in range(n)) for j in range(n)]
    if not all(s == magic_constant for s in col_sums):
        return False, magic_constant, "Column sums don't match"
    
    # Check main diagonal
    main_diag = sum(square[i][i] for i in range(n))
    if main_diag != magic_constant:
        return False, magic_constant, "Main diagonal sum doesn't match"
    
    # Check anti-diagonal
    anti_diag = sum(square[i][n - 1 - i] for i in range(n))
    if anti_diag != magic_constant:
        return False, magic_constant, "Anti-diagonal sum doesn't match"
    
    return True, magic_constant, "Valid magic square"


def print_magic_square(square):
    """Print a magic square in a formatted way."""
    n = len(square)
    magic_constant = n * (n * n + 1) // 2
    
    print(f"\n{'=' * 60}")
    print(f"Magic Square of size {n}×{n}")
    print(f"Magic Constant: {magic_constant}")
    print(f"{'=' * 60}\n")
    
    # Calculate column widths
    max_num = n * n
    col_width = len(str(max_num)) + 2
    
    for i, row in enumerate(square):
        print("  ".join(f"{num:>{col_width}}" for num in row))
        if i < n - 1:
            print()
    
    # Verify
    is_magic, constant, details = verify_magic_square(square)
    print(f"\nVerification: {details}")
    print(f"Expected magic constant: {constant}")
    print(f"{'=' * 60}")


def main():
    print("=" * 60)
    print("Magic Square Generator")
    print("=" * 60)
    
    # Generate magic squares of different sizes
    sizes = [3, 4, 5]
    
    for size in sizes:
        try:
            print(f"\nGenerating {size}×{size} magic square...")
            square = generate_magic_square(size)
            print_magic_square(square)
        except ValueError as e:
            print(f"Error generating {size}×{size} square: {e}")
    
    # Show a larger example
    print("\n" + "=" * 60)
    print("Generating 7×7 magic square (odd size)...")
    try:
        square = generate_magic_square(7)
        print_magic_square(square)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

