n = int(input('Enter value: '))

result = []

def convertBinary(n):
    if n > 1:
        convertBinary(n // 2)
    result.append(( n % 2 ))

convertBinary(n)

print(' '.join(map(str, result)))