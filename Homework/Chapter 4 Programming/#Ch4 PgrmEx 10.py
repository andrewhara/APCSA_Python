#Ch4 PgrmEx 10

tuition = 8000
yr = 5
i = 1
while i <= yr:
    print("The tuition is", round(tuition, 2) ,"for year number", i)
    tuition += tuition * 0.03
    i += 1
    