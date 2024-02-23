import utils


def is_pandigital(start, end, num):
    if len(num) == end - start + 1:
        checker = set()
        for char in num:
            if char in checker or char == '0':
                return False
            checker.add(char)
        return True
    return False


def is_pandigital_gpt(start, end, num):
    return set(num) == set("123456789") and len(num) == end - start + 1


def pandigital_products():
    products = set()
    for n in range(1, 100 // 2):
        for m in range(1, 2000):
            product = n * m
            if product in products:
                break
            res = f"{n}{m}{product}"
            if is_pandigital_gpt(1, 9, res):
                products.add(product)
    return sum(products)


print(pandigital_products(), utils.runtime(pandigital_products))

# 45228
# {5346, 5796, 6952, 7852, 4396, 7632, 7254}
