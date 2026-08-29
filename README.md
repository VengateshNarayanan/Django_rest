# Django REST API

A hands-on project created while learning **Django REST Framework (DRF)** and REST API development.

This repository focuses on understanding how APIs are designed, implemented, routed, and connected with Django models and databases.

## About the Project

The project explores the core building blocks of a REST API using Django REST Framework, including serializers, API views, CRUD operations, ViewSets, routers, authentication, and permissions.

The main objective is to understand how a client request moves through the backend and is converted into a structured JSON response.

```text
Client Request
      ↓
URL / Router
      ↓
View / ViewSet
      ↓
Serializer
      ↓
Model / Database
      ↓
JSON Response
```

## Tech Stack

| Technology            | Purpose              |
| --------------------- | -------------------- |
| Python                | Programming language |
| Django                | Backend framework    |
| Django REST Framework | REST API development |
| SQLite                | Development database |
| Django ORM            | Database interaction |
| JSON                  | API data format      |

## Concepts Covered

* Django project and application structure
* Django Models and ORM
* Serializers and data validation
* REST API development
* HTTP methods and CRUD operations
* Function-based API Views
* Class-based API Views
* ViewSets
* Routers and URL routing
* Authentication and Permissions
* JSON request and response handling

## Project Structure

```text
Django_rest/
│
├── backend_transaction/
│
├── backend_turf/
│
└── README.md
```

The backend implementations are organized into separate directories to experiment with different Django REST Framework concepts.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/VengateshNarayanan/Django_rest.git
```

### 2. Navigate to the Project

```bash
cd Django_rest
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install django djangorestframework
```

### 5. Run Migrations

Navigate to the directory containing `manage.py` and run:

```bash
python manage.py migrate
```

### 6. Start the Server

```bash
python manage.py runserver
```

The API can then be accessed locally at:

```text
http://127.0.0.1:8000/
```

## Learning Outcome

Through this project, I developed a practical understanding of **Django REST Framework and backend API architecture**, including how models, serializers, views, ViewSets, routers, and databases work together to build RESTful services.

## Future Improvements

* JWT Authentication
* Advanced Permissions
* API Filtering and Searching
* Pagination
* Automated API Testing
* Swagger / OpenAPI Documentation
* PostgreSQL Integration
* Deployment

