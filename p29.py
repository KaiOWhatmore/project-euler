def distinct_powers(min_limit, max_limit):
    distinct_powers = set()
    for a in range(min_limit, max_limit + 1):
        for b in range(min_limit, max_limit + 1):
            distinct_powers.add(a ** b)
    return len(distinct_powers)`


print(distinct_powers(2, 100))
