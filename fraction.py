"""
Input:          Integers 'a' and 'b'
Outputs:        An integer value that is the Greatest Common Divisor
Relations:      The function uses integers 'a' and 'b' to find the
                greatest common divisor between the two and returns
                it
Pre-Conditions: 'a' and 'b' must be integers

Psuedo-Code:
(psuedo code obtained from your slides <euclidean algorithm>)

function Euclid(a, b)
    if b = 0: return a
    return Euclid(b, mod a)

"""

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


"""
Input:          Integers 'p' and 'q'
Outputs:        Returns the numerator and denomiator 'p' and 'q'
                such that they are reduced
Relations:      This function reduces the numerator and denominator
                (p, q) and returns its result to the caller in the
                form (p, q)
Pre-Conditions: 'q' cannot equal zero as dividing by zero is unde-
                 fined behaviour

Psuedo-Code:

    assert q != 0
    if q < 0
        (p,q) = -(p,q)
    calculate gcd of (p, q)
    return (p,q)//gcd

"""
def reduce_fraction(p, q):
    if q == 0:
        raise ZeroDivisionError("Denominator cannot be zero.")
    if q < 0:
        p, q = -p, -q
    g = gcd(p, q)
    return p // g, q // g


"""
Input:          Integers 'p1','q1','p2' and 'q2'
Outputs:        Integers 'num'erator and 'den'onomiator of the added fractions 
Relations:      The input integers resemble the numerator and denomiator of
                two fractions, 1 and 2. They are then added together to form
                the result of just one fraction
Pre-Conditions: p1, q1, p2, q2 must all be integers

Psuedo-Code:
(multiply the numerators by opposing denominator to addition work for two
 possibly different denomator fractions and then return them reduced)

    numerator = p1*q2 + p2*q1
    denomiator = q1*q2
    return reduced_fraction(numerator, denomiator)

"""
# p1 = numerator of first fraction, q1 denominator of first fraction
# p2 = numerator of second fraction, q2 denominator of second fraction
def add_frac(p1, q1, p2, q2):
    num = p1 * q2 + p2 * q1
    den = q1 * q2
    return reduce_fraction(num, den)


"""
Input:          Integers p, q, n where (p, q) is a fraction and
                'n' is the digit place after the decimal we are
                searching for
Outputs:        It will output the digit that is found in the
                n'th place after the decimal
Relations:      This function uses a fraction (p,q) and searches
                for the n'th digit after the decimal after put-
                ting the fraction in decimal form
Pre-Conditions: n must be a positive integer

Psuedo-Code:

    assert n > 0
    reduce_fraction of (p,q)
    remainder is absolute_value(p) mod q
    digit is 0

    repeat n times
        remainder is remainder * 10
        digit is integer division of remainder by q
        remainder is remainder mod q

    return digit
"""
def digit_of_fraction(p, q, n):
    if n <= 0:
        raise ValueError("n must be positive.")
    
    p, q = reduce_fraction(p, q)
    remainder = abs(p) % q
    digit = 0
    for _ in range(n):
        remainder *= 10
        digit = remainder // q
        remainder %= q
    return digit


"""
Input:          Integers 'm' and 'n'
Outputs:        Returns the n'th digit after the decimal
                that is calculated in the digit_of_fraction
                function
Relations:      Uses the hsum algorithm to calculate the
                n'th digit harmonic number of 'm' and
                return the found value
Pre-Conditions: 'n' and 'm' are integers greater than or
                equal to 0

Psuedo-Code:

    assert n and m > 0
    numerator is 0
    denominator is 1

    repeat n times
        num, den is add(curr num, den to next 1/j)
    (function call to digit_of_fraction)
    find the n'th digit and return

"""
def hsum(n, m):
    if n <= 0 or m <= 0:
        raise ValueError("Error(hsum): 'n' and 'm' must be positive.")

    num, den = 0, 1
    for j in range(1, n + 1):
        num, den = add_frac(num, den, 1, j)

    return digit_of_fraction(num, den, m)
