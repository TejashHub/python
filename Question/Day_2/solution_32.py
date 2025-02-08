first = int(input('Enter first: '))
second = int(input('Enter second: '))

def addvalues(first, second):
    print(f'Addition of value is {first + second}')

def subtractvalues(first, second):
    print(f'Substraction of value is {first - second}')

def multiplyvalues(first, second):
    print(f'Multiplication of value is {first * second}')

def dividevalues(first, second):
    print(f'Division of value is {first % second}')


def main():
    print('\n Simple Calculator')
    print('*' * 70)
    print('\n')

    print('1. Add Values')
    print('2. Subtract Values')
    print('3. Multiply Values')
    print('4. Divide Values')
    print('5. Exit')
    print('\n')

    choice = input('Enter your choice from 1-4: ')

    match choice:

        case '1':
            addvalues(first, second)

        case '2':
            subtractvalues(first, second)
        
        case '3':
            multiplyvalues(first, second)
        
        case '4':
            dividevalues(first, second)

        case '5':
            exit()

        case _:
            print('Invalid choice')

if __name__ == '__main__':
    main()