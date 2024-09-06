def foo():
    print('Hello World!')
    print('Go Celts!')
    print("Hook 'em good!")
    print("(10.5+2*3)/(45-3.5) = ", (10.5+2**3)/-3.5)
    
def age():
    birth_year = int (input("Please enter your year of birthing: "))
    current_year = int (input("Please enter the current year: "))
    age = current_year - birth_year
    print("You will be", age, "years old in", current_year)
        
age()
