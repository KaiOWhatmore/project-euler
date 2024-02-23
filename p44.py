def pent_nums(n):
    return (n * (3 * n - 1)) // 2


def is_pentagonal(n):
    return (1 + (1 + 24 * n) ** 0.5) % 6 == 0


def pentagon_nums():
    for i in range(1, 3000):
        for j in range(3000, 0, -1):
            if is_pentagonal(pent_nums(i) + pent_nums(j)) and \
                    is_pentagonal(abs(pent_nums(j) - pent_nums(i))):
                        return pent_nums(i), pent_nums(j), i, j, abs(pent_nums(i) - pent_nums(j))


print(pentagon_nums())
print(pentagon_nums()[-1] == 5482660)
print(abs(1560090 - 7042750))  # 5482660
