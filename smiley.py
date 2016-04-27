import turtle
turtle.shape("arrow")
turtle.color("green")
turtle.home()

def make_smiley(size, mood):
    turtle.penup()
    turtle.right(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.pendown()
    turtle.circle(size)
    turtle.penup()
    turtle.forward(-size/3)
    turtle.left(90)
    turtle.forward(size)
    turtle.pendown()
    turtle.forward(size/2)
    turtle.penup()
    turtle.right(90)
    turtle.forward(size/1.5)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(size/2)
    turtle.penup()
    turtle.forward(size/2)
    turtle.right(90)
    turtle.pendown()
    if mood=="happy":
        turtle.right(90)
        turtle.circle(size/3, -180)
    elif mood=="meh":
        turtle.forward(size/1.5)
    elif mood=="sad":
        turtle.right(90)
        turtle.circle(size/3, 180)
    else:
        print("what mood are we in today?")

make_smiley(200, "happy")

input("press enter to exit")
