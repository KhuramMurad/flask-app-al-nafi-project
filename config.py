<<<<<<< HEAD
=======

>>>>>>> 1124320 (enhancements are made for the final project)
import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/todo_db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
<<<<<<< HEAD
=======
    DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "yes")
>>>>>>> 1124320 (enhancements are made for the final project)
