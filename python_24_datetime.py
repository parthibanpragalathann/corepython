'''
DTAETIME FUCNTION IN PYTHON



'''
import datetime as d

current_date = d.date.today()
print("current date : ", current_date)

date_value = d.date(2021, 9, 30)
print("my birth year : ", date_value.year)
print("my birth month : ", date_value.month)
print("my birth day : ", date_value.day)

time_value= d.time(18, 45, 5, 555505)
print("my birth hour : ", time_value.hour)
print("my birth minute : ", time_value.minute)
print("my birth seconds : ", time_value.second)
print("my birth moicro seconds : ", time_value.microsecond)

current_time = d.datetime.now()
print("current time ", current_time)

print("string format time : ", current_time.strftime("%A %b %d %y"))

'''
OUTPUT
current date :  2022-01-01
my birth year :  2021
my birth month :  9
my birth day :  30
my birth hour :  18
my birth minute :  45
my birth seconds :  5
my birth moicro seconds :  555505
current time  2022-01-01 19:54:21.258649
string format time :  Saturday Jan 01 22
'''
