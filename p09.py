""" (1000 - a - b)^2 = a^2 + b^2 """
import functools


def eq1(a, b):
    return (1000 - a - b) ** 2


def eq2(a, b):
    return a * a + b * b


def find_pythagorean_triplet(limit):
    bound = limit // 2
    result_set = []
    for i in range(bound):
        for j in range(bound):
            if eq2(i, j) == eq1(i, j):
                result_set.append((i, j))
                break
        if result_set:
            break

    a = result_set[0][0]
    b = result_set[0][1]
    c = abs(limit - a - b)

    return a * b * c


def find_triplet(limit):
    for a in range(1, limit // 2):
        """ solve for b with simultaneous equations """
        b = (limit * limit - 2 * limit * a) // (2 * limit - 2 * a)
        c = (limit - a - b)

        if c * c == a * a + b * b:
            return a * b * c, [a, b, c]

# print(find_triplet(1000)) (31875000, [200, 375, 425])

# print(find_pythagorean_triplet(1000))
# 31875000
