db = {}

def get_user(user_id):
    return db.get(user_id, {})

def save_user(user_id, data):
    db[user_id] = data