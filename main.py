import os
import mysql.connector
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

load_dotenv()
app = FastAPI(title="Student Management API")


class Student(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    age: int = Field(ge=1, le=120)


def run(query, params=(), fetch=None):
    conn = mysql.connector.connect(
        host="localhost", user="root",
        password=os.getenv("DB_PASSWORD"), database="school",
    )
    cur = conn.cursor(dictionary=True)
    try:
        cur.execute(query, params)
        if fetch == "one":
            return cur.fetchone()
        if fetch == "all":
            return cur.fetchall()
        conn.commit()
        return {"lastrowid": cur.lastrowid}
    finally:
        cur.close()
        conn.close()


@app.post("/students", status_code=201)
def create_student(s: Student):
    result = run("INSERT INTO students (name, age) VALUES (%s, %s)", (s.name, s.age))
    return {"id": result["lastrowid"], **s.model_dump()}


@app.get("/students")
def list_students():
    return run("SELECT * FROM students", fetch="all")


@app.get("/students/{student_id}")
def get_student(student_id: int):
    student = run("SELECT * FROM students WHERE id = %s", (student_id,), fetch="one")
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@app.put("/students/{student_id}")
def update_student(student_id: int, s: Student):
    get_student(student_id)  # raises 404 if missing
    run("UPDATE students SET name = %s, age = %s WHERE id = %s", (s.name, s.age, student_id))
    return {"id": student_id, **s.model_dump()}


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    get_student(student_id)  # raises 404 if missing
    run("DELETE FROM students WHERE id = %s", (student_id,))
    return {"message": "Student deleted"}