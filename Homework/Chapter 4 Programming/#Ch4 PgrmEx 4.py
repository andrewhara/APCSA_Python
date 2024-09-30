#Ch4 PgrmEx 4

speed = int(input("Please enter the speed of your train in miles per hour: "))
time = int(input("Please enter how long your train has been going in hours: "))
i = 1
print("Hour			Distance Traveled")
print("-----------------------------------------")
while i <= time:
    print(i," 				", i * speed)
    i += 1