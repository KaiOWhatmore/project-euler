"""
odd_comp = prime + 2 * perf_square
odd_comp - prime // 2 = perf_square
if not is_perf_square(odd_comp - prime // 2) => return
"""
import math

import utils


def is_conjecture(num):
    primes = set()
    for n in range(1, math.isqrt(num)):
        potential_prime = num - 2 * n * n
        if potential_prime in primes:
            return True
        if utils.is_prime(potential_prime):
            primes.add(potential_prime)
            return True
    return False


def goldbachs_conjecture():
    n = 9
    while True:
        if n % 2 == 0:
            n += 1
            continue
        if utils.is_prime(n):
            n += 1
            continue
        if not is_conjecture(n):
            return n
        n += 1


print(goldbachs_conjecture())
