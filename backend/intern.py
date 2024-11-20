# Author: Nachat Kaewmeesang
# This code is used for internship for Vanness Plus Consulting Co., Ltd
# intern.py contains business logic for managing intern list

from enum import Enum
import mysql.connector
from pydantic import BaseModel
from datetime import date

# I'd keep the db file next to the features they're servicing for
# The idea is that each service might have different database requirements
# Which means they'll have their own database connections
def connect_to_db():
    # FYI: these MySQL environment variables are defined in compose.yaml
    return mysql.connector.connect(
        host="mysql",
        user="root",
        password="",
        database="interns_db"
    )

# Enumeration of allowed values of intern
# This is as described by the instructions
# Prefer to put this into enum to auto-generate docs
class InternStatus(str, Enum):
    NEW  = "New"
    WIP  = "WIP"
    WAIT = "Wait"
    PASS = "Pass"
    FAIL = "Fail"
    HIRE = "Hire"

class RequestAddIntern(BaseModel):
    name:           str     = "John Doe"
    applied_date:   date    = date(2024, 1, 1)
    role:           str     = "Web Application Trainee"
    status:         InternStatus = InternStatus.NEW

def add_intern(body: RequestAddIntern) -> bool:
        
    mydb = connect_to_db()
    mycursor = mydb.cursor()
    mycursor.execute("""
        INSERT INTO `interns` 
        (`name`, `applied_date`, `role`, `status`) 
        VALUES (%(name)s, %(applied_date)s, %(role)s, %(status)s);
    """, body.model_dump())
    mycursor.close()
    mydb.commit()

    return True

class RequestRemoveIntern(BaseModel):
    id: int

def remove_intern(body: RequestRemoveIntern) -> bool:
        
    mydb = connect_to_db()
    mycursor = mydb.cursor()
    mycursor.execute("""
        DELETE FROM interns WHERE id = %(id)s
    """, body.model_dump())
    mycursor.close()
    mydb.commit()

    return True


class RequestGetInterns(BaseModel):
    ...

class ResponseGetInterns(BaseModel):
    id:             int
    name:           str
    applied_date:   date
    role:           str
    status:         InternStatus

def get_intern(body: RequestGetInterns) -> list[ResponseGetInterns]:
        
    mydb = connect_to_db()
    mycursor = mydb.cursor()
    mycursor.execute("""
        SELECT 
            `id`, `name`, `applied_date`, `role`, `status` 
        FROM interns
    """)
    result: list[ResponseGetInterns] = []
    for i in mycursor.fetchall():
        resp = ResponseGetInterns(**{
            k: v for k, v in zip( ResponseGetInterns.model_fields.keys(), i )
        })
        result.append(resp)
    mycursor.close()

    return result