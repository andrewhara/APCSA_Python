#Ch5 PgrmEx 6

def yumyum():
    fat = int(input("Please enter the grams of fat you consumed today: "))
    carbs = int(input("Please enter the grams of carbs you entered today: "))
    
    calories_from_fat = fat * 9
    calories_from_carb = carbs * 4
    
    print("The amount of calories you are getting from fat alone is:", calories_from_fat)
    print("The amount of calories you are getting from carbs alone is:", calories_from_carb)
    
    
yumyum()