#Ch4 PgrmEx 5

yr = int(input("Please enter a number of years: "))
i = 1
inches = 0
while i <= yr:
    j = 1
    while j <= 12:
        inches = inches + int(input("How many inches of rain were there this month?"))
        j += 1
    i += 1
months = yr * 12
print("Over the course of", months , "months, there was", inches, "inches of rain. \nThere was an average of", (inches / months), "inches of rain every month")
    