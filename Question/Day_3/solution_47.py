set1 = input('Set1 (space-separated numbers): ')  
set2 = input('Set2 (space-separated numbers): ') 

result_set1 = {int(i) for i in set1.split()}
result_set2 = {int(i) for i in set2.split()}

def main():
    print('\n')
    print(f'set 1 value is:  {result_set1}')
    print(f'set 2 value is:  {result_set2}')
    print('\n')

    print('Illustrate Different Set Operations')
    print('\n')

    print('1. Union')
    print('2. Intersection')
    print('3. Deference')
    print('4. Symmetic Difference')
    print('5. Exit App')

    print('\n')
    choice = input('enter choice: ')
    print('\n')

    match choice:

        case '1':
            print(f'Union: {result_set1 | result_set2}')

        case '2':
            print(f'Intersection: {result_set1 & result_set2}')

        case '3':
            print(f'Difference (Set1 - Set2): {result_set1 - result_set2}')
            print(f'Difference (Set2 - Set1): {result_set2 - result_set1}')

        case '4':
            print(f'Symmetric Difference: {result_set1 ^ result_set2}')

        case '5':
            exit()

        case _:
            print('Invalid choice. Please enter a number between 1-5.')

if __name__ == '__main__':
    main()