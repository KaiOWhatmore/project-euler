"""
r=1, d=0
(r, r, d, d) 1100
(r, d, r, d) 1010
(r, d, d, r) 1001
(d, r, r, d) 0110
(d, r, d, r) 0101
(d, d, r, r) 0011
arr_len=4

k!(n−k)!n!

20! / 10! (20 - 10)!
20! / 10! * 10!
"""
import utils
import itertools


def lattice_paths(grid_width):
    """
    we have a combinatorial problem
    so we're going to use the binomial
    coefficient
    """
    a = utils.factorial_iterative(grid_width * 2)
    b = utils.factorial_iterative(grid_width)

    return a // (b * b)


def generate_bit_permutations(n, k):
    # Generate all positions for 1s in the sequence
    positions = range(n)
    arr = []
    # Use itertools.combinations to generate all possible positions for 1s
    for ones_positions in itertools.combinations(positions, k):
        # Create a list of 0s of length n
        bit_sequence = ['0'] * n
        # Set the positions of 1s
        for pos in ones_positions:
            bit_sequence[pos] = '1'
        # arr.append(bit_sequence)
    return len(arr)


# Example usage: 4-bit sequences with 2 1s
# print(lattice_paths(20)) 137846528820
print(lattice_paths(2))
print(lattice_paths(4))
print(generate_bit_permutations(4, 2))