first = int(input('enter first value: '))
second = int(input('enter second value: '))

def HighestCommanFactor(first, second):
    while second:
        first, second = second, first % second
    return first

HighestCommanFactor = HighestCommanFactor(first, second)

print(f'The HCF of {first} and {second} is : {HighestCommanFactor}')