from fastapi import FastAPI
from pydantic import BaseModel
import math


app = FastAPI()

class Numbers(BaseModel):
    a: int
    b: int

class TaskArgs(BaseModel):
    name: str
    args: Numbers

@app.post("/my/")
async def handler(obj: TaskArgs):
    a = obj.args.a
    b = obj.args.b
    return {"result" : int(math.sqrt(a) + b), "task" : obj.name}
@app.get("/hello")
async def handler():
    return {
        "hello" : "world",
    }