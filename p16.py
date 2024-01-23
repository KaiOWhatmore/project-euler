def sum_digits(num):
    sum = 0
    while num:
        sum += num % 10
        num //= 10
    return sum


def sum_digits_recursive(num):
    # return num % 10 + sum_digits_recursive(num // 10) if num else 0
    if not num:
        return 0
    return num % 10 + sum_digits_recursive(num // 10)
