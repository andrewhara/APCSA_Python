#Ch3 PgrmEx 15

Seconds = int(input("Enter the number of Seconds: "))
SecondsPerDay = 86400
SecondsPerHour = 3600
SecondsPerMinute = 60

days = 0
hours = 0
minutes = 0

if Seconds >= SecondsPerDay:
    days = Seconds // SecondsPerDay
    Seconds %= SecondsPerDay

if Seconds >= SecondsPerHour:
    hours = Seconds // SecondsPerHour
    Seconds %= SecondsPerHour

if Seconds >= SecondsPerMinute:
    minutes = Seconds // SecondsPerMinute
    Seconds %= SecondsPerMinute


if days > 0:
    print(days, "Days", hours, "Hours", minutes, "Minutes", Seconds ,"Seconds")
elif hours > 0:
    print(hours, "Hours", minutes, "Minutes", Seconds ,"Seconds")
elif minutes > 0:
    print(minutes, "Minutes", Seconds ,"Seconds")
else:
    print(Seconds ,"Seconds")



