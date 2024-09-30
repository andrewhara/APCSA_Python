#Ch4 AlgWkbh 2

j = 0

while j < 1:
    x = int(input("Please enter a number: "))
    y = int(input("Please enter another number: "))
    print(x+y)
    repeat = int(input("Would you like to add again? \n(1 = yes) (2 = no)"))
    if repeat != 1 and repeat != 2:
        print("Please enter a valid response")
    elif repeat == 2:
        j += 1