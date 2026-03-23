# Django Task Tracker API

## Overview

This project is a simple full-stack web application built with Django and Django REST Framework. It is designed as a learning and demonstration project to showcase the ability to:

- Build a RESTful API
- Perform full CRUD operations
- Structure a Django project
- Integrate backend services with a frontend
- Deploy a Django application to a remote server
- Work with JSON-based communication between client and server

The project is intentionally kept simple to clearly demonstrate core concepts without unnecessary complexity.

---

## Features

### Backend (API)
- Create tasks
- Retrieve all tasks
- Retrieve a single task
- Update tasks
- Delete tasks

### Task Model
Each task includes:
- Title (string)
- Description (text)
- Date (date, with default value)
- Completed (boolean)
- Auto-generated ID (primary key)

---

## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite (local development)
- PostgreSQL (production, if configured via environment)
- Gunicorn (production server)
- Render (deployment platform)

---

## Project Structure

- `models.py` — Defines the Task data model
- `serializers.py` — Translates model instances into JSON
- `views.py` — Contains API logic for handling requests
- `urls.py` — Routes API endpoints
- `settings.py` — Project configuration
- `templates/` — Basic frontend (in progress)

---

## API Endpoints

Base URL: https://djangoproject-zxlp.onrender.com



Endpoints:
- `GET /api/tasks/` — Retrieve all tasks
- `GET /api/tasks/<id>/` — Retrieve a single task
- `POST /api/tasks/create/` — Create a new task
- `PUT /api/tasks/update/<id>/` — Update a task
- `DELETE /api/tasks/delete/<id>/` — Delete a task

---

## Example Task JSON

```json
{
  "title": "Example Task",
  "description": "This is a sample task",
  "date": "2026-03-23",
  "completed": false
}
