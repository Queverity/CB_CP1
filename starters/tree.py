# CB 1st 11/21 Starter

# Import turtle module
import turtle as t

# function for drawing branch
def draw_branch(length):
    if length > 5:
        for i in range(3):
            turtle.forward(length)
            draw_branch(length/3)
            turtle.backward(length)
            turtle.right(10)

turtle = t.Turtle()
turtle.speed(0)
turtle.color("lightblue")
turtle.pensize(10)
turtle.goto(0,0)

for i in range(6):
    draw_branch(100)
    t.right(60)

turtle.hideturtle()

t.done()