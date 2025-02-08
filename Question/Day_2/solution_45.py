stringValue = input('Enter String: ')

vowels = ['a','i','o','u','l']

count = 0

for s in stringValue:
    if s in vowels:
        count += 1

print(f'total vowel is {count}')