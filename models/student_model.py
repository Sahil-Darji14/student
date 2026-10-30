
from pydantic import BaseModel, EmailStr, Field


class StudentCreate(BaseModel):
    name: str = Field(..., min_length=2)
    email: EmailStr
    course: str = Field(..., min_length=2)


class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    course: str
