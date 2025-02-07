first = int(input('First value: '))
second = int(input('Second value: '))
third = int(input('Third value: '))

if (first > second) and (first > third):
    print(f'{first} is greaterthan')

elif (second > first) and (second > third):
    print(f'{second} is greaterthan')

elif (third > first) and (third > second):
    print(f'{third} is greaterthan')

else:
    print('All values are equal or there are duplicates.')

    