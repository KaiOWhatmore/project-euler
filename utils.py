import math
import time


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True


def sieve_of_eratosthenes_l(limit):
    nums = [True] * limit
    primes = []
    for i in range(2, limit):
        if nums[i]:
            primes.append(i)
            for j in range(i * i, limit, i):
                nums[j] = False
    return primes


def sieve_of_eratosthenes_s(limit):
    nums = [True] * limit
    primes = set()
    for i in range(2, limit):
        if nums[i]:
            primes.add(i)
            for j in range(i * i, limit, i):
                nums[j] = False
    return primes


def is_number_palindrome(number):
    if number < 0:
        return False  # Negative numbers are not palindromes

    original_number = number
    reversed_number = 0

    while number > 0:
        digit = number % 10  # Extract the last digit
        reversed_number = (reversed_number * 10) + digit  # Build the reversed number
        number //= 10  # Remove the last digit

    return original_number == reversed_number


def is_palindrome(s):
    return str(s)[::] == str(s)[::-1]


def parse_grid(grid_text):
    grid_lines = grid_text.splitlines()
    grid_as_ints = []
    for grid_row in grid_lines:
        row_values = [int(num) for num in grid_row.split(" ")]
        grid_as_ints.append(row_values)
    return grid_as_ints


def factorial_r(n):
    """ recursively calculates factorial """
    if n == 0:
        return 1
    return n * factorial_r(n - 1)


def factorial_r_m(n, memo={}):
    """ recursively calculates factorial with memo """
    if n == 0:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = n * factorial_r_m(n - 1)
    return memo[n]


def factorial_i(num):
    """ iteratively calculates factorial  """
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result


def number_addition_sum_r(num):
    if not num:
        return 0
    return num % 10 + number_addition_sum_r(num // 10)


def number_addition_sum_i(num):
    result = 0
    while num:
        result += num % 10
        num //= 10
    return result


def return_proper_divisors_sum(num):
    proper_divisors = set()
    proper_divisors.add(1)
    for n in range(2, math.isqrt(num) + 1):
        if num % n == 0:
            proper_divisors.add(n)
            proper_divisors.add(num // n)
    return sum(proper_divisors)


def return_divisors_amount_list(num):
    proper_divisors = set()
    proper_divisors.add(1)
    proper_divisors.add(num)
    for n in range(2, math.isqrt(num) + 1):
        if num % n == 0:
            proper_divisors.add(n)
            proper_divisors.add(num // n)
    return len(proper_divisors), proper_divisors


def return_divisors_amount_int(num):
    # total = 1 if num == 1 else 2
    root = math.isqrt(num)
    divisors = 0
    for n in range(1, root + 1):
        if num % n == 0:
            divisors += 2
    if root * root == num:
        divisors -= 1
    return divisors


def gcd_r(a, b):
    """ a > b """
    if b > a:
        tmp = a
        a = b
        b = tmp
    if a % b == 0:
        return b
    return gcd_r(a % b, b)


def gcd_r_clean(a, b):
    r = a % b
    if r == 0:
        return b
    return gcd_r_clean(b, r)


def gcd_i(a, b):
    """ a > b """
    if b > a:
        tmp = b
        b = a
        a = tmp
    while True:
        r = a % b
        a = b
        b = r
        if a % b == 0:
            return b


def lcm(a, b):
    return (a * b) // gcd_r(a, b)


def fib_r(n, memo):
    if n <= 2:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = fib_r(n - 1, memo) + fib_r(n - 2, memo)
    return memo[n]


def fib_i(n):
    a, b = 1, 1
    for i in range(2, n):
        total = a + b
        a = b
        b = total
    return b


def integer_length(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count


def is_perfect_square(n):
    i = 2
    while i * i <= n:
        if n == i * i:
            return True
        i += 1
        # print(i)
    return False


def index_of_letter(c):
    if c.isupper():
        return ord(c) - ord('A') + 1
    return ord(c) - ord('a') + 1


def runtime(func, *args, **kwargs):
    t1 = time.time()
    func(*args, **kwargs)
    return time.time() - t1


def permutations_s_c(s):
    """ returns a list of permutations
        this uses pure strings during computation
        and list comprehension
        the syntax is made to be as flat as possible at
        perhaps the cost of readability """
    res = []
    if len(s) == 1:
        return [s]
    for i in range(len(s)):
        res.extend([perm + s[i] for perm in permutations_s_c(s[:i] + s[i + 1:])])
    return res


def permutations_s(s):
    """ returns a list of permutations.
        uses strings during computation.
        nested for loop is used for the sake
        of readability """
    res = []
    if len(s) == 1:
        return [s]
    for i in range(len(s)):
        s_sub_list = s[:i] + s[i + 1:]
        for perm in permutations_s(s_sub_list):
            res.append(perm + s[i])
    return res


def permutations_s_l(s):
    """ returns a list of permutations
        uses a mixture of lists and strings
        for computation """
    s_list = list(s)
    res = []
    if len(s_list) == 1:
        return s
    for i in range(len(s_list)):
        s_sub_list = s_list[::]
        s_sub_list.pop(i)
        perms = permutations_s_l(s_sub_list)
        for perm in perms:
            perm += s_list[i]
            res.append(perm)
    return res


def permutations_l(s):
    """ returns a list of permutations
        uses a list for computation """
    s_list = list(s)
    res = []
    if len(s_list) == 1:
        return [s_list]
    for i in range(len(s_list)):
        s_sub_list = s_list[::]
        s_sub_list.pop(i)
        perms = permutations_l(s_sub_list)
        for perm in perms:
            perm.append(s_list[i])
            res.append(perm)
    return res
