# Advanced API Project

## Overview
A Django project with Django REST Framework (DRF) for managing `Author` and `Book` models, featuring nested serializers, CRUD operations, and permissions.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/<your-username>/Alx_DjangoLearnLab.git
    cd Alx_DjangoLearnLab/advanced-api-project
    ```

2. Install dependencies:

    ```bash
    pip install django djangorestframework
    ```

3. Apply migrations:

    ```bash
    python manage.py migrate
    ```

4. (Optional) Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

## API Endpoints

| Method | Endpoint                 | Description                   |
|--------|--------------------------|-------------------------------|
| GET    | `/api/books/`             | List all books                |
| POST   | `/api/books/`             | Create a new book             |
| GET    | `/api/books/<id>/`        | Retrieve a book by ID         |
| PUT    | `/api/books/<id>/update/` | Update a book by ID           |
| DELETE | `/api/books/<id>/delete/` | Delete a book by ID           |

## Features
- **Generic Views**: List, retrieve, create, update, and delete books.
- **Nested Serializers**: Handle author-book relationships.
- **Permissions**: Authenticated users can create, update, and delete; unauthenticated users can only view.

---

# Advanced API Project

## Overview

This Django project provides an API for managing authors and books, built with Django REST Framework (DRF). It includes advanced query capabilities such as filtering, searching, and ordering to enhance API consumer interactions.

## Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/Alx_DjangoLearnLab.git
   cd Alx_DjangoLearnLab/advanced-api-project


## Testing Overview

### Test Cases
1. **Create Book**: Verifies that a book can be created successfully.
2. **Update Book**: Ensures that book updates are correctly applied.
3. **Delete Book**: Checks that a book is deleted properly.
4. **Filter Books**: Tests filtering functionality by title.
5. **Search Books**: Verifies search functionality.
6. **Ordering Books**: Checks that ordering by publication year works as expected.
7. **Permission**: Ensures that unauthenticated users cannot create books.

### Running Tests
Execute tests using Django’s test management command:
```bash
python manage.py test api
