# CB 1st Maze Generator

import turtle as t
import random as ran

def walls():
    wall_drawer = t.Turtle()
    wall_drawer.hideturtle()


def initalize():
    wn = t.Screen()
    wn.bgcolor("lightblue")
    wn.title("Maze Generator")
    wn.setup(width=1000, height=1000)


initalize()
t.done()

