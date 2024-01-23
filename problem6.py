""" sum square difference """

N = 100


def sum_square_difference_iterate(N):
    """ this uses pure code to iterate over the values """
    sum_of_squares = sum(n ** 2 for n in range(N + 1))
    squares_of_sum = sum(n for n in range(N + 1)) ** 2
    return abs(sum_of_squares - squares_of_sum)


def sum_square_difference_maths(n):
    """ this uses a maths equation to calculate a series """
    sum_of_squares = n * (n + 1) * (2 * n + 1) // 6
    square_of_sum = (n * (n + 1) // 2) ** 2
    return square_of_sum - sum_of_squares


print(sum_square_difference_maths(100) == sum_square_difference_iterate(100))
