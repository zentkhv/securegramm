from tkinter import *
from tkinter import messagebox
root = Tk()

def button_click():

    print('Click!')
    #login = loginInput.get()
    #password = passInput.get()

    #info_str = f'Данные: {str(login)}, {str(password)}'
    #messagebox.showinfo(title='Название', massage=info_str)
    messagebox.showinfo(title='Название', massage='Hello')


root['bg'] = '#fafafa'
root.title('Название программы')
#root.wm_attributes('-alpha', 0.7)
root.geometry('300x250')
#root.resizable(width=False, height=False)

canvas = Canvas(root, height=300, width=250)
canvas.pack()

frame = Frame(root, bg='red')
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

title = Label(frame, text='Текст', bg='gray', font=40)
title.pack()

button=Button(frame,text='Кнопка', bg='green', command=button_click)
button.pack()

loginInput=Entry(frame, bg='white')
loginInput.pack()

passInput=Entry(frame, bg='white', show='*')
passInput.pack()

root.mainloop()
