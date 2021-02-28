import tkinter as tk
from tkinter import messagebox
import re
import subprocess
import sys  # Используется!
import time
from tkinter import *

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
        self.add_img_connect = tk.PhotoImage(file='image/connect.png')
        self.add_img_info = tk.PhotoImage(file='image/info.png')
        self.add_img_rename = tk.PhotoImage(file='image/rename.png')
        self.add_img_about = tk.PhotoImage(file='image/about.png')
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

        # Кнопка "Соединить"
        button_connect = setup_button()
        button_connect.config(text="Начать", image=self.add_img_connect, command=self.start_connect)
        button_connect.pack(side=tk.LEFT)

        # Кнопка "Смена ника"
        button_rename = setup_button()
        button_rename.config(text="Смена ника", image=self.add_img_rename, command=self.open_nickname)
        button_rename.pack(side=tk.LEFT)

        # Кнопка "О программе"
        button_info = setup_button()
        button_info.config(text="О программе", image=self.add_img_info, command=self.open_info)
        button_info.pack(side=tk.LEFT)

        # Кнопка "Об авторе"
        button_about = setup_button()
        button_about.config(text="Об авторе", image=self.add_img_about, command=self.open_about)
        button_about.pack(side=tk.LEFT)

        # Разделяющий фрэйм
        frame_separation = tk.Frame(bg=master_color_5)
        frame_separation.pack(side=tk.TOP, fill=tk.X, ipady=5)

        # Промежуточный фрэйм для подписи над полями
        frame_middle = tk.Frame(bg=master_color_1)
        frame_middle.pack(side=tk.TOP, fill=tk.X)
        tk.Label(frame_middle, text='Данные для подключения', font='Calibri 20', bg=master_color_1,
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
            return tk.Entry(frame_entry, width=40, bg=master_color_3, fg=master_color_2, font=10)

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
        label_password.config(text='Общий пароль')

        self.entry_password = setup_entry()
        self.entry_password.config(show='*')

        # Расположение entry и label
        label_id.grid(row=0, column=0, sticky="W,E")
        label_hash.grid(row=1, column=0, sticky="W,E")
        label_friend.grid(row=2, column=0, sticky="W,E", padx=10)
        label_password.grid(row=3, column=0, sticky="W,E")

        self.entry_id.grid(row=0, column=1, pady=5)
        self.entry_hash.grid(row=1, column=1, pady=5)
        self.entry_friend.grid(row=2, column=1, pady=5)
        self.entry_password.grid(row=3, column=1, pady=5)

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
        file = open('last_password.txt', 'w')
        if self.entry_password.get() != '':
            file.writelines(f'{self.entry_password.get()}')
        else:
            file.writelines(' ')
        file.close()

    def start_connect(self):
        if self.entry_id.get() == '' or self.entry_hash.get() == '' or self.entry_friend.get() == '':
            messagebox.showerror("Ошибка ввода данных", "Недостаточно данных!\nСоединение не удалось...")
        else:
            self.save_session_data()
            self.transfer_password()

            process = subprocess.Popen([sys.executable, "first.py"])
            process.wait()
            time.sleep(0.1)

            process2 = subprocess.Popen([sys.executable, "second.py"])
            process2.wait()
            time.sleep(0.1)

            process3 = subprocess.Popen([sys.executable, "third.py"])
            # process3.wait()
            time.sleep(0.1)


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


def destroy_main(root):
    root.destroy()


# Тело программы
if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Securegram")
    root.geometry("+300+100")
    root.iconbitmap('image/main_icon.ico')
    # root.wm_attributes('-alpha', 0.94)
    root.resizable(False, False)

    app.fill_entry()

    root.mainloop()
