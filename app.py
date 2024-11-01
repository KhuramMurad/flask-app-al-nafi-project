from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize the Flask application
app = Flask(__name__)

<<<<<<< HEAD
# Load configuration from config.py
app.config.from_object("config.Config")
=======
# Load configuration from environment variables for improved security
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:///tasks.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
>>>>>>> 1124320 (enhancements are made for the final project)

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

<<<<<<< HEAD
# Root route to display tasks webpage (now same as /view-tasks)
@app.route("/")
def home():
    tasks = Task.query.all()
    return render_template("tasks.html", tasks=tasks)
=======
# Root route to display tasks webpage
@app.route("/")
def home():
    return render_template("tasks.html")
>>>>>>> 1124320 (enhancements are made for the final project)

# GET route to retrieve all tasks (API endpoint)
@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])

<<<<<<< HEAD
# POST route to add a new task (API endpoint)
@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    task = Task(title=data["title"], description=data.get("description"))
    db.session.add(task)
    db.session.commit()
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
    return render_template("tasks.html", tasks=tasks)

# Automatically create the tables on the first request
@app.before_first_request
def create_tables():
    db.create_all()

# Run the Flask application
if __name__ == "__main__":
    app.run(host="0.0.0.0")
=======
# POST route to create a new task
@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    title = data.get("title")
    description = data.get("description", "")

    if not title:
        return jsonify({"error": "Title is required"}), 400

    new_task = Task(title=title, description=description)
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.to_dict()), 201

# PUT route to update a task
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.get_json()
    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    db.session.commit()
    return jsonify(task.to_dict()), 200

# DELETE route to delete a task
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"}), 200

# Run the app only if executed directly (useful for debugging)
if __name__ == "__main__":
    db.create_all()  # Create tables if they don't exist
    app.run(host="0.0.0.0", port=5000, debug=True)
>>>>>>> 1124320 (enhancements are made for the final project)

