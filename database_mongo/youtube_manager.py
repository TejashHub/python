from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://youtubeManager:youtubeManager@cluster0.kitjx.mongodb.net/youtubeManager")

db = client['youtube_manager']

Collection = db["videos"]

def list_all_videos():
    videos = Collection.find()
    for video in videos:
        print(f"video id: {video['_id']}  video name: {video['name']}  video time: {video['time']}")

def add_video(name, time):
    Collection.insert_one({'name':name, 'time':time})
    print("Video added successfully!")

def update_video(_id, name, time):
    print(_id, name, time)
    try:
        result = Collection.update_one({'_id': ObjectId(_id) }, {'$set':{'name':name, 'time':time}})
        if result.matched_count:
                print("Video updated successfully!")
        else:
                print("Video not found!")
    except Exception as e:
        print(e)

def delete_video(_id): 
    try:
        result = Collection.delete_one({'_id': ObjectId(_id) })
        if result.deleted_count:
                print("Video deleted successfully!")
        else:
                print("Video not found!")
    except Exception as e:
        print(e)

def main():
    while True:
        print('\n')
        print('*'* 70)
        print('Youtube Management App')
        print('*'* 70)
        print('\n')
        print('1. List all videos')
        print('2. Add a new videos')
        print('3. Update a new videos')
        print('4. Delete a videos')
        print('5. Exit App')
        print('\n')
        choice = input("Enter Your Choice: ")

        match choice:

            case '1':
                print('\n')
                print('*'* 70)
                list_all_videos()
                print('*'* 70)
                print('\n')

            case '2':
                name = input('Enter Youtube Name: ')
                time = input('Enter Youtube Time: ')
                add_video(name, time)

            case '3':
                _id = input('Enter Youtube ID: ')
                name = input('Enter New Youtube Name: ')
                time = input('Enter New Youtube Time: ')
                update_video(_id ,name, time)

            case '4':
                _id = input('Enter Youtube ID: ')
                delete_video(_id)

            case '5':
                break

            case _:
                print('Invalid Choice')

if __name__ == '__main__':
    main()