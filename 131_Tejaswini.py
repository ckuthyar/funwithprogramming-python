import os
import datetime as dt
today=dt.datetime.now()
y1=str(today.year)
m1=str(today.month).zfill(2)
d1=str(today.day).zfill(2)
h1=str(today.hour).zfill(2)
m2=str(today.minute).zfill(2)
fname2=y1+m1+d1+"_"+h1+m2
fname1="phfile_"
fname3=".txt"
file_name=fname1+fname2+fname3

info1=os.listdir()

list1=[]
list2=[]

list1.append(info1)
print(list1)

for photos in info1:
    if photos.endswith('.jpg'):
        list2.append(photos)
    elif photos.endswith('.jpeg'):
        list2.append(photos)
    elif photos.endswith('.png'):
        list2.append(photos)

print(list2)


with open(file_name,'w')as file:
     for names in list2:
         file.write('%s\n'%names)
