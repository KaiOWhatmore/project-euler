import math


def return_proper_divisors_sum(num):
    proper_divisors = set()
    proper_divisors.add(1)
    for n in range(2, math.isqrt(num)):
        if num % n == 0:
            proper_divisors.add(n)
            proper_divisors.add(num // n)
    return sum(proper_divisors)


def amicable_numbers(num):
    divisor_sums = {}
    result = 0
    for n in range(1, num + 1):
        proper_divisor_sum = return_proper_divisors_sum(n)
        if proper_divisor_sum in divisor_sums:
            continue
        if n == return_proper_divisors_sum(
                proper_divisor_sum) and n != proper_divisor_sum:
            divisor_sums[n] = proper_divisor_sum
            result += n + proper_divisor_sum
    return result


def amicable_numbers2(limit):
    """
    Calculate the sum of all the amicable numbers under a given limit. GPT-4
    """
    divisor_sums = {}
    result = 0
    for n in range(1, limit + 1):
        if n not in divisor_sums:
            divisor_sums[n] = return_proper_divisors_sum(n)
        sum_n = divisor_sums[n]

        if sum_n not in divisor_sums:
            divisor_sums[sum_n] = return_proper_divisors_sum(sum_n)

        if n != sum_n and divisor_sums[sum_n] == n:
            result += n
    return result

# print(amicable_numbers(10000)) 31626
# print(amicable_numbers(10000))
