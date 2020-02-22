# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

date = list(map(int,input().split()))
day = calendar.weekday(date[2],date[0],date[1])
# print(day)
mydict ={6:"SUNDAY",0:"MONDAY",1:"TUESDAY",2:"WEDNESDAY",3:"THURSDAY",4:"FRIDAY",5:"SATURDAY"}
print(mydict[day])


