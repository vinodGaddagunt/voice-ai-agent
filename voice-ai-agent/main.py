from fastapi import FastAPI, WebSocket
from agent.agent import process_input
import json

app = FastAPI()

@app.websocket("/ws")
async def ws_endpoint(ws: WebSocket):
    await ws.accept()
    session_id = "user1"

    while True:
        data = await ws.receive_text()
        response = process_input(session_id, data)
        await ws.send_text(json.dumps(response))


@app.get("/")
def home():
    return {"status": "API working"}

@app.get("/test")
def test():
    return {"status": "success"}