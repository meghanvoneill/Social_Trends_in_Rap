import requests


def main():

    API_URL = 'http://api.genius.com/'
    HEADERS = {'Authorization': 'Bearer '}

    response = requests.get(API_URL + 'songs/378195', headers=HEADERS)

    print(response)
    print(response.text)


if __name__ == '__main__':
    main()
