import os
path1="D:/Coding/Python"
for (root,dirs,files) in os.walk(path1):
    print(root)
