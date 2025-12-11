🎬 Movies Database — CLI Application
---
A command-line application for managing a personal movie collection.
Movies are stored in an SQLite database, and the app fetches movie details automatically from the OMDb API.
You can add, delete, update, sort, search, generate statistics, and export movies to an HTML page.

## Features:
- **List movies** – display all saved movies  
- **Add movie** – fetch details from OMDb API  
- **Delete movie**  
- **Update movie rating**  
- **Statistics** (average, median, best/worst)  
- **Search by title**  
- **Sort by rating or year**  
- **Generate HTML page**

## Requirements

- Python 3.8+
- Internet connection (for OMDb API)
- OMDb API key (if used in your setup)
- SQLite (included with Python)



```text

project/
├── main.py                     # Main CLI program
├── movie_storage_sql.py        # SQLite database handling
├── OMDb_API.py                 # OMDb API requests
├── generate_html.py            # HTML generator
├── _static/                    # Static files for website
│   ├── index_template.html     # HTML template used to generate index.html
│   └── index.html              # Generated HTML page with movie collection
├── movies.db                   # Local SQLite database
├── .env                        # Environment variables (API keys, config)
├── .gitignore                  # Specifies files/folders Git should ignore
└── README.md                   # Project documentation


