"""
Elliptic Curve Cryptography (ECC)

A comprehensive implementation of elliptic curve operations and cryptographic
protocols including ECDSA (digital signatures) and ECDH (key exchange).

Demonstrates the mathematics behind modern secure communications used in
Bitcoin, TLS/SSL, and messaging apps.
"""

import hashlib
import secrets
from typing import Optional, Tuple


class Point:
    """
    Represents a point on an elliptic curve.
    
    The special point at infinity is represented with x=None, y=None.
    """
    
    def __init__(self, x: Optional[int], y: Optional[int]):
        self.x = x
        self.y = y
    
    def is_infinity(self) -> bool:
        """Check if this is the point at infinity (identity element)."""
        return self.x is None and self.y is None
    
    def __eq__(self, other) -> bool:
        """Points are equal if coordinates match."""
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y
    
    def __repr__(self) -> str:
        """String representation of the point."""
        if self.is_infinity():
            return "Point(∞)"
        return f"Point({self.x}, {self.y})"


class EllipticCurve:
    """
    Elliptic curve over finite field Fp defined by y² = x³ + ax + b (mod p).
    
    Implements group operations: point addition and scalar multiplication.
    """
    
    def __init__(self, a: int, b: int, p: int):
        """
        Initialize an elliptic curve.
        
        Args:
            a: Coefficient a in y² = x³ + ax + b
            b: Coefficient b in y² = x³ + ax + b
            p: Prime defining the finite field Fp
        """
        self.a = a
        self.b = b
        self.p = p
        
        # Verify curve is non-singular: 4a³ + 27b² ≠ 0 (mod p)
        discriminant = (4 * a**3 + 27 * b**2) % p
        if discriminant == 0:
            raise ValueError("Curve is singular (discriminant = 0)")
    
    def is_on_curve(self, point: Point) -> bool:
        """
        Check if a point lies on the curve.
        
        Args:
            point: Point to check
        
        Returns:
            True if point is on curve or is point at infinity
        """
        if point.is_infinity():
            return True
        
        # Check y² ≡ x³ + ax + b (mod p)
        left = (point.y ** 2) % self.p
        right = (point.x ** 3 + self.a * point.x + self.b) % self.p
        return left == right
    
    def add(self, P: Point, Q: Point) -> Point:
        """
        Add two points on the elliptic curve: P + Q.
        
        Uses geometric interpretation: draw line through P and Q,
        find third intersection with curve, reflect over x-axis.
        
        Args:
            P: First point
            Q: Second point
        
        Returns:
            Sum P + Q
        """
        # Validate points are on curve
        if not self.is_on_curve(P) or not self.is_on_curve(Q):
            raise ValueError("Points must be on the curve")
        
        # Identity: P + O = P
        if P.is_infinity():
            return Q
        if Q.is_infinity():
            return P
        
        # Inverse: P + (-P) = O
        if P.x == Q.x and (P.y + Q.y) % self.p == 0:
            return Point(None, None)  # Point at infinity
        
        # Compute slope λ
        if P == Q:
            # Point doubling: λ = (3x₁² + a) / (2y₁)
            numerator = (3 * P.x ** 2 + self.a) % self.p
            denominator = (2 * P.y) % self.p
        else:
            # Point addition: λ = (y₂ - y₁) / (x₂ - x₁)
            numerator = (Q.y - P.y) % self.p
            denominator = (Q.x - P.x) % self.p
        
        # Compute modular inverse using Fermat's little theorem: a⁻¹ ≡ a^(p-2) (mod p)
        denominator_inv = pow(denominator, self.p - 2, self.p)
        slope = (numerator * denominator_inv) % self.p
        
        # Compute new point coordinates
        x3 = (slope ** 2 - P.x - Q.x) % self.p
        y3 = (slope * (P.x - x3) - P.y) % self.p
        
        return Point(x3, y3)
    
    def double(self, P: Point) -> Point:
        """
        Double a point: 2P = P + P.
        
        Optimized version of add(P, P).
        
        Args:
            P: Point to double
        
        Returns:
            Point 2P
        """
        return self.add(P, P)
    
    def scalar_multiply(self, k: int, P: Point) -> Point:
        """
        Scalar multiplication: kP = P + P + ... + P (k times).
        
        Uses double-and-add algorithm for O(log k) efficiency:
        - Binary representation of k
        - Double for each bit, add if bit is 1
        
        This is the fundamental operation in ECC and must be fast.
        
        Args:
            k: Scalar (integer)
            P: Point to multiply
        
        Returns:
            Point kP
        """
        if k == 0:
            return Point(None, None)  # 0P = O
        
        if k < 0:
            # Handle negative scalars: (-k)P = k(-P)
            k = -k
            P = Point(P.x, (-P.y) % self.p)
        
        # Double-and-add algorithm
        result = Point(None, None)  # Start with point at infinity
        addend = P
        
        while k:
            if k & 1:  # If bit is 1, add current power of P
                result = self.add(result, addend)
            addend = self.double(addend)  # Double for next bit
            k >>= 1  # Move to next bit
        
        return result
    
    def __repr__(self) -> str:
        """String representation of the curve."""
        return f"EllipticCurve(y² = x³ + {self.a}x + {self.b} mod {self.p})"


