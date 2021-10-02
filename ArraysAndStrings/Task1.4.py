print('Input the string:')
input_string = input().lower().replace(' ', '')


def replace_characters(string):
    first_string_map = {}

    for character in string:
        if character not in first_string_map:
            first_string_map[character] = 1
        else:
            first_string_map[character] += 1

    single_chars_amount = 0
    for character in first_string_map:
        if first_string_map[character] % 2 == 1:
            single_chars_amount += 1
        if single_chars_amount > 1:
            return False
    return True


print(replace_characters(input_string))
