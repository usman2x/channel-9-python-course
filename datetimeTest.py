from datetime import datetime, timedelta

today = datetime.now()

oneDay = timedelta(days=1)
yesterday = today - oneDay
print("Yesterday was " + str(yesterday))

print("Today is " + str(today))

tomorrow = today + oneDay
print("Tomorrow will be " + str(tomorrow))

birthDay = "2020-06-25"
birthDay = datetime.fromisoformat(birthDay)
print("My next birth day will be on " + str(birthDay))