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

@app.post("/students/create", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student.id)
    if db_student:
        raise HTTPException(status_code=400, detail="Student Id already registered")
    return crud.create_student(db=db, student=student)


@app.get("/students/", response_model=list[schemas.Student])
def read_students(db: Session = Depends(get_db)):
    students = crud.get_students(db)
    return students


@app.get("/students/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db=db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="student not found")
    return db_student


@app.get("/students/{student_name}", response_model=schemas.Student)
def read_student_by_name(student_name: str, db: Session = Depends(get_db)):
    db_student = crud.get_student_by_name(db=db, student_name=student_name)
    if db_student is None:
        raise HTTPException(status_code=404, detail="student not found")
    return db_student


@app.put("/student/update/{student_id}", response_model=schemas.Student)
def update_student(student: schemas.StudentUpdate, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student.id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found!")
    return crud.update_student(db=db, student=student)


@app.delete("/students/delete/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    crud.delete_student_by_id(db=db, student_id=student_id)
    return {"massage": f"student with id: {student_id} successfully deleted"}


# application of teachers
# -------------------------------------------------------------------------------------------------------

@app.post("/teacher/create", response_model=schemas.Teacher)
def create_teacher(teacher: schemas.TeacherCreate, db: Session = Depends(get_db)):
    db_teacher = crud.get_teacher(db, teacher_id=teacher.id)
    if db_teacher:
        raise HTTPException(status_code=400, detail="teacher Id already registered")
    return crud.create_teacher(db=db, teacher=teacher)


@app.get("/teachers/", response_model=list[schemas.Teacher])
def read_teachers(db: Session = Depends(get_db)):
    teachers = crud.get_teachers(db)
    return teachers


@app.get("/teachers/{teacher_id}", response_model=schemas.Teacher)
def read_teacher(teacher_id: int, db: Session = Depends(get_db)):
    db_teacher = crud.get_teacher(db, teacher_id=teacher_id)
    if db_teacher is None:
        raise HTTPException(status_code=404, detail="teacher not found")
    return db_teacher


@app.get("/teacher/{teacher_name}", response_model=schemas.Teacher)
def read_teacher_by_name(teacher_name: str, db: Session = Depends(get_db)):
    db_teacher = crud.get_teacher_by_name(db=db, teacher_name=teacher_name)
    if db_teacher is None:
        raise HTTPException(status_code=404, detail="teacher not found")
    return db_teacher


@app.put("/teacher/update/{teacher_id}", response_model=schemas.Teacher)
def update_teacher(teacher: schemas.TeacherUpdate, db: Session = Depends(get_db)):
    db_teacher = crud.get_teacher(db, teacher_id=teacher.id)
    if db_teacher is None:
        raise HTTPException(status_code=404, detail="teacher not found!")
    return crud.update_teacher(db=db, teacher=teacher)


@app.delete("/teachers/delete/{teacher_id}")
def delete_teacher(teacher_id: int, db: Session = Depends(get_db)):
    crud.delete_teacher_by_id(db=db, teacher_id=teacher_id)
    return {"massage": f"teacher with id: {teacher_id} successfully deleted"}


# application of prerequisite
# -------------------------------------------------------------------------------------------------------

@app.post("/prerequisite/create", response_model=schemas.Prerequisite)
def create_prerequisite(prerequisite: schemas.PrerequisiteCreate, db: Session = Depends(get_db)):
    db_prerequisite = crud.get_prerequisite(db, prerequisite_id=prerequisite.id)
    if db_prerequisite:
        raise HTTPException(status_code=400, detail="prerequisite Id already registered")
    return crud.create_prerequisite(db=db, prerequisite=prerequisite)


@app.get("/prerequisite/", response_model=list[schemas.Prerequisite])
def read_prerequisites(db: Session = Depends(get_db)):
    prerequisites = crud.get_prerequisites(db)
    return prerequisites


@app.get("/prerequisite/{prerequisite_id}", response_model=schemas.Prerequisite)
def read_prerequisite(prerequisite_id: int, db: Session = Depends(get_db)):
    db_prerequisite = crud.get_prerequisite(db, prerequisite_id=prerequisite_id)
    if db_prerequisite is None:
        raise HTTPException(status_code=404, detail="prerequisite not found")
    return db_prerequisite


@app.put("/prerequisite/update/{prerequisite_id}", response_model=schemas.Prerequisite)
def update_prerequisite(prerequisite: schemas.PrerequisiteUpdate, db: Session = Depends(get_db)):
    db_prerequisite = crud.get_prerequisite(db, prerequisite_id=prerequisite.id)
    if db_prerequisite is None:
        raise HTTPException(status_code=404, detail="prerequisite not found!")
    return crud.update_prerequisite(db=db, prerequisite=prerequisite)


@app.delete("/prerequisite/delete/{prerequisite_id}")
def delete_prerequisite(prerequisite_id: int, db: Session = Depends(get_db)):
    crud.delete_prerequisite_by_id(db=db, prerequisite_id=prerequisite_id)
    return {"massage": f"prerequisite with id: {prerequisite_id} successfully deleted"}


# application of courses
# -------------------------------------------------------------------------------------------------------


@app.post("/course/create", response_model=schemas.Course)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id=course.id)
    if db_course:
        raise HTTPException(status_code=400, detail="course Id already registered")
    return crud.create_course(db=db, course=course)


@app.get("/course/", response_model=list[schemas.Course])
def read_courses(db: Session = Depends(get_db)):
    courses = crud.get_courses(db)
    return courses


@app.get("/course/{course_id}", response_model=schemas.CourseRelations)
def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="course not found")
    return db_course


@app.get("/course/{course_name}", response_model=schemas.Course)
def read_course_by_name(course_name: str, db: Session = Depends(get_db)):
    db_course = crud.get_course_by_name(db=db, course_name=course_name)
    if db_course is None:
        raise HTTPException(status_code=404, detail="course not found")
    return db_course


@app.put("/course/update/{course_id}", response_model=schemas.Course)
def update_course(course: schemas.CourseUpdate, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id=course.id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="course not found!")
    return crud.update_course(db=db, course=course)


@app.delete("/course/delete/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    crud.delete_course_by_id(db=db, course_id=course_id)
    return {"massage": f"course with id: {course_id} successfully deleted"}


# application of presentation
# -------------------------------------------------------------------------------------------------------


@app.post("/presentation/create", response_model=schemas.Presentation)
def create_presentation(presentation: schemas.PresentationCreate, db: Session = Depends(get_db)):
    db_presentation = crud.get_presentation(db, presentation_id=presentation.id)
    if db_presentation:
        raise HTTPException(status_code=400, detail="presentation Id already registered")
    return crud.create_presentation(db=db, presentation=presentation)


@app.get("/presentation/{presentation_id}", response_model=schemas.Presentation)
def read_presentation(presentation_id: int, db: Session = Depends(get_db)):
    db_presentation = crud.get_presentation(db, presentation_id=presentation_id)
    if db_presentation is None:
        raise HTTPException(status_code=404, detail="presentation not found")
    return db_presentation


@app.put("/presentation/update/{presentation_id}", response_model=schemas.Presentation)
def update_presentation(presentation: schemas.PresentationUpdate, db: Session = Depends(get_db)):
    db_presentation = crud.get_presentation(db, presentation_id=presentation.id)
    if db_presentation is None:
        raise HTTPException(status_code=404, detail="presentation not found!")
    return crud.update_presentation(db=db, presentation=presentation)


@app.delete("/presentation/delete/{presentation_id}")
def delete_presentation(presentation_id: int, db: Session = Depends(get_db)):
    crud.delete_presentation_by_id(db=db, presentation_id=presentation_id)
    return {"massage": f"presentation with id: {presentation_id} successfully deleted"}


# application of class
# -------------------------------------------------------------------------------------------------------


@app.post("/class/create", response_model=schemas.Class)
def create_class(class_: schemas.ClassCreate, db: Session = Depends(get_db)):
    db_class = crud.get_class(db, class_id=class_.id)
    if db_class:
        raise HTTPException(status_code=400, detail="class Id already registered")
    return crud.create_class(db=db, class_=class_)


@app.get("/class/", response_model=list[schemas.Class])
def read_classes(db: Session = Depends(get_db)):
    classes = crud.get_classes(db)
    return classes


@app.get("/class/{class_id}", response_model=schemas.Class)
def read_class(class_id: int, db: Session = Depends(get_db)):
    db_class = crud.get_class(db, class_id=class_id)
    if db_class is None:
        raise HTTPException(status_code=404, detail="class not found")
    return db_class


@app.get("/class/{class_name}", response_model=schemas.Class)
def read_class_by_name(class_name: str, db: Session = Depends(get_db)):
    db_class = crud.get_class_by_name(db=db, class_name=class_name)
    if db_class is None:
        raise HTTPException(status_code=404, detail="student not found")
    return db_class


@app.put("/class/update/{class_id}", response_model=schemas.Class)
def update_class(class_: schemas.ClassUpdate, db: Session = Depends(get_db)):
    db_class = crud.get_class(db, class_id=class_.id)
    if db_class is None:
        raise HTTPException(status_code=404, detail="class not found!")
    return crud.update_class(db=db, class_=class_)


@app.delete("/class/delete/{class_id}")
def delete_class(class_id: int, db: Session = Depends(get_db)):
    crud.delete_class_by_id(db=db, class_id=class_id)
    return {"massage": f"class with id: {class_id} successfully deleted"}


# application of schedule
# -------------------------------------------------------------------------------------------------------


@app.post("/schedule/create", response_model=schemas.Schedule)
def create_schedule(schedule: schemas.ScheduleCreate, db: Session = Depends(get_db)):
    db_schedule = crud.get_schedule(db, schedule_id=schedule.id)
    if db_schedule:
        raise HTTPException(status_code=400, detail="schedule Id already registered")
    return crud.create_schedule(db=db, schedule=schedule)


@app.get("/schedule/{schedule_id}", response_model=schemas.Schedule)
def read_schedule(schedule_id: int, db: Session = Depends(get_db)):
    db_schedule = crud.get_schedule(db, schedule_id=schedule_id)
    if db_schedule is None:
        raise HTTPException(status_code=404, detail="schedule not found")
    return db_schedule


@app.put("/schedule/update/{schedule_id}", response_model=schemas.Schedule)
def update_schedule(schedule: schemas.ScheduleUpdate, db: Session = Depends(get_db)):
    db_schedule = crud.get_schedule(db, schedule_id=schedule.id)
    if db_schedule is None:
        raise HTTPException(status_code=404, detail="schedule not found!")
    return crud.update_schedule(db=db, schedule=schedule)


@app.delete("/schedule/delete/{schedule_id}")
def delete_schedule(schedule_id: int, db: Session = Depends(get_db)):
    crud.delete_schedule_by_id(db=db, schedule_id=schedule_id)
    return {"massage": f"schedule with id: {schedule_id} successfully deleted"}


# application of schedule
# -------------------------------------------------------------------------------------------------------


@app.post("/selected_course/create", response_model=schemas.SelectedCourse)
def create_selected_course(selected_course: schemas.SelectedCourseCreate, db: Session = Depends(get_db)):
    db_selected_course = crud.get_selected_course(db, selected_course_id=selected_course.id)
    if db_selected_course:
        raise HTTPException(status_code=400, detail="selected course Id already registered")
    return crud.create_selected_course(db=db, selected_course=selected_course)


@app.get("/selected_course/{selected_course_id}", response_model=schemas.SelectedCourse)
def read_selected_course(selected_course_id: int, db: Session = Depends(get_db)):
    db_selected_course = crud.get_selected_course(db, selected_course_id=selected_course_id)
    if db_selected_course is None:
        raise HTTPException(status_code=404, detail="selected course not found")
    return db_selected_course


@app.put("/selected_course/update/{selected_course_id}", response_model=schemas.SelectedCourse)
def update_selected_course(selected_course: schemas.SelectedCourseUpdate, db: Session = Depends(get_db)):
    db_selected_course = crud.get_selected_course(db, selected_course_id=selected_course.id)
    if db_selected_course is None:
        raise HTTPException(status_code=404, detail="selected course not found!")
    return crud.update_selected_course(db=db, selected_course=selected_course)


@app.delete("/selected_course/delete/{selected_course_id}")
def delete_selected_course(selected_course_id: int, db: Session = Depends(get_db)):
    crud.delete_selected_course_by_id(db=db, selected_course_id=selected_course_id)
    return {"massage": f"selected course with id: {selected_course_id} successfully deleted"}
