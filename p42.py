import math

import utils

"""
tn = 1/2 * n * (n + 1)
55 = 1/2 * n * (n + 1) 
110 = n * (n + 1) 
n * n + n - 110 = 0 

n = - b +/- sqrt(b * b - 4ac) / 2a 
n = - 1 +/- sqrt(1 - 4 * 2 * letter_sum) % 2 == 0 
 
"""


def is_triangle_number(n):
    return ((-1 + math.sqrt(1 + 8 * n)) / 2).is_integer()


with open('p42_words.txt') as file:
    file_contents = file.read().replace('"', '').split(',')

count = 0
for word in file_contents:
    letter_sum = sum(utils.index_of_letter(c) for c in word)

    if is_triangle_number(letter_sum):
        count += 1

print(count)
