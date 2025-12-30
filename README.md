# Student Manager Flask API

A robust and scalable RESTful API built with Flask to demonstrate a production-ready backend solution for a student management system. This project showcases a clean architecture, modern development practices, and a comprehensive feature set designed to impress.

## Features

- **Secure User Authentication**: JWT-based authentication for protected endpoints.
- **Comprehensive Data Management**: Full CRUD operations for students, users, and grades.
- **Advanced Querying**: Includes powerful filtering and pagination for student records.
- **Integrated Services**:
    - **AWS S3**: For seamless student profile picture uploads.
    - **SMS Notifications**: To send updates directly to students.
- **Designed for Integration**: A complete suite of API endpoints ready for any frontend application.


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

A comprehensive set of RESTful API endpoints are available for managing:

- **Auth**: User login and logout to manage authentication tokens.
- **Users**: CRUD operations for user management.
- **Students**: CRUD operations for student records, including functionalities for sending SMS and uploading profile pictures.
- **Student Grades**: CRUD operations for managing grades associated with individual students.

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
