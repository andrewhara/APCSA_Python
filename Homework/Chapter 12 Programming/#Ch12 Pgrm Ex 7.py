#Ch12 PgrmEx 7

#Ch12 Pgrm Ex 7

def main():
    result = 1
    x = int(input("Please enter a number you want to be the base: "))
    y = int(input("Please enter a number you want to be the exponent: "))
    i = 0
    while i < y:
        result *= powah(x,y)
        i += 1
    print(result)
    
    
def powah(x,y):
    total = 1
    if y == 1:
        return x
    elif y == 0:
        return 1
    else:
        y -= 1
        total *= powah(x,y)
        return total
        
main()
