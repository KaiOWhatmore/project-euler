def find_limit(power):
    # increment = 9 ** power
    # limit = increment
    n = 1
    while n * (9 ** power) > 10 ** n:
        n += 1
        # limit += increment
    return n * (9 ** power)


def find_limit_2(power):
    n = 1
    while 10 ** n <= n * (9 ** power):
        n += 1
    return n * (9 ** power)


power = 4


def sum_power_digits(power):
    power_limit = find_limit_2(power)
    result = 0
    for n in range(2, power_limit):
        total = sum(int(c) ** power for c in str(n))
        if total == n:
            result += total
    return result


# print(sum_power_digits(5)) 443839
