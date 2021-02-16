import tkinter as tk


# from tkinter import *


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


# Условие проверяющее, вызывается ли скрипт как основной
if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Securegram. Настройка соединения")
    root.geometry("650x450+200+200")
    root.resizable(False, False)

    root.mainloop()
