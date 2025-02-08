number = int(input('Enter value: '))

def NaturalNumSum(n):
    if n <= 1:
        return n 
    else:
        return n + NaturalNumSum(n - 1)

if number <= 1:
    print('It is not a natural number')
else:
    print(f'Sum of natural numbers up to {number} is: {NaturalNumSum(number)}')