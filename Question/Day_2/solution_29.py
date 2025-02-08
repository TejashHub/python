import os

folder = input('Enter folder: ')

def createIfNotExit(folder):
    try:
        if not os.path.exists(folder):
            os.mkdir(folder)
            print(f'{folder} created successfully')
        else:
            print(f'{folder} already exist')
    except Exception as e:
        print(e)

def removeIfNotExit(folder):
    try:
        if os.path.exists(folder):
            os.rmdir(folder)
            print(f'{folder} remove successfully')
        else:
            print(f'{folder} already remove')
    except Exception as e:
        print(e)
    
def main():

    print('Folder Handle App')

    print('\n1. Create folder')
    print('\n2. Remove folder\n')

    choice = input('\nEnter choice: ')

    match choice:

        case '1':
            createIfNotExit(folder)

        case '2':
            removeIfNotExit(folder)


if __name__ == '__main__':
    main()