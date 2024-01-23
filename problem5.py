import utils


def is_divisible_up_until(num, ceil):
    for n in range(1, ceil + 1):
        if num % n != 0:
            return False
    return True

ceil = 10
i = ceil * ceil
while True:
    print(i)
    if is_divisible_up_until(i, ceil):
        print(f"smallest number divisible by 1-{ceil} is {i}")
        break
    i += 1

# print(is_divisible_up_until(2520, 10))
