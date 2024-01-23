def fib_recursive(n):
    if n <= 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n):
    if n <= 1:
        return 1
    a, b = 1, 1
    for i in range(2, n + 1):
        tmp = b
        b += a
        a = tmp
    return b


def fib_recursive_memo(n, memo={}):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return 1
    memo[n] = fib_recursive_memo(n - 1) + fib_recursive_memo(n - 2)
    return memo[n]


def sum_even_fib_numbers(max_fib_value):
    i = 1
    total = 0
    while True:
        n = fib_recursive_memo(i)
        if n % 2 == 0:
            total += n
        if n > max_fib_value:
            break
        print(f"{i}: {n}")
        i += 1
    return total


def sum_every_third_fib_number(max_fib_value):
    """ every third number in the fib sequence is an even number """
    i = 2
    total = 0
    while True:
        n = fib_recursive_memo(i)
        if n > max_fib_value:
            break
        total += n
        i += 3
    return total

max_sum = 4_000_000
print(sum_every_third_fib_number(max_sum)) # 4613732
