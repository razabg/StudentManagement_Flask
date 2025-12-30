# Student Manager Flask API

This is a comprehensive Flask-based RESTful API for managing students and their grades. It provides a complete backend solution with features like user authentication, student data management, grade tracking, and more.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [API Endpoints](#api-endpoints)
  - [Auth](#auth)
  - [Users](#users)
  - [Students](#students)
  - [Student Grades](#student-grades)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- User registration and authentication with JWT.
- CRUD operations for students, users, and student grades.
- Advanced filtering and pagination for student records.
- SMS notifications to students.
- Profile picture uploads for students.
- A comprehensive suite of API endpoints for seamless integration with any frontend application.

## Technologies Used

- **Backend:**
  - [Flask](https://flask.palletsprojects.com/): A lightweight WSGI web application framework in Python.
  - [Flask-RESTX](https://flask-restx.readthedocs.io/): An extension for Flask that adds support for quickly building REST APIs.
  - [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/): An extension for Flask that adds support for SQLAlchemy.
  - [Flask-Migrate](https://flask-migrate.readthedocs.io/): An extension that handles SQLAlchemy database migrations for Flask applications using Alembic.
  - [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/): A Flask extension that provides bcrypt hashing utilities for your application.
- **Database:**
  - [PostgreSQL](https://www.postgresql.org/): A powerful, open-source object-relational database system.
  - [SQLAlchemy](https://www.sqlalchemy.org/): The Python SQL toolkit and Object Relational Mapper.
  - [Alembic](https://alembic.sqlalchemy.org/): A lightweight database migration tool for usage with the SQLAlchemy Database Toolkit.
- **Deployment:**
  - [Docker](https://www.docker.com/): A platform for developing, shipping, and running applications in containers.
- **AWS Integration:**
  - [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html): The AWS SDK for Python, used for services like S3 for file uploads.

## Getting Started

### Prerequisites

- [Docker](https.docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/Student_manager_Flask.git
   cd Student_manager_Flask
   ```

2. **Create a `.env` file** from the `.env.example` and update the environment variables as needed.

   ```bash
   cp .env.example .env
   ```

3. **Build and run the application using Docker Compose:**

   ```bash
   docker-compose up -d --build
   ```

4. **Initialize the database and apply migrations:**

   ```bash
   docker exec -it pyserver flask --app manage.py db init
   docker exec -it pyserver flask --app manage.py db migrate -m "Initial migration"
   docker exec -it pyserver flask --app manage.py db upgrade
   ```

The application will be running at `http://localhost:5000`.

## API Endpoints

### Auth

- `POST /auth/login`: Authenticate a user and receive a JWT token.
- `POST /auth/logout`: Log out a user and invalidate their token.

### Users

- `GET /users/`: Get a list of all users.
- `POST /users/`: Create a new user.
- `GET /users/{public_id}`: Get a specific user by their public ID.

### Students

- `GET /students/`: Get a list of all students with optional filtering and pagination.
- `POST /students/`: Create a new student.
- `GET /students/{id}`: Get a specific student by their ID.
- `PUT /students/{id}`: Update a student's information.
- `DELETE /students/{id}`: Delete a student.
- `POST /students/sms`: Send an SMS to a list of students.
- `POST /students/picture`: Upload a profile picture for a student.

### Student Grades

- `GET /students/{student_id}/grade`: Get all grades for a specific student.
- `POST /students/{student_id}/grade`: Add a new grade for a student.
- `PUT /students/{student_id}/grade/{id}`: Update a specific grade.
- `DELETE /students/{student_id}/grade/{id}`: Delete a specific grade.

## Project Structure

```
├── app
│   ├── main
│   │   ├── controller
│   │   ├── model
│   │   ├── service
│   │   └── util
│   └── test
├── migrations
├── .dockerignore
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── README.md
└── requirements.txt
```

- `app/main`: The core application logic.
  - `controller`: Defines the API endpoints.
  - `model`: Contains the database models.
  - `service`: Implements the business logic.
  - `util`: Utility functions and decorators.
- `app/test`: Contains the application's tests.
- `migrations`: Database migration scripts.
- `manage.py`: The main entry point for running the application and managing database migrations.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or feature requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
