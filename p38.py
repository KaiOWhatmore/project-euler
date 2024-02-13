def pandigital_multiples():
    checker = set("123456789")
    max_pan = 0
    for n in range(1, 10000):
        total = ''
        for m in range(1, 10):
            total += str(m * n)
            if len(total) > 9:
                break
            if len(total) == 9 and set(total) == checker:
                total_int = int(total)
                if total_int > max_pan:
                    max_pan = total_int
                break

    return max_pan


print(pandigital_multiples())
# answer: 932718654
