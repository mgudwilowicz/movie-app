import webbrowser
import os

def generate_movies_html(movies):
    """Generates an HTML file by inserting animal data into a template and adding UTF-8 metadata."""
    with open("_static/index_template.html", "r", encoding="utf-8") as f:
        html_template = f.read()
        html_template = html_template.replace("<head>","<head>\n    <meta charset=\"UTF-8\">")

    html_output = html_template.replace("__TEMPLATE_TITLE__", "My Movie app")
    print(movies)
    output = ''
    for movie in movies.items():
        title, info = movie
        year = info['year']
        poster = info['poster']
        output += generate_card(poster, title, year)


    html_output = html_output.replace("__TEMPLATE_MOVIE_GRID__",output )

    output_path = "_static/index.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_output)


    absolute_path = os.path.abspath(output_path)

    try:
        webbrowser.open(f"file://{absolute_path}")
        print("Website was generated successfully.")
    except Exception as e:
        print(f"Could not open browser automatically: {e}")



def generate_card(poster, title, year):
    card = ''
    card += '<li>'
    card += '<div class="movie">'
    card += f'<img class="movie-poster" src="{poster}">'
    card += f'<div class="movie-title">{title}</div>'
    card += f'<div class="movie-year">{year}</div>'
    card += '</div>'
    card += '</li>'
    return card
