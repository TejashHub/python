number = int(input('Number: '))

for n in range(1,11):
    if n == 5:
        continue
    print(f'{number} x {n} = {number * n}')