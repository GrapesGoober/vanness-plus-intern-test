
# Author: Nachat Kaewmeesang
# This code is used for internship for Vanness Plus Consulting Co., Ltd
# main.py contains APIs for the app

from typing import Annotated
from fastapi import FastAPI, Query
import intern

app = FastAPI()

@app.put("/api/intern")
async def edit_intern(body: intern.InternInfo) -> bool:
    return intern.edit_intern(body)

@app.post("/api/intern")
async def add_intern(body: intern.InternInfo) -> bool:
    return intern.add_intern(body)

@app.delete("/api/intern")
async def remove_intern(id: int) -> bool:
    return intern.remove_intern(id)

@app.get("/api/intern")
async def get_intern(filter: Annotated[intern.GetInternsFilter, Query()]) -> list[intern.InternInfo]:
    return intern.get_intern(filter)