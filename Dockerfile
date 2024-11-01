# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 5000 for Flask
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]
