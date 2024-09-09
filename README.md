<h1 align="center">QuickNote</h1>

<h2 align="center">QuickNote is a simple and efficient note-taking web application built with Flask. It allows users to create, store, and manage personal notes securely.</h2>

## Table of Contents

- [Features](#features) 
- [Technologies](#technologies) 
- [Setup](#setup) 
- [Usage](#usage)

## Features

- **User Authentication**: Users can sign up and log in to manage their notes. 
- **Add Notes**: Authenticated users can create and save notes. 
- **Secure Storage**: Passwords are hashed using secure methods. 
- **Responsive Design**: The user interface is optimized for both desktop and mobile devices using Bootstrap. 
- **Database Integration**: Data is stored in a SQLite database.

## Technologies

- **Backend**: Flask (Python Web Framework) 
- **Frontend**: HTML, CSS (with Bootstrap), JavaScript 
- **Database**: SQLite (via SQLAlchemy ORM) 
- **User Authentication**: Flask-Login and Werkzeug for secure password handling 
- **Templating Engine**: Jinja2 (Flask's built-in)

## Setup

To get the QuickNote project up and running on your local machine, follow these steps:

1. **Clone the repository:** 
   ```bash 
   git clone https://github.com/AhmedRady66/QuickNote

2. **Navigate to the project directory:**

    ```bash
    cd QuickNote 

3. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv 
    source venv/bin/activate  # On Windows use `venv\Scripts\activate` 

4. **Run the Flask development server:**

    ```bash
    flask run 
The app should now be running on http://127.0.0.1:5000/.

## Usage
1. Open your browser and go to http://127.0.0.1:5000/.
1. Sign up for a new account.
1. Log in and start creating notes.
1. Add new notes, view existing ones, and manage your note-taking efficiently.

