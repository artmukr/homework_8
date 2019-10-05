# Write a function that takes a list of strings and removes those strings
# that don't consist of unique letters


def remove_string_doubles(strings: list) -> list:
    output = []
    not_double = ()
    for word in strings:
        for num, el in enumerate(word, start=1):
            if word[num:-1].find(el) == -1 and word[-1] != word[-2]:
                not_double = True
            else:
                not_double = False
                break
        if not_double is True:
            output.append(word)
    return output


assert remove_string_doubles(['cat', 'escape', 'template', 'head']) == \
       ['cat', 'head']
assert remove_string_doubles(['lamp', 'hash']) == ['lamp']
