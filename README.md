# 🚀 Django REST Framework Core Concepts

<p align="center">
  <img src="https://shields.io" alt="Django" />
  <img src="https://shields.io" alt="DRF" />
  <img src="https://shields.io" alt="Python" />
  <img src="https://shields.io" alt="Git" />
</p>

A dedicated repository containing hands-on implementation, study notes, and architectural patterns explored while learning **REST APIs** and **Django REST Framework (DRF)**.

---

## 📌 Project Overview

This repository serves as a structured sandbox covering everything from standard HTTP methods to advanced API engineering concepts. It demonstrates how to transition a traditional monolithic Django application into a scalable, decoupled backend service.

### ⚡ Key Features Explored
* **Serialization & Deserialization:** Converting complex data types/models into native Python datatypes that can then be easily rendered into `JSON` or `XML`.
* **API Views:** Utilizing function-based views (`@api_view`) and Class-Based Views (`APIView`) for clean request handling.
* **Generic Views & ViewSets:** Writing robust CRUD operations with minimal boilerplate code.
* **Authentication & Permissions:** Securing endpoints using Token-based and Session-based authentication.
* **Routing:** Automatic URL routing configurations using DRF Routers.

---

## 📁 Repository Structure

```text
django_rest/
│
└── rest/                 # Core learning folder containing the Django Project
    ├── manage.py         # Django management script
    ├── [project_name]/   # Project configuration directory
    └── [app_name]/       # Main application folder with API logic
        ├── models.py     # Database schemas
        ├── serializers.py# DRF Serializers mapped to models
        ├── urls.py       # API Endpoint routing
        └── views.py      # Business logic and API viewsets
```

---

## 🛠️ Tech Stack & Dependencies

* **Language:** Python
* **Framework:** Django 
* **Toolkit:** Django REST Framework (DRF)
* **Database:** SQLite (Default / Development)

---

## 🚀 Getting Started Locally

Follow these steps to set up and explore the code on your local system:

### 1. Clone the repository
```bash
git clone https://github.com
cd django_rest/rest
```

### 2. Set up a Virtual Environment
```bash
# Windows
python -m venv env
.\env\Scripts\activate

# macOS/Linux
python3 -m venv env
source env/bin/activate
```

### 3. Install Dependencies
```bash
pip install django djangorestframework
```

### 4. Run Migrations & Start Server
```bash
python manage.py migrate
python manage.py runserver
```
Once started, visit `http://126.0.0` in your browser to view the interactive browsable API interface provided by DRF!

---

## 📈 Learning Roadmap & Achievements
- [x] Setting up Django with REST Framework
- [x] Building basic Serializers
- [x] Utilizing Class-Based APIViews
- [ ] Implementing Custom Permissions and JWT Authentication
- [ ] Integrating Pagination and Filtering for large datasets

---

<p align="center">
  Generated with ❤️ while diving deep into backend engineering.
</p>
