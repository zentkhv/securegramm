import re

f = open('test.txt')
data = f.readlines()[0].split(',')
for i in range(0, len(data)):
    data[i] = re.sub("^\s+|\n|\r|\s+$", "", str(data[i]))
print(data)
print(len(data))
