# turtle house by AlyBytes

import turtle

# turtle.shape("turtle")  # optional
turtle.speed(1)  # optional
turtle.color('blue')
turtle.pensize(5)


def backwards_move(distance):
    turtle.penup()
    turtle.right(90)
    turtle.back(distance)
    turtle.right(270)
    turtle.pendown()

def back_move(distance):
    turtle.penup()
    turtle.back(distance)
    turtle.pendown()

def triangle_turtle(side):
    for i in range(3):
        turtle.forward(side)
        turtle.left(120)


def square_turtle(side):
    for i in range(4):
        turtle.forward(side)
        turtle.left(90)


len = 100
for i in range(2):
    square_turtle(len)
    backwards_move(len)
    triangle_turtle(len)
    back_move(200)
    turtle.color("red")
    len += 50

turtle.Screen().exitonclick()
