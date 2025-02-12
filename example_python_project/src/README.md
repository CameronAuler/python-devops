# Source Directory (`src/`)

## Overview
The `src/` directory contains all source code for the **Example Python Project**. This directory houses the core application logic, structured in a modular and maintainable way, following best practices for enterprise-level Python development. It serves as the foundation of the project and contains essential components for running the application.

## Directory Structure
```
src/
├── example_python_project/    # Root package for the application
│   ├── README.md              # Documentation for the package
├── manage.py                  # Django management script (if applicable)
├── wsgi.py                    # Web Server Gateway Interface (WSGI) entry point
├── asgi.py                    # Asynchronous Server Gateway Interface (ASGI) entry point
└── README.md                  # This file
```

## Files Explained
### `example_python_project/`
This is the main package that contains the core logic of the project, including API implementations, services, models, repositories, utilities, configuration files, and middleware. Refer to its `README.md` for an in-depth explanation of its components.

### `manage.py`
This script is used primarily for managing a Django-based application. It provides command-line utilities for running the development server, performing database migrations, creating superusers, and managing other administrative tasks.

**Usage Examples:**
```bash
# Start the Django development server
python manage.py runserver

# Run database migrations
python manage.py migrate

# Create a Django superuser
python manage.py createsuperuser
```

### `wsgi.py`
The **Web Server Gateway Interface (WSGI)** is the standard interface between Python web applications and web servers (such as Gunicorn, uWSGI, or Apache with mod_wsgi). This file is used when deploying the application in a production environment that relies on WSGI-compatible servers.

**WSGI is primarily used for synchronous applications** and is the default for Django applications.

**Usage in Deployment:**
```bash
# Running with Gunicorn
gunicorn example_python_project.wsgi:application --bind 0.0.0.0:8000
```

### `asgi.py`
The **Asynchronous Server Gateway Interface (ASGI)** is the next-generation standard for Python web applications, enabling support for **asynchronous processing** and WebSockets. ASGI allows Django or FastAPI applications to handle both synchronous and asynchronous requests.

**ASGI is recommended for real-time applications** that require WebSockets, GraphQL subscriptions, or background task execution.

**Usage in Deployment:**
```bash
# Running with Uvicorn (for ASGI applications)
uvicorn example_python_project.asgi:application --host 0.0.0.0 --port 8000
```

## Running the Application
```bash
# Start the application (if using Django or Flask)
python src/manage.py runserver
```

## Additional Notes
- The structure promotes modularity and maintainability.
- WSGI is used for synchronous applications, while ASGI is required for handling asynchronous workflows.
- Ensure you select the appropriate interface (WSGI or ASGI) based on your application's needs.
- Follow best practices for coding and file organization.
- Refer to individual `README.md` files in each module for further details.