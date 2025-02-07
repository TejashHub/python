number = int(input('Your Number: '))

count = 1

for i in range(1, number + 1):
    count *= i

print(f'{number} Factorial is: {count}')
