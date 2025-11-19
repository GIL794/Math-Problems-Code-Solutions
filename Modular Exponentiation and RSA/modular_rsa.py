"""
Modular Exponentiation and RSA Cryptography Demo

This module demonstrates:
1. Fast modular exponentiation (computing a^b mod m efficiently)
2. Extended Euclidean algorithm for finding modular inverses
3. RSA encryption/decryption with key generation
4. Chinese Remainder Theorem optimization

Modular exponentiation is fundamental to modern cryptography, especially RSA.
"""

import random
import time


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


def extended_gcd(a, b):
    """
    Extended Euclidean algorithm.
    Finds integers x, y such that ax + by = gcd(a, b)
    
    Args:
        a, b: Two integers
    
    Returns:
        Tuple (gcd, x, y) where gcd = ax + by
    """
    if b == 0:
        return a, 1, 0
    
    gcd_val, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    
    return gcd_val, x, y


def mod_inverse(a, m):
    """
    Find the modular multiplicative inverse of a modulo m.
    Returns x such that (a * x) % m == 1
    
    Args:
        a: Number to find inverse of
        m: Modulus
    
    Returns:
        Modular inverse, or None if it doesn't exist
    """
    gcd_val, x, _ = extended_gcd(a, m)
    
    if gcd_val != 1:
        return None  # Inverse doesn't exist
    
    return x % m


def power_mod_naive(base, exp, mod):
    """
    Naive modular exponentiation: (base^exp) % mod
    Inefficient for large exponents - included for comparison.
    
    Args:
        base: Base number
        exp: Exponent
        mod: Modulus
    
    Returns:
        (base^exp) % mod
    """
    result = 1
    base = base % mod
    
    for _ in range(exp):
        result = (result * base) % mod
    
    return result


def power_mod_fast(base, exp, mod):
    """
    Fast modular exponentiation using binary exponentiation (square-and-multiply).
    Computes (base^exp) % mod efficiently in O(log exp) time.
    
    Algorithm:
    - If exp is even: a^exp = (a^(exp/2))^2
    - If exp is odd: a^exp = a * a^(exp-1)
    
    Args:
        base: Base number
        exp: Exponent
        mod: Modulus
    
    Returns:
        (base^exp) % mod
    """
    result = 1
    base = base % mod
    
    while exp > 0:
        # If exp is odd, multiply base with result
        if exp % 2 == 1:
            result = (result * base) % mod
        
        # exp must be even now
        exp = exp >> 1  # Divide exp by 2
        base = (base * base) % mod  # Square the base
    
    return result


