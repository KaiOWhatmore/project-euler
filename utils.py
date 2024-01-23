import math


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True


def sieve_of_eratosthenes(limit):
    nums = [True] * limit
    primes = []
    for i in range(2, limit):
        if nums[i]:
            primes.append(i)
            for j in range(i * i, limit, i):
                nums[j] = False
    return primes


def is_number_palindrome(number):
    if number < 0:
        return False  # Negative numbers are not palindromes

    original_number = number
    reversed_number = 0

    while number > 0:
        digit = number % 10  # Extract the last digit
        reversed_number = (reversed_number * 10) + digit  # Build the reversed number
        number //= 10  # Remove the last digit

    return original_number == reversed_number


def is_palindrome(s):
    return str(s)[::] == str(s)[::-1]


def parse_grid(grid_text):
    grid_lines = grid_text.splitlines()
    grid_as_ints = []
    for grid_row in grid_lines:
        row_values = [int(num) for num in grid_row.split(" ")]
        grid_as_ints.append(row_values)
    return grid_as_ints

