import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cusor = conn.cursor()

cusor.execute(''' 
    CREATE TABLE IF NOT EXISTS video(
            id  INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
        )
''')

def list_videos():
    cusor.execute("SELECT * FROM video")
    for row in cusor.fetchall():
        print(row)

def add_videos(name, time):
    cusor.execute("INSERT INTO video (name, time) VALUES (?, ?)", (name, time))

def update_videos(_id, name, time):
    cusor.execute("UPDATE video SET name = ?, time = ? where id = ?",(name, time, _id))

def delete_videos(_id):
    cusor.execute("DELETE FROM video where id = ?",(_id,))

def main():
    while True:
        print('\n Youtube Manager App  with Sqlite3')
        print('*' * 70)
        print('\n')
        print('1. List all video')
        print('2. Add Video')
        print('3. Update Video')
        print('4. Delete Video')
        print('5. Exits App')
        print('\n')

        choice = input('Enter your choice: ')

        if choice == '1':
            list_videos()

        elif choice == '2':
            name = input('Enter video name: ')
            time = input('Enter video time: ')
            add_videos(name, time)
        
        elif choice == '3':
            _id = input('Enter video ID to update: ')
            name = input('Enter video name: ')
            time = input('Enter video time: ')
            update_videos(_id, name, time)
        
        elif choice == '4':
            _id = input('Enter video ID to delete: ')
            delete_videos(_id)
        
        elif choice == '5':
            break

        else:
            print('Invalid Choice')

    conn.close()

if __name__ == "__main__" : 
    main()