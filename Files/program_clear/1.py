import subprocess
import sys
import time

process = subprocess.Popen([sys.executable, "start.py"])
process.wait()
time.sleep(0.2)

process3 = subprocess.Popen([sys.executable, "OBMEN.py"])
process3.wait()
time.sleep(0.2)

process2 = subprocess.Popen([sys.executable, "11111.py"])
process2.wait()
