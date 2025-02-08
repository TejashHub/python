celsius = int(input('Enter value: '))

def fahrenheitChecker(celsius):
    formula = (celsius * 9/5) + 32
    print(f'Fahrenheit Value is : {formula}')

fahrenheitChecker(celsius)