import time

number = int(input('Enter Number: '))

def PrimeChecker(number):
    time.sleep(2)
    if number < 2:
        return f'{number} is not prime number'
    for i in (range(2, number)):
        if (number % i) == 0:
            return f'{number} is not prime number'
    return f'{number} is prime number'

print(PrimeChecker(number))