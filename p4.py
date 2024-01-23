import utils


def largest_palindrome(digit_number):
    N = digit_number
    result = 0
    for n in range(N, 100, -1):
        for m in range(N, n - 1, -1):
            product = n * m
            if utils.is_palindrome(product):
                result = max(product, result)

    return result


def largest_palindrome_optimised(digit_number):
    # N = 10 ** digit_number - 1  # Largest number with 'digit_number' digits
    N = digit_number
    result = 0
    for n in range(N, 100, -1):
        for m in range(N, n - 1, -1):
            product = n * m
            if product <= result:
                break  # Further iterations will not yield a larger product
            if utils.is_palindrome(product):
                result = product  # Found a larger palindrome
                break  # No need to check smaller values of m for this n

    return result


print(largest_palindrome(999))
# Largest palindrome: 906609 (Product of 913 and 993)
