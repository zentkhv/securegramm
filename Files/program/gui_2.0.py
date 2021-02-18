import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess
import sys
import time
import sqlite3
from telethon import TelegramClient
import json
import asyncio
from telethon import events
from tkinter import *
import threading
import os
from lorem_text import lorem
from datetime import datetime


# Класс основного окна
class Main(tk.Frame):
    # Конструктор
    def __init__(self, root):
        super().__init__(root)
        self.add_img = tk.PhotoImage(file='connection2.png')
        self.init_main()

    # Создание элементов окна
    def init_main(self):
        # Главное окно программы: создание и упакова
        frame_toolbar = tk.Frame(bg="#d7d8e0")
        frame_toolbar.pack(side=tk.TOP, fill=tk.X)

        # Кнопка "Соединить"
        button_open_dialog = tk.Button(frame_toolbar, text="Соединить", command=self.stage_0, bg='#d7d8e0', bd=0,
                                       compound=tk.TOP, image=self.add_img)
        button_open_dialog.pack(side=tk.RIGHT)

        canvas = tk.Canvas(self)
        canvas.pack(fill=tk.X)

        # Подписи к полям ввода: создание и упаковка
        label_id = tk.Label(frame_toolbar, text='API ID', bg="#d7d8e0")
        label_id.place(x=20, y=10)

        label_hash = tk.Label(frame_toolbar, text='API Hash', bg="#d7d8e0")
        label_hash.place(x=20, y=40)

        label_friend = tk.Label(frame_toolbar, text='Ник собеседника', bg="#d7d8e0")
        label_friend.place(x=20, y=70)

        label_password = tk.Label(frame_toolbar, text='Общий пароль', bg="#d7d8e0")
        label_password.place(x=20, y=100)

        # Поля ввода: создание и упаковка
        self.entry_id = ttk.Entry(frame_toolbar, width=40)
        self.entry_id.place(x=140, y=10)

        self.entry_hash = ttk.Entry(frame_toolbar, width=40)
        self.entry_hash.place(x=140, y=40)

        self.entry_friend = ttk.Entry(frame_toolbar, width=40)
        self.entry_friend.place(x=140, y=70)

        self.entry_password = ttk.Entry(frame_toolbar, width=40, show='*')
        self.entry_password.place(x=140, y=100)

    # Метод 0-ой фазы: открытие дочернего окна и сохранения данных о сессии в файл, переход на 1-ую фазу
    def stage_0(self):
        self.save_session_data()
        Child()
        self.stage_1()

    # Метод заполнения полей значениями из файла
    def fill_entry(self):
        f = open('last_session.txt')
        fd = f.readlines()
        self.entry_id.insert(0, fd[0][0:len(fd[0]) - 1])
        self.entry_hash.insert(0, fd[1][0:len(fd[1]) - 1])
        self.entry_friend.insert(0, fd[2][0:len(fd[2]) - 1])
        self.entry_password.insert(0, fd[3][0:len(fd[3]) - 1])
        f.close()

    # Метод записи данных о сессии в файл
    def save_session_data(self):
        file = open('last_session.txt', 'w')
        file.writelines(self.entry_id.get() + '\n')
        file.writelines(self.entry_hash.get() + '\n')
        file.writelines(self.entry_friend.get() + '\n')
        file.writelines(self.entry_password.get() + '\n')
        file.close()

    # Метод фазы №1: создание БД, подключение к API 2 раза (одна сессия слушает, вторая говорит)
    def stage_1(self):
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

        api_id = self.entry_id.get()
        api_hash = self.entry_hash.get()
        name = self.entry_friend.get()
        password = self.entry_password.get()

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
            self.stage_2()


    # Метод фазы №2: обмен открытыми ключами
    def stage_2(self):
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

        entity = client.get_entity(name)

        id_Friend = entity.id
        m = str(id_Friend)
        print(m)
        time.sleep(1)
        cur.execute(f'UPDATE Account SET ID_SOB = ? WHERE ID = ?', (m, 1))
        db.commit()
        time.sleep(1)

# Класс дочернего окна, вызываемого основным
class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title('Диалог с ...')
        self.geometry('400x220+400+300')
        self.resizable(False, False)
        # self.iconbitmap('telegram.ico')

        self.grab_set()
        self.focus_set()


# Условие проверяющее, вызывается ли скрипт как основной
if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Securegram. Настройка соединения")
    root.geometry("550x140+300+200")
    # root.iconbitmap('telegram.ico')
    root.resizable(False, False)

    app.fill_entry()

    root.mainloop()
