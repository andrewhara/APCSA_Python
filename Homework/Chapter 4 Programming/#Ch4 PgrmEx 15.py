#Ch4 PgrmEx 15
row = int(input("How many rows would you like?: "))
i = 0
while i < row:
    if i == 0:
        print("##")
        i += 1
    else:
        print("#", end = "")
        j = 0
        while j < i:
            print(" ", end = "")
            j += 1
        print("#")
        i += 1
    
