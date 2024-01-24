"""
perfect number: n==return_proper_divisors_sum(n)
deficient number: n > return_proper_divisors_sum(n)
abundant number: n < return_proper_divisors_sum(n)

smallest abundant number: sam=12
smallest composite abundant number: scam=24
    scam = 2*12

if n > 28123 then:
    (n+1) ... (n + k) = (an1 + an2)

∑ (12 + n + ... + 28123)
where n != (an1 + an2)

strategy:
1. find all abundant numbers < 28123
2. filter all numbers which are composites of an abundant_number. i.e:
    non_composite_abundant_numbers[i % abundant_number == 0] == False
3. filter all numbers which can

3. find all non composite abundant numbers
nums = [True] * 28123

   non_composite_abundant_numbers = []
   for i in range(12, 28123) do
    if nums[i]:
        non_composite_abundant_numbers.append(i)
        for j in range(i, 28123, i) do
            nums[j] = False
    return non_composite_abundant_numbers
"""
import time

import utils

CIEL = 28123


def is_abundant_number(n):
    return utils.return_proper_divisors_sum(n) > n


def return_abundant_numbers(ciel):
    return [n for n in range(1, ciel + 1) if is_abundant_number(n)]


def return_sum_non_two_sum_abundant_nums(nums, abundant_numbers, ciel):
    result = 0
    for i in abundant_numbers:
        for j in abundant_numbers:
            if i + j <= ciel:
                nums[i + j] = False

    for i in range(len(nums)):
        if nums[i]:
            result += i

    return result


start_time = time.time()

nums = [True] * (CIEL + 1)
abundant_numbers = return_abundant_numbers(CIEL)

ANSWER = 4179871
tmp_answer = return_sum_non_two_sum_abundant_nums(nums, abundant_numbers, CIEL)
print(f"{tmp_answer}")
print(f"total-time: {time.time() - start_time}")
# print(tmp_answer == ANSWER)
