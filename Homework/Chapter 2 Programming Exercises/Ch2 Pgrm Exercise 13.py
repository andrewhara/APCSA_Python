#Number 13
def vineyard():
    R = float(input("How long is your row of grapevines(in feet)?: "))
    E = float(input("How much space will your end-post assembly be(in feet)?: "))
    S = float(input("How much space will be between vines(in feet)?: "))
    grapevines = ((R - 2*E)/S)
    int (grapevines)
    if (grapevines < 0):
        print("Congratulations, you somehow managed to plant negative grapevines")
        
    if (grapevines == 0):
        print("Congratulations, you have a failing grapevine farm, since you cant plant any")
        
    if (grapevines > 0):
        print("You will be able to fit", grapevines, "grapevines in your row")
        
