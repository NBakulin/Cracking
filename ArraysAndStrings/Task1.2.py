alphabet = 'abcdefghijklmnopqrstuvwxyz'
print('Input the first string:')
first_string = input()
print('Input the second string:')
second_string = input()


def are_strings_permutations(first_str, second_str):
    first_string_map = {}
    second_string_map = {}

    for character in first_str:
        if character not in first_string_map:
            first_string_map[character] = 1
        else:
            first_string_map[character] += 1
    for character in second_str:
        if character not in second_string_map:
            second_string_map[character] = 1
        else:
            second_string_map[character] += 1

    for character in first_string_map:
        if character not in second_string_map or first_string_map[character] != second_string_map[character]:
            return False

    return True


print(are_strings_permutations(first_string, second_string))

