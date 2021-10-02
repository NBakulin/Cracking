print('Input the string:')
first_string = input()


def replace_characters(first_str, search, replace):
    result = ''
    for character in first_str:
        if character == search:
            result = result + replace
        else:
            result = result + character

    return result


print(replace_characters(first_string, ' ', '%20'))