from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud
import models
import schemas
from models import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# application of students
# -------------------------------------------------------------------------------------------------------

@app.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student.id)
    # if db_student:
    #     raise HTTPException(status_code=400, detail="Student Id already registered")
    return crud.create_student(db=db, student=student)


@app.get("/students/", response_model=list[schemas.Student])
def read_students(db: Session = Depends(get_db)):
    students = crud.get_students(db)
    return students


@app.get("/students/{student_id}", response_model=list[schemas.Student])
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="student not found")
    return db_student


@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    crud.delete_student_by_id(db=db, student_id=student_id)
    return {"massage": f"student with id: {student_id} successfully deleted"}


# application of teachers
# -------------------------------------------------------------------------------------------------------

@app.post("/teacher/", response_model=schemas.Teacher)
def create_teacher(teacher: schemas.TeacherCreate, db: Session = Depends(get_db)):
    db_teacher = crud.get_teacher(db, teacher_id=teacher.id)
    # if db_student:
    #     raise HTTPException(status_code=400, detail="Student Id already registered")
    return crud.create_teacher(db=db, teacher=teacher)


@app.get("/teachers/", response_model=list[schemas.Teacher])
def read_teachers(db: Session = Depends(get_db)):
    teachers = crud.get_teachers(db)
    return teachers


@app.get("/teachers/{teacher_id}", response_model=list[schemas.Teacher])
def read_teacher(teacher_id: int, db: Session = Depends(get_db)):
    db_teacher = crud.get_teacher(db, teacher_id=teacher_id)
    if db_teacher is None:
        raise HTTPException(status_code=404, detail="teacher not found")
    return db_teacher


@app.delete("/teachers/{teacher_id}")
def delete_teacher(teacher_id: int, db: Session = Depends(get_db)):
    crud.delete_teacher_by_id(db=db, teacher_id=teacher_id)
    return {"massage": f"teacher with id: {teacher_id} successfully deleted"}


# application of prerequisite
# -------------------------------------------------------------------------------------------------------

@app.post("/prerequisite/", response_model=schemas.Prerequisite)
def create_prerequisite(prerequisite: schemas.PrerequisiteCreate, db: Session = Depends(get_db)):
    db_prerequisite = crud.get_prerequisite(db, prerequisite_id=prerequisite.id)
    # if db_student:
    #     raise HTTPException(status_code=400, detail="Student Id already registered")
    return crud.create_prerequisite(db=db, prerequisite=prerequisite)


@app.get("/prerequisite/", response_model=list[schemas.Prerequisite])
def read_prerequisites(db: Session = Depends(get_db)):
    prerequisites = crud.get_prerequisites(db)
    return prerequisites


@app.get("/prerequisite/{prerequisite_id}", response_model=list[schemas.Prerequisite])
def read_prerequisite(prerequisite_id: int, db: Session = Depends(get_db)):
    db_prerequisite = crud.get_prerequisite(db, prerequisite_id=prerequisite_id)
    if db_prerequisite is None:
        raise HTTPException(status_code=404, detail="prerequisite not found")
    return db_prerequisite


@app.delete("/prerequisite/{prerequisite_id}")
def delete_prerequisite(prerequisite_id: int, db: Session = Depends(get_db)):
    crud.delete_prerequisite_by_id(db=db, prerequisite_id=prerequisite_id)
    return {"massage": f"prerequisite with id: {prerequisite_id} successfully deleted"}


# application of courses
# -------------------------------------------------------------------------------------------------------


@app.post("/course/", response_model=schemas.Course)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id=course.id)
    # if db_student:
    #     raise HTTPException(status_code=400, detail="Student Id already registered")
    return crud.create_course(db=db, course=course)


@app.get("/course/", response_model=list[schemas.Course])
def read_courses(db: Session = Depends(get_db)):
    courses = crud.get_courses(db)
    return courses


@app.get("/course/{course_id}", response_model=list[schemas.CourseRelations])
def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="course not found")
    return db_course


