# Flask CRUD Application

This is a simple CRUD application built using Flask, SQLAlchemy, PostgreSQL, and Docker. The application allows users to manage a list of tasks through a web interface, providing full functionality for adding, viewing, editing, and deleting tasks. This project is used as part of my oral presentation at AL-Nafi.

## Features

- **Add Tasks**: Users can add new tasks by providing a title and description.
- **View Tasks**: View all tasks with titles and descriptions in a list format.
- **Edit Tasks**: Update the title and description of an existing task.
- **Delete Tasks**: Remove tasks from the list with a single click.
- **Dark Theme**: The application has a dark theme for enhanced user experience.

## Project Structure

```
.
├── app.py                   # Main Flask application file
├── config.py                # Configuration file for database and settings
├── Dockerfile               # Dockerfile to containerize the application
├── docker-compose.yml       # Docker Compose file for multi-container setup
├── requirements.txt         # List of Python dependencies
├── .gitignore               # Git ignore file
├── .env                     # Environment variables file
└── templates
    └── tasks.html           # HTML template for displaying and managing tasks
```

## Installation and Setup

### Prerequisites

- **Docker** and **Docker Compose** installed on your system.

### Clone the Repository

```bash
git clone https://github.com/yourusername/flask-crud-app.git
cd flask-crud-app
```

### Set Up Environment Variables

Create a `.env` file in the root directory and add the following environment variables:

```plaintext
DATABASE_URL=postgresql://user:password@db:5432/todo_db
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=todo_db
```

### Run the Application with Docker Compose

1. Build and start the application using Docker Compose:
   ```bash
   docker-compose up --build
   ```
   
2. The application will be available at [http://localhost:5000](http://localhost:5000).

## Usage

1. **Access the Web Application**:
   - Go to [http://localhost:5000](http://localhost:5000) to use the app.

2. **Adding a Task**:
   - Enter the task title and description in the input fields and click **Add Task**.

3. **Editing a Task**:
   - Click **Edit** next to the task you want to modify. Update the title and description, then click **Update Task**.

4. **Deleting a Task**:
   - Click **Delete** next to the task you want to remove.

## Technology Stack

- **Flask**: Web framework for building the application.
- **SQLAlchemy**: ORM for interacting with the PostgreSQL database.
- **PostgreSQL**: Database used for storing tasks.
- **Docker**: Containerization of the application for easy deployment.
- **JavaScript**: Frontend scripting to handle add, edit, and delete actions.

## Presentation

This project is being used for my oral presentation at **AL-Nafi**, demonstrating the fundamentals of web development, containerization, and database management with Flask and Docker.

## Future Enhancements

- **User Authentication**: Adding user login and registration for individual task management.
- **Search Functionality**: Allow users to search for specific tasks.
- **Enhanced Error Handling**: Improve error messages and handling across the application.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
