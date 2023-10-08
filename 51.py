import datetime as dt

names=[]
dob=[]
pwd=[]
f1=open("namesdob.txt","r")
f2=open("password.txt","w")
content=f1.readlines()
len1=len(content)

today=dt.datetime.now()
year2=today.year
month2=today.month
day2=today.day
d2=dt.date(year2,month2,day2)

for i in range(0,len1,1):
    line1=content[i].split(",")
    names.append(line1[0])
    dob.append(line1[1])
    list1=dob[i].split("-")
    year1=int(list1[0])
    month1=int(list1[1])
    day1=int(list1[2])
    d1=dt.date(year1,month1,day1)
    pwd.append(abs(d2-d1).days)
    f2.write(names[i])
    f2.write(":")
    f2.write(str(pwd[i]))
    f2.write("\n")
print(names)
print(pwd)
f2.close()
             

