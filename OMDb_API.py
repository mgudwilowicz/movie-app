import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

BASE_URL = f"http://www.omdbapi.com/?apikey={API_KEY}"


def getMovieByTitle(title):
    url = f'{BASE_URL}&t={title}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        name = data['Title']
        year = data['Year']
        rating = data['imdbRating']
        poster = data['Poster']
        print(name)
        print(year)
        print(rating)
        print(poster)
        return name, year, rating, poster
    else:
        print("Error:", response.status_code)

getMovieByTitle('titanic')