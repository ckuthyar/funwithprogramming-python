def finddays1(year1,month1,day1):
    
    import datetime
    today=datetime.datetime.now()
    y1=today.year
    m1=today.month
    d1=today.day
    print(y1,m1,d1)

    d1=datetime.date(y1,m1,d1)
    d2=datetime.date(year1,month1,day1)
    diff=(d2-d1).days
    print(diff)
finddays1(2023,7,10)
