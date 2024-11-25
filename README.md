# Flask CRUD Application with Kubernetes (AWS EKS)

A 3-tier CRUD (Create, Read, Update, Delete) web application built with Flask, PostgreSQL, and Docker. This application allows users to manage tasks with functionalities like adding, updating, and deleting tasks. It includes a web interface for task management, a RESTful API for programmatic access, and Kubernetes-based deployment for scalability and resilience.

---

## Features

- **RESTful API**: Built with Flask for CRUD operations on tasks.
- **Interactive Web Interface**: Buttons for creating, updating, and deleting tasks.
- **Input Validation**: Prevents adding empty tasks.
- **Kubernetes Deployment**: Scalable and highly available deployment on AWS EKS.
- **Dockerized Setup**: PostgreSQL and Flask application fully containerized.
- **Monitoring and Observability**: Integrated Prometheus and Grafana for application monitoring.

---

## Project Structure


```
.
├── app
│   ├── app.py
│   ├── config.py
│   ├── __pycache__
│   │   ├── app.cpython-39.pyc
│   │   └── config.cpython-39.pyc
│   ├── ssl
│   │   ├── nginx.crt
│   │   └── nginx.key
│   └── templates
│       └── tasks.html
├── deployment
│   ├── docker-compose.yml
│   └── nginx.conf
├── docker
│   ├── Dockerfile
│   ├── nginx.conf
│   └── requirements.txt
├── monitoring
│   ├── grafana
│   │   └── dashboard.json
│   └── prometheus.yml
├── README.md
├── terraform-workspace
│   ├── backend.tf
│   ├── eks-cluster
│   │   ├── main.tf
│   │   ├── outputs.tf
│   │   ├── terraform.tfstate
│   │   ├── terraform.tfstate.backup
│   │   └── variables.tf
│   ├── rds
│   │   ├── main.tf
│   │   ├── outputs.tf
│   │   └── variables.tf
│   └── vpc
│       ├── main.tf
│       ├── outputs.tf
│       ├── terraform.tfstate
│       ├── terraform.tfstate.backup
│       └── variables.tf
└── tests
    ├── test_app.py
    └── test_config.py

```

---

## Prerequisites

To run this project, ensure you have the following installed:

- **Docker**: For containerized deployment.
- **Kubernetes (kubectl)**: To manage your EKS cluster.
- **Terraform**: To provision AWS infrastructure.
- **AWS CLI**: For managing AWS resources.
- **Git**: For version control.

---

## Getting Started

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/KhuramMurad/flask-app-al-nafi-project.git
cd flask-app-al-nafi-project
```
----------

### 2. Local Deployment with Docker

Run the application locally using Docker Compose:

```bash
docker-compose up --build
```
-   The Flask app will be accessible at [http://localhost:5000](http://localhost:5000).
-   Use the web interface or the RESTful API to interact with the application.

----------

### 3. Deploy to AWS EKS

#### Step 1: Build and Push Docker Image

Build the Docker image and push it to AWS Elastic Container Registry (ECR):

```bash
docker build -t flask-app .
docker tag flask-app:latest <your-account-id>.dkr.ecr.us-east-1.amazonaws.com/flask-app:latest
docker push <your-account-id>.dkr.ecr.us-east-1.amazonaws.com/flask-app:latest
```

#### Step 2: Deploy on Kubernetes

Use the Kubernetes manifests in the `deployment/` directory to deploy the app on EKS:

```bash
kubectl apply -f deployment/flask-deployment.yaml
kubectl apply -f deployment/flask-service.yaml
```

#### Step 3: Verify Deployment

Check the status of your pods and service:

```bash
kubectl get pods
kubectl get svc
```

----------

## Features

### RESTful API

The application exposes the following API endpoints:

-   **GET /tasks**: Retrieve all tasks.
-   **POST /tasks**: Add a new task (expects JSON body with `title` and `description`).
-   **PUT /tasks/**: Update an existing task by ID.
-   **DELETE /tasks/**: Delete a task by ID.

Example usage with `curl`:

```bash
# Add a new task
curl -X POST http://localhost:5000/tasks \
-H "Content-Type: application/json" \
-d '{"title": "Sample Task", "description": "This is a sample task"}'

# List all tasks
curl http://localhost:5000/tasks
```

----------
### Frontend Features

-   **Task Input Form**: Fields to enter a task title and description.
-   **CRUD Buttons**: Buttons for adding, editing, updating, and deleting tasks.
-   **Validation**: Displays a warning message if an attempt is made to add an empty task.
----------

## Observability and Monitoring

The application integrates **Prometheus** and **Grafana** for observability:

-   **Prometheus** scrapes metrics from the Flask app using a `/metrics` endpoint.
-   **Grafana** visualizes these metrics with pre-configured dashboards.

### Set Up Monitoring

Deploy Prometheus and Grafana using Helm:

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install prometheus prometheus-community/kube-prometheus-stack --namespace monitoring --create-namespace
```

----------

## Environment Variables

The application uses environment variables for database and configuration settings. Modify these in the `docker-compose.yml` or Kubernetes deployment YAML as needed.

### Key Environment Variables

-   `DATABASE_URL`: PostgreSQL connection string.

Example in `docker-compose.yml`:

```yaml
environment:
  - DATABASE_URL=postgresql://user:password@db:5432/todo_db

```

----------

## Screenshots
![image](https://github.com/user-attachments/assets/fa07c9bf-259a-4e9d-b85d-e0c4f6013a34)


----------

## License

This project is licensed under the **GPL License**. See the LICENSE file for more details.

----------
## Contributing

Contributions are welcome! To contribute:

1.  Fork the repository.
2.  Create a new branch with a descriptive name.
3.  Make your changes and test thoroughly.
4.  Submit a pull request with a clear description of the changes.

----------
## Acknowledgments

This project is part of a multi-cloud infrastructure design for demonstrating secure, scalable, and compliant Kubernetes-based application deployment using AWS EKS.
