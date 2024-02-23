def hexagonal(n):
    return 2 * n * n - n


def is_pentagonal(n):
    return (1 + (1 + 24 * n) ** 0.5) % 6 == 0


def tri_pent_hex():
    n = 144
    while True:
        if is_pentagonal(hexagonal(n)):
            return hexagonal(n)
        n += 1


print(tri_pent_hex())