class ECDSA:
    """
    Elliptic Curve Digital Signature Algorithm.
    
    Allows signing messages and verifying signatures using ECC.
    """
    
    def __init__(self, curve: EllipticCurve, G: Point, n: int):
        """
        Initialize ECDSA with curve parameters.
        
        Args:
            curve: Elliptic curve
            G: Generator point (base point)
            n: Order of generator G (number of points in group)
        """
        self.curve = curve
        self.G = G
        self.n = n
    
    def generate_keypair(self) -> Tuple[int, Point]:
        """
        Generate a public/private keypair.
        
        Returns:
            (private_key, public_key) where:
            - private_key: Random integer in [1, n-1]
            - public_key: Point dG where d is private key
        """
        # Private key: random integer
        private_key = secrets.randbelow(self.n - 1) + 1
        
        # Public key: scalar multiplication
        public_key = self.curve.scalar_multiply(private_key, self.G)
        
        return private_key, public_key
    
    def sign(self, message: bytes, private_key: int) -> Tuple[int, int]:
        """
        Sign a message using private key.
        
        Returns signature (r, s) where:
        - r: x-coordinate of kG (mod n)
        - s: k⁻¹(hash(m) + rd) (mod n)
        
        Args:
            message: Message to sign
            private_key: Private key (integer)
        
        Returns:
            Signature (r, s)
        """
        # Hash the message
        message_hash = int.from_bytes(
            hashlib.sha256(message).digest(), 
            byteorder='big'
        )
        
        # Generate signature
        while True:
            # Random nonce k (CRITICAL: must be random and unique!)
            k = secrets.randbelow(self.n - 1) + 1
            
            # Compute kG
            kG = self.curve.scalar_multiply(k, self.G)
            r = kG.x % self.n
            
            if r == 0:
                continue  # Try again with different k
            
            # Compute s = k⁻¹(H(m) + rd) mod n
            k_inv = pow(k, -1, self.n)  # Modular inverse
            s = (k_inv * (message_hash + private_key * r)) % self.n
            
            if s == 0:
                continue  # Try again with different k
            
            return (r, s)
    
    def verify(self, message: bytes, signature: Tuple[int, int], 
               public_key: Point) -> bool:
        """
        Verify a signature using public key.
        
        Verifies that signature (r, s) is valid for message.
        
        Args:
            message: Original message
            signature: Signature (r, s)
            public_key: Public key (point)
        
        Returns:
            True if signature is valid, False otherwise
        """
        r, s = signature
        
        # Validate signature parameters
        if not (1 <= r < self.n and 1 <= s < self.n):
            return False
        
        # Hash the message
        message_hash = int.from_bytes(
            hashlib.sha256(message).digest(),
            byteorder='big'
        )
        
        # Compute verification values
        s_inv = pow(s, -1, self.n)  # Modular inverse of s
        u1 = (message_hash * s_inv) % self.n
        u2 = (r * s_inv) % self.n
        
        # Compute point P = u1*G + u2*Q
        point1 = self.curve.scalar_multiply(u1, self.G)
        point2 = self.curve.scalar_multiply(u2, public_key)
        P = self.curve.add(point1, point2)
        
        if P.is_infinity():
            return False
        
        # Signature is valid if r ≡ P.x (mod n)
        return r == (P.x % self.n)


