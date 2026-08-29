# Django REST API

A hands-on project built while learning **Django REST Framework (DRF)** and REST API development.

This repository focuses on understanding how to create, structure, and test APIs using Django and DRF.

## Tech Stack

* Python
* Django
* Django REST Framework
* SQLite
* REST API
* JSON

## Concepts Covered

* Django project and app structure
* Models and Django ORM
* Serializers
* API Views
* CRUD operations
* ViewSets
* Routers
* URL routing
* Authentication and Permissions

## Project Structure

```text
Django_rest/
│
├── backend_transaction/
├── backend_turf/
└── README.md
```

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

### 4. Install Dependencies

```bash
pip install django djangorestframework
```

### 5. Apply Migrations

Navigate to the directory containing `manage.py`, then run:

```bash
python manage.py migrate
```

### 6. Start the Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## API Request Flow

```text
Client
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

## Learning Outcome

Through this project, I developed a practical understanding of **Django REST Framework, API architecture, serialization, CRUD operations, ViewSets, routers, and backend request handling**.

## Future Improvements

* JWT Authentication
* Advanced Permissions
* API Filtering
* Pagination
* API Testing
* Swagger / OpenAPI Documentation
* PostgreSQL Integration
* Deployment

## Author

**Vengatesh Narayanan**

B.Tech Computer Science Engineering

[GitHub](https://github.com/VengateshNarayanan)
