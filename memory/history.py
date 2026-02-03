from sqlite_utils import Database

db = Database("data/history.db")

if "commands" not in db.table_names():
    db["commands"].create({
        "command": str,
        "intent": str,
        "confidence": float
    })

def save_command(command, intent, confidence):
    db["commands"].insert({
        "command": command,
        "intent": intent,
        "confidence": confidence
    })
