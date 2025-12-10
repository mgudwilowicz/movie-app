from sqlalchemy import create_engine, text


DB_URL = "sqlite:///movies.db"
engine = create_engine(DB_URL)


with engine.connect() as connection:
    connection.execute(text("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT UNIQUE NOT NULL,
            year INTEGER NOT NULL,
            rating REAL NOT NULL,
            poster TEXT NOT NULL
        )
    """))
    connection.commit()
print("Table 'movies' created (or already exists).")


def get_movies():
    """Return a list of all movies from the database as dictionaries with title, year, and rating."""
    with engine.connect() as connection:
        result = connection.execute(text("SELECT title, year, rating, poster FROM movies"))
        movies = result.fetchall()

    return {row[0]: {"year": row[1], "rating": row[2], 'poster': row[3]} for row in movies}


def add_movie(title, year, rating, poster):
    """Add a new movie with the given title, year, and rating to the database."""
    with engine.connect() as connection:
            try:
                connection.execute(text("INSERT INTO movies (title, year, rating, poster) VALUES (:title, :year, :rating, :poster)"),
                                   {"title": title, "year": year, "rating": rating, "poster": poster})
                connection.commit()
                print(f"Movie '{title}' added successfully.")
            except Exception as e:
                print(f"Error: {e}")


def delete_movie(title):
    """Delete the movie with the given title from the database."""
    with engine.connect() as connection:
        try:
            connection.execute(
                text("DELETE FROM movies WHERE title = :title"),
                {"title": title}
            )
            connection.commit()
            print(f"Movie '{title}' deleted successfully.")
        except Exception as e:
            print(f"Error: {e}")


def update_movie(title, rating):
    """Update the rating of the movie with the given title in the database."""
    with engine.connect() as connection:
        try:
            connection.execute(
                text("UPDATE movies SET rating = :rating WHERE title = :title"),
                {"rating": rating, "title": title}
            )
            connection.commit()
            print(f"Movie '{title}' updated successfully.")
        except Exception as e:
            print(f"Error: {e}")
