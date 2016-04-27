import turtle
turtle.shape("turtle")
turtle.color("blue")
turtle.home

def make_rec(width, height):
    turtle.penup()
    turtle.forward(-width/2)
    turtle.pendown()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)

make_rec(200, 100)
input("press enter to exit")
