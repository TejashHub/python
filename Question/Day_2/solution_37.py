number = int(input('Enter value: '))

def Factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * Factorial(n - 1)

print(Factorial(number))