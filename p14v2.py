import time


def collatz_seq_memo(n, memo):
    original_n = n
    count = 0
    while n != 1 and n >= original_n:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1

    # We check if n is in memo to avoid KeyErrors
    memo[original_n] = count + memo.get(n, 0)
    return memo[original_n]

def longest_collatz_chain(end):
    memo = {1: 1}
    max_length = 0
    max_num = 1
    for i in range(2, end + 1):
        length = collatz_seq_memo(i, memo)
        if length > max_length:
            max_length = length
            max_num = i
    return max_num, memo[max_num]


# Timing the execution
start_time = time.time()
result = longest_collatz_chain(1000000)
elapsed_time = time.time() - start_time

print(f"The number under 1,000,000 with the longest Collatz sequence is: {result[0]} and is {result[1]}")
print(f"Time taken: {elapsed_time} seconds")
