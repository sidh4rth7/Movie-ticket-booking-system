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


Deploying app:

![DeployApp](https://github.com/sidh4rth7/Movie-ticket-booking-system/assets/64648070/51e0892a-7dd1-4d75-9efb-6bc74916ba6f)

Signing up:

![SignUp](https://github.com/sidh4rth7/Movie-ticket-booking-system/assets/64648070/9f007d3a-19c6-44c9-b76b-c362ab99007e)

LogIn Success:

![LogInSuccess](https://github.com/sidh4rth7/Movie-ticket-booking-system/assets/64648070/69d0270a-4d43-4132-bf4b-59f6fccb9808)

LogIn Fail(other case):

![LogInFail](https://github.com/sidh4rth7/Movie-ticket-booking-system/assets/64648070/9e405940-423c-4bae-9941-bc012c8f1eaa)

Browse Movie:

![BrowseMovie](https://github.com/sidh4rth7/Movie-ticket-booking-system/assets/64648070/b5922e62-2415-4554-a5c8-04392b0ac11e)
![ViewMovieByYear](https://github.com/sidh4rth7/Movie-ticket-booking-system/assets/64648070/610356ba-5fcc-4d92-a85e-6e24f6110bfb)

Movie Booking:

![MovieBooking](https://github.com/sidh4rth7/Movie-ticket-booking-system/assets/64648070/211a41c6-7952-423f-8105-845143b0718d)

## Installation and Usage

1. Clone this repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Set up your database and update the connection details in `config.py`.
4. Run the application using `streamlit run mbs_app.py`.

## Contributing

Contributions to this project are welcome. Please submit bug reports, feature requests, or pull requests through the GitHub repository.
