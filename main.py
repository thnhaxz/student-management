from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

import models
import crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

templates = Jinja2Templates(directory="templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
def read_students(request: Request):
    db = SessionLocal()
    students = crud.get_students(db)
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "students": students}
    )


@app.get("/add", response_class=HTMLResponse)
def add_form(request: Request):
    return templates.TemplateResponse("add_student.html", {"request": request})


@app.post("/add")
def add_student(
    student_id: str = Form(...),
    name: str = Form(...),
    birth_year: int = Form(...),
    major: str = Form(...),
    gpa: float = Form(...)
):
    db = SessionLocal()

    student = {
        "student_id": student_id,
        "name": name,
        "birth_year": birth_year,
        "major": major,
        "gpa": gpa
    }

    crud.create_student(db, type("obj", (object,), student))

    return RedirectResponse("/", status_code=303)


@app.get("/delete/{student_id}")
def delete(student_id: str):
    db = SessionLocal()
    crud.delete_student(db, student_id)

    return RedirectResponse("/", status_code=303)