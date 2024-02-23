limit = 1_000_000


def champernownes_constant(limit):
    p = str(123456789)
    power = 1
    result = 1
    for n in range(10, limit):
        p += str(n)
        ten_to_the_power = 10 ** power
        if len(p) >= ten_to_the_power:
            index = ten_to_the_power - 1
            result *= int(p[index])
            power += 1
            if 10 ** power == limit:
                return result


print(champernownes_constant(limit))
# 210


def champernownes_constant_gpt(limit):
    p = "123456789"  # Starting string, covering 1 to 9
    nth_power = 1  # To track the powers of 10
    result = 1  # Initialize result to multiply digits into
    for n in range(10, limit):  # Start appending from 10 onwards
        p += str(n)  # Append each number as a string
        while len(p) >= 10 ** nth_power:  # Check if we've reached or exceeded the next power of 10
            index = 10 ** nth_power - 1  # Calculate the index to find the digit
            result *= int(p[index])  # Multiply the digit at the calculated index
            nth_power += 1  # Move to the next power of 10
            if 10 ** nth_power > limit:  # If the next power of 10 exceeds the limit, no need to continue
                return result
    return result  # Return the result if the loop completes normally


# print(champernownes_constant_gpt(limit))


def digit_length(num):
    count = 0
    while num:
        count += 1
        num //= 10
    return count


def nearest_ten(num):
    return 10 ** (digit_length(num) - 1)

# print(digit_length(1234))
# print(nearest_ten(9989898123))
