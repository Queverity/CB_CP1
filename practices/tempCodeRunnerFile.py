for i in range(1,6):
        maze_drawer.penup()
        drawer_y_value -= 100
        maze_drawer.goto(-300,drawer_y_value)

        for a in row_grid[i]:
            if a == 0:
                maze_drawer.penup()
                maze_drawer.forward(100)
            elif a == 1:
                maze_drawer.pendown()
                maze_drawer.forward(100)