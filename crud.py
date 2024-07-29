from sqlalchemy import select, update
from sqlalchemy.orm import Session
from models import engine
import models
import schemas


# Student CRUD
# ----------------------------------------------------------------------------------------------------------------------


def get_student(db: Session(engine), student_id: int):
    db_student = db.scalars(select(models.Student).where(models.Student.id == student_id))
    if not [*db_student]:
        return None
    return db.scalars(select(models.Student).where(models.Student.id == student_id)).one()


def get_student_by_name(db: Session(engine), student_name: str):
    db_student = db.scalars(select(models.Student).where(models.Student.name == student_name))
    if not [*db_student]:
        return None
    return db.scalars(select(models.Student).where(models.Student.name == student_name)).one()


def get_students(db: Session(engine)):
    return db.scalars(select(models.Student))


def create_student(db: Session(engine), student: schemas.StudentCreate):
    db_student = models.Student(id=student.id, name=student.name, field=student.field, semester_no=student.semester_no)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def update_student(db: Session(engine), student: schemas.StudentUpdate):
    db_student = db.scalars(select(models.Student).where(models.Student.id == student.id)).one()
    db_student.name = student.name
    db_student.field = student.field
    db_student.semester_no = student.semester_no
    db.commit()
    db_student = db.scalars(select(models.Student).where(models.Student.id == student.id))
    return db_student


def delete_student_by_id(db: Session(engine), student_id: int):
    db_student = db.get(models.Student, student_id)
    db.delete(db_student)
    db.commit()
    return db_student


# Teacher CRUD
# ----------------------------------------------------------------------------------------------------------------------


def get_teacher(db: Session(engine), teacher_id: int):
    db_teacher = db.scalars(select(models.Teacher).where(models.Teacher.id == teacher_id))
    if not [*db_teacher]:
        return None
    return db.scalars(select(models.Teacher).where(models.Teacher.id == teacher_id)).one()


def get_teacher_by_name(db: Session(engine), teacher_name: str):
    db_teacher = db.scalars(select(models.Teacher).where(models.Teacher.name == teacher_name))
    if not [*db_teacher]:
        return None
    return db.scalars(select(models.Teacher).where(models.Teacher.name == teacher_name)).one()


def get_teachers(db: Session(engine)):
    return db.scalars(select(models.Teacher))


def create_teacher(db: Session(engine), teacher: schemas.TeacherCreate):
    db_teacher = models.Teacher(id=teacher.id, name=teacher.name, profession=teacher.profession)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher


def delete_teacher_by_id(db: Session(engine), teacher_id: int):
    db_teacher = db.get(models.Teacher, teacher_id)
    db.delete(db_teacher)
    db.commit()
    return db_teacher


# Prerequisite CRUD
# ----------------------------------------------------------------------------------------------------------------------


def get_prerequisite(db: Session(engine), prerequisite_id: int):
    db_prerequisite = db.scalars(select(models.Prerequisite).where(models.Prerequisite.id == prerequisite_id))
    if not [*db_prerequisite]:
        return None
    return db.scalars(select(models.Prerequisite).where(models.Prerequisite.id == prerequisite_id)).one()


def get_prerequisites(db: Session(engine)):
    return db.scalars(select(models.Teacher))


def create_prerequisite(db: Session(engine), prerequisite: schemas.PrerequisiteCreate):
    db_prerequisite = models.Prerequisite(id=prerequisite.id, main_course_id=prerequisite.main_course_id,
                                          prerequisite_id=prerequisite.prerequisite_id)
    db.add(db_prerequisite)
    db.commit()
    db.refresh(db_prerequisite)
    return db_prerequisite


def delete_prerequisite_by_id(db: Session(engine), prerequisite_id: int):
    db_prerequisite = db.get(models.Prerequisite, prerequisite_id)
    db.delete(db_prerequisite)
    db.commit()
    return db_prerequisite


# Course CRUD
# ----------------------------------------------------------------------------------------------------------------------


def get_course(db: Session(engine), course_id: int):
    db_course = db.scalars(select(models.Course).where(models.Course.id == course_id))
    if not [*db_course]:
        return None
    return db.scalars(select(models.Course).where(models.Course.id == course_id)).one()


def get_course_by_name(db: Session(engine), course_name: str):
    db_course = db.scalars(select(models.Course).where(models.Course.name == course_name))
    if not [*db_course]:
        return None
    return db.scalars(select(models.Course).where(models.Course.id == course_name)).one()