def is_prime_miller_rabin(n, k=5):
    """
    Miller-Rabin primality test.
    Probabilistic test - if it returns False, n is definitely composite.
    If it returns True, n is probably prime with high confidence.
    
    Args:
        n: Number to test
        k: Number of rounds (higher k = more confidence)
    
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
        x = power_mod_fast(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(r - 1):
            x = power_mod_fast(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    
    return True


def generate_prime(bits):
    """
    Generate a random prime number of specified bit length.
    
    Args:
        bits: Desired bit length
    
    Returns:
        A prime number with the specified bit length
    """
    while True:
        # Generate random odd number
        num = random.getrandbits(bits)
        num |= (1 << bits - 1) | 1  # Set MSB and LSB to ensure proper bit length and odd
        
        if is_prime_miller_rabin(num):
            return num


def generate_rsa_keys(bits=16):
    """
    Generate RSA public and private keys.
    
    Args:
        bits: Bit length for each prime (n will be ~2*bits long)
    
    Returns:
        Tuple ((e, n), (d, n)) where:
        - (e, n) is the public key
        - (d, n) is the private key
    """
    # Generate two distinct primes
    p = generate_prime(bits)
    q = generate_prime(bits)
    while q == p:
        q = generate_prime(bits)
    
    n = p * q
    phi_n = (p - 1) * (q - 1)
    
    # Choose e (commonly 65537 for real RSA, but we'll choose dynamically)
    e = 65537
    if e >= phi_n or gcd(e, phi_n) != 1:
        # If 65537 doesn't work, find a suitable e
        e = 3
        while gcd(e, phi_n) != 1:
            e += 2
    
    # Calculate d (modular inverse of e)
    d = mod_inverse(e, phi_n)
    
    return ((e, n), (d, n), p, q, phi_n)


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
    return power_mod_fast(message, e, n)


def rsa_decrypt(ciphertext, private_key):
    """
    Decrypt a message using RSA private key.
    
    Args:
        ciphertext: Encrypted message
        private_key: Tuple (d, n)
    
    Returns:
        Decrypted message (plaintext)
    """
    d, n = private_key
    return power_mod_fast(ciphertext, d, n)


def rsa_decrypt_crt(ciphertext, private_key, p, q):
    """
    Decrypt using Chinese Remainder Theorem for faster computation.
    About 4x faster than standard decryption.
    
    Args:
        ciphertext: Encrypted message
        private_key: Tuple (d, n)
        p, q: Prime factors of n
    
    Returns:
        Decrypted message (plaintext)
    """
    d, n = private_key
    
    # Compute using CRT
    dp = d % (p - 1)
    dq = d % (q - 1)
    q_inv = mod_inverse(q, p)
    
    m1 = power_mod_fast(ciphertext, dp, p)
    m2 = power_mod_fast(ciphertext, dq, q)
    h = (q_inv * (m1 - m2)) % p
    m = m2 + h * q
    
    return m


def demonstrate_modular_exponentiation():
    """Demonstrate different methods of modular exponentiation."""
    print(f"\n{'=' * 70}")
    print("Modular Exponentiation: Computing (base^exp) mod m")
    print(f"{'=' * 70}")
    
    examples = [
        (2, 10, 1000),
        (3, 100, 1000),
        (7, 256, 1000),
        (123, 456, 789),
    ]
    
    print("\nExamples:")
    for base, exp, mod in examples:
        result = power_mod_fast(base, exp, mod)
        print(f"  {base}^{exp} mod {mod} = {result}")
    
    # Performance comparison
    print(f"\n{'=' * 70}")
    print("Performance Comparison: Naive vs Fast Algorithm")
    print(f"{'=' * 70}")
    
    base, exp_small, mod = 123, 100, 10000
    
    print(f"\nComputing {base}^{exp_small} mod {mod}")
    
    start = time.time()
    result_naive = power_mod_naive(base, exp_small, mod)
    time_naive = time.time() - start
    
    start = time.time()
    result_fast = power_mod_fast(base, exp_small, mod)
    time_fast = time.time() - start
    
    print(f"  Naive method: {result_naive} (Time: {time_naive*1000:.4f} ms)")
    print(f"  Fast method:  {result_fast} (Time: {time_fast*1000:.4f} ms)")
    print(f"  Speedup: {time_naive/time_fast:.1f}x")
    
    # Demonstrate with very large exponent (fast method only)
    print(f"\nComputing with large exponent (fast method only):")
    base, exp_large, mod = 2, 10000, 1000000007
    
    start = time.time()
    result = power_mod_fast(base, exp_large, mod)
    elapsed = time.time() - start
    
    print(f"  {base}^{exp_large} mod {mod} = {result}")
    print(f"  Time: {elapsed*1000:.4f} ms")
    
    print(f"\n{'=' * 70}")


def demonstrate_rsa():
    """Demonstrate RSA encryption and decryption."""
    print(f"\n{'=' * 70}")
    print("RSA Cryptography Demonstration")
    print(f"{'=' * 70}")
    
    print("\nGenerating RSA keys...")
    public_key, private_key, p, q, phi_n = generate_rsa_keys(bits=16)
    e, n = public_key
    d, _ = private_key
    
    print(f"\nKey Generation:")
    print(f"  Prime p: {p}")
    print(f"  Prime q: {q}")
    print(f"  Modulus n = p × q: {n}")
    print(f"  φ(n) = (p-1)(q-1): {phi_n}")
    print(f"  Public exponent e: {e}")
    print(f"  Private exponent d: {d}")
    print(f"  Verification: e × d mod φ(n) = {(e * d) % phi_n} (should be 1)")
    
    # Encrypt and decrypt messages
    print(f"\n{'=' * 70}")
    print("Encryption and Decryption Examples")
    print(f"{'=' * 70}")
    
    messages = [42, 1234, 9999, 12345]
    
    for msg in messages:
        if msg >= n:
            print(f"\nMessage {msg} is too large (must be < {n})")
            continue
        
        # Encrypt
        ciphertext = rsa_encrypt(msg, public_key)
        
        # Decrypt (standard)
        decrypted = rsa_decrypt(ciphertext, private_key)
        
        # Decrypt (CRT)
        decrypted_crt = rsa_decrypt_crt(ciphertext, private_key, p, q)
        
        print(f"\nMessage: {msg}")
        print(f"  Encrypted: {ciphertext}")
        print(f"  Decrypted (standard): {decrypted}")
        print(f"  Decrypted (CRT): {decrypted_crt}")
        print(f"  Verification: {'✓' if msg == decrypted == decrypted_crt else '✗'}")
    
    # Performance comparison
    print(f"\n{'=' * 70}")
    print("Decryption Performance: Standard vs CRT")
    print(f"{'=' * 70}")
    
    test_msg = 12345
    test_cipher = rsa_encrypt(test_msg, public_key)
    
    # Standard decryption
    start = time.time()
    for _ in range(100):
        rsa_decrypt(test_cipher, private_key)
    time_standard = time.time() - start
    
    # CRT decryption
    start = time.time()
    for _ in range(100):
        rsa_decrypt_crt(test_cipher, private_key, p, q)
    time_crt = time.time() - start
    
    print(f"\n100 decryptions:")
    print(f"  Standard method: {time_standard*1000:.2f} ms")
    print(f"  CRT method: {time_crt*1000:.2f} ms")
    print(f"  Speedup: {time_standard/time_crt:.2f}x")
    
    print(f"\n{'=' * 70}")


def demonstrate_security():
    """Demonstrate RSA security concepts."""
    print(f"\n{'=' * 70}")
    print("RSA Security Concepts")
    print(f"{'=' * 70}")
    
    print("\n1. Public Key Cryptography:")
    print("   - Public key (e, n) is shared openly")
    print("   - Private key (d, n) is kept secret")
    print("   - Encrypt with public key, decrypt with private key")
    print("   - Even knowing e and n, finding d requires factoring n")
    
    print("\n2. Security Based on Factoring:")
    print("   - Given n = p × q, it's hard to find p and q")
    print("   - For 2048-bit n, factoring is computationally infeasible")
    print("   - But if you know p and q, computing φ(n) is easy")
    print("   - And if you know φ(n), finding d from e is easy")
    
    print("\n3. Key Size Recommendations:")
    print("   - 1024 bits: Deprecated, can be broken")
    print("   - 2048 bits: Currently secure for most purposes")
    print("   - 3072 bits: High security applications")
    print("   - 4096 bits: Maximum security, slower performance")
    
    print("\n4. Real-World Usage:")
    print("   - SSH keys for secure remote access")
    print("   - SSL/TLS certificates for HTTPS")
    print("   - Digital signatures for authentication")
    print("   - Email encryption (PGP, S/MIME)")
    
    print(f"\n{'=' * 70}")


def demonstrate_euler_theorem():
    """Demonstrate Euler's theorem: a^φ(n) ≡ 1 (mod n) when gcd(a,n)=1."""
    print(f"\n{'=' * 70}")
    print("Euler's Theorem: a^φ(n) ≡ 1 (mod n) when gcd(a,n) = 1")
    print(f"{'=' * 70}")
    
    print("\nThis theorem is the foundation of RSA!")
    print("It ensures that (m^e)^d ≡ m (mod n)")
    
    examples = [
        (3, 10),  # φ(10) = 4
        (2, 9),   # φ(9) = 6
        (5, 14),  # φ(14) = 6
        (7, 15),  # φ(15) = 8
    ]
    
    print("\nExamples:")
    for a, n in examples:
        if gcd(a, n) != 1:
            print(f"  Skipping ({a}, {n}): gcd({a}, {n}) ≠ 1")
            continue
        
        # Calculate φ(n) using basic method
        phi_n = sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)
        
        # Verify Euler's theorem
        result = power_mod_fast(a, phi_n, n)
        
        print(f"  {a}^φ({n}) = {a}^{phi_n} ≡ {result} (mod {n}) {'✓' if result == 1 else '✗'}")
    
    print(f"\n{'=' * 70}")


def main():
    print("=" * 70)
    print("MODULAR EXPONENTIATION AND RSA CRYPTOGRAPHY")
    print("=" * 70)
    print("\nThis program demonstrates:")
    print("1. Fast modular exponentiation (square-and-multiply algorithm)")
    print("2. RSA public-key cryptography")
    print("3. Chinese Remainder Theorem optimization")
    print("4. Euler's theorem and its applications")
    print("=" * 70)
    
    # Demonstrate modular exponentiation
    demonstrate_modular_exponentiation()
    
    # Demonstrate Euler's theorem
    demonstrate_euler_theorem()
    
    # Demonstrate RSA
    demonstrate_rsa()
    
    # Security concepts
    demonstrate_security()
    
    print("\n" + "=" * 70)
    print("Mathematical Foundations:")
    print("- Modular exponentiation: O(log n) using binary method")
    print("- RSA security: Based on difficulty of integer factorization")
    print("- Euler's theorem: Guarantees correct encryption/decryption")
    print("- Extended Euclidean algorithm: Finds modular inverses")
    print("=" * 70)


if __name__ == "__main__":
    main()
