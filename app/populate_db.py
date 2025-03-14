from database import SessionLocal
from models import Employee
from datetime import datetime

# Dados dos funcionários
employees = [
    {
        "name": "Anakin Skywalker",
        "email": "skywalker@ssys.com.br",
        "department": "Architecture",
        "salary": 4000.00,
        "birth_date": datetime.strptime("01-01-1983", "%d-%m-%Y").date(),
    },
    {
        "name": "Obi-Wan Kenobi",
        "email": "kenobi@ssys.com.br",
        "department": "Back-End",
        "salary": 3000.00,
        "birth_date": datetime.strptime("01-01-1977", "%d-%m-%Y").date(),
    },
    {
        "name": "Leia Organa",
        "email": "organa@ssys.com.br",
        "department": "DevOps",
        "salary": 5000.00,
        "birth_date": datetime.strptime("01-01-1980", "%d-%m-%Y").date(),
    },
]

# Populando o banco
db = SessionLocal()
for emp in employees:
    db_employee = Employee(**emp)
    db.add(db_employee)
db.commit()
db.close()

try:
    for emp in employees:
        db_employee = Employee(**emp)
        db.add(db_employee)
    db.commit()
    print("Banco populado com sucesso!")
except Exception as e:
    print(f"Erro ao popular o banco: {e}")
finally:
    db.close()

