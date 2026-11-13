# Starter Code: Building REST APIs with FastAPI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Student Management API")

class Student(BaseModel):
    id: int
    name: str
    grade: int

# In-memory database
students_db: List[Student] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the Student API!"}

# TODO: Implement GET /students
# @app.get("/students", response_model=List[Student])
# def get_students():
#     ...

# TODO: Implement POST /students
# @app.post("/students", response_model=Student)
# def create_student(student: Student):
#     ...

# TODO: Implement DELETE /students/{student_id}
# @app.delete("/students/{student_id}")
# def delete_student(student_id: int):
#     ...
