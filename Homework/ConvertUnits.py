#File: ConvertUnits.py
#Student: Andrew Hara
#
#Date: 18 September 2024
#Github: andrewhara

inputFeet = float(input("Enter number of feet: "))
inputinches = float(input("Enter the number of inches: "))

inches = inputFeet*12 + inputinches
feet = inches / 12
yards = feet / 3
miles = feet / 5280
meters = feet / 0.3048
centimeters = meters * 100
millimeters = centimeters * 10
kilometers = meters / 1000

print(inputFeet, "feet and", inputinches, "inches equals:")

print("English Units")
print(" feet:", feet)
print("inches:", inches)
print(" yards:", yards)
print(" miles:", miles)
print("Metric Units")
print(" meters:", meters)
print(" centimeters:", centimeters)
print(" millimeters:", millimeters)
print(" kilometers:", kilometers)