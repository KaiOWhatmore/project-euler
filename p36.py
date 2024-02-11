import utils

result = 0
for n in range(1, 1000_000):
    if utils.is_palindrome(n) and utils.is_palindrome(bin(n)[2:]):
        result += n

print(result)
# print(bin(585)[2:])