async def app(scope, receive, send):
  assert scope["type"] == "http"
  print(type(scope["headers"]))
  for k, v in scope['headers']:
    print(f"{k.title()} : {v}")
  await send({
    "type": "http.response.start",
    "status": 200,
    "headers": [
      [b"content-type", b"text/plain"],
    ]
  })

  await send({
    "type": "http.response.body",
    "body": b"Hello world! What the f**k is going on?!" ,
  })



