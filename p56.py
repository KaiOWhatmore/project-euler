def digit_sum(number):
    total = 0
    while number:
        digit = number % 10
        number //= 10
        total += digit
    return total


def powerful_digit_sum(number):
    result = 0
    for a in range(2, number):
        for b in range(2, number):
            result = max(result, digit_sum(a ** b))
    return result


print(powerful_digit_sum(100))
