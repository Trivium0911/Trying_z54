from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Body
from fastapi import Query

import math


app = FastAPI()

class Numbers(BaseModel):
    a: int
    b: int

class TaskArgs(BaseModel):
    name: str
    args: Numbers
numbers = []
@app.post("/my/")
async def handler(obj: TaskArgs):
    a = obj.args.a
    b = obj.args.b
    return {"result" : int(math.sqrt(a) + b), "task" : obj.name}
@app.post("/task/4")
async def handler(data: str = Body(...)):
    if data == "stop":
        return sum(numbers)
    else:
        assert data.isdigit()
        numbers.append(int(data))
        return numbers
