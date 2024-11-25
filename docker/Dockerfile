# Use a Python image as base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Use Gunicorn to serve the app
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000", "--workers=2", "--timeout=120", "--worker-class=gevent"]

