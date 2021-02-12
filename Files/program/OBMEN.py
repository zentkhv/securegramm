from telethon import sync, events
import time
from telethon import TelegramClient

import sqlite3

db = sqlite3.connect('Account.db', timeout=30)
cur = db.cursor() 


cur.execute(f"SELECT API_ID FROM Account WHERE ID = '{1}'")

api_id = str(cur.fetchone()[0])
time.sleep(1)
cur.execute(f"SELECT API_HASH FROM Account WHERE ID = '{1}'")

api_hash = str(cur.fetchone()[0])
time.sleep(1)

session = "anon31"
client = TelegramClient(session, api_id, api_hash)
client.start()

myself = client.get_me()
k = str(myself.id)
cur.execute(f'UPDATE Account SET MY_ID = ? WHERE ID = ?', (k, 1))
db.commit()
time.sleep(1)

cur.execute(f"SELECT NAME FROM Account WHERE ID = '{1}'")
name = str(cur.fetchone()[0])
print(name)
time.sleep(1)

#entity = client.get_dialogs()
entity = client.get_entity(name)

id_Friend = entity.id
m = str(id_Friend)
print(m)
time.sleep(1)
cur.execute(f'UPDATE Account SET ID_SOB = ? WHERE ID = ?', (m, 1))
db.commit()
time.sleep(1)


