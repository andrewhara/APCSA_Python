#Ch4 PgrmEx 12

n = int(input("Enter a non negative integer: "))
result = 1
for i in range(2,n+1):
    result *= i
print("Factorial of", n, "=" ,result)