def pandigital_nums(num, digit_length):
    result = []
    limit = int('9' * digit_length)
    for n in range(num, limit, num):
        if len(set(str(n))) == digit_length:
            result.append(n)
    return result


def pandigital_sum(current_num, depth=0):
    """returns a sum of the results"""
    primes = [17, 13, 11, 7, 5, 3, 2]
    result = 0
    if depth == len(primes):
        return int(current_num)
    if len(current_num) > 3 and int(current_num[:3]) % primes[depth] > 0:
        return 0
    for n in range(10):
        test_digit = str(n)
        if test_digit not in current_num:
            new_num = test_digit + current_num
            result += int(pandigital_sum(new_num, depth + 1))
    return result


def pandigital_sum_memo(current_num, depth=0, cache=None):
    """returns a sum of the results"""
    if cache is None:
        cache = {}
    cache_key = (current_num, depth)

    if cache_key in cache:
        return cache[cache_key]

    primes = [17, 13, 11, 7, 5, 3, 2]
    result = 0
    if depth == len(primes):
        return int(current_num)
    if len(current_num) > 3 and int(current_num[:3]) % primes[depth] > 0:
        return 0

    for n in range(10):
        test_digit = str(n)
        if test_digit not in current_num:
            new_num = test_digit + current_num
            result += int(pandigital_sum(new_num, depth + 1))

    cache[cache_key] = result
    return result


divisibility_roots = pandigital_nums(17, 3)
answer = sum(pandigital_sum(str(root)) for root in divisibility_roots)
answer_memo = sum(pandigital_sum_memo(str(root)) for root in divisibility_roots)
print(answer == answer_memo)  # 16695334890

# def pandigital_list(current_num, depth=0):
#     """returns a list of the results"""
#     primes = [17, 13, 11, 7, 5, 3, 2]
#     result = []
#     if depth == len(primes):
#         return [current_num]
#     if len(current_num) > 3 and int(current_num[:3]) % primes[depth] > 0:
#         return []
#     for i in range(10):
#         new_digit = str(i)
#         if new_digit not in current_num:
#             new_num = new_digit + current_num
#             result.extend(pandigital_list(new_num, depth + 1))
#     return result
