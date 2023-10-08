from datetime import datetime
today=datetime.today()
yy=int(today.year)
mm=int(today.month)
dd=int(today.day)
yob=int(input('Enter your year of Birth in YYYY format: '))
mob=int(input('Enter your month of Birth in mm format: '))
dob=int(input('Enter your year of Birth in dd format: '))
print('Today is',today)
print('Your Date of birth is',dob,mob,yob,)
years=int(yy)-int(yob)
months=mm-mob
days=dd-dob
print(years,'years',months,'months',days,'days')  
