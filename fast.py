import math
import os
import traceback
from collections import defaultdict
from contextlib import closing
from typing import Optional, List

import psycopg2
from fastapi import Body
from fastapi import FastAPI, Request, Query
from psycopg2 import sql
from pydantic import BaseModel
from starlette.responses import Response

app = FastAPI()

def execute_sql(sql: str) -> List[tuple]:
    rows = []

    dsn = os.getenv("DATABASE_URL", "").replace("postgresql", "postgres")
    print(f"{dsn = }")
    if not dsn:
        return rows

    with closing(psycopg2.connect(dsn)) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute(sql)
            connection.commit()

            try:
                if cursor.rowcount:
                    rows = cursor.fetchall()
            except psycopg2.ProgrammingError:
                traceback.print_exc()

    return rows


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
    return os.urandom(16).hex()


def get_user(request: Request):
    return request.cookies.get("user")


def get_number(user: str) -> Optional[int]:
    sql = f"""
        SELECT n FROM numbers
        WHERE name = '{user}'
        ;
    """
    r = execute_sql(sql)
    try:
        n = r[0][0]
    except IndexError:
        return None
    return n


def user_exists(user: str) -> bool:
    n = get_number(user)
    return n is not None


def update_number(user: str, number: int) -> None:
    n = get_number(user)
    n += number

    sql = f"""
        UPDATE numbers
        SET
            n = {n}
        WHERE
            name = '{user}'
        ;
    """
    execute_sql(sql)


def insert_new_user(user: str, number: int) -> None:
    sql = f"""
        INSERT INTO numbers(name, n)
        VALUES ('{user}', {number})
        ;
    """
    execute_sql(sql)


def save_number(user: str, number: int) -> None:
    if user_exists(user):
        update_number(user, number)
    else:
        insert_new_user(user, number)


@app.post("/task/4")
def handler(
    request: Request,
    response: Response,
    data: str = Body(...),
):
    user = get_user(request) or gen_random_name()
    response.set_cookie("user", user)

    if data == "stop":
        return get_number(user)
    else:
        save_number(user, int(data))
        return data