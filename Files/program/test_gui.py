import tkinter as tk
from tkinter import messagebox
import re  # Используется!
import subprocess
import sys  # Используется!
import time
from tkinter import *
import sqlite3
import json
from telethon import sync, events  # Используется!
import asyncio
# from telethon import events
from telethon import TelegramClient
import threading
import os
from lorem_text import lorem
from datetime import datetime


# Класс для создания окна "Об авторе"
class About(tk.Toplevel):
    # Конструктор
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title("Об авторе")
        # self.geometry("300x300+400+150")
        self.geometry("+400+150")
        self.iconbitmap('image/main_icon.ico')
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()

        frame_about = tk.Frame(self, bg=master_color_1)
        frame_about.pack()
        text_value = "Автор программы: Ильченко Михаил Александрович"
        label_about = tk.Label(frame_about, bg=master_color_1, fg=master_color_4, font='Calibri 13', text=text_value)
        label_about.pack()
        text_value1 = "Группа: СО251КОБ\n\nВконтакте: https://vk.com/mikhail27rus\nЯзык программирования: Python"
        label_about1 = tk.Label(frame_about, bg=master_color_1, fg=master_color_4, font='Calibri 13', text=text_value1)
        label_about1.pack()


# Класс для создания окна "Справка"
class Info(tk.Toplevel):
    # Конструктор
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title("О программе")
        # self.geometry("300x300+400+150")
        self.geometry("+400+150")
        self.iconbitmap('image/main_icon.ico')
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()

        frame_about = tk.Frame(self, bg=master_color_1)
        frame_about.pack()
        text_value = "Добро пожаловать в Securegram!\n\nЭта программа предназначена для безопасного обмена сообщениями."
        label_about = tk.Label(frame_about, bg=master_color_1, fg=master_color_4, font='Calibri 13', text=text_value)
        label_about.pack()


# Класс для создания окна "Сменить ник"
class Nickname(tk.Toplevel):
    # Конструктор
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title("Смена ника")
        # self.geometry("300x300+400+150")
        self.geometry("+400+150")
        self.iconbitmap('image/main_icon.ico')
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()

        f = open('self_name.txt')
        data = f.readlines()[0].split(',')
        for i in range(0, len(data)):
            data[i] = re.sub("^\s+|\n|\r|\s+$", "", str(data[i]))

        frame_about = tk.Frame(self, bg=master_color_1)
        frame_about.pack()

        label_about = tk.Label(frame_about, bg=master_color_1, fg=master_color_4, font='Calibri 13',
                               text="Текущее имя пользователя:")
        entry_about2 = tk.Entry(frame_about, disabledbackground=master_color_3, font=10, fg=master_color_2)
        entry_about2.insert(0, data[0])
        entry_about2.config(state=tk.DISABLED)
        label_about3 = tk.Label(frame_about, bg=master_color_1, fg=master_color_4, font='Calibri 13',
                                text='Новое имя пользователя:')

        self.entry_nickname = tk.Entry(frame_about, bg=master_color_3, fg=master_color_2, font=10)
        button_nickname = tk.Button(frame_about, text="Сохранить", relief='groove', font='Calibri 13',
                                    command=self.button_save)

        label_about.grid(row=0, column=0, sticky="E", padx=5)
        entry_about2.grid(row=0, column=1, sticky="W", padx=5)
        label_about3.grid(row=1, column=0, sticky="E", padx=5)
        self.entry_nickname.grid(row=1, column=1, sticky="W", padx=5)
        button_nickname.grid(row=2, column=0, columnspan=2, pady=5)

        self.entry_nickname.insert(0, "@")

    def button_save(self):
        if self.entry_nickname.get() != '@' and self.entry_nickname.get() != '':
            file = open('self_name.txt', 'w')
            file.writelines(self.entry_nickname.get())
            file.close()
            self.destroy()
            messagebox.showinfo('Успех', 'Ваше имя пользователя успешно изменено!')
        else:
            self.destroy()
            # self.quit()
            messagebox.showwarning('Внимание', 'Изменение не удалось.\n Ваше имя пользователя не изменилось.')


# Мастер-цвета
master_color_1 = '#f0f0f0'
# Текст в entry
master_color_2 = 'black'
# Задний фон кнопок и entry
master_color_3 = '#abcdff'
# Текст кнопок и лейблов
master_color_4 = 'black'
# Линия разделения
master_color_5 = 'White'

# Главное окно
root = tk.Tk()
root.title("Securegram")
root.geometry("+300+100")
root.iconbitmap('image/main_icon.ico')
# root.wm_attributes('-alpha', 0.94)
root.resizable(False, False)

# Кнопочный фрэйм
frame_toolbar = tk.Frame(bg=master_color_1)
frame_toolbar.pack(side=tk.TOP, fill=tk.X)


# Методы открытия дочерних окон
def open_about():
    About()


def open_info():
    Info()


def open_nickname():
    Nickname()


# Метод заполнения entry при загрузке приложения
def fill_entry():
    f = open('last_session.txt')
    data = f.readlines()[0].split(',')
    for i in range(0, len(data)):
        data[i] = re.sub("^\s+|\n|\r|\s+$", "", str(data[i]))
    if len(data) == 3:
        entry_id.insert(0, data[0])
        entry_hash.insert(0, data[1])
        entry_friend.insert(0, data[2])
    else:
        messagebox.showwarning("Внимание", "Не удалось загрузить данные о прошлой сессии.\nФайл будет перезаписан "
                                           "после установления следующего соединения.")
    f.close()


