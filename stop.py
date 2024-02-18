# Draw a stop sign by AlyBytes
import turtle

# turtle.shape("turtle")  # optional
turtle.speed(1) # optional
turtle.color('blue')
turtle.pensize(5)

def backwards_move(distance):
    turtle.penup()
    turtle.back(distance)
    turtle.pendown()

def rectangle_turtle(wide, high):
    for i in range(2):
        turtle.forward(wide)
        turtle.right(90)
        turtle.forward(high)
        turtle.right(90)

def octagon_turtle(side):
    for i in range(8):
        turtle.forward(side)
        turtle.left(45)

def stop_sign(side):
    octagon_turtle(side)
    turtle.forward(3/8*side)
    rectangle_turtle(1/5*side, 2*side)

# stop_sign(100)

side = 50

for i in range(3):
    stop_sign(side)
    backwards_move(200)
    turtle.color('green')
    side += 25

turtle.Screen().exitonclick()
