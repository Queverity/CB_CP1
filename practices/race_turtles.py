# CB 1st Race Turtles

# importing all required libaries
import random
import turtle

# setting variable names before setting their value
global green
global red
global purple
global orange
global blue

# creating a turtle to make text on the screen
writing = turtle.Turtle()

# makes the turtle invisible
writing.hideturtle()

# makes it so the turtles won't draw when moving
writing.penup()

# setting turtle location
writing.goto(500,500)

# making it so the turtle can write again
writing.pendown()

# setting pen color and size
writing.pencolor("black")
writing.pensize(2)

# variable for running the game loop
global game
game = True


# initalizing game window
wn = turtle.Screen()
wn.title("Turtle Racing")
wn.bgcolor("pink")

# function to check for win
def win_condition():

    # calling variables
    global green
    global red
    global purple
    global orange
    global blue
    global game

    # this makes it so the window does not update until told so
    wn.tracer(0)

    # checks if the x-cord of a turtle overlaps the finish line
    # if it does, the game loop will stop running (the turtles stop moving), and print "(Color) Wins!" onto the window
    if green.xcor() > 165:
        game = False
        writing.write("Green Wins!",font=("Arial", 50, "bold"))
    
    elif red.xcor() > 165:
        game = False
        writing.write("Red Wins!",font=("Arial", 50, "bold"))
    
    elif purple.xcor() > 165:
        game = False
        writing.write("Purple Wins!",font=("Arial", 50, "bold"))
    
    elif orange.xcor() > 165:
        game = False
        writing.write("Orange Wins!",font=("Arial", 50, "bold"))
    
    elif blue.xcor() > 165:
        game = False
        writing.write("Blue Wins!",font=("Arial", 50, "bold"))

    # update the screen with the writing
    wn.update()

    # make it so the screen updates automatically again
    wn.tracer(1)

# function to move the turtles forward
def turtle_movement():

    # call variables
    global green
    global red
    global purple
    global orange
    global blue
    global game


    # moves all turtles forward a random amount of steps between 1 and 10, then calls win condtition to see if any of them have crossed the finish line
    while game == True:
        green.forward(random.randint(1,10))

        red.forward(random.randint(1,10))

        purple.forward(random.randint(1,10))

        orange.forward(random.randint(1,10))

        blue.forward(random.randint(1,10))
        
        win_condition()
    

def intialize():

    # makes it so the screen doesn't update until told to
    wn.tracer(0)

    # call variables
    global green
    global red
    global purple
    global orange
    global blue


    # make turtle to draw line
    line_drawer = turtle.Turtle()

    # make turtle invisible
    line_drawer.hideturtle()

    # set turtle and pen color to black
    line_drawer.color("black")

    # set turtle speed to max
    line_drawer.speed(10)

    # make it so the turtle won't draw a line while moving
    line_drawer.penup()

    # set turtle to starting position
    line_drawer.goto(200,650)

    # make it so turtle can draw again
    line_drawer.pendown()

    # set pen size
    line_drawer.pensize(2)

    # make turtle draw line to end position
    line_drawer.goto(200,-650)


    # set up all the turtles by setting color, shape, position, and pen color. making sure to set penup before moving and then putting it back down after moving
    green = turtle.Turtle()
    green.color("green")
    green.shape("turtle")
    green.penup()
    green.goto(-500,500)
    green.pendown()
    green.pencolor("green")
    green.shapesize(stretch_wid=2, stretch_len=2, outline=1)

    red = turtle.Turtle()
    red.color("red")
    red.shape("turtle")
    red.penup()
    red.goto(-500,250)
    red.pendown()
    red.pencolor("red")
    red.shapesize(stretch_wid=2, stretch_len=2, outline=1)

    purple = turtle.Turtle()
    purple.color("purple")
    purple.shape("turtle")
    purple.penup()
    purple.goto(-500,0)
    purple.pendown()
    purple.pencolor("purple")
    purple.shapesize(stretch_wid=2, stretch_len=2, outline=1)

    orange = turtle.Turtle()
    orange.color("orange")
    orange.shape("turtle")
    orange.penup()
    orange.goto(-500,-250)
    orange.pendown()
    orange.pencolor("orange")
    orange.shapesize(stretch_wid=2, stretch_len=2, outline=1)

    blue = turtle.Turtle()
    blue.color("blue")
    blue.shape("turtle")
    blue.penup()
    blue.goto(-500,-500)
    blue.pendown()
    blue.pencolor("blue")
    blue.shapesize(stretch_wid=2, stretch_len=2, outline=1)

    # update the screen
    wn.update()

    # make it so the screen updates automatically again
    wn.tracer(1)

    

# call intialize function to set up turtles and finish line
intialize()

# start the turtle movement loop
turtle_movement()

# make it so the window won't close until X button is clicked
turtle.done()