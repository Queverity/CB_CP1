# CB 1st Race Turtles
import random
import time
import turtle

global green
global red
global purple
global orange
global blue

writing = turtle.Turtle()
writing.hideturtle()
writing.penup()
writing.goto(500,500)
writing.pendown()
writing.pencolor("black")
writing.pensize(2)
global game
game = True



wn = turtle.Screen()
turtle.title = ("Turtle Racing")
turtle.bgcolor = ("red")

turtles = ["green","red","purple","orange","blue"]

def win_condition():
    global green
    global red
    global purple
    global orange
    global blue
    global game
    wn.tracer(0)

    if green.xcor() > 184:
        game = False
        writing.write("Green Wins!",font=("Arial", 50, "bold"))
    
    elif red.xcor() > 184:
        game = False
        writing.write("Red Wins!",font=("Arial", 50, "bold"))
    
    elif purple.xcor() > 184:
        game = False
        writing.write("Purple Wins!",font=("Arial", 50, "bold"))
    
    elif orange.xcor() > 184:
        game = False
        writing.write("Orange Wins!",font=("Arial", 50, "bold"))
    
    elif blue.xcor() > 184:
        game = False
        writing.write("Blue Wins!",font=("Arial", 50, "bold"))

    wn.update()
    wn.tracer(1)

def turtle_movement():
    global green
    global red
    global purple
    global orange
    global blue
    global game

    while game == True:
        green.forward(random.randint(1,10))

        red.forward(random.randint(1,10))

        purple.forward(random.randint(1,10))

        orange.forward(random.randint(1,10))

        blue.forward(random.randint(1,10))
        
        win_condition()
    

def intialize():
    wn.tracer(0)

    global green
    global red
    global purple
    global orange
    global blue


    line_drawer = turtle.Turtle()
    line_drawer.hideturtle()
    line_drawer.color("black")
    line_drawer.speed(10)
    line_drawer.penup()
    line_drawer.goto(200,650)
    line_drawer.pendown()
    line_drawer.pensize(2)
    line_drawer.goto(200,-650)

    green = turtle.Turtle()
    green.color("green")
    green.shape("turtle")
    green.penup()
    green.goto(-500,500)
    green.pendown()
    green.pencolor("green")

    red = turtle.Turtle()
    red.color("red")
    red.shape("turtle")
    red.penup()
    red.goto(-500,250)
    red.pendown()
    red.pencolor("red")

    purple = turtle.Turtle()
    purple.color("purple")
    purple.shape("turtle")
    purple.penup()
    purple.goto(-500,0)
    purple.pendown()
    purple.pencolor("purple")

    orange = turtle.Turtle()
    orange.color("orange")
    orange.shape("turtle")
    orange.penup()
    orange.goto(-500,-250)
    orange.pendown()
    orange.pencolor("orange")

    blue = turtle.Turtle()
    blue.color("blue")
    blue.shape("turtle")
    blue.penup()
    blue.goto(-500,-500)
    blue.pendown()
    blue.pencolor("blue")

    wn.update()
    wn.tracer(1)

    

intialize()
turtle_movement()

turtle.done()