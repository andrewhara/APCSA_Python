#Ch3 PgrmEx 7

Ex1 = int(input("What score did you recieve for the first test?: "))
Ex2 = int(input("What score did you recieve for the second test?: "))
Main = int(input("What score did you recieve for the Main Exam?: "))
Total = Ex1 + Ex2 + Main

if Ex1 > 25 or Ex1 < 0 or Ex2 > 25 or Ex2 < 0 or Main > 50 or Main < 0:
    print("You have put in an incorrect number")
    
elif Total < 50 or Main < 25:
    print("You failed, womp womp.")
    
elif Total >= 80:
    print("Distinction.")
    
elif Total <= 59 and Total >= 50:
    print("Pass")
    
elif Total < 80 and Total >= 60:
    print("Credit")

