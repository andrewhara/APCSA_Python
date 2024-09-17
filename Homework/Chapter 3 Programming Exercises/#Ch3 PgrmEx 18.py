#Ch3 PgrmEx 18

#Restaurant Selector

Veg = input("Is anyone in your party vegetarian? ")
Vegan = input("Is anyone in your party vegan? ")
Gluten = input("Is anyone in your party gluten-free? ")

if Veg == "Yes" or Veg == "yes":
    
    if Vegan == "Yes" or Vegan == "yes":
        
        if Gluten == "Yes" or Gluten == "yes":
            print("Corner Cafe \nThe Chef's Kitchen")
        
        elif Gluten == "No" or Gluten =="no":
            print("Corner Cafe \nThe Chef's Kitchen")
    
    elif Vegan == "No" or "no":
        
        if Gluten == "Yes" or Gluten == "yes":
            print("Corner Cafe \nMain Street Pizza Company \nThe Chef's Kitchen")
        
        elif Gluten == "No" or Gluten =="no":
            print("Corner Cafe \nMain Street Pizza Company \nThe Chef's Kitchen \n Mama's Fine Italian")
            
elif Veg == "No" or Veg == "no":
    if Vegan == "Yes" or Vegan == "yes":
        
        if Gluten == "Yes" or Gluten == "yes":
            print("Corner Cafe \nThe Chef's Kitchen")
        
        elif Gluten == "No" or Gluten =="no":
            print("Corner Cafe \nThe Chef's Kitchen")
    
    elif Vegan == "No" or "no":
        
        if Gluten == "Yes" or Gluten == "yes":
            print("Corner Cafe \nMain Street Pizza Company \nThe Chef's Kitchen")
        
        elif Gluten == "No" or Gluten =="no":
            print("Joe's Gourmet Burgers \nCorner Cafe \nMain Street Pizza Company \nThe Chef's Kitchen \n Mama's Fine Italian")
