import os

from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi import Body
from collections  import defaultdict
import math

from starlette.responses import Response

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

numbers = defaultdict(list)
def gen_random_name():
    return os.urandom(16),hex()

def get_user(request: Request):
    return request.cookies.get("user")

@app.post("/task/4")
def handler(request: Request, response: Response, data: str = Body(...)):

    user = get_user(request) or gen_random_name()
    response.set_cookie("user",user)

    if data == "stop":
        return sum(numbers[user])
    else:
        assert data.isdigit()
        numbers[user].append(int(data))
        return numbers
