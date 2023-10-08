import datetime as dt
names=["Shashank", "Shekar"]
dob=["1994-9-15","1962-12-12"]
days1=[]
len1=len(names)

list1=dob[0].split("-")
year1=int(list1[0])
month1=int(list1[1])
day1=int(list1[2])
d1=dt.date(year1,month1,day1)

today=dt.datetime.now()
year2=today.year
month2=today.month
day2=today.day
d2=dt.date(year2,month2,day2)

result1=abs(d2-d1).days

print(d1)
print(d2)
print(result1)

