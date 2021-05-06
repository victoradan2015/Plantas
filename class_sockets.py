import json
from websocket import create_connection

class Websockets:
    def send_message(self):
        ws = create_connection("ws://invernanderointeligente.herokuapp.com/adonis-ws")
        ws.send(json.dumps({
        "t":1,
        "d":{
        "topic":"chat",
        "event":"message",
        "data":"putoss"
        }
        }))
        result = ws.recv()
        result = json.loads(result)
        ws.send(json.dumps({
        "t":7,
        "d":{
        "topic":"chat",
        "event":"message",
        "data":"14"
        }
        }))

        ws.send(json.dumps({
        "t":7,
        "d":{
        "topic":"chat",
        "event":"message",
        "data":"EDUARDO Y LUIS NOBIOS"
        }
        }))
        print("Received '%s'")
