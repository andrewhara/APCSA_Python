#Ch4 PgrmEx 13

population = int(input("Starting number of organisms: "))
Avg_Daily_Increase = int(input("Agerage daily increase (in percentage): "))
Days_To_Multiply = int(input("Number of days to multiply: "))
print("Day Approximate			Population")
i = 1
while i <= Days_To_Multiply:
    print(i, "			", int(population))
    population += population * (Avg_Daily_Increase / 100)
    i += 1