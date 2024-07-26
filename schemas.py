from pydantic import BaseModel


class Student(BaseModel):
    id: int
    name: str
    field: str
    semester_no: int


class StudentCreate(Student):
    pass


class StudentUpdate(Student):
    pass


class Teacher(BaseModel):
    id: int
    name: str
    profession: str


class TeacherCreate(Student):
    pass


class Prerequisite(BaseModel):
    id: int
    main_course_id: int
    prerequisite_id: int

    class Config:
        orm_mode = True


class PrerequisiteCreate(Prerequisite):
    pass


class Course(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class CourseCreate(Course):
    pass


class Presentation(BaseModel):
    id: int
    course_id: int
    teacher_id: int
    time: str

    class Config:
        orm_mode = True


class PresentationCreate(Presentation):
    pass


class Class(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class ClassCreate(Class):
    pass


class Schedule(BaseModel):
    id: int
    presentation_id: int
    class_id: int
    time: str

    class Config:
        orm_mode = True


class ScheduleCreate(Schedule):
    pass


class SelectedCourse(BaseModel):
    id: int
    student_id: int
    presentation_id: int

    class Config:
        orm_mode = True


class SelectedCourseCreate(SelectedCourse):
    pass


class StudentRelations(Student):
    selected_course: list[SelectedCourse] = []

    class Config:
        orm_mode = True


class TeacherRelations(Teacher):
    presentation: list[Presentation] = []

    class Config:
        orm_mode = True


class CourseRelations(Course):
    prerequisite: list[Prerequisite] = []
    prerequisite_1: list[Prerequisite] = []
    presentation: list[Presentation] = []

    class Config:
        orm_mode = True


class PresentationRelations(Presentation):
    schedule: list[Schedule] = []
    selected_course: list[SelectedCourse] = []

    class Config:
        orm_mode = True


class ClassRelations(Class):
    schedule: list[Schedule] = []

    class Config:
        orm_mode = True
