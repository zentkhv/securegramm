import asyncio
from telethon import events
from telethon import TelegramClient
import time
import sqlite3
from tkinter import *
import threading
import json
import os
from datetime import datetime
import sys
import pyperclip
import main_GOST
import lorem

db = sqlite3.connect('Account.db', timeout=30)
cur = db.cursor()

cur.execute(f"SELECT NAME FROM Account WHERE ID = '{1}'")
friend = str(cur.fetchone()[0])
time.sleep(0.1)

window = Tk()
window.resizable(False, False)
window.grab_set()
window.focus_set()
window.title(f'Securegram. Диалог с {friend}')

messages = Text(window, bg="#d7d8e0")

f = open('self_name.txt')
self_name = str(f.readlines()[0])
f.close()

input_user = StringVar()
input_field = Entry(window, text=input_user)

cur.execute(f"SELECT API_ID FROM Account WHERE ID = '{1}'")
api_id = str(cur.fetchone()[0])
time.sleep(0.1)

cur.execute(f"SELECT API_HASH FROM Account WHERE ID = '{1}'")
api_hash = str(cur.fetchone()[0])
time.sleep(0.1)

session = "anon31"

client = TelegramClient("anon31", api_id, api_hash).start()
client.start()
time.sleep(0.1)
cur.execute(f"SELECT ID_SOB FROM Account WHERE ID = '{1}'")
id_sob = str(cur.fetchone()[0])
zorro = int(id_sob)
time.sleep(0.1)


def enter_pressed(event):
    input_get = input_field.get()
    print("------------------------------------------")
    print("Этап 0. Получено сообщение: " + input_get)
    # Шифрование ГОСТ
    hide = main_GOST.encrypt(input_get)
    print("Этап 1. Применен шифр ГОСТ: " + hide)

    # Начало формирование сообщения stegcloak
    sms = lorem.sentence()
    print("Этап 2. Сгенерирована фраза: " + sms)

    with open("1.json") as f:
        data4 = f.read()
    d = json.loads(data4)
    d["cover"] = sms
    d["secret"] = hide
    with open("1.json", 'w') as f:
        f.write(json.dumps(d))

    os.system("stegcloak hide --config 1.json")
    print("Этап 3. Применено шифрование AES256, сообщение сокрыто: " + pyperclip.paste())

    # print("Отправка шифровки")
    cur.execute(f"SELECT NAME FROM Account WHERE ID = '{1}'")
    name = str(cur.fetchone()[0])

    async def main():
        await client.send_message(name, pyperclip.paste())

    client.loop.run_until_complete(main())

    # Формирование строки вывода в окно и непосредственно вывод
    messages.insert(INSERT, f'\n{datetime.now().strftime("%d.%m.%y %H:%M")} {self_name}: {input_get}')
    # messages.insert(INSERT, f"\n{input_get}")
    input_user.set('')
    return "break"


frame = Frame(window)

frame.pack()
messages.pack()
input_field.pack(side=BOTTOM, fill=X)
input_field.bind("<Return>", enter_pressed)


def run_bot_events():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(async_run_events(loop))


async def async_run_events(loop):
    eventing_client = await TelegramClient("anon32", api_id, api_hash, loop=loop).start()

    @eventing_client.on(events.newmessage.NewMessage(from_users=zorro))
    async def handler(event):
        hhh = event.message.message
        print("------------------------------------------")
        print("Этап 0. Получено сообщение: " + hhh)

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
                print("Этап 1: Раскрыт следующий шифр-текст: " + data2)

        # Расшифровка ГОСТ
        end_data = main_GOST.decrypt(data2)
        print("Этап 2. Расшифрованное сообщение: " + end_data)

        # Формирование строки вывода  в окно и непосредственно вывод
        messages.insert(INSERT, f'\n{datetime.now().strftime("%d.%m.%y %H:%M")} {friend}: {end_data}')
        # messages.insert(INSERT, f"\n{end_data}")

    await eventing_client.run_until_disconnected()


threading.Thread(target=run_bot_events).start()
window.mainloop()