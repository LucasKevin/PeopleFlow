from pydantic import BaseModel
from datetime import date

class EmployeeBase(BaseModel):
    name: str
    email: str
    department: str 
    salary: float
    birth_date: date

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeResponse(EmployeeBase):
    id: int

    class Config:
        orm_mode = True