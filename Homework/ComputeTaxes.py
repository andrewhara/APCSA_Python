# File: ComputeTaxes.py
# Student: Andrew Hara
#
# Date: 26 September 2024
# Description of Program: A python program that computes and reports the tax burden for an individual
# based on marital status and taxable income
# GitHub: andrewhara


def tax_bracket():
    print("Welcome to our friendly tax computing program. \nPlease follow the directions.")
    married = input("Please enter your marital status (s or m): ")
    if (married != "s" and married != "m"): #Checking for valid input
        print("Bad marital status entered! Try again later.")
        return
    
    income = float(input("Please enter your taxable income: "))
    if income < 0: #Checking for valid income
        print("Negative income entered, get your money up not your funny up.")
        return
        
    if married == "s": #Checking tax brackets for single people
        if income <= 8000:
            tax = income * 0.10
        elif income <= 32000:
            tax = 800 + (income - 8000) * 0.15
        else:
            tax = 4400 + (income - 32000) * 0.25
        status = "Single"
    
    else: #Checking tax brackets for married people
        if income <= 16000:
            tax = income * 0.10
        elif income <= 64000:
            tax = 1600 + (income - 16000) * 0.15
        else:
            tax = 8800 + (income - 64000) * 0.25
        status = "Married"
    
    print("Marrital status:", status)
    print("Taxable income:", round(income, 2))
    print("Taxes owed:", round(tax, 2))

tax_bracket()