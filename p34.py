import utils

factorial_nums = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880}


def get_digits(num):
    while num:
        r = num % 10
        yield r
        num //= 10


def digits_factorial_sum(num):
    return sum(factorial_nums[n] for n in get_digits(num))


def digit_factorials(limit):
    return sum(n for n in range(10, utils.factorial_i(limit)) if n == digits_factorial_sum(n))


print(digit_factorials(9)) # 40730
