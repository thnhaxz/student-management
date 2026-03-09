from sqlalchemy.orm import Session
import models

def get_students(db: Session):
    return db.query(models.Student).all()

def create_student(db: Session, student):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_id):
    student = db.query(models.Student).filter(
        models.Student.student_id == student_id
    ).first()

    if student:
        db.delete(student)
        db.commit()

def update_student(db: Session, student_id, data):
    student = db.query(models.Student).filter(
        models.Student.student_id == student_id
    ).first()

    if student:
        student.name = data.name
        student.birth_year = data.birth_year
        student.major = data.major
        student.gpa = data.gpa
        db.commit()