import time


def collatz_recur(n, count=1):
    if n == 1:
        return count
    if n % 2 == 0:
        return collatz_recur(n // 2, count + 1)
    return collatz_recur(3 * n + 1, count + 1)


def collatz_seq(n):
    count = 1
    while True:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        count += 1
        if n == 1:
            return count


def longest_collatz_chain(end):
    max_length = 0
    for i in range(end, end // 2, - 1):
        print(f"longest_collatz_chain: {i / end}%", end='\r')
        collatz_chain_length = collatz_seq(i)
        if collatz_chain_length > max_length:
            max_length = collatz_chain_length
            max_int = i
    return max_length, max_int


# s1 = time.time()
# print(longest_collatz_chain(1000_000 - 1))
# print(time.time() - s1)


def collatz_sequence_memo(n, memo):
    count = 0
    original_n = n
    while n != 1 and n >= original_n:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        count += 1
    memo[original_n] = count + memo.get(n, 0)
    return memo


def seq(n):
    memo = {1: 1}
    for n in range(2, n):
        x = collatz_sequence_memo(n, memo)
    return x


print(seq(20))
