from tkinter import *
from tkinter import messagebox

# Параметры главного окна
root = Tk()

root['bg'] = '#ccc'
root.title('Securegram. Параметры ')
# root.wm_attributes('-alpha', 0.7)   Прозрачность окна
root.geometry('310x400')
root.resizable(width=False, height=False)


# Функции
def button_enter_click():
    value_id = entry_id.get()
    value_hash = entry_hash.get()
    value_friend = entry_friend.get()
    value_password = entry_password.get()

    file = open('last_session.txt', 'w')
    file.writelines(value_id + '\n')
    file.writelines(value_hash + '\n')
    file.writelines(value_friend + '\n')
    file.writelines(value_password + '\n')
    file.close()

    messagebox.showinfo('Успех', f'Вход совершен, данные записаны. value_id: {value_id}')


# Создание элементов
label_id = Label(text='API ID', font='Comfort 15', fg='#3d3d42', bg='#ccc')
entry_id = Entry(root, font='Consoles 15', fg='#eff5c9', bg='#48494f', relief='solid', justify='center', width=15)
# relief: solid, raised, ridge, groove, flat, sunken

label_hash = Label(text='API Hash', font='Comfort 15', fg='#3d3d42', bg='#ccc')
entry_hash = Entry(root, font='Consoles 15', fg='#eff5c9', bg='#48494f', relief='solid', justify='center', width=20)

label_friend = Label(text='Ник собеседника', font='Comfort 15', fg='#3d3d42', bg='#ccc')
entry_friend = Entry(root, font='Consoles 15', fg='#eff5c9', bg='#48494f', relief='solid', justify='center', width=10)

label_password = Label(text='Общий пароль', font='Comfort 15', fg='#3d3d42', bg='#ccc')
entry_password = Entry(root, font='Consoles 15', fg='#eff5c9', bg='#48494f', relief='solid', justify='center', show='*')

checkbutton_save = Checkbutton(text='Не записывать данные соединения', font='Comfort 12', fg='#3d3d42', bg='#ccc',
                               activeforeground='#3d3d42',
                               activebackground='#ccc')

button_enter = Button(text='Соединить', font='Comfort 15', fg='#eff5c9', bg='#48494f', relief='solid',
                      activeforeground='#eff5c9',
                      activebackground='#6e6f73',
                      command=button_enter_click)

# Бинды
button_enter.bind('<Button-1>', button_enter_click)

# Упаковка
label_id.pack()
entry_id.pack()
label_hash.pack()
entry_hash.pack()
label_friend.pack()
entry_friend.pack()
label_password.pack()
entry_password.pack()
checkbutton_save.pack()
button_enter.pack()

# События для реализации после запуска и всех подготовок

# Проверка файла на наличие прошлых сессий, выгрузка данных если сессия уже была

f = open('last_session.txt')
fd = f.readlines()
entry_id.insert(0, fd[0][0:len(fd[0]) - 1])
entry_hash.insert(0, fd[1][0:len(fd[1]) - 1])
entry_friend.insert(0, fd[2][0:len(fd[2]) - 1])
entry_password.insert(0, fd[3][0:len(fd[3]) - 1])
f.close()

# Петля IndexError
root.mainloop()
