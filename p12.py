import utils

# 1, 3, 6, 10, 15, 21, 28

""" 
1 + 2 + 3 + 4 + 5 + 6 + 7 
U = {1, 2, 3, 4, 5, 6, 7}, n=8 
(7 + 1) + (2 + 6) + (3 + 5) + 4 = 28 
8 + 8 + 8 + 4
3 * 8 + 4 
3 * (n + 1) + (4 + 4) / 2 
3 * (n + 1) + (n + 1) / 2 
(n + 1)(3 + 1/2)
(n + 1)(7) / 2 
(n + 1) * n / 2  
Σ start:n=1 limit: n=7, where n is the size of the set   
"""



# for n in range(1, 11):
n=100
print(f"{n} triangle number: {n * (n + 1) // 2}")


def divisible_triangle_number(limit):
    n = 1
    while True:
        tri_number = n * (n + 1) // 2
        if utils.return_divisors_amount_int(tri_number) > limit:
            return tri_number
        n += 1

# print(divisible_triangle_number(7)) 76576500
