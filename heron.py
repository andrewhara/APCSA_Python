#A = sqrt(s(s-a)(s-b(s-c))
#s = (a+b+c)/2 = perimeter/s


def trianglearea(a,b,c):
    print("Triangle Area Calculator")
    s = (a + b + c)/2
    
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    
    print(area)
    
def main():
    a = float(input("Value of side a: "))
    b = float(input("Value of side b: "))
    c = float(input("Value of side c: "))
    trianglearea(a,b,c)
    trianglearea(5,12,13)
    
main()