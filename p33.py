def gcd_i_opt(a, b):
    while a % b:
        a, b = b, a % b
    return b


def remove_like_terms(a, b):
    c, d = a, b
    a1, a2 = str(a)
    b_str = str(b)
    if a1 in b_str:
        c, d = int(a2), int(b_str.replace(a1, '', 1))
    if a2 in b_str:
        c, d = int(a1), int(b_str.replace(a2, '', 1))
    return c, d


def reduced_fraction(a, b):
    gcd = gcd_i_opt(a, b)
    return a // gcd, b // gcd


def dig_cancel_frac_opt():
    n_product, d_product = 1, 1
    for n1 in range(11, 100):
        for d1 in range(n1 + 1, 100):
            if d1 % 10 == 0 or n1 % 10 == 0:
                continue
            n2, d2 = remove_like_terms(n1, d1)
            if (n2, d2) != (n1, d1) and n2 * d1 == n1 * d2:
                n_product *= n2
                d_product *= d2
    _, d = reduced_fraction(n_product, d_product)
    return d


print(dig_cancel_frac_opt())

"""
def dig_cancel_frac():
    limit = 100
    start = 11
    n_product, d_product = 1, 1
    for n1 in range(start, limit):
        for d1 in range(n1 + 1, limit):
            if d1 % 10 != 0 and n1 % 10 != 0 and str(d1) != str(n1)[::-1]:
                n2, d2 = remove_like_terms(n1, d1)
                if reduced_fraction(n1, d1) == reduced_fraction(n2, d2) and n1 != n2 and d1 != d2:
                    n_product *= n2
                    d_product *= d2
    n, d = reduced_fraction(n_product, d_product)
    return d


def gcd_r(a, b):
    if a % b == 0:
        return b
    return gcd_r(b, a % b)


def gcd_i(a, b):
    r = a % b
    while r:
        a = b
        b = r
        r = a % b
    return b
"""
