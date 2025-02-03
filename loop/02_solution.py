number = int(input('Number: '))

count = 0

for n in range(1, number + 1):
    if(n % 2 == 0):
        count += n
        
print('Sum of Even Number: ',count)