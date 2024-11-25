# Flask CRUD Application with Docker

A 3-tier CRUD (Create, Read, Update, Delete) web application built with Flask, PostgreSQL, and Docker. This application allows users to manage tasks with functionalities like adding, updating, and deleting tasks. It includes a web interface for task management, a RESTful API for programmatic access, and a Dockerized setup for simplified deployment.

## Features

- **RESTful API** built with Flask for CRUD operations on tasks.
- **Interactive Web Interface** with buttons for creating, updating, and deleting tasks.
- **Input Validation** to prevent adding empty tasks.
- **Dockerized Setup** with PostgreSQL, making it easy to deploy the entire application stack.

## Project Structure

The project follows a simple structure:

```plaintext
.
├── app.py
├── config.py
├── docker-compose.yml
├── Dockerfile
├── nginx.conf
├── README.md
├── requirements.txt
├── ssl
│   ├── nginx.crt
│   └── nginx.key
└── templates
    └── tasks.html
```
---

## Prerequisites

To run this project, ensure you have the following installed:

- [Docker](https://www.docker.com/products/docker-desktop) and [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/) for version control

> **Note**: Python is optional, only required if you wish to run the app locally without Docker.

---

## Getting Started

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/KhuramMurad/flask-app-al-nafi-project.git
cd flask-app-al-nafi-project
```

### 2. Run the Application with Docker

Build and run the application using Docker Compose:

```bash
docker-compose up --build
```

This command will start both the Flask application and a PostgreSQL database within Docker containers.

- The Flask app will be accessible at `http://localhost:5000`.

### 3. Access the Web Interface

Navigate to `http://localhost:5000` in your browser. You’ll see the main task management interface, allowing you to:

- **Add New Tasks**
- **Edit and Update Tasks**
- **Delete Tasks**

You can also access the RESTful API for programmatic task management.

---
## API Endpoints

The application exposes the following API endpoints:

- **`GET /tasks`**: Retrieve all tasks.
- **`POST /tasks`**: Add a new task (expects JSON body with `title` and `description`).
- **`PUT /tasks/<id>`**: Update an existing task by ID.
- **`DELETE /tasks/<id>`**: Delete a task by ID.

### Example Usage

Use `curl` or Postman to interact with the API endpoints:

- **Add a new task**:
  ```bash
  curl -X POST http://localhost:5000/tasks -H "Content-Type: application/json" -d '{"title": "Sample Task", "description": "This is a sample task"}'
  ```

- **List all tasks**:
  ```bash
  curl http://localhost:5000/tasks
  ```
---

## Frontend Features

The web interface provides the following functionalities:

- **Task Input Form**: Fields to enter a task title and description.
- **CRUD Buttons**: Buttons for adding, editing, updating, and deleting tasks.
- **Validation**: Displays a warning message if an attempt is made to add an empty task.

---

## Environment Variables

The application uses environment variables for database configuration. You can modify these settings in `config.py` or in the `docker-compose.yml` file as needed.

### Key Environment Variables

- **`DATABASE_URL`**: The URL for connecting to the PostgreSQL database.

Example (in `docker-compose.yml`):
```yaml
environment:
  - DATABASE_URL=postgresql://user:password@db:5432/todo_db
```
---

## Screenshots
![image](https://github.com/user-attachments/assets/49a861ec-0458-4e31-82a3-44ef625c04c7)

---

## Folder Structure and Key Files

- **`app.py`**: Contains the main application logic, including routes and database models.
- **`config.py`**: Configuration settings for connecting to PostgreSQL.
- **`templates/tasks.html`**: HTML frontend with JavaScript for dynamic task management.
- **`Dockerfile`** and **`docker-compose.yml`**: Docker configuration files for building and managing the application stack.

---

## License

This project is licensed under the **GPL License**. See the [LICENSE](LICENSE) file for more details.

---

## Contributing

Contributions are welcome! If you’d like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch with a descriptive name.
3. Make your changes and test thoroughly.
4. Submit a pull request with a clear description of the changes.

---

## Acknowledgments

This project is inspired by the need for a simple and effective CRUD application setup that demonstrates both backend and frontend development with Dockerized deployment.
