from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine
from fastapi.security import OAuth2PasswordRequestForm
from auth import ACCESS_TOKEN_EXPIRE_MINUTES
from database import get_db
from fastapi import HTTPException

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

@app.get("/employees/", response_model=list[schemas.EmployeeResponse])
def read_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)

@app.post("/employees/", response_model=schemas.EmployeeResponse)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, employee)

@app.get("/employees/{employee_id}", response_model=schemas.EmployeeResponse)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    return crud.get_employee(db, employee_id)

@app.put("/employees/{employee_id}", response_model=schemas.EmployeeResponse)
def update_employee(employee_id: int, updated_data: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.update_employee(db, employee_id, updated_data)

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    return crud.delete_employee(db, employee_id)

@app.get("/reports/employees/age/")
def age_report(db: Session = Depends(get_db)):
    return crud.get_age_report(db)

@app.get("/reports/employees/salary/")
def salary_report(db: Session = Depends(get_db)):
    return crud.get_salary_report(db)

from auth import authenticate_user, create_access_token, get_current_user
from datetime import timedelta

@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Usuário ou senha incorretos")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}
