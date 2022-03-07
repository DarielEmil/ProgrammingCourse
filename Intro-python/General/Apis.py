import requests

if __name__ == '__main__':
    url = "https://www.freetogame.com/api/games"
    response = requests.get(url)

    # print(response)

    if response.status_code == 200:
        content = response.json()
        print(content[0])
