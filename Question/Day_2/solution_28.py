currency = int(input('Enter currency: '))

def currencyConvertor(currency, convertor):
    return f'Your currency is {currency * convertor}, '
    
def main():

    print('\nCurrency Convertor App\n')

    print('1. United States Dollar')
    print('2. Euro')
    print('3. British Pound Sterling')
    print('4. Japanese Yen')
    print('5. Chinese Yuan (Renminbi)')
    print('6. Australian Dollar')
    print('7. Canadian Dollar')
    print('8. Swiss Franc ')
    print('9. Exit App ')

    print('\n')
    choice = input('Enter choice: ')
    print('\n')
    
    match choice:

        case '1':
            convertor = 1.0000
            print(currencyConvertor(currency, convertor))

        case '2':
            convertor = 0.8320
            print(currencyConvertor(currency, convertor))

        case '3':
            convertor = 0.8057
            print(currencyConvertor(currency, convertor))
            
        case '4':
            convertor = 4.8021
            print(currencyConvertor(currency, convertor))

        case '5':
            convertor = 7.2882
            print(currencyConvertor(currency, convertor))

        case '6':
            convertor = 1.5944
            print(currencyConvertor(currency, convertor))

        case '7':
            convertor = 1.4294
            print(currencyConvertor(currency, convertor))

        case '8':
            convertor = 0.7993
            print(currencyConvertor(currency, convertor))

        case '9':
            exit()

        case _:
            print('Invalid Choice')

if __name__ == '__main__':
    main()