# Turtles by AlyBytes
# The first & last lines should be in every turtle program you write.

import turtle


# side = int(input("how big is your square's side? "))
# wide = int(input("how wide is your rectangle? "))
# high = int(input("how high is your rectangle? "))
# distance = int(input("how far apart do you want next square to be? "))


def backwards_move(distance):
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
        turtle.right(90)


def rectangle_turtle(wide, high):
    for i in range(2):
        turtle.forward(wide)
        turtle.left(90)
        turtle.forward(high)
        turtle.left(90)

#side = 50
#for i in range(2):
def house(side):
    square_turtle(side)
    triangle_turtle(side)
    # backwards_move(150)
    # side += 55
    # turtle.color('red')

def main():
# turtle.shape("turtle")  # optional
    turtle.speed(1) # optional
    turtle.color('blue')
    house(50)
    turtle.pensize(5)
    turtle.color("green")
    backwards_move(150)
    house(100)

main()

   # rectangle_turtle(110, 225)



turtle.Screen().exitonclick()
