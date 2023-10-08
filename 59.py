def finddays1(year1,month1,day1):
    
    import datetime
    today=datetime.datetime.now()
    d1=datetime.date(today.year,today.month,today.day)
    d2=datetime.date(year1,month1,day1)
    diff=(d2-d1).days
    print(diff)
finddays1(2023,7,16)
