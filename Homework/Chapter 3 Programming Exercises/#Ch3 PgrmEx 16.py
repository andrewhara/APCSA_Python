#Ch3 PgrmEx 16


 
print("Type in a year and the program will determine")
yr = int(input("if the year is a leap year:"))
                                
if (yr % 400 == 0) or (yr % 4 == 0 and yr % 100 != 0):
    print("In", yr, "Febuary has 29 days.")
else:
    print("In", yr, "Febuary has 28 days.")
        

