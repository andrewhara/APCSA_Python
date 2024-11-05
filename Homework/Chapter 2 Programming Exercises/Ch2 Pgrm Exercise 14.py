#Number 14
def compound_intrest():
    P = float(input("What is the starting amount?: "))
    r = (float(input("What is the annual intrest rate(as a percentage)?: ")) / 100)
    n = float(input("What is the number of times per year that intrest is compounded?: "))
    t = float(input("How many years are you going to leave your money in for?: "))
    print("You will have", P*(1+(r / n))**(n*t) ,"dollars after", t ,"years.")
