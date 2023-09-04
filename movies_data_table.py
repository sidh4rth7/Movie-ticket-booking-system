import sqlite3
import pandas as pd

# Initialize SQLite database
conn = sqlite3.connect('movie_ticket_app.db')
c = conn.cursor()

# Load CSV data into the database
df = pd.read_csv('movies.csv')
df.to_sql('movies', conn, if_exists='replace', index=False)

# Close the database connection
conn.close()

#             (id INTEGER PRIMARY KEY AUTOINCREMENT, 
   #          title TEXT,
    #         description TEXT,
     #        release_year INTEGER)