def third_def():
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

        # Формирование строки вывода в окно и непосредственно вывод
        messages.insert(INSERT, '%s\n' % f'{datetime.now().strftime("%d.%m.%y %H:%M")} {self_name}: {input_get}')

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

            # Формирование строки вывода  в окно и непосредственно вывод
            messages.insert(INSERT, '%s\n' % f'{datetime.now().strftime("%d.%m.%y %H:%M")} {friend}: {data2}')

        # messages.insert(INSERT, '%s\n' % data2)

        await eventing_client.run_until_disconnected()

    threading.Thread(target=run_bot_events).start()
    window.mainloop()
    messagebox.showwarning('third', 'end')


# Метод сохранения данных по нажатию кнопки соединения
def save_session_data():
    file = open('last_session.txt', 'w')
    file.writelines(f'{entry_id.get()},{entry_hash.get()},{entry_friend.get()}')
    file.close()


# Метод передачи пароля в файл (для использования в first)
def transfer_password():
    file = open('last_password.txt', 'w')
    if entry_password.get() != '':
        file.writelines(f'{entry_password.get()}')
    else:
        file.writelines(' ')
    file.close()


# Метод для выколнения по нажатию кнопки соединения
def start_connect():
    if entry_id.get() == '' or entry_hash.get() == '' or entry_friend.get() == '':
        messagebox.showerror("Ошибка ввода данных", "Недостаточно данных!\nСоединение не удалось...")
    else:
        save_session_data()
        transfer_password()

        process = subprocess.Popen([sys.executable, "first.py"])
        process.wait()
        time.sleep(0.1)

        process2 = subprocess.Popen([sys.executable, "second.py"])
        process2.wait()
        time.sleep(0.1)

        third_def()


# Мастер-кнопка
def setup_button():
    return tk.Button(frame_toolbar, bg=master_color_1, bd=0, fg=master_color_4, compound=tk.TOP, font='Tahoma')


add_img_connect = tk.PhotoImage(file='image/connect.png')
add_img_info = tk.PhotoImage(file='image/info.png')
add_img_rename = tk.PhotoImage(file='image/rename.png')
add_img_about = tk.PhotoImage(file='image/about.png')

# Кнопка "Соединить"
button_connect = setup_button()
button_connect.config(text="Начать", image=add_img_connect, command=start_connect)
button_connect.pack(side=tk.LEFT)

# Кнопка "Смена ника"
button_rename = setup_button()
button_rename.config(text="Смена ника", image=add_img_rename, command=open_nickname)
button_rename.pack(side=tk.LEFT)

# Кнопка "О программе"
button_info = setup_button()
button_info.config(text="О программе", image=add_img_info, command=open_info)
button_info.pack(side=tk.LEFT)

# Кнопка "Об авторе"
button_about = setup_button()
button_about.config(text="Об авторе", image=add_img_about, command=open_about)
button_about.pack(side=tk.LEFT)

# Разделяющий фрэйм
frame_separation = tk.Frame(bg=master_color_5)
frame_separation.pack(side=tk.TOP, fill=tk.X, ipady=5)

# Промежуточный фрэйм для подписи над полями
frame_middle = tk.Frame(bg=master_color_1)
frame_middle.pack(side=tk.TOP, fill=tk.X)
tk.Label(frame_middle, text='Данные для подключения', font='Calibri 20', bg=master_color_1, fg=master_color_4).pack()

# Фрэйм для полей ввода и лейблов
frame_entry = tk.Frame(bg=master_color_1)
frame_entry.pack(side=tk.TOP, fill=tk.X)


# Элементы заполнения данных
# Мастер-label
def setup_label():
    return tk.Label(frame_entry, bg=master_color_1, fg=master_color_4, font='Calibri 13')


# Мастер-entry
def setup_entry():
    return tk.Entry(frame_entry, width=40, bg=master_color_3, fg=master_color_2, font=10)


# Объекты API ID
label_id = setup_label()
label_id.config(text='API ID')
entry_id = setup_entry()

# Объекты API Hash
label_hash = setup_label()
label_hash.config(text='API Hash')
entry_hash = setup_entry()

# Объекты собеседника
label_friend = setup_label()
label_friend.config(text='Ник собеседника')
entry_friend = setup_entry()

# Объекты пароля
label_password = setup_label()
label_password.config(text='Общий пароль')

entry_password = setup_entry()
entry_password.config(show='*')

# Расположение entry и label
label_id.grid(row=0, column=0, sticky="W,E")
label_hash.grid(row=1, column=0, sticky="W,E")
label_friend.grid(row=2, column=0, sticky="W,E", padx=10)
label_password.grid(row=3, column=0, sticky="W,E")

entry_id.grid(row=0, column=1, pady=5)
entry_hash.grid(row=1, column=1, pady=5)
entry_friend.grid(row=2, column=1, pady=5)
entry_password.grid(row=3, column=1, pady=5)

fill_entry()

root.mainloop()
