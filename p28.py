def number_spiral_diag(grid_size):
    result = 1
    for n in range(3, grid_size + 1, 2):
        n_squared = n * n
        for _ in range(4):
            result += n_squared
            n_squared += - (n - 1)
    return result


def number_spiral_diag_gpt(grid_size):
    result = 1
    for n in range(3, grid_size + 1, 2):
        corner_value = n * n
        decrement = n - 1
        for corner in range(4):
            result += corner_value - decrement * corner
    return result


# print(number_spiral_diag(1001))
