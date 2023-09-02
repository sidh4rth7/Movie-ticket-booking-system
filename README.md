# Movie Ticket Booking System

## Introduction

The Movie Ticket Booking System is a web application that allows users to browse and book movie tickets for their favorite movies. Users can create accounts, browse available movies by release year, select showtimes, choose seats, and view their booking history.

## Database Schemas and Entities

### Users Table

- `id` (INTEGER, PRIMARY KEY AUTOINCREMENT): Unique identifier for each user.
- `username` (TEXT): User's username for authentication.
- `password` (TEXT): User's hashed password for authentication.

### Movies Table

- `id` (INTEGER, PRIMARY KEY AUTOINCREMENT): Unique identifier for each movie.
- `title` (TEXT): Title of the movie.
- `description` (TEXT): Description or summary of the movie.
- `release_year` (INTEGER): Year of the movie's release.

### Bookings Table

- `id` (INTEGER, PRIMARY KEY AUTOINCREMENT): Unique identifier for each booking.
- `user_id` (INTEGER): Foreign key referencing the Users table, identifying the user who made the booking.
- `movie_id` (INTEGER): Foreign key referencing the Movies table, identifying the movie booked.
- `num_tickets` (INTEGER): Number of tickets booked.
- `showtime` (TEXT): Selected showtime for the movie.
- `seats` (TEXT): Comma-separated list of booked seats.

## Screenshots



## Installation and Usage

1. Clone this repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Set up your database and update the connection details in `config.py`.
4. Run the application using `streamlit run mbs_app.py`.

## Contributing

Contributions to this project are welcome. Please submit bug reports, feature requests, or pull requests through the GitHub repository.