def get_courses(db: Session(engine)):
    return db.scalars(select(models.Course))


def create_course(db: Session(engine), course: schemas.CourseCreate):
    db_course = models.Course(id=course.id, name=course.name)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


def delete_course_by_id(db: Session(engine), course_id: int):
    db_course = db.get(models.Course, course_id)
    db.delete(db_course)
    db.commit()
    return db_course


# Presentation CRUD
# ----------------------------------------------------------------------------------------------------------------------


def get_presentation(db: Session(engine), presentation_id: int):
    db_presentation = db.scalars(select(models.Presentation).where(models.Presentation.id == presentation_id))
    if not [*db_presentation]:
        return None
    return db.scalars(select(models.Presentation).where(models.Presentation.id == presentation_id)).one()


def get_presentations(db: Session(engine)):
    return db.scalars(select(models.Presentation))


def create_presentation(db: Session(engine), presentation: schemas.PresentationCreate):
    db_presentation = models.Presentation(id=presentation.id, course_id=presentation.course_id,
                                          teacher_id=presentation.teacher_id, time=presentation.time)
    db.add(db_presentation)
    db.commit()
    db.refresh(db_presentation)
    return db_presentation


def delete_presentation_by_id(db: Session(engine), presentation_id: int):
    db_presentation = db.get(models.Presentation, presentation_id)
    db.delete(db_presentation)
    db.commit()
    return db_presentation


# Class CRUD
# ----------------------------------------------------------------------------------------------------------------------


def get_class(db: Session(engine), class_id: int):
    db_class = db.scalars(select(models.Class).where(models.Class.id == class_id))
    if not [*db_class]:
        return None
    return db.scalars(select(models.Class).where(models.Class.id == class_id)).one()


def get_class_by_name(db: Session(engine), class_name: str):
    db_class = db.scalars(select(models.Class).where(models.Class.name == class_name))
    if not [*db_class]:
        return None
    return db.scalars(select(models.Class).where(models.Class.id == class_name)).one()


def get_classes(db: Session(engine)):
    return db.scalars(select(models.Class))


def create_class(db: Session(engine), class_: schemas.ClassCreate):
    db_class = models.Class(id=class_.id, name=class_.name, )
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class


def delete_class_by_id(db: Session(engine), class_id: int):
    db_class = db.get(models.Class, class_id)
    db.delete(db_class)
    db.commit()
    return db_class


# Schedule CRUD
# ----------------------------------------------------------------------------------------------------------------------


def get_schedule(db: Session(engine), schedule_id: int):
    db_schedule = db.scalars(select(models.Schedule).where(models.Schedule.id == schedule_id))
    if not [*db_schedule]:
        return None
    return db.scalars(select(models.Schedule).where(models.Schedule.id == schedule_id)).one()


def get_schedules(db: Session(engine)):
    return db.scalars(select(models.Schedule))


def create_schedule(db: Session(engine), schedule: schemas.ScheduleCreate):
    db_schedule = models.Schedule(id=schedule.id, presentation_id=schedule.presentation_id,
                                  class_id=schedule.class_id, time=schedule.time)
    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)
    return db_schedule


def delete_schedule_by_id(db: Session(engine), schedule_id: int):
    db_schedule = db.get(models.Schedule, schedule_id)
    db.delete(db_schedule)
    db.commit()
    return db_schedule


# Selected Course CRUD
# ----------------------------------------------------------------------------------------------------------------------


def get_selected_course(db: Session(engine), selected_course_id: int):
    db_selected_course = db.scalars(select(models.SelectedCourse).where(models.SelectedCourse.id == selected_course_id))
    if not [*db_selected_course]:
        return None
    return db.scalars(select(models.SelectedCourse).where(models.SelectedCourse.id == selected_course_id)).one()


def get_selected_courses(db: Session(engine)):
    return db.scalars(select(models.SelectedCourse))


def create_selected_course(db: Session(engine), selected_course: schemas.SelectedCourse):
    db_selected_course = models.SelectedCourse(id=selected_course.id, student_id=selected_course.student_id,
                                               presentation_id=selected_course.presentation_id)
    db.add(db_selected_course)
    db.commit()
    db.refresh(db_selected_course)
    return db_selected_course


def delete_selected_course_by_id(db: Session(engine), selected_course_id: int):
    db_selected_course = db.get(models.SelectedCourse, selected_course_id)
    db.delete(db_selected_course)
    db.commit()
    return db_selected_course
