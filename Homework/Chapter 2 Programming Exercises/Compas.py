#Chapter 2 Programming Excersises #15
#Mr. Lopez Answer

import turtle as turt

turt.forward(200)
turt.right(180)
turt.forward(400)
turt.right(180)
turt.forward(200)

turt.right(90)
turt.forward(200)
turt.right(180)
turt.forward(400)

turt.penup()
turt.goto(50,0)
turt.pendown()
turt.circle(50)

turt.penup()
turt.goto(0,210)
turt.write("North")

turt.goto(215,0)
turt.write("East")

turt.goto(0,-220)
turt.write("South")

turt.goto(-220,0)
turt.write("West")




turt.hideturtle()
input("Press any key to exit")
