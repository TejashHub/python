import string
import random

lowercase = string.ascii_lowercase 
uppercase = string.ascii_uppercase 
digit = string.digits 
punctuation = string.punctuation

def passwordGenerator(combine, choice_password_len):
    password = ''.join(random.sample(combine, choice_password_len))
    print(f'Your password: {password}\n')

def main():

    print('\n Password Generator')

    print('\n1. Password with (lowercase , uppercase and digit)')
    print('\n2. Password with (lowercase , punctuation and digit)')
    print('\n3. Password with (lowercase , uppercase and punctuation)')
    print('\n4. Password with (lowercase , uppercase and punctuation and digit)')
    print('\n5. Password with (uppercase , punctuation and digit)')
    print('\n6. Exit App')

    print('\n')

    choice = input('Enter choice: ')
    choice_password_len = int(input('Enter choice_password_length: '))

    if 5 <= choice_password_len <= 8:
        print('')
    else:
        print('Check Password Length')

    print('\n')

    match choice:
        case '1':
            combine = (lowercase + uppercase + digit)
            passwordGenerator(combine, choice_password_len)

        case '2':
            combine = (lowercase + punctuation + digit)
            passwordGenerator(combine, choice_password_len)


        case '3':
            combine = (lowercase + uppercase + punctuation)
            passwordGenerator(combine, choice_password_len)


        case '4':
            combine = (lowercase + uppercase + digit + punctuation)
            passwordGenerator(combine, choice_password_len)


        case '5':
            combine = (punctuation + uppercase + digit)
            passwordGenerator(combine, choice_password_len)

        case '6':
            exit()

        case _:
            print('Invalid Choice')

if __name__ == "__main__":
    main()

