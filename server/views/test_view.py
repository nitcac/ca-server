from server import api

import json


@api.route('/')
def greet_world(req, resp):
    resp.text = "root!!!"

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