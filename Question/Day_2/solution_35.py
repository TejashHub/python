n = int(input('Enter a number: '))

def Fibonacci(n):
    if n < 0:
        return "Invalid input" 
    if n == 0:
        return 0 
    if n == 1:
        return 1 
    if n == 2:
        return 2 
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)  

print(Fibonacci(n))
