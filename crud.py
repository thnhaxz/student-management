from sqlalchemy.orm import Session
import models


def get_students(db: Session):
    return db.query(models.Student).all()


def create_student(db: Session, student_id, name, birth_year, major, gpa):
    student = models.Student(
        student_id=student_id,
        name=name,
        birth_year=birth_year,
        major=major,
        gpa=gpa
    )

    db.add(student)
    db.commit()
    db.refresh(student)

    return student


def delete_student(db: Session, student_id):
    student = db.query(models.Student).filter(models.Student.student_id == student_id).first()
    
    if student:
        db.delete(student)
        db.commit()