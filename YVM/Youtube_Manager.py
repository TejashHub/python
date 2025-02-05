import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos, file)
        
def list_all_videos(videos):
    result = enumerate(videos, start=1)
    print('\n')
    print("*" * 70)
    for index, video in result:
        print(f'{index}: Video name: {video['name']}, Duration is: {video['time']}')
    print("*" * 70)

def add_video(videos):
    name = input('Enter video name: ')
    time = input('Enter video time: ')
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input('Enter the video number to update: '))
    if 1 <= index <= len(videos):
        name = input('Enter new video name: ')
        time = input('Enter new video time: ')
        videos[index-1] = {'name':name, 'time':time}
        save_data_helper(videos)
    else:
        print("Invalid Index Selected")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input('Enter the video number to be delete: '))
    if 1 <= index <= len(videos):
        del videos[index-1] 
        save_data_helper(videos)
    else:
        print("Invalid Video Index Selected")

def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all Youtube Videos")
        print("2. Add Youtube Video")
        print("3. Update Youtube Video")
        print("4. Delete Youtube Video")
        print("5. Exit the App")

        choice = input("Enter Your Choice: ")

        match choice:
            case '1':
                list_all_videos(videos)
            
            case '2':
                add_video(videos)

            case '3':
                update_video(videos)
            
            case '4':
                delete_video(videos)
            
            case '5':
                break
            
            case _:
                print("Invalid Choice")

if __name__ ==  "__main__":
    main()