from num2words import num2words


def number_letter_counts(num):
    result = 0
    for i in range(1, num + 1):
        number_in_words = num2words(i, lang='en_GB').replace(' ', '').replace('-', '')
        result += len(number_in_words)
    return result

# 21124
