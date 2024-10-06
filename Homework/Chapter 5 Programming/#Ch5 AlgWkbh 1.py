#Ch5 AlgWkbh 1

def shout():
    string = list(input("What do you want to shout? ")) 
    
    for i in range(len(string)): 
        if 97 <= ord(string[i]) <= 122: #Checks if the character is lowercase
            string[i] = chr(ord(string[i]) - 32) #Changes lowercase letters to uppercase
    
    string = "".join(string) #Smushes all of the elements back into a string
    print(string.rstrip(" ") + "!") #prints the string with a ! at the end without a space between

shout()
