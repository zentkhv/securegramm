import subprocess
import sys
import time

process = subprocess.Popen([sys.executable, "first.py"])
process.wait()
time.sleep(0.2)

process2 = subprocess.Popen([sys.executable, "second.py"])
process2.wait()
time.sleep(0.2)

process3 = subprocess.Popen([sys.executable, "third.py"])
process3.wait()
