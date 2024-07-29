from sqlalchemy import create_engine
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql+psycopg2://postgres:13821382@localhost:5432/postgres", echo=True)


class Base(DeclarativeBase):
    pass


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


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
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    main_course_id = mapped_column(Integer, ForeignKey("Course.id"))
    prerequisite_id = mapped_column(Integer, ForeignKey("Course.id"))

    main_course: Mapped["Course"] = relationship(back_populates="prerequisite",
                                                 foreign_keys=[main_course_id])
    prerequisite_course: Mapped["Course"] = relationship(back_populates="prerequisite_1",
                                                         foreign_keys=[prerequisite_id])

    def __repr__(self) -> str:
        return (f"Prerequisite(id={self.id!r}, main course id={self.main_course_id!r},"
                f" prerequisite id={self.prerequisite_id!r})")


class Course(Base):
    __tablename__ = "Course"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    prerequisite: Mapped[list["Prerequisite"]] = relationship(back_populates="main_course",
                                                              foreign_keys=[Prerequisite.main_course_id])
    prerequisite_1: Mapped[list["Prerequisite"]] = relationship(back_populates="prerequisite_course",
                                                                foreign_keys=[Prerequisite.prerequisite_id])
    presentation: Mapped[list["Presentation"]] = relationship(back_populates="course")

    def __repr__(self) -> str:
        return f"Course(id={self.id!r}, name={self.name!r})"


class Presentation(Base):
    __tablename__ = "Presentation"
    id: Mapped[int] = mapped_column(primary_key=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("Course.id"))
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
