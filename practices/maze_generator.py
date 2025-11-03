# CB 1st Maze Generator

import turtle as t
import random as ran

row_grid = []
col_grid = []

def is_solvable(row_grid,col_grid):
    pass

def draw_walls():
    wall_drawer = t.Turtle()
    wall_drawer.color("black")
    wall_drawer.speed(10)
    wall_drawer.hideturtle()
    wall_drawer.penup()
    wall_drawer.goto(300,300)
    wall_drawer.pendown()
    wall_drawer.goto(300,-300)
    wall_drawer.goto(33,-300)
    wall_drawer.penup()
    wall_drawer.goto(0,-300)
    wall_drawer.pendown()
    wall_drawer.goto(-300,-300)
    wall_drawer.goto(-300,300)
    wall_drawer.goto(0,300)
    wall_drawer.penup()
    wall_drawer.goto(33,300)
    wall_drawer.pendown()
    wall_drawer.goto(300,300)

def generate_maze(row_grid,col_grid):
    for _ in range(1,6):
        rand_col = ran.randint(1,3)
        rand_row = ran.randint(1,3)
        if rand_col == 1:
            col_grid.append(" ")
        elif rand_col == 2:
            col_grid.append("_")
        elif rand_col == 3:
            col_grid.append("|")

        if rand_row == 1:
            row_grid.append(" ")
        elif rand_col == 2:
            row_grid.append("_")
        elif rand_col == 3:
            row_grid.append("|")
    maze_drawer = t.Turtle()
    maze_drawer.hideturtle()
    maze_drawer.color("black")

    for i in row_grid:
        if i == " ":
            maze_drawer.penup()
            



def initalize_screen():
    wn = t.Screen()
    wn.bgcolor("lightblue")
    wn.title("Maze Generator")
    wn.setup(width=1000, height=1000)


initalize_screen()
draw_walls()
t.done()

