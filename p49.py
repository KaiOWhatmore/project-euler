import collections

import utils


def sieve(num):
    primes = [False, False] + [True] * (num - 2)
    all_primes = [2]

    for n in range(3, num, 2):
        if primes[n]:
            all_primes.append(n)
            for i in range(n * n, num, 2 * n):
                primes[i] = False

    result = [prime for prime in all_primes if prime > 1000]

    return result


def prime_permutations():
    primes_less_than_10000 = sieve(10000)
    grouped_primes = collections.defaultdict(list)
    for prime in primes_less_than_10000:
        hashed_prime = ''.join(sorted(str(prime)))
        grouped_primes[hashed_prime].append(prime)

    count = 0
    for hashed_prime, primes in grouped_primes.items():
        for i, prime in enumerate(primes[:-1]):
            for next_prime in primes[i + 1:]:
                diff = next_prime - prime
                if next_prime + diff in primes:
                    count += 1
                    if count > 1:
                        return f"Sequence is: {prime}{next_prime}{next_prime + diff}"


print(prime_permutations())  # 296962999629
utils.runtime(prime_permutations)
