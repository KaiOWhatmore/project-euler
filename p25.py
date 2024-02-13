import utils


def big_digit_fib_number_index(limit):
    n = 0
    while True:
        fib_num = utils.fib_i(n)
        if utils.integer_length(fib_num) >= limit:
            return n
        n += 1


print(big_digit_fib_number_index(1000))
