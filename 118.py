import os
list1=os.listdir()
len1=len(list1)
for i in range(1,120,1):
    status=os.path.isfile(list1[i])
    if status:
        f1=open(list1[i],"r")
        info1=f1.readline()
        if info1=="Devil\n":
            print("Virus found in",list1[i])
        continue
    else:
        continue

