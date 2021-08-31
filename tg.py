import os

import httpx

token = os.getenv("TG_BOT_TOKEN")
assert token, "no tg token provided"


def api_call(method_name: str):
    url = f"https://api.telegram.org/bot{token}/{method_name}"

    r = httpx.post(url)
    return r.json()


def getMe():
    r = api_call("getMe")
    return r


print(getMe())
