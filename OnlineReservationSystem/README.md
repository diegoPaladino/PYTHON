# OnlineReservationSystem

## Introduction
OnlineReservationSystem is a web-based application developed using Python and Flask. It allows users to make reservations online, specifying their name, email, desired date, and time. The system stores reservations in an SQLite database and provides an interface for viewing all reservations.

## List of Necessary Materials
- Python 3.x
- Flask
- Flask-SQLAlchemy
- SQLite

## Project Purpose
The purpose of this project is to provide a simple and efficient online reservation system. Users can easily make reservations, and administrators can view all reservations in a centralized location. This system is suitable for restaurants, events, or any service requiring reservations.

## Pros and Cons
### Pros
- Simple and user-friendly interface
- Easy to set up and deploy
- Uses a lightweight SQLite database
### Cons
- Basic functionality, may need customization for specific needs
- Does not include user authentication

## General Guidelines
### Setup and Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/OnlineReservationSystem.git
    ```
2. Navigate to the project directory:
    ```bash
    cd OnlineReservationSystem
    ```
3. Install the required packages:
    ```bash
    pip install flask flask_sqlalchemy
    ```
4. Run the application:
    ```bash
    python app.py
    ```

### Usage
1. Open a web browser and go to `http://127.0.0.1:5000/`.
2. Use the form to make a reservation.
3. View all reservations at `http://127.0.0.1:5000/reservations`.

## License
This project is open-source and free to use. Feel free to modify and distribute it as needed.
