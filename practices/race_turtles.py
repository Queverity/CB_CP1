# CB 1st Race Turtles
import random
import turtle

wn = turtle.Screen()
turtle.title = ("Turtle Racing")
turtle.bgcolor = ("red")

line_drawer = turtle.Turtle()
line_drawer.hideturtle()
line_drawer.speed(10)
line_drawer.penup()
line_drawer.goto(100,50)
line_drawer.pendown()
line_drawer.goto(100,150)

turtle.done()