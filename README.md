# Student Management REST API

A REST API to create, read, update and delete student records.
Built with Python, FastAPI and MySQL, tested with pytest.

## Features
- CRUD endpoints for students
- Request validation with Pydantic (returns 422 on bad input)
- 404 error handling for missing records
- Automated tests with pytest

## Endpoints
| Method | URL | Description |
|--------|-----|-------------|
| POST | /students | Create a student |
| GET | /students | List all students |
| GET | /students/{id} | Get one student |
| PUT | /students/{id} | Update a student |
| DELETE | /students/{id} | Delete a student |

## Setup
1. Create the database: `CREATE DATABASE school;`
2. Create the table by running `python crud.py` once.
3. `pip install -r requirements.txt`
4. Create a `.env` file: `DB_PASSWORD=your_mysql_password`
5. Run: `uvicorn main:app --reload`
6. Open http://127.0.0.1:8000/docs to try the API.

## Run tests
`pytest -v`