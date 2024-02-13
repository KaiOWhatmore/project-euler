import utils

LIMIT = 2_000_000
primes_below_2000_000 = utils.sieve_of_eratosthenes_l(LIMIT)
print(sum(primes_below_2000_000)) # 142913828922