#Ch3 PgrmEx 1

x = int(input("Please input a number: "))
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")
    
if (x % 2) == 1:
    print("Odd")
    
if (x % 2) == 0:
    print("Even")
