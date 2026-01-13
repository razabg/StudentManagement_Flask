# Student Manager Flask API

A production-ready RESTful API for student management, built with Flask and modern backend technologies. Demonstrates clean architecture, cloud integration, and security best practices.

## 🚀 Tech Stack

**Backend:** Python 3.x • Flask • SQLAlchemy • PostgreSQL • Flask-Migrate  
**Security:** JWT (Flask-JWT-Extended) • Bcrypt  
**DevOps:** Docker • Docker Compose • Gunicorn  
**Cloud:** AWS S3 • SMS Gateway Integration  
**API Documentation:** Swagger/OpenAPI • Flask-RESTX  

## ✨ Key Features

- JWT-based authentication with token refresh
- Full CRUD operations for students, users, and grades
- Advanced filtering, sorting, and pagination
- AWS S3 integration for profile picture uploads
- SMS notification system
- Interactive API documentation with Swagger UI
- Layered architecture (Controller → Service → Model)
- Fully containerized with Docker

## 🚦 Getting Started

### Prerequisites
Docker • Docker Compose

### Quick Start

1. **Clone and configure:**
   ```bash
   git clone https://github.com/your-username/Student_manager_Flask.git
   cd Student_manager_Flask
   cp .env.example .env  # Update with your credentials
   ```

2. **Run with Docker:**
   ```bash
   docker-compose up -d --build
   ```

3. **Initialize database:**
   ```bash
   docker exec -it pyserver flask --app manage.py db init
   docker exec -it pyserver flask --app manage.py db migrate -m "Initial migration"
   docker exec -it pyserver flask --app manage.py db upgrade
   ```

API runs at `http://localhost:5000`

## 📚 API Documentation

Interactive Swagger UI available at: `http://localhost:5000/swagger`

Explore and test all endpoints directly from your browser with automatically generated API documentation.

## 📡 API Endpoints

**Auth:** `/auth/login`, `/auth/logout`, `/auth/refresh`  
**Users:** `/users` - Full CRUD operations  
**Students:** `/students` - CRUD + SMS + Photo upload  
**Grades:** `/students/<id>/grades` - Grade management



## 🤝 Contributing

Contributions welcome! Fork, create a feature branch, and submit a PR.

## 📝 License

MIT License - see [LICENSE](LICENSE) file.

---

**Built with:** Flask • PostgreSQL • Docker • AWS S3 • JWT • Swagger
