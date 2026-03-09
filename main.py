from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from database import engine, SessionLocal
from models import Base, Student

app = FastAPI()

templates = Jinja2Templates(directory="templates")

Base.metadata.create_all(bind=engine)


@app.get("/", response_class=HTMLResponse)
def read_students(request: Request):
    db = SessionLocal()
    students = db.query(Student).all()
    return templates.TemplateResponse("index.html", {"request": request, "students": students})


@app.get("/add", response_class=HTMLResponse)
def add_page(request: Request):
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

    student = Student(
        student_id=student_id,
        name=name,
        birth_year=birth_year,
        major=major,
        gpa=gpa
    )

    db.add(student)
    db.commit()

    return RedirectResponse("/", status_code=303)