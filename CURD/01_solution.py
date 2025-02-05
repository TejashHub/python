import json

def load_data():
    try:
        with open('test.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open('test.txt','w') as file:
        json.dump(videos, file)

def list_all_video(videos):
    result = enumerate(videos, start=1)
    for index, video in result:
        print(f'{index}:{video}')

def add_video(videos):
    name = input('Enter video name: ')
    time = input('Enter video time: ')
    videos.append({'name':name, 'time':time})
    save_data_helper(videos)

def update_video(videos):
    list_all_video(videos)
    index = int(input('Enter video number to be update: '))
    if 1 <= index <= len(videos):
        name = input('Enter video name: ')
        time = input('Enter video time: ')
        videos[-index] = {'name':name, 'time':time}
        save_data_helper(videos)
    else:
        print("Invalid Index Selected")

def delete_video(videos):
    list_all_video(videos)
    index = int(input('Enter video number to be deleted: '))
    if 1 <= index <= len(videos):
        del videos[-index]
        save_data_helper(videos)
    else:
        print("Invalid Index Selected")

def main():
    while True:
        videos = load_data()

        print('1. List all videos')
        print('2. Add video')
        print('3. Update videos')
        print('4. Delete videos')
        print('5. Exit App')

        choice = input('Enter your choice: ')

        match choice:
            case '1':
                list_all_video(videos)
            
            case '2':
                add_video(videos)
            
            case '3':
                update_video(videos)
            
            case '4':
                delete_video(videos)
            
            case '5':
                break

            case _:
                print('Invalid Choice')

if __name__ == '__main__': 
    main()
