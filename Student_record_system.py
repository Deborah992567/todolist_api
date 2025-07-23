from fastapi import FastAPI , HTTPException , Path, Query
from pydantic import BaseModel 
from typing import Optional


app = FastAPI()
students = {
    1: {"name": "Uchechi Iwuh", "age": 20, "department": "Computer Science", "cgpa": 3.8, "enrolled": True},
    2: {"name": "Adaeze Obi", "age": 22, "department": "Mechanical Engineering", "cgpa": 3.2, "enrolled": False},
    3: {"name": "Chuka Eze", "age": 19, "department": "Electrical Engineering", "cgpa": 3.5, "enrolled": True},
    4: {"name": "Fatima Musa", "age": 21, "department": "Biochemistry", "cgpa": 4.0, "enrolled": True},
    5: {"name": "Tomiwa Adebayo", "age": 23, "department": "Economics", "cgpa": 2.9, "enrolled": False},
    6: {"name": "Daniel Etim", "age": 20, "department": "Computer Science", "cgpa": 3.4, "enrolled": True},
    7: {"name": "Ngozi Chinedu", "age": 24, "department": "Law", "cgpa": 3.1, "enrolled": False},
    8: {"name": "Emeka Okoro", "age": 22, "department": "Accounting", "cgpa": 3.6, "enrolled": True},
    9: {"name": "Blessing Ade", "age": 21, "department": "Mass Communication", "cgpa": 3.7, "enrolled": True},
    10: {"name": "Musa Bello", "age": 25, "department": "Architecture", "cgpa": 2.8, "enrolled": False}
}

class Students(BaseModel):
    name: str
    age: int
    department: str
    cgpa: float
    enrolled: bool
    
@app.get("/")
def read_students_record():
    return {"message": "welcome to students record fastapi"}    
