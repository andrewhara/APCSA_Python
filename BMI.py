#A program that asks the user for their height and  weight in meters in kilograms, respecitvely
#Then calculates BMI

def bmi():
    
    a = 1
    
    while a > 0:
    
        print('This program will compute BMI.')
        
        height = float(input('Please enter your height in meters: '))
        mass = float(input('Please enter your weight in kilograms: '))
        
        #Compute and display BMI
        
        bmi = (mass/ height **2) #bmi is automatically a float bc of math
        
        bmi = int(bmi * 10)/ 10 ## keep result as a real number with one decimal place
        
        print('Current BMI with a weight of ', mass, 'and a height of ', height, 'is', bmi)
        
        if bmi >= 30.0:
            print("Obese")
            
        elif bmi >= 25.0 and bmi <= 29.9:
            print("Overweight")
            
        elif bmi >= 18.5 and bmi <= 24.9:
            print("Healthy")
        
        elif bmi < 18.5:
            print("Underweight")
            
        a = int(input("Continue? Press 0 for NO, and 1 for yes"))
        
    
    
bmi()