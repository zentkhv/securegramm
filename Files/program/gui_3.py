import tkinter as tk

root = tk.Tk()
root.title("Securegram. Настройка соединения")
root.geometry("500x500+300+200")
root.resizable(False, False)
root.iconbitmap('main_icon.ico')

frame_toolbar = tk.Frame(root, bg='red')
#frame_toolbar.pack(side=tk.TOP, fill=tk.X)
frame_toolbar.pack()




root.mainloop()
