import streamlit as st
import sqlite3
import hashlib
import pandas as pd

# Initialize SQLite database
conn = sqlite3.connect('movie_ticket_app.db')
c = conn.cursor()

# Create Users table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users 
             (id INTEGER PRIMARY KEY AUTOINCREMENT, 
             username TEXT, 
             password TEXT)''')

# Create Movies table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS movies''')

# Create Bookings table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS bookings 
             (id INTEGER PRIMARY KEY AUTOINCREMENT, 
             user_id INTEGER,
             movie_id INTEGER,
             num_tickets INTEGER,
             showtime TEXT,
             seats TEXT)''')

# Function to create a new user
def create_user(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()

# Function to check if a user exists
def user_exists(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed_password))
    return c.fetchone() is not None

# Function to get the user's ID by username
def get_user_id(username):
    c.execute("SELECT id FROM users WHERE username = ?", (username,))
    result = c.fetchone()
    if result:
        return result[0]
    else:
        return None

# Function to create a new movie
def create_movie(title, description, release_year):
    c.execute("INSERT INTO movies (title, description, release_year) VALUES (?, ?, ?)", (title, description, release_year))
    conn.commit()

# Function to get a list of movies by release year
def get_movies_by_release_year(year):
    c.execute("SELECT movie_name, release_date FROM movies WHERE strftime('%Y', release_date) = ?", (str(year),))
    return c.fetchall()

# Function to book tickets
def book_tickets(user_id, movie_id, num_tickets, showtime, seats):
    c.execute("INSERT INTO bookings (user_id, movie_id, num_tickets, showtime, seats) VALUES (?, ?, ?, ?, ?)",
              (user_id, movie_id, num_tickets, showtime, seats))
    conn.commit()

# Function to get booking history for a user
def get_booking_history(user_id):
    c.execute("""
        SELECT b.id, m.title, b.showtime, b.seats 
        FROM bookings b 
        JOIN movies m ON b.movie_id = m.id 
        WHERE b.user_id = ?
    """, (user_id,))
    return c.fetchall()


# Streamlit app layout
st.title("Movie Ticket Booking App")

# Streamlit SessionState to manage user sessions
if 'user' not in st.session_state:
    st.session_state.user = None

# Login or Sign-up option
option = st.radio("Choose an option:", ("Login", "Sign-up"))

if option == "Sign-up":
    st.subheader("Sign-up")
    new_username = st.text_input("Username:")
    new_password = st.text_input("Password:", type="password")
    
    if st.button("Sign-up"):
        if new_username and new_password:
            create_user(new_username, new_password)
            st.success("Account created successfully. You can now log in.")
        else:
            st.error("Both username and password are required for sign-up.")
elif option == "Login":
    st.subheader("Login")
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")
    
    if st.button("Login"):
        if username and password:
            if user_exists(username, password):
                st.success(f"Welcome, {username}!")
                st.session_state.user = username
                # Redirect to the movie booking page
            else:
                st.error("Invalid username or password. Please try again.")
        else:
            st.error("Both username and password are required for login.")

# Movie browsing page
if st.session_state.user:
    st.subheader("Browse Movies by Release Year")
    
    # Filter movies by release year
    st.write("Select a release year to browse movies:")
    selected_year = st.selectbox("Release Year:", range(1900, 2101))
    
    movies = get_movies_by_release_year(selected_year)
    
    if movies:
        st.write(f"Movies released in {selected_year}:")
        for movie in movies:
            st.write(f"**Movie Name:** {movie[0]}")
            st.write(f"**Release Date:** {movie[1]}")
            st.write("----")
    else:
        st.warning("No movies found for the selected year.")
    
    # Filter movies by release year
    st.write("Select a release year to browse movies:")
    selected_year = st.selectbox("Release Year:", range(1900, 2101))
    
    movies = get_movies_by_release_year(selected_year)
    
    if movies:
        st.write(f"Movies released in {selected_year}:")
        for movie in movies:
            st.write(f"**Title:** {movie[0]}")
            st.write(f"**Description:** {movie[1]}")
            st.write("----")
    else:
        st.warning("No movies found for the selected year.")

# Movie booking page
if st.session_state.user:
    st.subheader("Movie Booking")
    
    # Sample movie data
    movies = [
        {"title": "Movie A", "description": "Action-packed thriller"},
        {"title": "Movie B", "description": "Romantic comedy"},
        {"title": "Movie C", "description": "Sci-fi adventure"},
    ]
    
    # Create a DataFrame from the movie data
    movies_df = pd.DataFrame(movies)
    
    # Display movie selection dropdown
    selected_movie = st.selectbox("Select a movie:", movies_df["title"])
    
    # Display movie description
    st.write(f"**Description:** {movies_df.loc[movies_df['title'] == selected_movie]['description'].values[0]}")
    
    # Number of tickets to book
    num_tickets = st.number_input("Number of Tickets:", min_value=1, max_value=10, value=1)
    
    # Showtime selection
    showtime = st.text_input("Showtime (e.g., 7:00 PM):")
    
    # Seat selection (up to 10 seats)
    st.write("Select up to 10 seats:")
    selected_seats = st.multiselect("Seats:", ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"])
    
    # Book button
    if st.button("Book Tickets"):
        if len(selected_seats) <= 10:
            user_id = get_user_id(st.session_state.user)
            if user_id:
                # Retrieve the movie ID
                movie_id = movies_df.loc[movies_df['title'] == selected_movie].index[0] + 1
                
                # Convert selected seats to a comma-separated string
                seats_str = ",".join(selected_seats)
                
                book_tickets(user_id, movie_id, num_tickets, showtime, seats_str)
                st.success(f"Booked {num_tickets} ticket(s) for {selected_movie} on {showtime}. Seats: {seats_str}")
        else:
            st.error("You can book a maximum of 10 seats.")

# Booking history page
if st.session_state.user:
    st.subheader("Booking History")
    
    user_id = get_user_id(st.session_state.user)
    if user_id:
        bookings = get_booking_history(user_id)
        
        if bookings:
            st.write("Your Booking History:")
            for booking in bookings:
                st.write(f"**Movie:** {booking[1]}")
                st.write(f"**Showtime:** {booking[2]}")
                st.write(f"**Seats:** {booking[3]}")
                st.write("----")
        else:
            st.info("No booking history available.")
    else:
        st.warning("User not found.")

# Close the database connection
conn.close()
