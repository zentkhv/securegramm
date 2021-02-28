import tkinter as tk
import subprocess
import sys
import time


def connect():
    process = subprocess.Popen([sys.executable, "first.py"])
    process.wait()
    time.sleep(0.1)

    process2 = subprocess.Popen([sys.executable, "second.py"])
    process2.wait()
    time.sleep(0.1)

    process3 = subprocess.Popen([sys.executable, "third.py"])
    # process3.wait()
    time.sleep(0.1)


root = tk.Tk()
root.title("Telegram")
root.geometry("300x50")
tk.Button(root, text='Connect', command=connect).pack()
root.resizable(False, False)
root.mainloop()
