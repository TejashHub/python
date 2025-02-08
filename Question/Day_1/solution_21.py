number = int(input('Enter value: '))

divide = []

for i in range(1, number + 1): 
    if (number % i) == 0: 
        divide.append(i) 

print("Divisors of", number, "are:", divide)
