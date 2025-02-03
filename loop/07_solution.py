while True:
    number = int(input('Enter Value between 1 and 10: '))
    if number in range(1,11):
        print('Thanks')
        break
    else:
        print('invalid number, try again')
