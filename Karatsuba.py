#File: Karatsuba.py
#Student: Andrew Hara
#
#Date: Spetember 13, 2024
#This program will use a special case of the Karatsuba Multiplication process, which takes two 4-digit integers supplied by the user.
#The computer will us an algorithm which will match up to the actual answer of the two 4-digit numbers.
#GitHub: andrewhara




def kat():
    print()
    n1 = int(input("Please enter a 4 digit number: "))
    n2 = int(input("Please enter another 4 digit number: "))
    a = n1 // 100
    b = n1 % 100
    c = n2 //100
    d = n2 % 100
    e = a*c
    f = b*d
    g = (a+b)*(c+d)
    h = g-(e+f)
    i = e*10000
    j = h*100
    k = i+j+f
    ans = n1*n2
     
    print("According to Andrey Kolmogorov, the answer is", k , "\n")
    print("According to the black magic of masic multiplication, the answer is", ans)
    
    
kat()
    
    