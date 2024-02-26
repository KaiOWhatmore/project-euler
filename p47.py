import utils


def prime_factors(n):
    divisor = 2
    result = set()

    while n > 1:
        while n % divisor == 0:
            result.add(divisor)
            n //= divisor
        divisor += 1
        if divisor * divisor > n:
            if n > 1:
                result.add(n)
                break
    return len(result)


def consecutive_sequence(target):
    sequence_length = 0
    n = 644
    while True:
        if prime_factors(n) == target:
            sequence_length += 1
            if sequence_length == target:
                return n - sequence_length + 1
        else:
            sequence_length = 0
        n += 1


print(consecutive_sequence(4))
# print(utils.runtime(consecutive_sequence, 4))
