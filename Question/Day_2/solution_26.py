total = 0

while(True):
    userInput = input('Enter the product price: \n')
    if (userInput != 'exit'):
        total += int(userInput)
    else:
        print(f'Your total bill is : {total}')
        print('Thanks for coming to the Kirana Store!')
        break
