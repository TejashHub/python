message = input('Enter your string: ').lower()

result = message[::-1]

if message == result.lower():
    print(f'String is a Palindrome')
else:
    print(f'String is not a Palindrome')
