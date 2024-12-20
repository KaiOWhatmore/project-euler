import utils

big_num = 1_000_000 * 2


def prime_opt(num):
    return [n for n in range(num) if utils.is_prime_opt(n)]


def prime(num):
    return [n for n in range(num) if utils.is_prime(n)]


print(prime(big_num))
print(prime_opt(big_num))
cProfile.run('goldbachs_conjecture()', 'p46_output_file.prof')
