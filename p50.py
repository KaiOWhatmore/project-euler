import utils

limit = 1000_000


def consecutive_prime_sum(limit):
    primes = utils.sieve_of_eratosthenes_l(limit)
    primes_set = set(primes)
    max_prime = 0
    result = 0
    for i in range(len(primes)):
        total = primes[i]
        j = i + 1
        while total < limit and j < len(primes):
            if total in primes_set and j - i > result:
                result = j - i
                max_prime = total
            total += primes[j]
            j += 1

    return max_prime


print(consecutive_prime_sum(limit))
