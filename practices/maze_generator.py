# CB 1st Maze Generator




# Importing important libaries
import turtle as t
import random as ran

# Setting lists for the columns and rows of the maze
row_grid = [[],[],[],[],[],[]]
col_grid = [[],[],[],[],[],[]]

# list for random wall generator to pick from
wall_list = [0,1]


# create turtle for drawing the mzze
maze_drawer = t.Turtle()
# hide maze drawing turtle
maze_drawer.hideturtle()
# set maze pensize to 2
maze_drawer.pensize(2)
# set maze pen color to black
maze_drawer.color("black")
# set medium speed
maze_drawer.speed(5)
# set x and y values for the the drawer to start
drawer_y_value = 300
drawer_x_value = -300

# make it so the turtle won't draw when moving
maze_drawer.penup()

# send turtle to preset x and y coords
maze_drawer.goto(drawer_x_value,drawer_y_value)

# create lightblue screen titled "Maze Generator" that is 1000x1000 pixels wide
wn = t.Screen()
wn.bgcolor("lightblue")
wn.title("Maze Generator")
wn.setup(width=1000, height=1000)


def solvable(row_grid, col_grid):
    size = len(row_grid) - 1
    visited = set()
    stack = [(0, 0)]

    while stack:
        x, y = stack.pop()
        if x == size - 1 and y == size - 1:  # Reached the bottom-right corner
            return True
        
        if (x, y) in visited:
            continue

        visited.add((x, y))
        
        # Move right (check col_grid for wall)
        if x < size - 1 and col_grid[y][x] == 0:
            stack.append((x + 1, y))
        
        # Move down (check row_grid for wall)
        if y < size - 1 and row_grid[y][x] == 0:
            stack.append((x, y + 1))

        # Move left (check col_grid for wall)
        if x > 0 and col_grid[y][x - 1] == 0:
            stack.append((x - 1, y))

        # Move up (check row_grid for wall)
        if y > 0 and row_grid[y - 1][x] == 0:
            stack.append((x, y - 1))

    return False


# function to draw outer maze walls
def draw_walls(wn):
    # make it so screen won't update until told to
    wn.tracer(0)
    # setup wall drawing turtle
    wall_drawer = t.Turtle()
    wall_drawer.color("black")
    wall_drawer.speed(5)
    wall_drawer.pensize(2)
    wall_drawer.hideturtle()

    # make turtle draw a 600x600 pixel square with 100 pixel wide entrance and exit and the top right and bottom left respectively 
    wall_drawer.penup()
    wall_drawer.goto(300,300)
    wall_drawer.pendown()
    wall_drawer.goto(300,-300)
    wall_drawer.goto(-200,-300)
    wall_drawer.penup()
    wall_drawer.goto(-300,-300)
    wall_drawer.pendown()
    wall_drawer.goto(-300,300)
    wall_drawer.goto(200,300)
    wall_drawer.penup()
    wall_drawer.goto(300,300)

    # update screen
    wn.update()

    # make it so screen updates automatically again
    wn.tracer(1)
    

# function for generating the maze
def generate_maze(row_grid,col_grid,maze_drawer,drawer_y_value,drawer_x_value,wall_list):
   
    # for loops to generate either a 1 or 0 and add that to either the row_grid list or col_grid list. These numbers tell if there will be a wall or not (1 being a wall, 0 being no wall)
    for i in range(0,6):
        for _ in range(0,6):
            random_gen = ran.choice(wall_list)
            row_grid[i].append(random_gen)
    for i in range(0,6):
        for _ in range(0,6):
            random_gen = ran.choice(wall_list)
            col_grid[i].append(random_gen)


    # This for loop first subtracts 100 (width of maze path) from the maze drawer y value to have it go down, then sets its location to -300 x, drawer_y_value. After that, a for loop will go through each list in row_grid, and have the maze_drawer make a 100 pixel wide wall (to the right) if the for loop goes over a 1, and have no wall drawn if it is 0.   
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

    # turn maze_drawer 90 degree to make it face down
    maze_drawer.right(90)

        # This for loop first adds 100 (width of maze path) from the maze drawer x value to have it go forward, then sets its location to drawer_x_value, 300. After that, a for loop will go through each list in row_grid, and have the maze_drawer make a 100 pixel wide wall (downwards) if the for loop goes over a 1, and have no wall drawn if it is 0.
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

    



# draw outer maze walls
draw_walls(wn)

# while loop to run until a solvable maze is generated
while True:
    # make it so the screen won't update until told so
    wn.tracer(0)  
    # generate maze
    generate_maze(row_grid,col_grid,maze_drawer,drawer_y_value,drawer_x_value,wall_list)
    # check if maze is solvable
    solved = solvable(row_grid,col_grid)
    # if the maze is solvable
    if solved == True:
        # update screen and make it update automatically, then break the loop
        wn.update()
        wn.tracer(1)
        break
    else:
        # reset drawer y and x values, clear everything it has drawn, reset drawer direction, send drawer to original placement, and clear row_grid and col_grid lists, then continue.
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

# make it so the screen will not close out until clicked on
t.done()

