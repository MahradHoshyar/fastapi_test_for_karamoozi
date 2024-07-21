from pydantic import BaseModel


class BaseStudent(BaseModel):
    id: int
    name: str
    field: str
    semester_no: str


class StudentCreate(BaseStudent):
    password: str
    pass

class Student(BaseStudent):
    is_active: bool
    class Config:
        from_attributes = True
    
