import time

number = int(input('enter a value here: '))

sum = 0
temp = number
num_digits = len(str(number))

while temp > 0:
    time.sleep(3)
    digit = temp % 10
    cube = digit ** num_digits
    sum += cube
    temp //= 10

if sum == number:
    print('it is an Armstrong numbers')
else:
    print('it is not an Armstrong numbers')
