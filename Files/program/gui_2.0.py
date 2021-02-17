import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


# Класс основного окна
class Main(tk.Frame):
    # Конструктор
    def __init__(self, root):
        super().__init__(root)
        self.add_img = tk.PhotoImage(file='connection2.png')
        self.init_main()

    # Создание элементов окна
    def init_main(self):
        frame_toolbar = tk.Frame(bg="#d7d8e0")
        frame_toolbar.pack(side=tk.TOP, fill=tk.X)

        button_open_dialog = tk.Button(frame_toolbar, text="Соединить", command=self.open_dialog, bg='#d7d8e0', bd=0,
                                       compound=tk.TOP, image=self.add_img)
        button_open_dialog.pack(side=tk.RIGHT)

        canvas = tk.Canvas(self)
        canvas.pack(fill=tk.X)

        # Подписи к полям ввода
        label_id = tk.Label(frame_toolbar, text='API ID', bg="#d7d8e0")
        label_id.place(x=20, y=10)

        label_hash = tk.Label(frame_toolbar, text='API Hash', bg="#d7d8e0")
        label_hash.place(x=20, y=40)

        label_friend = tk.Label(frame_toolbar, text='Ник собеседника', bg="#d7d8e0")
        label_friend.place(x=20, y=70)

        label_password = tk.Label(frame_toolbar, text='Общий пароль', bg="#d7d8e0")
        label_password.place(x=20, y=100)

        # Поля ввода
        self.entry_id = ttk.Entry(frame_toolbar, width=40)
        self.entry_id.place(x=140, y=10)

        self.entry_hash = ttk.Entry(frame_toolbar, width=40)
        self.entry_hash.place(x=140, y=40)

        self.entry_friend = ttk.Entry(frame_toolbar, width=40)
        self.entry_friend.place(x=140, y=70)

        self.entry_password = ttk.Entry(frame_toolbar, width=40)
        self.entry_password.place(x=140, y=100)

    def open_dialog(self):
        Child()


# Класс дочернего окна, вызываемого основным
class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title('Диалог с ...')
        self.geometry('400x220+400+300')
        self.resizable(False, False)
        #self.iconbitmap('telegram.ico')

        self.grab_set()
        self.focus_set()


# Условие проверяющее, вызывается ли скрипт как основной
if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Securegram. Настройка соединения")
    root.geometry("550x140+300+200")
    #root.iconbitmap('telegram.ico')
    root.resizable(False, False)

    root.mainloop()
