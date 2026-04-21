import redis
import json

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

def get_session(session_id):
    data = r.get(session_id)
    return json.loads(data) if data else {}

def update_session(session_id, data):
    r.setex(session_id, 3600, json.dumps(data))