
# Author: Nachat Kaewmeesang
# This code is used for internship for Vanness Plus Consulting Co., Ltd
# main.py contains APIs for the app

from fastapi import FastAPI
import intern

app = FastAPI()

@app.post("/api/add_intern_record")
async def add_intern_record(body: intern.AddInternRecordBody):
    return intern.add_intern_record(body)