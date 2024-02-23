import utils


def is_pandigital(end, num):
    return set(str(num)) == set(''.join(str(n) for n in range(1, end + 1)))


limit = 8_000_000


# 7_652_413


def pandigital_prime(limit):
    primes = utils.sieve_of_eratosthenes_opt_s(limit)
    result = 0
    for prime in primes:
        if is_pandigital(len(str(prime)), prime):
            if prime > result:
                result = prime
    return result


print(utils.runtime(pandigital_prime, limit))
print(pandigital_prime(limit))
