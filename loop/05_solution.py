input_str = input('Your String: ')

new_input_str = ''

for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        new_input_str += char
        break

print(new_input_str)