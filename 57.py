import datetime
today=datetime.datetime.now()
y1=today.year
m1=today.month
d1=today.day
print(y1,m1,d1)

d1=datetime.date(y1,m1,d1)
d2=datetime.date(2023,7,10)
diff=(d2-d1).days
print(diff)
