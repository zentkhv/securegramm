from tkinter import *
from tkinter import messagebox as mb

def check():
    answer = mb.askyesno(
        title="Вопрос",
        message="Перенести данные?")
    if answer:
        s = entry.get()
        entry.delete(0, END)
        label['text'] = s

def info():
    mb.showinfo("Внимание", "Тут находится справка!")

root = Tk()
root.geometry('300x250')
entry = Entry()
entry.pack(pady=10)
Button(text='Передать', command=check).pack()
Button(text='Справка', command=info).pack()
label = Label(height=3)
label.pack()

root.mainloop()