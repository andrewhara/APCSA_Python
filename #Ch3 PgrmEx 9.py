#Ch3 PgrmEx 9

Number = int(input("Please input a number: "))

if Number == 0:
    print("Green")
elif Number % 2 == 0:
    if (Number <= 10 and Number >= 1) or (Number >= 19 and Number <= 28):
        print("Black")
    elif (Number >= 11 and Number <= 18) or (Number <= 29 and Number >= 36):
        print("Red")
        
elif Number % 2 != 0:
    if (Number <= 10 and Number >= 1) or (Number >= 19 and Number <= 28):
        print("Red")
    elif (Number >= 11 and Number <= 18) or (Number <= 29 and Number >= 36):
        print("Blue")
