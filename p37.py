import utils


def r_l_is_prime(num, primes):
    divisor = 10
    truncated_num = num % divisor
    while truncated_num != num:
        if truncated_num not in primes:
            return False
        divisor *= 10
        truncated_num = num % divisor
    return True


def l_r_is_prime(num, primes):
    divisor = 10
    truncated_num = num // divisor
    while truncated_num:
        if truncated_num not in primes:
            return False
        divisor *= 10
        truncated_num = num // divisor
    return True


def truncatable_primes(limit):
    primes = utils.sieve_of_eratosthenes_s(limit)
    result = 0
    for prime in primes:
        if l_r_is_prime(prime, primes) and r_l_is_prime(prime, primes):
            result += prime
    return result - 17


one_mil = 1_000_000
limit = 750_000
print(truncatable_primes(limit))
