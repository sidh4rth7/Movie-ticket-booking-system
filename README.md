# Movie Ticket Booking System

## Introduction

The Movie Ticket Booking System is a web application that allows users to browse and book movie tickets for their favorite movies. Users can create accounts, browse available movies by release year, select showtimes, choose seats, and view their booking history.

## Database Schemas and Entities

### Users Table

- `id` (INTEGER, PRIMARY KEY AUTOINCREMENT): Unique identifier for each user.
- `username` (TEXT): User's username for authentication.
- `password` (TEXT): User's hashed password for authentication.

### Movies Data Table

The `movies_data` table stores information about movies available for booking. This table is populated with data from an external CSV file containing movie details.

#### Table Schema

- `id` (INTEGER, PRIMARY KEY AUTOINCREMENT): Unique identifier for each movie.
- `movie_name` (TEXT): The name or title of the movie.
- `theatre_name` (TEXT): The name of the theatre where the movie is being screened.
- `theatre_location` (TEXT): The location or address of the theatre.
- `release_date` (TEXT): The release date of the movie.

#### Description

- `id`: This column serves as a unique identifier for each movie record in the table.

- `movie_name`: The name or title of the movie. Users can browse and select movies by their names.

- `theatre_name`: The name of the theatre where the movie is being screened. It provides information about the screening location.

- `theatre_location`: The location or address of the theatre where the movie is being screened. It helps users find the theatre easily.

- `release_date`: The release date of the movie. It indicates when the movie was released, allowing users to browse movies by release year.

#### Usage

The `movies_data` table is used to provide users with a list of available movies, including details such as the movie name, theatre name, theatre location, and release date. Users can browse and select movies for ticket booking based on this information.


### Bookings Table

- `id` (INTEGER, PRIMARY KEY AUTOINCREMENT): Unique identifier for each booking.
- `user_id` (INTEGER): Foreign key referencing the Users table, identifying the user who made the booking.
- `movie_id` (INTEGER): Foreign key referencing the Movies table, identifying the movie booked.
- `num_tickets` (INTEGER): Number of tickets booked.
- `showtime` (TEXT): Selected showtime for the movie.
- `seats` (TEXT): Comma-separated list of booked seats.

## Hosting "Movie Ticket Booking System" webapp using >StreamlitCommunityCloud

![Deploy](https://github.com/sidh4rth7/Movie-ticket-booking-system/assets/64648070/22d42bc1-2897-4cbf-8125-b51b471bab1d)
![deploy2](https://github.com/sidh4rth7/Movie-ticket-booking-system/assets/64648070/c6ef8be3-d74b-47b8-a9f1-f64b25525be1)


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

![browsemovie](https://github.com/sidh4rth7/Movie-ticket-booking-system/assets/64648070/d0892e31-e722-46aa-a222-932d7c8788ad)


Movie Booking:

![booktickets](https://github.com/sidh4rth7/Movie-ticket-booking-system/assets/64648070/3faa6a1d-3873-41be-80e3-ad41963f1179)

Booking History:

![bookinghistory](https://github.com/sidh4rth7/Movie-ticket-booking-system/assets/64648070/fad1d1cf-0142-4fb0-a92d-0b725bfc9e6a)


## Installation and Usage

1. Clone this repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Set up your database and update the connection details in `config.py`.
4. Run the application using `streamlit run mbs_app.py`.

## (or)
## Visit the web_app using --->[streamlit_link](https://sid-movieticketbookingsystem.streamlit.app/)

## Contribution
Contributions to this project are welcome. Please submit bug reports, feature requests, or pull requests through the GitHub repository.
