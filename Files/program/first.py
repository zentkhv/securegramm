import sqlite3
from telethon import TelegramClient
import json

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

f = open('last_session.txt')
data_file = f.readlines()[0].split(',')
f.close()

f = open('last_password.txt')
data_pass = str(f.readlines()[0])
if data_pass == ' ':
    data_pass = ''
f.close()

f = open('last_password.txt', 'w')
f.close()

api_id = data_file[0]
api_hash = data_file[1]
name = data_file[2]
password = data_pass

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
