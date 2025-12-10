import random

movies = {
    "The Shawshank Redemption": 9.5,
    "Happy Feet": 9.5,
    "Pulp Fiction": 8.8,
    "Motylek": 9.5,
    "The Room": 3.6,
    "The Godfather": 9.2,
    "The Godfather: Part II": 9.0,
    "The Dark Knight": 9.0,
    "12 Angry Men": 8.9,
    "Everything Everywhere All At Once": 8.9,
    "Forrest Gump": 8.8,
    "Star Wars: Episode V": 8.7,

}


def list_of_movies():
    print(f'{len(movies)} movies in total')
    for movie, rating in movies.items():
        print(f"{movie}: {rating}")


def add_movie():
    movie_name = input("Enter new movie name:")
    movie_rating = input("Enter new movie rating (0-10): ")
    movies[movie_name] = float(movie_rating)
    print(f'Movie {movie_name} successfully added')


def remove_movie():
    movie_to_delete = input('Enter movie name to delete: ')
    if movie_to_delete in movies.keys():
        print(f'Movie {movie_to_delete} successfully deleted')
        del movies[movie_to_delete]
    else:
        print(f'Movie {movie_to_delete} doesnt exist!')


def update():
    movie = input('Enter movie name: ')
    if movie in movies.keys():
        movie_rating = input(f'Enter new movie rating (0-10): ')
        movies[movie] = float(movie_rating)
        print(f'Movie {movie} successfully updated')
    else:
        print(f'Movie {movie} doesnt exist!')


def best_movies(best_rating):
    for title, rating in movies.items():
        if rating == best_rating:
            print(f'Best movie: {title}, {rating}')


def worst_movies(wors_rating):
    for title, rating in movies.items():
        if rating == wors_rating:
            print(f'Worst movie: {title}, {rating}')


def movies_median(list, n):
    if n % 2 == 1:
        median = list[n // 2]
    else:
        mid1 = list[n // 2 - 1]
        mid2 = list[n // 2]
        median = (mid1 + mid2) / 2

    print(f'Median rating: {round(median, 2)}')


def stats():
    ratings = list(movies.values())
    rating_sum = sum(ratings)
    print(f'Average rating: {round(rating_sum / len(movies), 2)}')

    ratings.sort()
    n = len(ratings)

    movies_median(ratings, n)

    best_rating = ratings[-1]
    worst_rating = ratings[0]

    best_movies(best_rating)
    worst_movies(worst_rating)


def random_movie():
    movie = random.choice(list(movies.items()))
    print(f"Your movie for tonight: {movie[0]}, it's rated {movie[1]}")


def search_movie():
    user_input = input("Enter part of movie name:")
    found = False

    for title in movies.keys():
        if user_input.lower() in title.lower():
            print(title, movies[title])
            found = True

    if not found:
        print(f'No movie matching "{user_input}" was found in the database.')


def sort_movies():
    sorted_movies = sorted(movies.items(), key=lambda item: item[1], reverse=True)

    for movie in sorted_movies:
        print(f'{movie[0]}: {movie[1]}')


def main():
    while True:
        user_input = input(
            "********** Movies Database **********\n \nMenu: \n1. List movies\n2. Add movie\n3. Delete movie\n4. Update movie\n5. Stats\n6. Random movie\n7. Search movie\n8. Movies sorted by rating\n\nEnter choice (1-8): ")

        if user_input != "":
            user_input = int(user_input)
        else:
            print('Choose number between 1 to 10')

        if user_input == 1:
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

        input('Press enter to continue')


if __name__ == "__main__":
    main()
