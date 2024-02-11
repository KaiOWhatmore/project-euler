import utils


def find_unit_fraction(divisor):
    n = 10
    res = ''
    remainders = {}
    while n:
        q = n // divisor
        res += str(q)
        r = n % divisor * 10
        n = r
        if r in remainders:
            start_pos = remainders[r]
            return res[start_pos:]
        else:
            remainders[r] = len(res)
    return res


def reciprocal_cycles(d):
    result = 0
    max_int = 0
    for i in range(1, d):
        cycle_length = len(find_unit_fraction(i))
        if cycle_length > result:
            result = cycle_length
            max_int = i
    return f"number for longest recurring cycle: {max_int}\nrecurring cycle length: {result}"


def rep_cyc(primes):
    res, max_i = 0, 0
    for prime in primes:
        cyc_len = len(find_unit_fraction(prime))
        if cyc_len > res:
            res = cyc_len
            max_i = prime
    return f"number for longest recurring cycle: {max_i}\nrecurring cycle length: {res}"


print(reciprocal_cycles(1000))

primes = utils.sieve_of_eratosthenes(1000)
print(rep_cyc(primes))
