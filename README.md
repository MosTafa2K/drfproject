# Django REST Framework Template Repository

This repository serves as a starter template for projects built with Django and Django REST Framework (DRF). By cloning this repository, you can quickly get started on new projects with a pre-configured structure and essential dependencies.

## Features

- **Modular Project Structure**: Separation of backend and frontend code for better organization.
- **Pre-installed Dependencies**: Essential packages like Django, Django REST Framework, and more are pre-configured.
- **Ready-to-use Configuration**: Includes basic settings, URL configuration, and application setup to get started quickly.

## Project Structure

```plaintext
├── LICENSE            # License file
├── README.md          # Project documentation
├── pdm.lock           # Dependency lock file
├── pyproject.toml     # Dependency and project configuration
├── src
│   ├── backend
│   │   ├── api          # Handles REST API-specific logic and endpoints
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── migrations
│   │   │   │   └── __init__.py
│   │   │   ├── models.py
│   │   │   ├── permissions.py
│   │   │   ├── serializers.py
│   │   │   ├── tests.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   ├── blog         # Manages blog-related functionality and templates
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── migrations
│   │   │   │   ├── 0001_initial.py
│   │   │   │   ├── 0002_alter_article_thumb.py
│   │   │   │   ├── 0003_remove_article_date.py
│   │   │   │   ├── 0004_alter_article_slug.py
│   │   │   │   └── __init__.py
│   │   │   ├── models.py
│   │   │   ├── templates
│   │   │   │   └── blog
│   │   │   │       └── article_list.html
│   │   │   ├── tests.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   ├── core          # Core module containing project-wide settings and configurations
│   │   │   ├── __init__.py
│   │   │   ├── asgi.py
│   │   │   ├── settings.py
│   │   │   ├── urls.py
│   │   │   └── wsgi.py
│   │   ├── db.sqlite3    # SQLite database (default)
│   │   └── manage.py     # Django management script
│   └── frontend          # Placeholder for frontend code
├── struct.txt           # Detailed structure of the project
└── tests
    └── __init__.py      # Placeholder for test cases
```

## Installed Packages

| Package              | Description                                      |
|----------------------|--------------------------------------------------|
| **Django**           | High-level Python web framework for rapid development and clean design. |
| **django-cors-headers** | Middleware to handle Cross-Origin Resource Sharing (CORS) in Django. |
| **djangorestframework** | Powerful toolkit for building Web APIs with Django. |
| **Markdown**         | Library to convert Markdown text to HTML, often used for API documentation. |

## Usage

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies:**
   This template uses `PDM` for dependency management. Install PDM if not already installed:
   ```bash
   pip install pdm
   ```
   Then install the project dependencies:
   ```bash
   pdm install
   ```

3. **Run migrations:**
   Apply the database migrations to set up the database schema:
   ```bash
   pdm run python src/backend/manage.py migrate
   ```

4. **Create a superuser:**
   To access the Django admin interface, create a superuser account:
   ```bash
   pdm run python src/backend/manage.py createsuperuser
   ```

5. **Run the development server:**
   ```bash
   pdm run python src/backend/manage.py runserver
   ```

6. **Start building your application!**

## Contribution

Feel free to open issues or submit pull requests to improve this template.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
