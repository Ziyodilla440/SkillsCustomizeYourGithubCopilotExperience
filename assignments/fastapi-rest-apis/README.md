# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to design, build, and test modern asynchronous RESTful web APIs using Python and the FastAPI framework with Pydantic data models.

## 📝 Tasks

### 🛠️ Task 1: Create FastAPI Application and Root Endpoint

#### Description
Initialize a FastAPI application instance and create a basic GET route at `/` returning a welcome JSON message.

#### Requirements
Completed program should:

- Import `FastAPI` and initialize the `app` instance
- Define a GET route at `/` that returns a dictionary `{"message": "Welcome to the Student API!"}`
- Configure the application to run with Uvicorn

### 🛠️ Task 2: Implement CRUD Endpoints with Pydantic Models

#### Description
Create an in-memory data store for students and implement endpoints to create, read, and delete student records.

#### Requirements
Completed program should:

- Define a Pydantic `Student` model with `id`, `name`, and `grade` fields
- Implement `GET /students` to return all students
- Implement `POST /students` to add a new student with validation
- Implement `DELETE /students/{student_id}` to remove a student by ID
