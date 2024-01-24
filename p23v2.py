import math
import time

# Constants
CIEL = 28123


# Function to return sum of proper divisors
def return_proper_divisors_sum(num):
    proper_divisors = set()
    proper_divisors.add(1)
    for n in range(2, math.isqrt(num) + 1):
        if num % n == 0:
            proper_divisors.add(n)
            proper_divisors.add(num // n)
    return sum(proper_divisors)


# Function to precompute abundant numbers
def precompute_abundant_numbers(ciel):
    return [n for n in range(1, ciel + 1) if return_proper_divisors_sum(n) > n]


# Main function to solve the problem
def return_sum_non_two_sum_abundant_nums(ciel):
    abundant_numbers = precompute_abundant_numbers(ciel)
    sum_set = set()

    # Generate set of all possible sums of two abundant numbers
    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            sum_abundant = abundant_numbers[i] + abundant_numbers[j]
            if sum_abundant <= ciel:
                sum_set.add(sum_abundant)

    # Calculate the sum of all numbers not in sum_set
    result = sum(n for n in range(1, ciel + 1) if n not in sum_set)

    return result


# Call the main function
ANSWER = 4179871
start_time = time.time()
print(return_sum_non_two_sum_abundant_nums(CIEL) == ANSWER)
print(f"total_time:{time.time()}")
