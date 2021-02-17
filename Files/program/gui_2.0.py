import tkinter as tk
from tkinter import ttk


# Класс основного окна
class Main(tk.Frame):
    # Конструктор
    def __init__(self, root):
        super().__init__(root)
        self.add_img = tk.PhotoImage(file='connection2.png')
        self.init_main()

    # Создание элементов окна
    def init_main(self):
        toolbar = tk.Frame(bg="#d7d8e0", bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        button_open_dialog = tk.Button(toolbar, text="Соединить", command=self.open_dialog, bg='#d7d8e0', bd=0,
                                       compound=tk.TOP, image=self.add_img)
        button_open_dialog.pack(side=tk.LEFT)


        # Подписи к полям ввода
        label_id = tk.Label(self, text='API ID')
        label_id.place(x=50, y=50)

        label_hash = tk.Label(self, text='API Hash')
        label_hash.place(x=50, y=80)

        label_friend = tk.Label(self, text='Ник собеседника')
        label_friend.place(x=50, y=110)

        label_password = tk.Label(self, text='Общий пароль')
        label_password.place(x=50, y=140)

        # Поля ввода
        self.entry_id = ttk.Entry(self)
        self.entry_id.place(x=200, y=50)

        self.entry_hash = ttk.Entry(self)
        self.entry_hash.place(x=200, y=80)

        self.entry_friend = ttk.Entry(self)
        self.entry_friend.place(x=200, y=110)

        self.entry_password = ttk.Entry(self)
        self.entry_password.place(x=200, y=140)

        # Поля для вывода информации в виде близком к таблице
        # self.tree = ttk.Treeview(self, columns=('ID', 'description', 'cost', 'total'), height=15, show="headings")
        #
        # self.tree.column('ID', width=30, anchor=tk.CENTER)
        # self.tree.column('description', width=30, anchor=tk.CENTER)
        # self.tree.column('cost', width=30, anchor=tk.CENTER)
        # self.tree.column('total', width=30, anchor=tk.CENTER)
        #
        # self.tree.heading('ID', text='ID')
        # self.tree.heading('description', text='Наименование')
        # self.tree.heading('cost', text='Статья дохода или расхода')
        # self.tree.heading('total', text='Сумма')
        # self.tree.pack()

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

        self.grab_set()
        self.focus_set()

        # Подписи к полям ввода
        label_id = tk.Label(self, text='API ID')
        label_id.place(x=50, y=50)

        label_hash = tk.Label(self, text='API Hash')
        label_hash.place(x=50, y=80)

        label_friend = tk.Label(self, text='Ник собеседника')
        label_friend.place(x=50, y=110)

        label_password = tk.Label(self, text='Общий пароль')
        label_password.place(x=50, y=140)

        # Поля ввода
        self.entry_id = ttk.Entry(self)
        self.entry_id.place(x=200, y=50)

        self.entry_hash = ttk.Entry(self)
        self.entry_hash.place(x=200, y=80)

        self.entry_friend = ttk.Entry(self)
        self.entry_friend.place(x=200, y=110)

        self.entry_password = ttk.Entry(self)
        self.entry_password.place(x=200, y=140)


# Условие проверяющее, вызывается ли скрипт как основной
if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Securegram. Настройка соединения")
    root.geometry("650x450+200+200")
    root.resizable(False, False)

    root.mainloop()
