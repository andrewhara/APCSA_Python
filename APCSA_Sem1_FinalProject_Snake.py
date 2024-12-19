import turtle as turt
import random

screen = turt.Screen()
screen.setup(620, 620)
screen.tracer(0)

#Creating the initial length
length = 3

#Snake turtle
trt = turt.Turtle('square')

#Fruit turtle
fruit_turtle = turt.Turtle()
fruit_turtle.shape('circle')
fruit_turtle.penup()
fruit_turtle.hideturtle()

#Global variable to track the snake's movement
hor = 0
vert = 0
fruit_position = None
snake_segments = []  #List to hold the segments of the snake


#Move snake to top-left corner to start the grid drawing
trt.penup()
trt.goto(-310, 310)
trt.pendown()

def fruit():
    global fruit_position
    #Clear previous fruit
    fruit_turtle.clear()

    fxcoord = random.randint(-7, 7) * 40  #Randomly choose an x-coordinate inside the grid box
    fycoord = random.randint(-7, 7) * 40  #Randomly choose a y-coordinate inside the grid box
    fruit_position = (fxcoord, fycoord)  #Store fruit position

    #Move fruit turtle to new coordinates and draw fruit
    fruit_turtle.goto(fxcoord, fycoord)
    fruit_turtle.showturtle()  #Show the fruit at the new position

#Forming the grid for the game
def make_grid():
    global hor, vert
    trt.speed(5)

    #Creating the grid with vertical lines
    hor = 0
    trt.penup()
    trt.goto(-300, 300)
    trt.pendown()

    while hor < 15:
        trt.right(90)
        trt.forward(600)
        trt.left(90)
        trt.penup()
        trt.goto(trt.xcor() + 40, 300)  #Move 40 pixels to the right
        trt.pendown()
        hor += 1

    #Reset position to start drawing horizontal lines
    trt.penup()
    trt.goto(-300, 300)
    trt.pendown()

    #Creating horizontal lines on the grid
    vert = 0
    while vert < 15:
        trt.forward(600)  #Draw a horizontal line
        trt.penup()
        trt.goto(-300, trt.ycor() - 40)  #Move 40 pixels down
        trt.pendown()
        vert += 1

#Runs a check to see if the snake is hitting the wall
def barrier():
    if trt.xcor() < -300 or trt.xcor() > 300 or trt.ycor() < -300 or trt.ycor() > 300:
        return False
    else:
        return True

#Runs a check to see if the snake is hitting itself
def self_collision():
    for segment in snake_segments:
        if trt.distance(segment) < 20:  #Adjust threshold for collision
            return True
    return False

def grow():
    #Create a new segment and add it to the snake's body
    segment = turt.Turtle('square')
    segment.penup()
    snake_segments.append(segment)  #Add segment to the list
    if length > 0:
        #Position the new segment behind the last one
        if len(snake_segments) > 1:
            last_segment = snake_segments[-2] 
        else:
            trt
    segment.goto(last_segment.position())

#Moves the snake forward and checks if it's within bounds
def move_snake():
    global length  #Make length global to modify it
    trt.speed(0)
    trt.penup()
    if barrier() and not self_collision():  #Check for wall collision and self-collision
        #Move the last segment to the position of the previous segment
        for i in range(len(snake_segments) - 1, 0, -1):
            x = snake_segments[i - 1].xcor()
            y = snake_segments[i - 1].ycor()
            snake_segments[i].goto(x, y)

        if len(snake_segments) > 0:
            snake_segments[0].goto(trt.position())  #Move the first segment to the snake's head

        trt.forward(40)
        screen.update()  #Update the screen after movement
        screen.ontimer(move_snake, 200)  #Continue movement every 200 ms
    else:
        print("Game Over")

    #Check if the snake eats the fruit
    if trt.distance(fruit_position) < 20:  #Adjust threshold for "eating" the fruit
        length += 1
        grow()  #Add a new segment to the snake
        fruit()  #Generate a new fruit

#These functions set the turtle's heading direction
def go_right():
    trt.setheading(0)

def go_up():
    trt.setheading(90)

def go_left():
    trt.setheading(180)

def go_down():
    trt.setheading(270)

#Binding WASD to movement
screen.onkey(go_right, 'd')
screen.onkey(go_up, 'w')
screen.onkey(go_left, 'a')
screen.onkey(go_down, 's')
screen.listen()

make_grid()

trt.penup()

#Start the turtle (snake) at the center of the screen (aligned with the grid)
trt.goto(0, 0)
trt.pendown()

fruit()  #Generate the first fruit
move_snake()

turt.mainloop()  #Keeps the window open
