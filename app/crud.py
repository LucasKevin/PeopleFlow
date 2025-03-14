from sqlalchemy.orm import Session
import models, schemas
from sqlalchemy.sql import func

def get_employees(db: Session):
    return db.query(models.Employee).all()

def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()

def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(**employee.model_dump())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def update_employee(db: Session, employee_id: int, updated_data: schemas.EmployeeCreate):
    db_employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if db_employee:
        for key, value in updated_data.model_dump().items():
            setattr(db_employee, key, value)
        db.commit()
        db.refresh(db_employee)
    return db_employee

def delete_employee(db: Session, employee_id: int):
    db_employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if db_employee:
        db.delete(db_employee)
        db.commit()
    return db_employee

def get_age_report(db: Session):
    employees = db.query(models.Employee).all()
    if not employees:
        return None

    younger = min(employees, key=lambda emp: emp.birth_date)
    older = max(employees, key=lambda emp: emp.birth_date)
    
    avg_age = sum((2024 - emp.birth_date.year) for emp in employees) / len(employees)

    return {
        "younger": younger,
        "older": older,
        "average": round(avg_age, 2)
    }

def get_salary_report(db: Session):
    employees = db.query(models.Employee).all()
    if not employees:
        return None

    lowest = min(employees, key=lambda emp: emp.salary)
    highest = max(employees, key=lambda emp: emp.salary)
    avg_salary = sum(emp.salary for emp in employees) / len(employees)

    return {
        "lowest": lowest,
        "highest": highest,
        "average": round(avg_salary, 2)
    }