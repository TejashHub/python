number = int(input('Enter value: '))

def fibonacci(number):
    a = 0
    b = 1
    for i in range(1, number + 1):
        temp = a + b
        a = b
        b = temp 
        print(temp)
    
fibonacci(number)