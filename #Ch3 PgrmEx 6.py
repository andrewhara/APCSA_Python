#Ch3 PgrmEx 6

month = int(input("Please enter a month in number form: "))
day = int(input("Please enter a day in number form: "))
year = int(input("Please enter the last two digits of a year: "))

if month*day == year:
    print("Your day is magic")
    
else:
    print("Your day is not magic:(")