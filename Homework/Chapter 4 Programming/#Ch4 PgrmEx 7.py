#Ch4 PgrmEx 7

money = 0.01
days = int(input("How long are you going to be working?: "))
print("Dollars		Days")
print("---------------------")
i = 1
while i <= days:
    print(money,"		", i)
    money = money * 2
    i += 1
print("---------------------")


total = 0

while i > 1:
    i -= 1
    total = total + money / 2
    money = money / 2
print("Total:", total)