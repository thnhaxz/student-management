from sqlalchemy.orm import Session
import models
import pandas as pd


def get_students(db: Session):
    return db.query(models.Student).all()


def search_students(db: Session, name):
    return db.query(models.Student).filter(
        models.Student.name.contains(name)
    ).all()


def create_student(db: Session, student):
    db_student = models.Student(**student)
    db.add(db_student)
    db.commit()


def delete_student(db: Session, student_id):
    student = db.query(models.Student).filter(
        models.Student.student_id == student_id
    ).first()

    if student:
        db.delete(student)
        db.commit()


def statistics(db: Session):

    students = db.query(models.Student).all()

    total = len(students)

    avg_gpa = sum([s.gpa for s in students]) / total if total else 0

    majors = {}

    for s in students:
        majors[s.major] = majors.get(s.major, 0) + 1

    return total, avg_gpa, majors


def export_csv(db: Session):

    students = db.query(models.Student).all()

    data = []

    for s in students:
        data.append({
            "student_id": s.student_id,
            "name": s.name,
            "major": s.major,
            "gpa": s.gpa
        })

    df = pd.DataFrame(data)

    df.to_csv("students_export.csv", index=False)