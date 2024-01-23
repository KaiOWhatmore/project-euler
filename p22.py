def letter_order_in_alphabet(s):
    return ord(s) - ord('A') + 1


def sum_of_letter_orders(s):
    return sum(letter_order_in_alphabet(c) for c in s)


with open('p22_0022_names.txt', 'r') as file:
    file_contents = file.read().replace('"', '').split(',')
    sorted_names = sorted(file_contents)


def names_scores(sorted_names):
    result = 0
    for i, name in enumerate(sorted_names):
        result += (i + 1) * sum_of_letter_orders(name)
    return result


# print(names_scores(sorted_names)) 871198282