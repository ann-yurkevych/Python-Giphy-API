import requests


def get_random_gif_url(search_term):
    URL = "https://api.giphy.com/v1/gifs/search"

    params = {
        "api_key": "GiFp2ffdGXNciyoQVRTWtMZogRbmzgua",
        "q": search_term,
        "limit": 1,
        "offset": 0,
        "rating": "g",
        "lang": "en",
        "bundle": "messaging_non_clips",
    }

    response = requests.get(URL, params=params)

    if response.status_code == 200:
        data = response.json()

        if "data" in data and len(data["data"]) > 0:
            gif_url = data["data"][0]["images"]["original"]["url"]
            return gif_url
        else:
            return None
    else:
        return None


def main():
    while True:
        search_term = input("Write the name of the GIF you want to find: ")
        gif_url = get_random_gif_url(search_term)

        if gif_url:
            print(f"We found a GIF for you! Link for {search_term}: {gif_url}")
            break
        else:
            print(f"Sorry, no GIFs found for search '{search_term}'. Please try again.")


if __name__ == "__main__":
    main()


