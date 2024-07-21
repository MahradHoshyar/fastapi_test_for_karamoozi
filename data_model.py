from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import select
from sqlalchemy import MetaData
from sqlalchemy import *
from sqlalchemy.orm import *

# creating tables


class Base(DeclarativeBase):
    metadata=MetaData(schema="public")
    pass


class Student(Base):
    __tablename__ = "Student"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    field: Mapped[str]
    semester_no: Mapped[int]
    selected_course: Mapped[list["SelectedCourse"]] = relationship(back_populates="student")

    def __repr__(self) -> str:
        return f"Student(id={self.id!r}, name={self.name!r}, field={self.field!r}, semester no={self.semester_no!r})"


class Teacher(Base):
    __tablename__ = "Teacher"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    profession: Mapped[str] = mapped_column(String(255))
    presentation: Mapped[list["Presentation"]] = relationship(back_populates="teacher")

    def __repr__(self) -> str:
        return f"Teacher(id={self.id!r}, name={self.name!r}, profession={self.profession!r})"


class Prerequisite(Base):
    __tablename__ = "Prerequisite"
    Pre_id: Mapped[int] = mapped_column(primary_key=True)
    main_course_id: Mapped[int] = mapped_column(ForeignKey("Course.C_id"))
    pre_course_id: Mapped[int] = mapped_column(ForeignKey("Course.C_id"))
    main_course = relationship("Course", foreign_keys=[main_course_id])
    pre_course = relationship("Course", foreign_keys=[pre_course_id])

    def __repr__(self) -> str:
        return (f"Prerequisite(id={self.id!r}, main_course_id={self.main_course_id!r},"
                f" pre_course_id={self.pre_course_id!r})")


class Course(Base):
    __tablename__ = "Course"
    C_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    presentation: Mapped[List["Presentation"]] = relationship(back_populates="course")
    as_pre_course: Mapped[List["Prerequisite"]] = relationship(foreign_keys=[Prerequisite.pre_course_id] ,back_populates="pre_course")
    as_main_course: Mapped[List["Prerequisite"]] = relationship(foreign_keys=[Prerequisite.main_course_id],back_populates="main_course")

    def __repr__(self) -> str:
        return f"Course(id={self.C_id!r}, name={self.name!r})"


class Presentation(Base):
    __tablename__ = "Presentation"
    id: Mapped[int] = mapped_column(primary_key=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("Course.C_id"))
    teacher_id: Mapped[int] = mapped_column(ForeignKey("Teacher.id"))
    time: Mapped[str]
    course: Mapped["Course"] = relationship(back_populates="presentation")
    teacher: Mapped["Teacher"] = relationship(back_populates="presentation")
    schedule: Mapped[list["Schedule"]] = relationship(back_populates="presentation")
    selected_course: Mapped[list["SelectedCourse"]] = relationship(back_populates="presentation")

    def __repr__(self) -> str:
        return (f"Presentation(id={self.id!r}, course id={self.course_id!r}, teacher id={self.teacher_id!r}, "
                f"time={self.time!r})")


class Class(Base):
    __tablename__ = "Class"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    schedule: Mapped[list["Schedule"]] = relationship(back_populates="class_")

    def __repr__(self) -> str:
        return f"Class(id={self.id!r}, name={self.name!r})"


class Schedule(Base):
    __tablename__ = "Schedule"
    id: Mapped[int] = mapped_column(primary_key=True)
    presentation_id: Mapped[int] = mapped_column(ForeignKey("Presentation.id"))
    class_id: Mapped[int] = mapped_column(ForeignKey("Class.id"))
    time: Mapped[str]
    presentation: Mapped["Presentation"] = relationship(back_populates="schedule")
    class_: Mapped["Class"] = relationship(back_populates="schedule")

    def __repr__(self) -> str:
        return (f"Schedule(id={self.id!r}, presentation id={self.presentation_id!r}, class id={self.class_id!r},"
                f"time={self.time!r})")


class SelectedCourse(Base):
    __tablename__ = "Selected Course"
    id: Mapped[int] = mapped_column(primary_key=True)
    student_id: Mapped[int] = mapped_column(ForeignKey("Student.id"))
    presentation_id: Mapped[int] = mapped_column(ForeignKey("Presentation.id"))
    student: Mapped["Student"] = relationship(back_populates="selected_course")
    presentation: Mapped["Presentation"] = relationship(back_populates="selected_course")

    def __repr__(self) -> str:
        return (f"Selected Course(id={self.id!r}, student id={self.student_id!r},"
                f" presentation id={self.presentation_id!r})")


engine = create_engine("postgresql://postgres:Mh8913hoshyar8913@localhost", echo=True)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
