import random
import movie_storage_sql as movie_storage
from OMDb_API import getMovieByTitle
from generate_html import generate_movies_html
from movie_storage_sql import get_movies


def list_of_movies():
    """Print all movies with their release year and rating."""
    movies = movie_storage.get_movies()
    print(f'{len(movies)} movies in total')

    for movie, details in movies.items():
        print(f'{movie}({details["year"]}): {details["rating"]}')


def add_movie():
    """Prompt user to add a new movie and save it to the database."""
    movies = movie_storage.get_movies()

    title= input("Enter new movie name:").strip()
    if not title:
        print("Movie name cannot be empty!")
        return
    if title in movies:
        print(f"Movie {title} already exist!")
        return

    name, year, rating, poster = getMovieByTitle(title)

    movie_storage.add_movie(name, year, rating, poster)
    print(f'Movie {name}({year}): {rating} successfully added')


def remove_movie():
    """Prompt user to delete a movie from the database."""
    movies = movie_storage.get_movies()
    movie_to_delete = input('Enter movie name to delete: ').strip()
    if not movie_to_delete:
        print("Movie name cannot be empty!")
        return

    if movie_to_delete in movies.keys():
        movie_storage.delete_movie(movie_to_delete)
        print(f'Movie {movie_to_delete} successfully deleted')
    else:
        print(f'Movie {movie_to_delete} doesnt exist!')


def update():
    """Prompt user to update the rating of an existing movie."""
    movies = movie_storage.get_movies()
    movie_title = input('Enter movie name: ').strip()
    if not movie_title:
        print("Movie name cannot be empty!")
        return

    if movie_title in movies:
        try:
            movie_rating = float(input(f'Enter new movie rating (0-10): ').strip())
            if not (0 <= movie_rating <= 10):
                print("Rating must be between 0 and 10!")
                return
        except ValueError:
            print("Invalid input for rating, must be a number!")
            return

        movie_storage.update_movie(movie_title, movie_rating)
        print(f'Movie {movie_title} successfully updated')
    else:
        print(f'Movie {movie_title} doesnt exist!')


def movies_median(ratings):
    """Calculate and return the median of a list of ratings."""
    n = len(ratings)
    ratings.sort()
    if n % 2 == 1:
        median = ratings[n // 2]
    else:
        mid1 = ratings[n // 2 - 1]
        mid2 = ratings[n // 2]
        median = (mid1 + mid2) / 2
    return round(median, 2)


def stats():
    """Print statistics: average, median, best and worst rated movies."""
    movies = movie_storage.get_movies()
    if not movies:
        print("No movies in database!")
        return

    ratings = [details["rating"] for details in movies.values()]
    avg_rating = sum(ratings) / len(ratings)
    median = float(movies_median(ratings))

    best_movie = max(movies.items(), key=lambda x: x[1]["rating"])
    worst_movie = min(movies.items(), key=lambda x: x[1]["rating"])

    print(f'Average rating: {avg_rating:.1f}')
    print(f'Median rating: {median:.1f}')
    print(f'Best movie: {best_movie[0]}({best_movie[1]["year"]}): {best_movie[1]["rating"]}')
    print(f'Worst movie: {worst_movie[0]}({worst_movie[1]["year"]}): {worst_movie[1]["rating"]}')


def random_movie():
    """Select and print a random movie from the database."""
    movies = movie_storage.get_movies()
    if not movies:
        print("No movies in database!")
        return

    movie= random.choice(list(movies.items()))
    title = movie[0]
    details = movie[1]
    print(f"Your movie for tonight: {title}({details['year']}), it's rated {details['rating']}")


def search_movie():
    """Search for movies by partial name match and print results."""
    movies = movie_storage.get_movies()

    user_input= input("Enter part of movie name:").strip().lower()
    found = False

    for movie, details in movies.items():
        if user_input.lower() in movie.lower():
            print(f"{movie}({details['year']}): {details['rating']}")
            found=True

    if not found:
        print(f'No movie matching "{user_input}" was found in the database.')


def sort_movies():
    """Print all movies sorted by rating in descending order."""
    movies = movie_storage.get_movies()
    if not movies:
        print("No movies in database!")
        return

    sorted_movies = sorted(movies.items(), key=lambda item: item[1]["rating"], reverse=True)
    for movie, details in sorted_movies:
        print(f'{movie}({details["year"]}): {details["rating"]}')


def sort_movies_chronologically():
    """Print all movies sorted by release year, ask user if newest first or oldest first."""
    movies = movie_storage.get_movies()
    if not movies:
        print("No movies in database!")
        return

    while True:
        choice = input("Show latest movies first or last? (latest/oldest): ").strip().lower()
        if choice not in ("latest", "oldest"):
            print("Please enter 'latest' or 'oldest'.")
            continue
        break

    reverse_order = True if choice == "latest" else False
    sorted_movies = sorted(movies.items(), key=lambda item: item[1]["year"], reverse=reverse_order)

    for movie, details in sorted_movies:
        print(f'{movie}({details["year"]}): {details["rating"]}')


def main():
    """Main program loop displaying the menu and handling user input."""
    while True:
        user_input = input(
            "********** Movies Database **********\n\n"
            "Menu:\n"
            "0. Exit\n"
            "1. List movies\n"
            "2. Add movie\n"
            "3. Delete movie\n"
            "4. Update movie\n"
            "5. Stats\n"
            "6. Random movie\n"
            "7. Search movie\n"
            "8. Movies sorted by rating\n"
            "9. Movies sorted by year\n"
            "10. Generate html site\n"
            
            "Enter choice (0-10): "
        ).strip()

        try:
            user_input = int(user_input)
        except ValueError:
            print("Choose a number between 0 and 10")
            continue

        if user_input == 0:
            print("Bye!")
            break
        elif user_input == 1:
            list_of_movies()
        elif user_input == 2:
            add_movie()
        elif user_input == 3:
            remove_movie()
        elif user_input == 4:
            update()
        elif user_input == 5:
            stats()
        elif user_input == 6:
            random_movie()
        elif user_input == 7:
            search_movie()
        elif user_input == 8:
            sort_movies()
        elif user_input == 9:
            sort_movies_chronologically()
        elif user_input == 10:
            generate_movies_html(get_movies())

        input('Press enter to continue')


if __name__ == "__main__":
  main()
