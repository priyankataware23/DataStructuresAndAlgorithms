from datetime import date, timedelta

sdate = date(2018, 01, 01)   # start date
edate = date(2018, 12, 31)   # end date

delta = edate - sdate       # as timedelta
list1=[]
for i in range(delta.days + 1):
    day = sdate + timedelta(days=i)
    print(day)