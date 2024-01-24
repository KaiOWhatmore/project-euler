import utils


def divisible_triangle_number(limit):
    n = 1
    while True:
        tri_number = n * (n + 1) // 2
        if utils.return_divisors_amount_int(tri_number) > limit:
            return tri_number
        n += 1

# print(divisible_triangle_number(7)) 76576500
