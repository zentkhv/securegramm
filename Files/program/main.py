import subprocess
import sys   # Используется!
import time
from tkinter import *

process = subprocess.Popen([sys.executable, "first.py"])
process.wait()
time.sleep(0.1)

process2 = subprocess.Popen([sys.executable, "second.py"])
process2.wait()
time.sleep(0.1)

process3 = subprocess.Popen([sys.executable, "third.py"])
process3.wait()
time.sleep(0.1)