def ecdh_key_exchange(curve: EllipticCurve, G: Point, 
                       alice_private: int, bob_private: int) -> Tuple[Point, Point]:
    """
    Elliptic Curve Diffie-Hellman key exchange.
    
    Alice and Bob establish a shared secret without transmitting it.
    
    Args:
        curve: Elliptic curve
        G: Generator point
        alice_private: Alice's private key
        bob_private: Bob's private key
    
    Returns:
        (alice_shared, bob_shared) - both should be equal
    """
    # Alice computes her public key: A = aG
    alice_public = curve.scalar_multiply(alice_private, G)
    
    # Bob computes his public key: B = bG
    bob_public = curve.scalar_multiply(bob_private, G)
    
    # Alice computes shared secret: S = aB = a(bG) = abG
    alice_shared = curve.scalar_multiply(alice_private, bob_public)
    
    # Bob computes shared secret: S = bA = b(aG) = abG
    bob_shared = curve.scalar_multiply(bob_private, alice_public)
    
    # Both should compute the same point!
    return alice_shared, bob_shared


def get_secp256k1():
    """
    Get secp256k1 curve parameters (Bitcoin's curve).
    
    Returns:
        (curve, G, n) tuple
    """
    # Curve parameters
    p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
    a = 0
    b = 7
    
    # Generator point G
    Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
    Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
    G = Point(Gx, Gy)
    
    # Order of G
    n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
    
    curve = EllipticCurve(a, b, p)
    
    return curve, G, n


