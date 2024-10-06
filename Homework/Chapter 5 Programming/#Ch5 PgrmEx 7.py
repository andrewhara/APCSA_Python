#Ch5 PgrmEx 7

def seats():
    a = int(input("Please enter the tickets sold for Class A tickets: "))
    b = int(input("Please enter the tickets sold for Class B tickets: "))
    c = int(input("Please enter the tickets sold for Class C tickets: "))
    
    total = (a * 20) + (b * 15) + (c * 10)
    print("The total income from the seats is", total, "dollars.")
    
    
    
seats()