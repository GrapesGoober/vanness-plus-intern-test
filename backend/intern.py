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

class InternBody(BaseModel):
    name:           str     = "John Doe"
    applied_date:   date    = date(2024, 1, 1)
    role:           str     = "Web Application Trainee"
    status:         InternStatus = InternStatus.NEW

def add_intern(body: InternBody) -> bool:
        
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

def remove_intern(id: int) -> bool:
        
    mydb = connect_to_db()
    mycursor = mydb.cursor()
    mycursor.execute("""
        DELETE FROM interns WHERE id = %s
    """, id)
    mycursor.close()
    mydb.commit()

    return True

class GetInternsFilter(BaseModel):
    ...

class GetInternItem(BaseModel):
    id:     int
    body:   InternBody

def get_intern(filter: GetInternsFilter) -> list[GetInternItem]:
        
    mydb = connect_to_db()
    mycursor = mydb.cursor()
    mycursor.execute("""
        SELECT 
            `id`, `name`, `applied_date`, `role`, `status` 
        FROM interns
    """)
    result: list[GetInternItem] = []
    for i in mycursor.fetchall():
        resp = GetInternItem(**{
            k: v for k, v in zip( GetInternItem.model_fields.keys(), i )
        })
        result.append(resp)
    mycursor.close()

    return result