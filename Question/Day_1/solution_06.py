# Method 1
km = int(input('Enter kilometers value: '))

def convertor(km):
    return f'Kilometer to miles convertor: { round(km * 0.621371, 2) }'

print(convertor(km))
