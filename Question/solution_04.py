base = int(input('Enter a Base value: '))
height = int(input('Enter a Height value: '))

def Triangle(base, height):
    return f'Area of triangle is: {int(0.5 * base * height)}'

print(Triangle(base, height))