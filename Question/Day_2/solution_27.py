number = int(input('Enter number: '))

def factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i

    print(f'factorial value is: {result}')

factorial(number)