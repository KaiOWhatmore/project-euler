import utils

one_mil = 1_000_000


def is_circular_n_prime(prime, primes):
    prime_str = str(prime)
    for i in range(len(prime_str)):
        if int(prime_str[i:] + prime_str[:i]) not in primes:
            return False
    return True


def circular_primes_opt(num):
    primes = utils.sieve_of_eratosthenes_s(num)
    count = 0
    for prime in primes:
        if is_circular_n_prime(prime, primes):
            count += 1
    return count


print(utils.runtime(circular_primes_opt, one_mil))


def circular_indices_n(num):
    num_str = str(num)
    length = len(num_str)
    for i in range(length):
        num = ''
        for j in range(length):
            rotated_i = (j + i) % length
            num += num_str[rotated_i]
        yield int(num)


def is_circular_primes_all_prime(circular_primes, primes):
    for prime in circular_primes:
        if prime not in primes:
            return False
    return True


def circular_primes(num):
    primes = utils.sieve_of_eratosthenes_s(num)
    count = 0
    for prime in primes:
        prime_rotations = circular_indices_n(str(prime))
        if is_circular_primes_all_prime(prime_rotations, primes):
            count += 1
    return count


print(utils.runtime(circular_primes, one_mil))


def circular_indices_l(num):
    num_str = str(num)
    for i in range(len(num_str)):
        indices = []
        for j in range(len(num_str)):
            indices.append((j + i) % len(num_str))
        yield int(''.join(num_str[i] for i in indices))
