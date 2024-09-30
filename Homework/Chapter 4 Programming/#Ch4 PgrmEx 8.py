#Ch4 PgrmEx 8

i = 0
j = 0
total_length = 0
while j < 1:
    word = input("Enter a word (or press Enter to finish): ")
    if word == "": 
        print("The average length of your words was", total_length // i)
        j += 1
    else:
        total_length = total_length + len(word)
    i += 1
    


    