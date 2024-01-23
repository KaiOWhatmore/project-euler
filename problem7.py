import utils

LIMIT = 10001


def find_prime_limit(limit):
    count = 0
    i = 2
    while True:
        if utils.is_prime(i):
            count += 1
        if count == LIMIT:
            return i
        i += 1


print(utils.sieve_of_eratosthenes(150000)[LIMIT - 1] == find_prime_limit(LIMIT))
