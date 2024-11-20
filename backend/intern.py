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
class InternRecordStatus(str, Enum):
    NEW  = "New"
    WIP  = "WIP"
    WAIT = "Wait"
    PASS = "Pass"
    FAIL = "Fail"
    HIRE = "Hire"

# The request body definition to add a new intern record
class AddInternRecordBody(BaseModel):
    name:           str     = "John Doe"
    applied_date:   date    = date(2024, 1, 1)
    role:           str     = "Web Application Trainee"
    status:         InternRecordStatus = InternRecordStatus.NEW

def add_intern_record(body: AddInternRecordBody) -> bool:
        
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