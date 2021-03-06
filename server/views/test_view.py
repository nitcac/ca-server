from server import api

import json
import base64


@api.route('/')
def greet_world(req, resp):
    resp.text = "root!!"


@api.route('/ws', websocket=True)
async def websocket(ws):
    await ws.accept()
    while True:
        text = await ws.receive_text()
        if text[0] == "{" and text[-1] == "}":
            data = json.loads(text)
            for key in data.keys():
                await ws.send_text(data[key])
    await ws.close()


@api.route('/hoge')
class HogeView:
    hoge = "fuga"
    async def on_request(self, req, resp):
        print(req.headers)
        print(resp.headers)
        resp.text = "hoge"
