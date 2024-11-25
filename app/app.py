from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize the Flask application
app = Flask(__name__)

# Load configuration from config.py
app.config.from_object("config.Config")

# Debug print statement to verify the database URI
print("Database URI:", app.config["SQLALCHEMY_DATABASE_URI"])

# Initialize the database
db = SQLAlchemy(app)

# Define the Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        return {"id": self.id, "title": self.title, "description": self.description}

# Define Routes

# Root route to display tasks webpage (now same as /view-tasks)
@app.route("/")
def home():
    tasks = Task.query.all()
    print("Retrieved tasks for display:", [task.to_dict() for task in tasks])  # Debugging line
    return render_template("tasks.html", tasks=tasks)

# GET route to retrieve all tasks (API endpoint)
@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])

# POST route to add a new task (API endpoint)
@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    print("Received data for new task:", data)  # Debugging line

    task = Task(title=data["title"], description=data.get("description"))
    db.session.add(task)
    db.session.commit()
    print("Task committed to the database:", task.to_dict())  # Debugging line

    return jsonify(task.to_dict()), 201

# PUT route to update a task by ID (API endpoint)
@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    data = request.get_json()
    task = Task.query.get_or_404(id)
    task.title = data["title"]
    task.description = data.get("description")
    db.session.commit()
    return jsonify(task.to_dict())

# DELETE route to delete a task by ID (API endpoint)
@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return '', 204

# Route to display tasks on a webpage (optional: can be removed if redundant)
@app.route("/view-tasks", methods=["GET"])
def view_tasks():
    tasks = Task.query.all()
    print("Retrieved tasks for display:", [task.to_dict() for task in tasks])  # Debugging line
    return render_template("tasks.html", tasks=tasks)

# Test route to verify database insertion
@app.route("/test_db_insert", methods=["GET"])
def test_db_insert():
    sample_task = Task(title="Sample Task", description="Testing database insertion")
    db.session.add(sample_task)
    db.session.commit()
    print("Sample task added to the database:", sample_task.to_dict())  # Debugging line
    return "Sample task added successfully."

# Automatically create the tables on the first request
@app.before_first_request
def create_tables():
    print("Creating tables if not exist")
    db.create_all()

# Run the Flask application
if __name__ == "__main__":
    app.run(host="0.0.0.0")

