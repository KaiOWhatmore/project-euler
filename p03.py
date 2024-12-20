import math

import utils

"""
Largest Prime Factor
"""


# N = 600851475143


def largest_prime_factor(N):
    ceil = math.isqrt(N)
    for n in range(ceil, 2, -1):
        if N % n == 0 and utils.is_prime(n):
            return n

# print(largest_prime_factor(N)) #6857