@app.delete("/course/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    crud.delete_course_by_id(db=db, course_id=course_id)
    return {"massage": f"course with id: {course_id} successfully deleted"}


# application of presentation
# -------------------------------------------------------------------------------------------------------


@app.post("/presentation/", response_model=schemas.Presentation)
def create_presentation(presentation: schemas.PresentationCreate, db: Session = Depends(get_db)):
    db_presentation = crud.get_presentation(db, presentation_id=presentation.id)
    # if db_student:
    #     raise HTTPException(status_code=400, detail="Student Id already registered")
    return crud.create_presentation(db=db, presentation=presentation)


@app.get("/presentation/{presentation_id}", response_model=list[schemas.Presentation])
def read_presentation(presentation_id: int, db: Session = Depends(get_db)):
    db_presentation = crud.get_presentation(db, presentation_id=presentation_id)
    if db_presentation is None:
        raise HTTPException(status_code=404, detail="presentation not found")
    return db_presentation


@app.delete("/presentation/{presentation_id}")
def delete_presentation(presentation_id: int, db: Session = Depends(get_db)):
    crud.delete_presentation_by_id(db=db, presentation_id=presentation_id)
    return {"massage": f"presentation with id: {presentation_id} successfully deleted"}


# application of class
# -------------------------------------------------------------------------------------------------------


@app.post("/class/", response_model=schemas.Class)
def create_class(class_: schemas.ClassCreate, db: Session = Depends(get_db)):
    db_class = crud.get_class(db, class_id=class_.id)
    # if db_student:
    #     raise HTTPException(status_code=400, detail="Student Id already registered")
    return crud.create_class(db=db, class_=class_)


@app.get("/class/", response_model=list[schemas.Class])
def read_classes(db: Session = Depends(get_db)):
    classes = crud.get_classes(db)
    return classes


@app.get("/class/{class_id}", response_model=list[schemas.Class])
def read_class(class_id: int, db: Session = Depends(get_db)):
    db_class = crud.get_class(db, class_id=class_id)
    if db_class is None:
        raise HTTPException(status_code=404, detail="class not found")
    return db_class


@app.delete("/class/{class_id}")
def delete_class(class_id: int, db: Session = Depends(get_db)):
    crud.delete_class_by_id(db=db, class_id=class_id)
    return {"massage": f"class with id: {class_id} successfully deleted"}


# application of schedule
# -------------------------------------------------------------------------------------------------------


@app.post("/schedule/", response_model=schemas.Schedule)
def create_schedule(schedule: schemas.ScheduleCreate, db: Session = Depends(get_db)):
    db_schedule = crud.get_schedule(db, schedule_id=schedule.id)
    # if db_student:
    #     raise HTTPException(status_code=400, detail="Student Id already registered")
    return crud.create_schedule(db=db, schedule=schedule)


@app.get("/schedule/{schedule_id}", response_model=list[schemas.Schedule])
def read_schedule(schedule_id: int, db: Session = Depends(get_db)):
    db_schedule = crud.get_schedule(db, schedule_id=schedule_id)
    if db_schedule is None:
        raise HTTPException(status_code=404, detail="schedule not found")
    return db_schedule


@app.delete("/schedule/{schedule_id}")
def delete_schedule(schedule_id: int, db: Session = Depends(get_db)):
    crud.delete_schedule_by_id(db=db, schedule_id=schedule_id)
    return {"massage": f"schedule with id: {schedule_id} successfully deleted"}


# application of schedule
# -------------------------------------------------------------------------------------------------------


@app.post("/selected_course/", response_model=schemas.SelectedCourse)
def create_selected_course(selected_course: schemas.SelectedCourseCreate, db: Session = Depends(get_db)):
    db_schedule = crud.get_selected_course(db, selected_course_id=selected_course.id)
    # if db_student:
    #     raise HTTPException(status_code=400, detail="Student Id already registered")
    return crud.create_selected_course(db=db, selected_course=selected_course)


@app.get("/selected_course/{selected_course_id}", response_model=list[schemas.SelectedCourse])
def read_selected_course(selected_course_id: int, db: Session = Depends(get_db)):
    db_selected_course = crud.get_selected_course(db, selected_course_id=selected_course_id)
    if db_selected_course is None:
        raise HTTPException(status_code=404, detail="selected course not found")
    return db_selected_course


@app.delete("/selected_course/{selected_course_id}")
def delete_selected_course(selected_course_id: int, db: Session = Depends(get_db)):
    crud.delete_selected_course_by_id(db=db, selected_course_id=selected_course_id)
    return {"massage": f"selected course with id: {selected_course_id} successfully deleted"}
