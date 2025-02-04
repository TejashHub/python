import math

def circle_status(r):
    area = f'Area of Circle : { round(math.pi * r * r)}'
    circumference = f'circumference of Circle : { round(2 * math.pi * r)}'
    return area, circumference

area, circumference = circle_status(5)
print(area)
print(circumference)
