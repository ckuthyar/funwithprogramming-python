import datetime as dt
names=["Shashank", "Shekar","Shanthi"]
dob=["1994-9-15","1962-12-12","1965-12-31"]
pwd=[]
len1=len(names)

today=dt.datetime.now()
year2=today.year
month2=today.month
day2=today.day
d2=dt.date(year2,month2,day2)

for i in range(0,len1,1):
    list1=dob[i].split("-")
    year1=int(list1[0])
    month1=int(list1[1])
    day1=int(list1[2])
    d1=dt.date(year1,month1,day1)

    pwd.append(abs(d2-d1).days)
print(names)
print(pwd)

