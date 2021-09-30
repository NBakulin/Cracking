alphabet = 'abcdefghijklmnopqrstuvwxyz'
print('Input the string:')
input_string = input()


def symbols_occur_once(string):
    for character in alphabet:
        if string.count(character) > 1:
            return True
    return False


print(symbols_occur_once(input_string))

