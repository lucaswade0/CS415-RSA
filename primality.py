"""
Input:          Integers 'n' and 'k'
Outputs:        String "yes" if n is prime, "no" if composite
Relations:      Tests if integer n is prime by first checking divisibility
                by small primes, then calling primality2 for Fermat test
Pre-Conditions: n must be a positive integer, k must be positive

Pseudo-Code:

    if n equals 2, 3, 5, 7, or 11: return "yes"
    if n divisible by 3, 5, 7, or 11: return "no"
    return primality2(n, k)

"""
def primality3(n, k):
    # Handle small primes
    if n == 2 or n == 3 or n == 5 or n == 7 or n == 11:
        return "yes"

    # First test if N is divisible by 3, 5, 7, or 11
    if n % 3 == 0 or n % 5 == 0 or n % 7 == 0 or n % 11 == 0:
        return "no"

    # Call primality2 if not divisible by those numbers
    return primality2(n, k)

"""
Input:          Integers 'n' and 'k'
Outputs:        String "yes" if n passes Fermat test, "no" if composite
Relations:      Performs k iterations of Fermat primality test by choosing
                random values a and testing if a^(n-1) ≡ 1 (mod n)
Pre-Conditions: n must be greater than 2, k must be positive

Pseudo-Code:

    repeat k times:
        choose random a where 1 < a < n
        if a^(n-1) mod n != 1: return "no"
    return "yes"

"""
def primality2(n, k):
    import random

    # Repeat Fermat test k times
    for _ in range(k):
        # Choose random a where 1 < a < n
        a = random.randint(2, n - 1)

        # Test if a^(n-1) ≡ 1 (mod n)
        if pow(a, n - 1, n) != 1:
            return "no"

    return "yes"

"""
Input:          Integers 'n' and 'k'
Outputs:        An n-bit prime number
Relations:      Generates random n-bit numbers with first and last bit set
                to 1, then tests primality using primality3 until a prime
                is found
Pre-Conditions: n must be at least 2, k must be positive

Pseudo-Code:

    while True:
        generate random n-2 bit string
        create n-bit number: '1' + middle_bits + '1'
        convert to decimal
        if primality3(number, k) == "yes": return number

"""
def generate_random_prime(n, k):
    import random

    while True:
        # Generate random n-2 bit string and add 1 as first and last bit to make it odd and keep it N bit
        middle_bits = ''.join(random.choice('01') for _ in range(n - 2))
        binary_string = '1' + middle_bits + '1'

        # Convert to decimal
        number = int(binary_string, 2)

        # Test if prime using primality3
        if primality3(number, k) == "yes":
            return number