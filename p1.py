"""
If we list all the natural numbers below 10 that are multiples of 3 or 5 we get 3, 5, 6 and 9 .
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000
"""


def multiples_of_three_or_five_iterative(n):
    total = 0
    for n in range(n):
        if n % 3 == 0 or n % 5 == 0:
            total += n
    return total


def multiples_of_three_or_five_generator(n):
    return sum(n for n in range(n) if n % 3 == 0 or n % 5 == 0)


print(multiples_of_three_or_five_generator(1000))
