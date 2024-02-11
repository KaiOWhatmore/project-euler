'''
c * c = b * b + a * a
=> a*a + b*b + c*c - 2*(c*c)
c = sqrt(b*b + a*a)
p = a + b + c

p = a + b + sqrt(a*a + b*a)

if a*a + b*b is a perfect square

p * p = (a + b + c)(a + b +c)
      = a * a + b * b + c * c + 2ab + 2ac + 2bc - 2*c*c
      =
'''
import collections


def integer_right_triangles(limit):
    number_of_solutions = 0
    max_p = 0
    result = {}
    for p in range(2, limit + 1, 2):
        for a in range(1, p // 2):
            for b in range(a, p // 2):
                c = (p * p - 2 * a * b) / (2 * p)
                if c.is_integer() and c > a and c + a + b == p:
                    result[p] = result.get(p, 0) + 1
                    if result[p] > number_of_solutions:
                        number_of_solutions = result[p]
                        max_p = p

    return max_p


integer_right_triangles(120)


def integer_right_angle_optimised(limit):
    result = {}
    max_solution = 0
    max_p = 0
    for p in range(2, limit + 1, 2):
        for a in range(2, p // 3 + 1):
            if (p * p - 2 * p * a) % (2 * p + 2 * a) == 0:
                result[p] = result.get(p, 0) + 1
                if result[p] > max_solution:
                    max_solution = result[p]
                    max_p = p

    return max_p


print(integer_right_angle_optimised(1000))
