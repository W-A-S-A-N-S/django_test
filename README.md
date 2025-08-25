# Django Test Project

This is a simple Django project created to demonstrate basic Django functionalities.

## Features

*   **Article Management:** Create, read, update, and delete articles.
*   **Memo Management:** Create and read memos.
*   **Basic Arithmetic Operations:** Simple API endpoints for addition and multiplication.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Python 3.x
*   Django 4.x

### Installation

1.  Clone the repo
    ```sh
    git clone https://github.com/your_username/django_test.git
    ```
2.  Install dependencies (assuming you have pip installed)
    ```sh
    pip install Django
    ```
3.  Apply migrations
    ```sh
    python manage.py migrate
    ```
4.  Run the development server
    ```sh
    python manage.py runserver
    ```

## Usage

The application will be available at `http://127.0.0.1:8000/`.

## Project Structure

```
.
├── config/             # Django project configuration
├── polls/              # Django app
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py           # Django's command-line utility
└── README.md
```

## API Endpoints

*   `/`: Displays a list of articles.
*   `/hello/`: Returns a "Hello, world!" message.
*   `/lion/<str:name>/`: Greets the user with the provided name.
*   `/good/`: Returns a "Good!" message.
*   `/moon/`: Returns a "Moon!" message.
*   `/add/<int:num1>/<int:num2>/`: Returns the sum of two numbers.
*   `/multiply/<int:num1>/<int:num2>/`: Returns the product of two numbers.
*   `/memo/`: Displays a list of memos.
*   `/memo/<int:memo_id>`: Displays a single memo.
