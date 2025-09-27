from primality import generate_random_prime
from fraction import gcd
import random

"""
Input:          Integers 'n' and 'k'
Outputs:        Returns five integers: p, q, N, E, D (RSA key components)
Relations:      Generates RSA encryption/decryption keys by creating two
                n-bit primes, computing N=p*q, finding encryption key E,
                and computing decryption key D using extended Euclidean algorithm
Pre-Conditions: n must be positive integer >= 2, k must be positive

Pseudo-Code:

    p = generate_random_prime(n, k)
    q = generate_random_prime(n, k)
    N = p * q
    phi = (p-1) * (q-1)
    find random 10-bit E where gcd(E, phi) = 1
    find D where DE congruent 1 (mod phi)
    return p, q, N, E, D

"""
def generate_rsa_keys(n, k):
    # Step 1: Generate two n-bit primes p and q
    p = generate_random_prime(n, k)
    q = generate_random_prime(n, k)

    # Step 2: Compute N = p * q
    N = p * q

    # Step 3: Find random 10-bit E where gcd(E, (p-1)(q-1)) = 1
    phi = (p - 1) * (q - 1)
    while True:
        E = random.randint(2**9, 2**10 - 1)  # 10-bit number
        if gcd(E, phi) == 1:
            break

    # Step 4: Find D using extended Euclidean algorithm where DE congruent 1 (mod phi)
    g, x, y = extended_gcd(E, phi)
    D = x if x >= 0 else x + phi
    
    if D < 0:
        D += phi

    return p, q, N, E, D

"""
Input:          Integers 'a' and 'b'
Outputs:        Returns tuple (gcd, x, y) where gcd is greatest common divisor
                and x, y satisfy ax + by = gcd
Relations:      Uses extended Euclidean algorithm to find coefficients x and y
                such that ax + by = gcd(a, b)
Pre-Conditions: a and b must be integers

Pseudo-Code:

    if a = 0: return (b, 0, 1)
    recursively call extended_gcd(b mod a, a)
    compute x and y from recursive result
    return (gcd, x, y)

"""
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1

    gcd_val, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1

    return gcd_val, x, y

"""
Input:          Integers 'M', 'E', and 'N'
Outputs:        Integer ciphertext
Relations:      Encrypts message M using RSA public key (E, N)
                by computing M^E mod N
Pre-Conditions: M must be less than N, E and N must be positive

Pseudo-Code:

    return M^E mod N

"""
def rsa_encrypt(M, E, N):
    # RSA encryption: ciphertext = M^E mod N
    return pow(M, E, N)

"""
Input:          Integers 'ciphertext', 'D', and 'N'
Outputs:        Integer plaintext
Relations:      Decrypts ciphertext using RSA private key (D, N)
                by computing ciphertext^D mod N
Pre-Conditions: ciphertext must be less than N, D and N must be positive

Pseudo-Code:

    return ciphertext^D mod N

"""
def rsa_decrypt(ciphertext, D, N):
    # RSA decryption: plaintext = ciphertext^D mod N
    return pow(ciphertext, D, N)

"""
Input:          Integers 'M', 'N', 'E', and 'D'
Outputs:        Tuple (encrypted, decrypted, match_result)
Relations:      Encrypts message M, then decrypts it, and checks if
                the result matches the original message
Pre-Conditions: M < N, all parameters must be positive integers

Pseudo-Code:

    encrypted = rsa_encrypt(M, E, N)
    decrypted = rsa_decrypt(encrypted, D, N)
    match = "yes" if decrypted == M else "no"
    print results
    return (encrypted, decrypted, match)

"""
def rsa_encrypt_decrypt_test(M, N, E, D):

    encrypted = rsa_encrypt(M, E, N)


    decrypted = rsa_decrypt(encrypted, D, N)

    match = "yes" if decrypted == M else "no"

    print(f"Original message: {M}")
    print(f"Encrypted message: {encrypted}")
    print(f"Decrypted message: {decrypted}")
    print(f"Match: {match}")

    return encrypted, decrypted, match