def main():
    """Demonstrate elliptic curve cryptography."""
    
    print("=" * 70)
    print("Elliptic Curve Cryptography (ECC)")
    print("=" * 70)
    print("\nThe mathematics behind Bitcoin, TLS, and secure messaging!")
    
    # Demo with simple curve first
    print("\n" + "=" * 70)
    print("Demo: Simple Toy Curve (for illustration)")
    print("=" * 70)
    
    # Small toy curve: y² = x³ + 2x + 3 (mod 97)
    toy_curve = EllipticCurve(a=2, b=3, p=97)
    print(f"\nCurve: y² = x³ + 2x + 3 (mod 97)")
    
    # Example points
    P = Point(3, 6)
    Q = Point(80, 10)
    
    print(f"\nP = {P}")
    print(f"Q = {Q}")
    print(f"P on curve: {toy_curve.is_on_curve(P)}")
    print(f"Q on curve: {toy_curve.is_on_curve(Q)}")
    
    # Point addition
    R = toy_curve.add(P, Q)
    print(f"\nP + Q = {R}")
    print(f"(P + Q) on curve: {toy_curve.is_on_curve(R)}")
    
    # Point doubling
    P2 = toy_curve.double(P)
    print(f"\n2P = {P2}")
    
    # Scalar multiplication
    P5 = toy_curve.scalar_multiply(5, P)
    print(f"5P = {P5}")
    
    # Real-world curve: secp256k1 (Bitcoin)
    print("\n" + "=" * 70)
    print("Bitcoin's Curve: secp256k1")
    print("=" * 70)
    
    curve, G, n = get_secp256k1()
    
    print(f"\nCurve: y² = x³ + 7 (mod p)")
    print(f"Field size p: {curve.p}")
    print(f"(This is a 256-bit prime!)")
    print(f"\nGenerator order n: {n}")
    print(f"(There are n points in the group)")
    
    # ECDSA Demonstration
    print("\n" + "=" * 70)
    print("ECDSA Digital Signatures")
    print("=" * 70)
    
    ecdsa = ECDSA(curve, G, n)
    
    # Generate keypair
    print("\nGenerating keypair...")
    private_key, public_key = ecdsa.generate_keypair()
    
    print(f"Private key: {hex(private_key)[:20]}... (kept secret)")
    print(f"Public key: ({hex(public_key.x)[:20]}..., {hex(public_key.y)[:20]}...)")
    
    # Sign a message
    message = b"Transfer 1 BTC to Alice"
    print(f"\nMessage: {message.decode()}")
    
    print("Signing message...")
    signature = ecdsa.sign(message, private_key)
    r, s = signature
    
    print(f"Signature (r, s):")
    print(f"  r = {hex(r)[:40]}...")
    print(f"  s = {hex(s)[:40]}...")
    
    # Verify signature
    print("\nVerifying signature...")
    is_valid = ecdsa.verify(message, signature, public_key)
    print(f"Signature valid: {is_valid} ✓")
    
    # Try with wrong message
    wrong_message = b"Transfer 100 BTC to Alice"
    is_valid_wrong = ecdsa.verify(wrong_message, signature, public_key)
    print(f"Wrong message: {is_valid_wrong} ✗ (correctly rejected)")
    
    # ECDH Key Exchange
    print("\n" + "=" * 70)
    print("ECDH Key Exchange")
    print("=" * 70)
    
    print("\nAlice and Bob establish shared secret without transmitting it!")
    
    # Generate private keys
    alice_private = secrets.randbelow(n - 1) + 1
    bob_private = secrets.randbelow(n - 1) + 1
    
    print(f"\nAlice's private key: {hex(alice_private)[:20]}... (secret)")
    print(f"Bob's private key: {hex(bob_private)[:20]}... (secret)")
    
    # Perform key exchange
    alice_shared, bob_shared = ecdh_key_exchange(curve, G, alice_private, bob_private)
    
    print(f"\nAlice computes shared secret: ({hex(alice_shared.x)[:20]}..., ...)")
    print(f"Bob computes shared secret:   ({hex(bob_shared.x)[:20]}..., ...)")
    
    print(f"\nShared secrets match: {alice_shared == bob_shared} ✓")
    print("Both can now use this shared point for symmetric encryption!")
    
    # Security demonstration
    print("\n" + "=" * 70)
    print("Why ECC is Secure: The Discrete Logarithm Problem")
    print("=" * 70)
    
    print("\nGiven: P (generator) and Q = kP (public key)")
    print("Find: k (private key)")
    print("\nFor 256-bit curves, this requires ~2¹²⁸ operations")
    print("That's: 340,282,366,920,938,463,463,374,607,431,768,211,456 operations")
    print("\nEven with all computers on Earth, this would take billions of years!")
    
    print("\n" + "=" * 70)
    print("ECC in the Real World")
    print("=" * 70)
    print("\n✓ Bitcoin/Cryptocurrency: All transactions use ECDSA")
    print("✓ TLS/HTTPS: Most websites use ECDHE for key exchange")
    print("✓ Signal/WhatsApp: End-to-end encryption uses Curve25519")
    print("✓ SSH: Modern key pairs use Ed25519 (EdDSA)")
    print("✓ IoT Devices: Smaller keys fit in constrained memory")
    
    print("\n" + "=" * 70)
    print("Key Sizes Comparison (for 128-bit security)")
    print("=" * 70)
    print(f"\nECC:  256 bits")
    print(f"RSA: 3072 bits (12x larger!)")
    print(f"\nECC is more efficient in every way: faster, smaller, less power")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()
