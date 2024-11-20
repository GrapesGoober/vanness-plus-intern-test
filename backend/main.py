
# Author: Nachat Kaewmeesang
# This code is used for internship for Vanness Plus Consulting Co., Ltd
# main.py contains APIs for the app

from fastapi import FastAPI
from pydantic import BaseModel
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

def connect_to_db():
    # these configs are defined in compose.yaml
    return mysql.connector.connect(
        # connects to mysql container, instead of normally via "localhost"
        host="mysql",
        user="root",
        password="",
        database="interns_db"
    )

class RecordTextBody(BaseModel):
    text: str

@app.post("/api/send_to_sql")
async def send_to_sql(body: RecordTextBody):
        
    mydb = connect_to_db()
    mycursor = mydb.cursor()
    mycursor.execute("INSERT INTO `interns` (`text`) VALUES (%s)", (body.text,))
    mycursor.close()
    mydb.commit()

    return True