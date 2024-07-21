import pydantic_models
from crud import *
import crud
from data_model import *
from pydantic_models import *
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from fastapi import Body


data_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

async def get_db():
    db = data_model.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/students/", response_model=pydantic_models.Student)
async def create_students(student: Annotated[pydantic_models.StudentCreate, Body(embed=True)], db: Session = Depends(get_db)):
    db_student = crud.get_student_by_id(db, id=student.id)
    if db_student:
        raise HTTPException(status_code=400, detail="ID already registered")
    return crud.create_student(db=db, student=student)


@app.get("/students/{student_id}", response_model=pydantic_models.Student)
async def get_student_by_id(id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student_by_id(db, id = id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="!User not found!")
    return db_student

@app.get("/students/", response_model=list[pydantic_models.Student])
async def get_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = crud.get_students(db, skip = skip, limit = limit)
    return students


@app.delete("/student/delete/{student_id}", response_model=pydantic_models.Student)
async def delete_a_student(student_id: int, db: Session = Depends(get_db)):
    dlb_student = crud.delete_student(db, student_id = student_id)
    if dlb_student is None:
        raise HTTPException(status_code=404, detail="!User not found!")
    return dlb_student


@app.put("/student/update/{student_id}", response_model=pydantic_models.Student)
async def update_student(student_id: int, name: str | None = None, field: str | None = None, semester_no: str | None = None, db: Session = Depends(get_db)):
    dus_student = crud.update_student(db, student_id = student_id, name = name, field = field, semester_no = semester_no)
    if name or field or semester_no:
        dus_student.update({name : name}, {field : field}, {semester_no : semester_no})
        db.commit()
        return dus_student
    if dus_student is None:
        raise HTTPException(status_code=404, detail="!User not found!")
    db.commit()
    return dus_student


















