
 
import asyncio
from telethon import events
from telethon import TelegramClient
import time
import sqlite3
from tkinter import *
import threading
import random
import json
import os
from lorem_text import lorem


db = sqlite3.connect('Account.db', timeout=30)
cur = db.cursor() 
 
window = Tk()
 
messages = Text(window)
 
 
input_user = StringVar()
input_field = Entry(window, text=input_user)
 
 
cur.execute(f"SELECT API_ID FROM Account WHERE ID = '{1}'")

api_id = str(cur.fetchone()[0])
time.sleep(1)
cur.execute(f"SELECT API_HASH FROM Account WHERE ID = '{1}'")

api_hash = str(cur.fetchone()[0])
time.sleep(1)
session = "anon31"
 
client = TelegramClient("anon31", api_id, api_hash).start()
client.start()
time.sleep(1)
cur.execute(f"SELECT ID_SOB FROM Account WHERE ID = '{1}'")
id_sob = str(cur.fetchone()[0])
zorro = int(id_sob)
time.sleep(1)

def Enter_pressed(event):
	input_get = input_field.get()
	print(input_get)
	
	print("Зашифровка")
	
	sms = lorem.sentence()
	
	with open("1.json") as f:
		data4 = f.read()
	d = json.loads(data4)
	d["cover"] = sms
	d["secret"] = input_get
	with open("1.json", 'w') as f:
		f.write(json.dumps(d))

	os.system("stegcloak hide --config 1.json") 

	print("Отправка шифровки")
	
	cur.execute(f"SELECT NAME FROM Account WHERE ID = '{1}'")
	name = str(cur.fetchone()[0])
	
	async def main():
		with open("out.txt", "r") as f1:
			data5 = f1.read()
			xxx = str(data5)
		await client.send_message(name, xxx)

	client.loop.run_until_complete(main())
	
	
	messages.insert(INSERT, '%s\n' % input_get)

	input_user.set('')

	return "break"
 
 
frame = Frame(window)
 
frame.pack()
messages.pack()
input_field.pack(side=BOTTOM, fill=X)
input_field.bind("<Return>", Enter_pressed)


def run_bot_events():
	loop = asyncio.new_event_loop()
	asyncio.set_event_loop(loop)
	loop.run_until_complete(async_run_events(loop))
	

			

	
async def async_run_events(loop):
	eventing_client = await TelegramClient("anon32", api_id, api_hash, loop=loop).start()
	

	@eventing_client.on(events.newmessage.NewMessage(from_users=zorro))
	async def handler(event):
		
		
		hhh = event.message.message
		if hhh is not None:
			with open("2.json") as f:
				data3 = f.read()
			d = json.loads(data3)
			d["message"] = str(hhh)
			with open("2.json", 'w') as f:
				f.write(json.dumps(d))
			os.system("stegcloak reveal --config 2.json")
				
			with open("out2.txt", "r") as f1:
				data2 = f1.read()
			print(data2)
			
		messages.insert(INSERT, '%s\n' % data2)
	await eventing_client.run_until_disconnected()

threading.Thread(target=run_bot_events).start()
window.mainloop()
