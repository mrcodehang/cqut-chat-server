# from sanic import Sanic
# from sanic.response import json
#
# app = Sanic(__name__)
#
# @app.route("/")
# async def test(request):
#     return json({ "hello": "world" })
#
# app.run(host="127.0.0.1", port=8888)

async def printAsync(text):
    if text:
        print(text)
    else:
        print("no")


printAsync("hello world")
print("true")