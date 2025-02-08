character = input('Enter a character : ')

if len(character) == 1: 
    print(f'the ASCII value of {character} is {ord(character)}')
else:
    print('Please enter only one character.')
    