# Author: Nachat Kaewmeesang
# This code is used for internship for Vanness Plus Consulting Co., Ltd
# intern.py contains business logic for managing intern list

from enum import Enum
from typing import Optional
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

class InternInfo(BaseModel):
    """
    Base model representing an intern.
    """
    name:           str     = "John Doe"
    applied_date:   date    = date(2024, 1, 1)
    role:           str     = "Web Application Trainee"
    status:         InternStatus = InternStatus.NEW

class InternInfoWithId(InternInfo):
    id: int = 0
    
class InternsFilter(BaseModel):
    """
    Filter used by get_intern. The logic for filtering is defined in get_intern.
    """
    applied_date: date = date(2024, 1, 1)
    status: InternStatus | None = None
    ...

def add_intern(body: InternInfo) -> bool:
    """
    Add a new intern. Ignores the `id` attribute. Returns `True` if success.
    """
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

def edit_intern(body: InternInfoWithId) -> bool:
    """
    Edits existing intern based on ID. Doesn't check whether intern exists.
    Returns `True` if success, regardless whether intern exists.
    Returns `False` if ID field not specified.
    """
    if body.id == None:
        return False

    mydb = connect_to_db()
    mycursor = mydb.cursor()
    mycursor.execute("""
        UPDATE `interns`
        SET `name` = %(name)s,
            `applied_date` = %(applied_date)s,
            `role` = %(role)s,
            `status` = %(status)s
        WHERE `id` = %(id)s;
    """, body.model_dump())
    mycursor.close()
    mydb.commit()

    return True

def remove_intern(id: int) -> bool:
    """
    Removes intern based on ID. Returns True if success, regardless if intern exists or not
    """
    mydb = connect_to_db()
    mycursor = mydb.cursor()
    mycursor.execute("""
        DELETE FROM interns WHERE id = %s
    """, id)
    mycursor.close()
    mydb.commit()

    return True

def get_intern(filter: InternsFilter) -> list[InternInfoWithId]:
    """
    Get a list of InternInfo, with filter GetInternsFilter.
    """
        
    mydb = connect_to_db()
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("""
        SELECT 
            `id`, `name`, `applied_date`, `role`, `status` 
        FROM interns
    """)
    result: list[InternInfoWithId] = []
    for i in mycursor.fetchall():
        resp = InternInfoWithId(**i)
        result.append(resp)
    mycursor.close()

    return result