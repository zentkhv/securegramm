import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import time
import about
import re
from tkinter import *

import sqlite3
from telethon import TelegramClient
from telethon import sync, events
import json
import asyncio
import threading
import json
import os
import lorem
from datetime import datetime
import pyperclip
import main

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


# Класс главного меню
class Main(tk.Frame):

    # Конструктор
    def __init__(self, root):
        super().__init__(root)
        self.state = False
        self.add_img_connect = tk.PhotoImage(file='image/connect.png')
        self.add_img_info = tk.PhotoImage(file='image/info.png')
        self.add_img_rename = tk.PhotoImage(file='image/rename.png')
        self.add_img_about = tk.PhotoImage(file='image/about.png')

        self.add_img_light_red = tk.PhotoImage(file='image/light_red.png')
        self.add_img_light_yellow = tk.PhotoImage(file='image/light_yellow.png')
        self.add_img_light_green = tk.PhotoImage(file='image/light_green.png')
        self.init_main()

    # Создание элементов окна
    def init_main(self):
        # Главное окно программы
        # Кнопочный фрэйм
        frame_toolbar = tk.Frame(bg=master_color_1)
        frame_toolbar.pack(side=tk.TOP, fill=tk.X)

        # Мастер-кнопка
        def setup_button():
            return tk.Button(frame_toolbar, bg=master_color_1, bd=0, fg=master_color_4, compound=tk.TOP, font='Tahoma')

        # Кнопка "Смена ника"
        button_rename = setup_button()
        button_rename.config(text="Смена имени", image=self.add_img_rename, command=self.open_nickname)
        # button_rename.pack(side=tk.LEFT)
        button_rename.grid(row=0, column=0, padx=20)

        # Кнопка "О программе"
        button_info = setup_button()
        button_info.config(text="О программе", image=self.add_img_info, command=self.open_info)
        # button_info.pack(side=tk.LEFT)
        button_info.grid(row=0, column=1, padx=20)

        # Кнопка "Об авторе"
        button_about = setup_button()
        button_about.config(text="Об авторе", image=self.add_img_about, command=self.open_about)
        # button_about.pack(side=tk.LEFT)
        button_about.grid(row=0, column=2, padx=20)

        # Разделяющий фрэйм
        frame_separation = tk.Frame(bg=master_color_5)
        frame_separation.pack(side=tk.TOP, fill=tk.X, ipady=5)

        # Промежуточный фрэйм для подписи над полями
        frame_middle = tk.Frame(bg=master_color_1)
        frame_middle.pack(side=tk.TOP, fill=tk.X)
        tk.Label(frame_middle, text='Данные для подключения', font='Calibri 16', bg=master_color_1,
                 fg=master_color_4).pack()

        # Фрэйм для полей ввода и лейблов
        frame_entry = tk.Frame(bg=master_color_1)
        frame_entry.pack(side=tk.TOP, fill=tk.X)

        # Элементы заполнения данных
        # Мастер-label
        def setup_label():
            return tk.Label(frame_entry, bg=master_color_1, fg=master_color_4, font='Calibri 13')

        # Мастер-entry
        def setup_entry():
            return tk.Entry(frame_entry, width=37, bg=master_color_3, fg=master_color_2, font=10)

        # Объекты API ID
        label_id = setup_label()
        label_id.config(text='API ID')
        self.entry_id = setup_entry()

        # Объекты API Hash
        label_hash = setup_label()
        label_hash.config(text='API Hash')
        self.entry_hash = setup_entry()

        # Объекты собеседника
        label_friend = setup_label()
        label_friend.config(text='Ник собеседника')
        self.entry_friend = setup_entry()

        # Объекты пароля
        label_password = setup_label()
        label_password.config(text='Пароль AES')

        self.entry_password = setup_entry()
        self.entry_password.config(show='*')

        # Объекты пароля ГОСТ
        label_password_gost = setup_label()
        label_password_gost.config(text='Пароль ГОСТ')

        self.entry_password_gost = setup_entry()
        self.entry_password_gost.config(show='*')

        # Кнопка Подключиться
        self.button_connect = tk.Button(frame_entry, text="Подключиться", relief='groove', font='Tahoma',
                                        command=self.start_connect)

        # Расположение entry и label
        label_id.grid(row=0, column=0, sticky="W,E")
        label_hash.grid(row=1, column=0, sticky="W,E")
        label_friend.grid(row=2, column=0, sticky="W,E", padx=10)
        label_password.grid(row=3, column=0, sticky="W,E")
        label_password_gost.grid(row=4, column=0, sticky="W,E")

        self.entry_id.grid(row=0, column=1, pady=5)
        self.entry_hash.grid(row=1, column=1, pady=5)
        self.entry_friend.grid(row=2, column=1, pady=5)
        self.entry_password.grid(row=3, column=1, pady=5)
        self.entry_password_gost.grid(row=4, column=1, pady=5)

        self.button_connect.grid(row=5, column=0, columnspan=2)

        # Разделяющий фрэйм
        frame_separation1 = tk.Frame(bg=master_color_5)
        frame_separation1.pack(side=tk.TOP, fill=tk.X, ipady=5)

        # Промежуточный фрэйм для подписи над полями
        frame_connect = tk.Frame(bg=master_color_1)
        frame_connect.pack(side=tk.TOP, fill=tk.X)
        self.label_connection = tk.Label(frame_connect, text='Соединение не установлено', font='Calibri 16',
                                         bg=master_color_1, fg=master_color_4)
        self.label_connection.pack()

        # Фрэйм для полей ввода и лейблов
        self.frame_end = tk.Frame(bg=master_color_1)
        self.frame_end.pack(side=tk.TOP, fill=tk.X)
        self.label_stage = tk.Label(self.frame_end, bg=master_color_1, fg=master_color_4, font='Calibri 13',
                                    image=self.add_img_light_red)
        self.label_stage.pack()

        self.button_close = tk.Button(self.frame_end, text="Закрыть соединение", relief='groove', font='Tahoma',
                                      state=tk.DISABLED)
        self.button_close.pack()

    # Метод заполнения полей значениями из файла и проверки
    def fill_entry(self):
        f = open('last_session.txt')
        data = f.readlines()[0].split(',')
        for i in range(0, len(data)):
            data[i] = re.sub("^\s+|\n|\r|\s+$", "", str(data[i]))
        if len(data) == 3:
            self.entry_id.insert(0, data[0])
            self.entry_hash.insert(0, data[1])
            self.entry_friend.insert(0, data[2])
        else:
            messagebox.showwarning("Внимание", "Не удалось загрузить данные о прошлой сессии.\nФайл будет перезаписан "
                                               "после установления следующего соединения.")
        f.close()

    def open_about(self):
        About()

    def open_info(self):
        Info()

    def open_nickname(self):
        Nickname()

    def save_session_data(self):
        file = open('last_session.txt', 'w')
        file.writelines(f'{self.entry_id.get()},{self.entry_hash.get()},{self.entry_friend.get()}')
        file.close()

    def transfer_password(self):
        # Запись общего пароля
        file = open('last_password.txt', 'w')
        if self.entry_password.get() != '':
            file.writelines(f'{self.entry_password.get()}')
        else:
            file.writelines(' ')
        file.close()

        # Запись пароля ГОСТ
        file1 = open('last_password_gost.txt', 'w')
        if self.entry_password_gost.get() != '':
            file1.writelines(f'{self.entry_password_gost.get()}')
        else:
            file1.writelines(' ')
        file1.close()

    def do_process(self):
        process = subprocess.Popen([sys.executable, "first.py"])
        # process.wait()
        time.sleep(0.1)

        process2 = subprocess.Popen([sys.executable, "second.py"])
        # process2.wait()
        time.sleep(0.7)

        self.label_stage.config(image=self.add_img_light_green)
        self.label_connection.config(text='Соединение активно')

        process3 = subprocess.Popen([sys.executable, "third.py"])
        # process3.wait()
        # time.sleep(0.1)

        def kill():
            process3.kill()
            self.label_stage.config(image=self.add_img_light_red)
            self.label_connection.config(text='Соединение отсутствует')
            self.button_close.config(state=tk.DISABLED)

            self.entry_id.config(state=tk.NORMAL)
            self.entry_hash.config(state=tk.NORMAL)
            self.entry_friend.config(state=tk.NORMAL)
            self.entry_password.config(state=tk.NORMAL)
            self.entry_password_gost.config(state=tk.NORMAL)

            self.button_connect.config(state=tk.NORMAL)

        self.button_close.config(state=tk.NORMAL, command=kill)

    def stop_use(self):
        self.entry_id.config(state=tk.DISABLED)
        self.entry_hash.config(state=tk.DISABLED)
        self.entry_friend.config(state=tk.DISABLED)
        self.entry_password.config(state=tk.DISABLED)
        self.entry_password_gost.config(state=tk.DISABLED)

        self.button_connect.config(state=tk.DISABLED)

        self.label_stage.config(image=self.add_img_light_yellow)
        self.label_connection.config(text='Пожалуйста, подождите. Идет соединение...')

    def start_connect(self):
        if self.entry_id.get() == '' or self.entry_hash.get() == '' or self.entry_friend.get() == '':
            messagebox.showerror("Ошибка ввода данных", "Недостаточно данных!\nСоединение не удалось...")
        elif self.entry_password.get() == '' or self.entry_password_gost.get() == '':
            messagebox.showerror("Ошибка ввода данных", "Необходимо указать секретные пароли!\nЭто необходимо для "
                                                        "конфиденциальности переписки.")
        else:
            self.save_session_data()
            self.transfer_password()
            self.stop_use()
            self.do_process()
            messagebox.showwarning('Внимание', "Соединение установлено! \n Пожалуйста, подождите. Сейчас откроется "
                                               "диалоговое окно.")


# Класс для создания окна "Об авторе"
class About(tk.Toplevel):
    # Конструктор
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title("Об авторе")
        # self.geometry("300x300+400+150")
        self.geometry("+400+200")
        self.iconbitmap('image/main_icon.ico')
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()

        frame_about = tk.Frame(self, bg=master_color_1)
        frame_about.pack()
        text_value = about.text_author()
        label_about = tk.Label(frame_about, bg=master_color_1, fg=master_color_4, font='Calibri 13', text=text_value)
        label_about.pack()
        text_value1 = about.text_about()
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
        text_value = about.text_program()
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


def destroy_main(root):
    root.destroy()


# Тело программы
if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Securegram. Безопасное общение")
    root.geometry("+300+40")
    root.iconbitmap('image/main_icon.ico')
    # root.wm_attributes('-alpha', 0.94)
    root.resizable(False, False)

    app.fill_entry()

    root.mainloop()
