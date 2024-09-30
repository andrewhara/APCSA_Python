#Ch4 PgrmEx 16

import turtle as turt
turt.speed(200)
i = 5
turt.penup()
turt.goto(250, -250)
turt.pendown()
while i <= 500:
    j = 1
    while j <= 4:
        turt.left(90)
        turt.forward(i)
        j += 1
    i += 5
    
