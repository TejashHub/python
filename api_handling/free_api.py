import requests

def fetch_random_user_freeapi():
    url = 'https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=20'

    response = requests.get(url)

    data = response.json()

    if data['success'] and 'data' in data and 'data' in data['data']:
        users = data['data']['data']
        if users:
            user = users[0] 
            username = user['login']['username']
            country = user['location']['country']
            email = user['email']
            return username, email, country
        else:
            raise Exception("No users found in the response!")
    else:
        raise Exception("Failed to Fetch User Data! ")
    
def main():
    try:
        username, email, country = fetch_random_user_freeapi()
        print(f'username: {username} email:  {email} country: {country}')
    except Exception as e:
        print(str(e))

if __name__ == '__main__' :
    main()