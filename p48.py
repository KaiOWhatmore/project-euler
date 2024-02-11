def self_powers(nums):
    return sum(n ** n for n in range(1, nums + 1)) % 10 ** 10


big_digit = self_powers(1000)
print(big_digit)


def self_powers_mod(nums):
    mod = 10 ** 10  # We only give a shit about the last ten digits
    total_sum = sum((n ** n) % mod for n in range(1, nums + 1))
    return total_sum % mod  # Just to be double sure we're clean and under ten digits

