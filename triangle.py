import turtle
turtle.shape("arrow")
turtle.color("red")

def make_triangle(edge):
    turtle.penup()
    turtle.forward(-edge/2)
    turtle.pendown()
    turtle.forward(edge)
    turtle.left(120)
    turtle.forward(edge)
    turtle.left(120)
    turtle.forward(edge)

make_triangle(100)
print("so triangle, such interesting, wow")
input("press enter to exit")
