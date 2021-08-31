from typing import Optional
from fastapi import Body
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response, HTMLResponse
import db
import tg
from users import gen_random_name
from users import get_user
from lessons import task_3
from util import apply_cache_headers, static_response


app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def _(response: Response):
    apply_cache_headers(response)

    return static_response("index.html", response_cls=HTMLResponse)


@app.get("/img", response_class=Response)
async def _(response: Response):
    apply_cache_headers(response)

    return static_response("image.gif")


@app.get("/js", response_class=Response)
async def _(response: Response):
    apply_cache_headers(response)

    return static_response("index.js")


@app.post("/task/3")
async def _(name: Optional[str] = Body(default=None)):
    result = task_3(name)
    return {"data": {"greeting": result}}


@app.post("/task/4")
async def _(request: Request, response: Response, data: str = Body(...)):
    user = get_user(request) or gen_random_name()
    response.set_cookie("user", user)

    if data == "stop":
        number = await db.get_number(user)
    else:
        number = await db.add_number(user, int(data))

    return {"data": {"n": number}}

@app.get("/abc/", response_class = Response)
async def handler():
    html = "<p>A </p>  <p> B </p> <p> C </p>"
    return Response(content=html, media_type="text/html")


@app.get ("/tg/about")
def _():
    r = tg.getMe()
    return r

