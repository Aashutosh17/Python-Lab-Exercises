#Given the integer N- the number of minutes that is passed since midnight- how many hours and minute are displayed on 24h digital clock?
# The program should print should two number the number of hours(between 0 and 23) and the number of minutes (between 0 and 59) for example, if N= 150 then 150 minutes have passed since mid night-i.e now is 2:30am.So,the program should print 2 30
N= int (input("Enter the minute passed since midnight:"))
hours= (N//60)
minutes=(N%60)
print(f"the hours is {hours}")
print(f"the minutes is {minutes}")
print(f"Its {hours}:{minutes}now")