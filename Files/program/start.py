import sqlite3
from telethon import TelegramClient
import time
import subprocess
import sys
import json
import gui

db = sqlite3.connect('Account.db', timeout=30)
cur = db.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Account (
    ID INTEGER PRIMARY KEY,
    API_ID TEXT,
    API_HASH TEXT,
    NAME TEXT,
    ID_SOB TEXT,
    MY_ID TEXT
)""")

db.commit()

api_id = gui.start_id
api_hash = gui.start_hash
name = gui.start_friend
password = gui.start_password

id_sob = "1"
my_id = "1"

with open("1.json") as f:
    data = f.read()
d = json.loads(data)
d["password"] = password
with open("1.json", 'w') as f:
    f.write(json.dumps(d))

with open("2.json") as f2:
    data2 = f2.read()
d2 = json.loads(data2)
d2["password"] = password
with open("2.json", 'w') as f2:
    f2.write(json.dumps(d2))

cur.execute(f"SELECT API_ID FROM Account WHERE API_ID = '{api_id}'")
if cur.fetchone() is None:
    cur.execute("""INSERT INTO Account(API_ID, API_HASH, NAME, ID_SOB, MY_ID) VALUES (?,?,?,?,?);""",
                (api_id, api_hash, name, id_sob, my_id))
    db.commit()
    print("Зарегистрированно!")

z = 1

while True:
    session = "anon3" + str(z)
    client = TelegramClient(session, api_id, api_hash)
    client.start()
    print("Аккаунт: " + str(z) + " Вход выполнен успешно!")
    z = z + 1
    if z == 3:
        print("Аккауты активированы!")
        break
