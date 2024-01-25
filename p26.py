a = 1/7
b = f"{a:.20f}"
b = b[2:]

print(b)
print(b[:6])
print(b[6:12])
print(b[12:18])

def longest_repeating_substring(s):
    longest_substr = ""
    n = len(s)

    for i in range(n):
        for j in range(i + 1, n + 1):
            substr = s[i:j]
            if s.count(substr) > 1 and len(substr) > len(longest_substr):
                longest_substr = substr

    return longest_substr

# Test the function
input_string = "abcabcabcabc"
print("Longest repeating substring:", longest_repeating_substring(input_string))
