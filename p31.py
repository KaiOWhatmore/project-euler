import time


def coin_sum_memo(target, coins, start_index=0, memo=None):
    # if not memo: interestingly this logic makes the function perform > 2s
    if memo is None:
        memo = {}
    if (target, start_index) in memo:
        return memo[(target, start_index)]

    count = 0
    if target == 0:
        return 1
    if target < 0:
        return 0

    for i in range(start_index, len(coins)):
        count += coin_sum_memo(target - coins[i], coins, i, memo)
    memo[(target, start_index)] = count
    return count


def coin_sum(target, coins, start_index=0):
    count = 0
    if target == 0:
        return 1
    if target < 0:
        return 0

    for i in range(start_index, len(coins)):
        count += coin_sum(target - coins[i], coins, i)
    return count


def coin_sum_gpt(target, coins, start_index=0):
    if target == 0:
        return 1
    if target < 0 or start_index >= len(coins):
        return 0
    # Option 1: Use the coin at start_index
    use_it = coin_sum_gpt(target - coins[start_index], coins, start_index)
    # Option 2: Don't use the coin at start_index
    skip_it = coin_sum_gpt(target, coins, start_index + 1)
    return use_it + skip_it


def coin_sum_gpt_helper(target, coins):
    def helper(target, start_index):
        if target == 0:
            return 1
        if target < 0:
            return 0
        count = 0
        for i in range(start_index, len(coins)):
            count += helper(target - coins[i], i)
        return count

    return helper(target, 0)


coins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200

t1 = time.time()
print("coin_sum_memo", coin_sum_memo(target, coins), f"|| time taken:{time.time() - t1}")

t1 = time.time()
print("coin_sum", coin_sum(target, coins), f"|| time taken:{time.time() - t1}")
