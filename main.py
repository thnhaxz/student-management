from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse
from fastapi.templating import Jinja2Templates
from database import SessionLocal, engine
import models
import crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request, search: str = ""):

    db = SessionLocal()

    if search:
        students = crud.search_students(db, search)
    else:
        students = crud.get_students(db)

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "students": students}
    )


@app.get("/add", response_class=HTMLResponse)
def add_form(request: Request):

    return templates.TemplateResponse("add_student.html",
                                      {"request": request})


@app.post("/add")
def add_student(
    student_id: str = Form(...),
    name: str = Form(...),
    birth_year: int = Form(...),
    major: str = Form(...),
    gpa: float = Form(...),
    class_id: str = Form(...)
):

    db = SessionLocal()

    student = {
        "student_id": student_id,
        "name": name,
        "birth_year": birth_year,
        "major": major,
        "gpa": gpa,
        "class_id": class_id
    }

    crud.create_student(db, student)

    return RedirectResponse("/", status_code=303)


@app.get("/delete/{student_id}")
def delete(student_id: str):

    db = SessionLocal()

    crud.delete_student(db, student_id)

    return RedirectResponse("/", status_code=303)


@app.get("/stats", response_class=HTMLResponse)
def stats(request: Request):

    db = SessionLocal()

    total, avg_gpa, majors = crud.statistics(db)

    return templates.TemplateResponse(
        "stats.html",
        {
            "request": request,
            "total": total,
            "avg_gpa": avg_gpa,
            "majors": majors
        }
    )


@app.get("/export")
def export():

    db = SessionLocal()

    crud.export_csv(db)

    return FileResponse("students_export.csv", filename="students.csv")