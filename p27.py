"""
f(n) = n**2 + a*n + b
f'(n) = 2*n + a = 0
    ... max value of a = -2n ?

f(n) = n**2 + -2n**2 + b will produe the largest prime number for a
"""
import utils

"""
b must be a prime number as f(0) = prime 
"""
b_canditates = utils.sieve_of_eratosthenes(1000)


def quadratic_primes(limit_a):
    max_val = 0
    max_a, max_b = 0, 0
    for b in b_canditates:
        for a in range(-limit_a + 1, limit_a):
            n = 0
            while utils.is_prime(n * n + a * n + b):
                n += 1
            if n > max_val:
                max_val = n
                max_a, max_b = a, b
    return max_a * max_b

# print(quadratic_primes(1000)) -59231
