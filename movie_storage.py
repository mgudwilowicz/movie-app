import json


def get_movies():
    """Return the dictionary of all movies from the JSON file."""
    with open("data.json", "r") as file:
        data = json.load(file)
    return data


def save_movies(movies):
    """Save the given dictionary of movies to the JSON file."""
    with open("data.json", "w", ) as file:
        json.dump(movies, file, indent=4)


def add_movie(title, year, rating):
    """Add a new movie with the given title, year, and rating to the database."""
    movies = get_movies()
    movies[title] = {"year": year, "rating" : rating}
    save_movies(movies)


def delete_movie(title):
    """Delete the movie with the given title from the database."""
    movies = get_movies()
    del movies[title]
    save_movies(movies)


def update_movie(title, rating):
    """Update the rating of the movie with the given title in the database."""
    movies = get_movies()
    movies[title]["rating"] = rating
    save_movies(movies)