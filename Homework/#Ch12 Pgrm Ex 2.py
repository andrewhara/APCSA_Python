#Ch12 Pgrm Ex 2

def main():
    product = 0
    x = int(input("Please enter a number you want multiplied: "))
    y = int(input("Please enter a number you want multiplied: "))
    i = 0
    while i < x:
        product += mult(x,y)
        i += 1
    print(product)
    
    
def mult(x,y):
    big_sum = 0
    if x == 1:
        return y
    elif y == 1:
        return x
    else:
        x -= 1
        big_sum += mult(x,y)
        return big_sum
        
main()