print('Python Convertor')
print('1. Binary Convertor')
print('2. Octal Convertor')
print('3. Hexadecimal Convertor')
print('4. Exit App')

number = int(input('Enter value: '))

def main():

    choice = input('Enter Choice: ')

    def binaryConvertor(number):
        binary = bin(number)
        print(f'number {number} to binary :{binary}')

    def octalConvertor(number):
        octal = oct(number)
        print(f'number {number} to octal :{octal}')

    def hexadecimalConvertor(number):
        hexadecimal = hex(number)
        print(f'number {number} to hexadecimal :{hexadecimal}')

    match choice:

        case '1':
            binaryConvertor(number)

        case '2':
            octalConvertor(number)

        case '3':
            hexadecimalConvertor(number)

        case '4':
            exit()

        case _:
            print('Invalid Choice')

if __name__ == '__main__':
    main()