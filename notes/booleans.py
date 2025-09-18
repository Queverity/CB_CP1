# CB 1st Booleans Notes

import time
import datetime as date

current_time = time.time()
readable_time = time.ctime(current_time)
new_current_time = date.datetime.now()
hour = new_current_time.strftime("%H")
# Hour: %H
# Minutes: %M
# Weekday: %A, %a
# Day: %d
# Month %B, %b
# Month NUm: %m
# Year: %Y, %y
# Seconds: %S


print(f"Current time in seconds since January 1st, 1970(epoch): {current_time}") 
print(f"Current time from datetime: {new_current_time}") 
print(f"Today is {readable_time}")
print(f"The hour is: {hour}")



print(f"The hour is saved as an integer: {isinstance(hour,int)}")
print(f"The hour is saved as an float: {isinstance(hour,float)}")
print(f"The hour is saved as an string: {isinstance(hour,str)}")

print(f"Hour has a value: {bool(hour)}")
print(f"0 has a value: {bool(0)}")
print(f"Any other number has a value: {bool(3.14159)}")

