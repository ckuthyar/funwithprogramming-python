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


start=int(input('Enter first number '))
end=int(input('Enter second number '))
for j in range(start,end+1,1):
    f1=str(j)+'_'+time1+'.txt'
    file1=open(f1,'w')
    for i in range(1,11,1):
        print(j,i,j*i)
        a=str(j)+' '+str(i)+' '+str(int(j*i))
        file1.write(a)
        file1.write('\n')

    print()
file1.write('\n ')   
file1.close()
