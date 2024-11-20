
# Author: Nachat Kaewmeesang
# This code is used for internship for Vanness Plus Consulting Co., Ltd
# main.py contains APIs for the app

from fastapi import FastAPI
import intern

app = FastAPI()

@app.post("/api/add_intern")
async def add_intern(body: intern.RequestAddIntern) -> bool:
    return intern.add_intern(body)

@app.post("/api/remove_intern")
async def remove_intern(body: intern.RequestRemoveIntern) -> bool:
    return intern.remove_intern(body)

@app.post("/api/get_intern")
async def get_intern(body: intern.RequestGetInterns) -> list[intern.ResponseGetInterns]:
    return intern.get_intern(body)