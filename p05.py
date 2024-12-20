import utils


def lcm_of_range(start, end):
    # current_lcm = start
    current_lcm = start
    for i in range(start + 1, end + 1):
        current_lcm = utils.lcm(current_lcm, i)
    return current_lcm


# print(lcm_of_range(1, 20)) 232792560
