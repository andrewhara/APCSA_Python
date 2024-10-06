#Ch5 PgrmEx 5

def property_tax():
    
    value = int(input("Please enter the value of your property: "))
    assess_value = value * 0.60
    tax = assess_value / 100
    prop_tax = tax * 0.72
    
    print("The assessment value of your property is", assess_value, "dollars")
    print("The tax for the property will be", round(prop_tax, 2), "dollars")
    
    
    
property_tax()