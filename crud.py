import data_model
import pydantic_models
from sqlalchemy.orm import Session
from typing import Annotated
from fastapi import Body
from fastapi import Depends, FastAPI, HTTPException
from data_model import engine

app = FastAPI()

async def get_student_by_id(db: Session, id: int):
    return db.query(data_model.Student).filter(data_model.Student.id == id).first()


async def create_student(student: Annotated[pydantic_models.StudentCreate, Body(embed=True)], db: Session ):
    db_student = data_model.Student(id=student.id, name=student.name , field=student.field, semester_no=student.semester_no)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return {"student" : student}

async def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(data_model.Student).offset(skip).limit(limit).all()

async def delete_student(db: Session, student_id: int):
    del_student = db.query(data_model.Student).filter(data_model.Student.id == student_id).first()
    db.delete(del_student)
    db.commit()


async def update_student(db: Session, student_id: int, name: str, field: str, semester_no: str):
    du_student = db.query(data_model.Student).filter(data_model.Student.id == student_id).first()
    du_student.name = name
    du_student.field = field
    du_student.semester_no = semester_no


































