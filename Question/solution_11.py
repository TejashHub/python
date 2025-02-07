number = int(input('Enter number: '))

def is_prime(number):
    if (number < 0):
        print(f'it is not prime number')
        return
    for i in range(2,number):
        if (number % i == 0):
            print(f'it is not prime number')
            return
    print(f'it is prime number')

is_prime(number)