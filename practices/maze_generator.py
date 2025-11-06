# CB 1st Maze Generator

import turtle as t
import random as ran

row_grid = [[],[],[],[],[],[]]
col_grid = [[],[],[],[],[],[]]
wall_list = [0,1]

maze_drawer = t.Turtle()
maze_drawer.hideturtle()
maze_drawer.pensize(2)
maze_drawer.color("black")
maze_drawer.speed(5)
drawer_y_value = 300
drawer_x_value = -300
maze_drawer.penup()
maze_drawer.goto(drawer_x_value,drawer_y_value)

wn = t.Screen()
wn.bgcolor("lightblue")
wn.title("Maze Generator")
wn.setup(width=1000, height=1000)

def solvable(row_grid, col_grid):

    size = len(row_grid) - 1
    visited = set()
    stack = [(2,0)]

    while stack:
        x, y = stack.pop()
        if x == size - 1 and y == size - 1:
            return True
        
        if (x,y) in visited:
            continue

        visited.add((x,y))

        if x < size - 1 and col_grid[y][x+1] == 0:
            stack.append((x+1,y))

        if y < size - 1 and row_grid[y+1][x] == 0:
            stack.append((x,y+1))

        if x > 0 and col_grid[y][x] == 0:
            stack.append((x-1, y))

        if y > 0 and row_grid[y][x] == 0:
            stack.append((x,y-1))

    return False


def draw_walls(wn):
    wn.tracer(0)
    wall_drawer = t.Turtle()
    wall_drawer.color("black")
    wall_drawer.speed(5)
    wall_drawer.pensize(2)
    wall_drawer.hideturtle()
    wall_drawer.penup()
    wall_drawer.goto(300,300)
    wall_drawer.pendown()
    wall_drawer.goto(300,-300)
    wall_drawer.goto(100,-300)
    wall_drawer.penup()
    wall_drawer.goto(0,-300)
    wall_drawer.pendown()
    wall_drawer.goto(-300,-300)
    wall_drawer.goto(-300,300)
    wall_drawer.goto(0,300)
    wall_drawer.penup()
    wall_drawer.goto(100,300)
    wall_drawer.pendown()
    wall_drawer.goto(300,300)
    wn.update()
    wn.tracer(1)
    

def generate_maze(row_grid,col_grid,maze_drawer,drawer_y_value,drawer_x_value,wall_list):
   
    
    for i in range(0,6):
        for _ in range(0,6):
            random_gen = ran.choice(wall_list)
            row_grid[i].append(random_gen)
    for i in range(0,6):
        for _ in range(0,6):
            random_gen = ran.choice(wall_list)
            col_grid[i].append(random_gen)
        
    for b in range(0,5):
        maze_drawer.penup()
        drawer_y_value -= 100
        maze_drawer.goto(-300,drawer_y_value)

        for a in row_grid[b]:
            if a == 0:
                maze_drawer.penup()
                maze_drawer.forward(100)
            elif a == 1:
                maze_drawer.pendown()
                maze_drawer.forward(100)

    maze_drawer.right(90)


    for c in range(0,5):
        maze_drawer.penup()
        drawer_x_value += 100
        maze_drawer.goto(drawer_x_value,300)
        
        for a in col_grid[c]:
            if a == 0:
                maze_drawer.penup()
                maze_drawer.forward(100)
            elif a == 1:
                maze_drawer.pendown()
                maze_drawer.forward(100)

    



draw_walls(wn)
while True:
    wn.tracer(0)  
    generate_maze(row_grid,col_grid,maze_drawer,drawer_y_value,drawer_x_value,wall_list)
    solved = solvable(row_grid,col_grid)
    if solved == True:
        wn.update()
        wn.tracer(1)
        break
    else:
        maze_drawer.clear()
        drawer_y_value = 300
        drawer_x_value = -300
        maze_drawer.penup()
        maze_drawer.goto(drawer_x_value,drawer_y_value)
        maze_drawer.left(90)
        for i in range(0,6):
            row_grid[i].clear()
        for i in range(0,6):
            col_grid[i].clear()
        continue
t.done()

