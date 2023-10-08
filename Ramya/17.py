import datetime as dt
today=dt.datetime.now()
y1=today.year
m1=(today.month)
d1=(today.day)
h1=(today.hour)
m2=(today.minute)
s1=(today.second)
time1=(str(y1)+str(m1)+str(d1)+str(h1)+str(m2)+str(s1))
print(time1)
