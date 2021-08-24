import httpx
import pytest
from fast import app



@pytest.mark.asyncio
async def test():
    url = "/task/4"

    async with httpx.AsyncClient(app=app, base_url="http://fast") as client:
        resp: httpx.Response = await client.post(url, json=1)
        assert resp.status_code == 200
        assert resp.json() == "1"

        resp = await client.post(url, json=1)
        assert resp.status_code == 200
        assert resp.json() == "1"

        resp = await client.post(url, json="stop")
        assert resp.status_code == 200
        assert resp.json() == 2
