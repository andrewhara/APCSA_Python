#Ch3 PgrmEx 12

price = 99

Quantity = int(input("How many packages would you like to order?: "))

if Quantity >= 10 and Quantity <= 19:
    price = price - 0.10*price
    print("You recieved a 10% discount, and your new total is", price)
    
elif Quantity >= 20 and Quantity <= 49:
    price = price - 0.20*price
    print("You recieved a 20% discount, and your new total is", price)
    
elif Quantity >= 50 and Quantity <= 99:
    price = price - 0.30*price
    print("You recieved a 30% discount, and your new total is", price)
    
elif Quantity >= 100:
    price = price - 0.40*price
    print("You recieved a 40% discount, and your new total is", price)
    
else:
    print("You get no discount, sowwy :(")