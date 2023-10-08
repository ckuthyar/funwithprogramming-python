import datetime
birth_date = input("Enter birth date (YYYY-MM-DD): ")
now = datetime.datetime.now()
birth_date = datetime.datetime.strptime(birth_date, "%Y-%m-%d").date()
age = (now.year - birth_date.year)-(now.month-birth_date.month)-(now.day- birth_date.day)
print( "your Age is:", age)
