# CB 1st Race Turtles
import random
import turtle

wn = turtle.Screen()
turtle.title = ("Turtle Racing")
turtle.bgcolor = ("red")

line_drawer = turtle.Turtle()
line_drawer.hideturtle()
line_drawer.color("black")
line_drawer.speed(10)
line_drawer.penup()
line_drawer.goto(200,500)
line_drawer.pendown()
line_drawer.pensize(5)
line_drawer.goto(200,-500)

wn.tracer(0)

green = turtle.Turtle()
green.color("green")
green.shape("turtle")
green.penup()
green.goto(0,200)

red = turtle.Turtle()
red.color("red")
red.shape("turtle")
red.penup()
red.goto(0,400)

purple = turtle.Turtle()
purple.color("purple")
purple.shape("turtle")
purple.penup()
purple.goto(0,600)

orange = turtle.Turtle()
orange.color("orange")
orange.shape("turtle")
orange.penup()
orange.goto(0,800)

blue = turtle.Turtle()
blue.color("orange")
blue.shape("turtle")
blue.penup()
blue.goto(0,1000)

wn.update()
wn.tracer(1)

turtle.done()