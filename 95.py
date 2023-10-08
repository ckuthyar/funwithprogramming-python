import os
cwd=os.getcwd()
print(cwd)

os.chdir("D:/Coding")
cwd=os.getcwd()
print(cwd)

#os.mkdir("D:/Coding/Python1")
list1=os.listdir("D:/Coding")
print(list1)

f1="in1.txt"
loc="D:/Coding/Python1"
path=os.path.join(loc,f1)
print(path)

os.remove(path)
os.rmdir(loc)
