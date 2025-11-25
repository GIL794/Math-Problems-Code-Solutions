"""
Modular Exponentiation & RSA Demo

Implements fast modular exponentiation using the binary exponentiation method
and demonstrates the basics of RSA public-key cryptography.

This showcases one of the most important algorithms in modern cryptography.
"""

import random
import math


def modular_exponentiation(base, exponent, modulus):
    """
    Calculate (base^exponent) mod modulus efficiently.
    Uses binary exponentiation (square-and-multiply algorithm).
    
    Time complexity: O(log exponent)
    
    Args:
        base: Base number
        exponent: Power to raise base to
        modulus: Modulus for the result
    
    Returns:
        (base^exponent) mod modulus
    """
    if modulus == 1:
        return 0
    
    result = 1
    base = base % modulus
    
    while exponent > 0:
        # If exponent is odd, multiply base with result
        if exponent % 2 == 1:
            result = (result * base) % modulus
        
        # Square the base and halve the exponent
        exponent = exponent >> 1  # Divide by 2
        base = (base * base) % modulus
    
    return result


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


def extended_gcd(a, b):
    """
    Extended Euclidean Algorithm.
    Returns gcd(a, b) and coefficients x, y such that ax + by = gcd(a, b).
    
    Args:
        a, b: Two integers
    
    Returns:
        Tuple (gcd, x, y)
    """
    if a == 0:
        return b, 0, 1
    
    gcd_val, x1, y1 = extended_gcd(b % a, a)
    
    x = y1 - (b // a) * x1
    y = x1
    
    return gcd_val, x, y


def modular_inverse(a, m):
    """
    Find the modular multiplicative inverse of a modulo m.
    Returns x such that (a * x) % m = 1.
    
    Args:
        a: Number to find inverse of
        m: Modulus
    
    Returns:
        Modular inverse of a mod m, or None if it doesn't exist
    """
    gcd_val, x, _ = extended_gcd(a, m)
    
    if gcd_val != 1:
        return None  # Modular inverse doesn't exist
    
    # Make sure result is positive
    return (x % m + m) % m


def is_prime(n, k=5):
    """
    Miller-Rabin primality test.
    
    Args:
        n: Number to test for primality
        k: Number of rounds (higher = more accurate)
    
    Returns:
        True if n is probably prime, False if definitely composite
    """
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    # Write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Witness loop
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = modular_exponentiation(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(r - 1):
            x = modular_exponentiation(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    
    return True


def generate_prime(bits=16):
    """
    Generate a random prime number with specified bit length.
    
    Args:
        bits: Bit length of the prime
    
    Returns:
        A random prime number
    """
    while True:
        # Generate random odd number
        n = random.randrange(2**(bits-1), 2**bits)
        if n % 2 == 0:
            n += 1
        
        if is_prime(n):
            return n


def generate_rsa_keypair(bits=16):
    """
    Generate RSA public and private key pair.
    
    Args:
        bits: Bit length for each prime (key will be 2*bits)
    
    Returns:
        Tuple ((e, n), (d, n)) representing (public_key, private_key)
    """
    # Generate two distinct primes
    p = generate_prime(bits)
    q = generate_prime(bits)
    while p == q:
        q = generate_prime(bits)
    
    # Compute n and φ(n)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    
    # Choose e (commonly 65537 if it's coprime to phi_n)
    e = 65537
    if gcd(e, phi_n) != 1:
        # Fall back to finding a suitable e
        e = 3
        while gcd(e, phi_n) != 1:
            e += 2
    
    # Compute d (modular inverse of e mod phi_n)
    d = modular_inverse(e, phi_n)
    
    public_key = (e, n)
    private_key = (d, n)
    
    return public_key, private_key


def rsa_encrypt(message, public_key):
    """
    Encrypt a message using RSA public key.
    
    Args:
        message: Integer message (must be less than n)
        public_key: Tuple (e, n)
    
    Returns:
        Encrypted message (ciphertext)
    """
    e, n = public_key
    return modular_exponentiation(message, e, n)


def rsa_decrypt(ciphertext, private_key):
    """
    Decrypt a ciphertext using RSA private key.
    
    Args:
        ciphertext: Encrypted message
        private_key: Tuple (d, n)
    
    Returns:
        Decrypted message (plaintext)
    """
    d, n = private_key
    return modular_exponentiation(ciphertext, d, n)


def text_to_number(text):
    """
    Convert text to a number for encryption.
    Simple method: concatenate ASCII values.
    
    Args:
        text: String to convert
    
    Returns:
        Integer representation
    """
    return int.from_bytes(text.encode(), 'big')


def number_to_text(number):
    """
    Convert a number back to text.
    
    Args:
        number: Integer to convert
    
    Returns:
        String representation
    """
    # Calculate byte length needed
    byte_length = (number.bit_length() + 7) // 8
    return number.to_bytes(byte_length, 'big').decode()


def demonstrate_modular_exponentiation():
    """Demonstrate the modular exponentiation algorithm."""
    print(f"\n{'=' * 60}")
    print("Modular Exponentiation Demonstration")
    print(f"{'=' * 60}")
    
    test_cases = [
        (2, 10, 1000),
        (3, 100, 7),
        (7, 256, 13),
        (123, 456, 789),
    ]
    
    for base, exp, mod in test_cases:
        result = modular_exponentiation(base, exp, mod)
        print(f"\n({base}^{exp}) mod {mod} = {result}")
        
        # Verify with Python's built-in pow (for educational purposes)
        verification = pow(base, exp, mod)
        status = "✓" if result == verification else "✗"
        print(f"  Verification: {status} (built-in pow: {verification})")


def demonstrate_rsa_basics():
    """Demonstrate basic RSA encryption and decryption."""
    print(f"\n{'=' * 60}")
    print("RSA Encryption Demonstration")
    print(f"{'=' * 60}")
    
    # Generate keys (using small primes for demonstration)
    print("\nStep 1: Generate RSA keys")
    print("-" * 60)
    public_key, private_key = generate_rsa_keypair(bits=16)
    e, n = public_key
    d, _ = private_key
    
    print(f"Public key:  (e={e}, n={n})")
    print(f"Private key: (d={d}, n={n})")
    print(f"Key size: ~{n.bit_length()} bits")
    
    # Test with numeric messages
    print("\nStep 2: Encrypt and decrypt numeric messages")
    print("-" * 60)
    
    test_messages = [42, 123, 999]
    
    for msg in test_messages:
        if msg >= n:
            print(f"\n  Message {msg} is too large (must be < {n})")
            continue
        
        # Encrypt
        ciphertext = rsa_encrypt(msg, public_key)
        
        # Decrypt
        decrypted = rsa_decrypt(ciphertext, private_key)
        
        status = "✓" if decrypted == msg else "✗"
        print(f"\n  Original:   {msg}")
        print(f"  Encrypted:  {ciphertext}")
        print(f"  Decrypted:  {decrypted} {status}")


def demonstrate_rsa_security():
    """Demonstrate why RSA is secure."""
    print(f"\n{'=' * 60}")
    print("RSA Security Principles")
    print(f"{'=' * 60}")
    
    print("\n1. One-way Function Property:")
    print("   Easy: Multiply two primes p × q = n")
    print("   Hard: Factor n back into p and q")
    
    print("\n2. Public Key Cryptography:")
    print("   • Public key (e, n) can be shared openly")
    print("   • Private key (d, n) must be kept secret")
    print("   • Knowing e and n doesn't help find d (without factoring n)")
    
    print("\n3. Key Generation Process:")
    print("   • Choose two large primes: p and q")
    print("   • Compute: n = p × q")
    print("   • Compute: φ(n) = (p-1)(q-1)")
    print("   • Choose e coprime to φ(n)")
    print("   • Compute d such that: d × e ≡ 1 (mod φ(n))")
    
    print("\n4. Encryption/Decryption:")
    print("   • Encrypt: c = m^e mod n")
    print("   • Decrypt: m = c^d mod n")
    print("   • Works because: m^(e×d) ≡ m (mod n) [Euler's Theorem]")
    
    print("\n5. Real-world Security:")
    print("   • Modern RSA uses 2048-4096 bit keys")
    print("   • Factoring such large numbers is computationally infeasible")
    print("   • Best known algorithms would take billions of years")


def compare_exponentiation_methods():
    """Compare naive vs. fast modular exponentiation."""
    print(f"\n{'=' * 60}")
    print("Algorithm Efficiency Comparison")
    print(f"{'=' * 60}")
    
    print("\nNaive Method: Compute base^exp, then take mod")
    print("  - Intermediate results can be HUGE")
    print("  - Example: 2^1000 has ~302 digits!")
    print("  - Time: O(exponent), Space: O(result size)")
    
    print("\nFast Method: Binary Exponentiation with Modulo")
    print("  - Keep results small by taking mod at each step")
    print("  - Uses squaring to reduce number of operations")
    print("  - Time: O(log exponent), Space: O(1)")
    
    base, exp, mod = 2, 1000, 1000000007
    
    print(f"\nExample: ({base}^{exp}) mod {mod}")
    result = modular_exponentiation(base, exp, mod)
    print(f"Result: {result}")
    print(f"Operations: ~{exp.bit_length()} (vs ~{exp} for naive)")


def main():
    print("=" * 60)
    print("Modular Exponentiation & RSA Demonstration")
    print("=" * 60)
    
    print("\nThis program demonstrates:")
    print("  1. Fast modular exponentiation (binary method)")
    print("  2. RSA public-key cryptography basics")
    print("  3. Why RSA is secure")
    
    # Demonstrate modular exponentiation
    demonstrate_modular_exponentiation()
    
    # Compare methods
    compare_exponentiation_methods()
    
    # Demonstrate RSA
    demonstrate_rsa_basics()
    
    # Explain security
    demonstrate_rsa_security()
    
    print(f"\n{'=' * 60}")
    print("Educational Notes")
    print(f"{'=' * 60}")
    print("\nThis is a simplified RSA implementation for education.")
    print("Production RSA requires:")
    print("  • Much larger keys (2048+ bits)")
    print("  • Proper padding schemes (OAEP)")
    print("  • Secure random number generation")
    print("  • Protection against timing attacks")
    print("  • Proper key management")
    
    print("\nFor real cryptography, use established libraries:")
    print("  • Python: cryptography, PyCryptodome")
    print("  • Never implement crypto for production yourself!")
    
    print(f"\n{'=' * 60}")


if __name__ == "__main__":
    main()
