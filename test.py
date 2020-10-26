# flower made with dots of increasing sizes

import turtle
import math


t = turtle.Turtle()
t.speed(0)

sides = 30
turn_angle = 360/30

side_length = 10   #side length of first circle
each_side = side_length


def radii(side):
    global sides
    radius = side/(2*math.sin(math.radians(180)/sides))
    return radius
print(radii(10))

for i in range(1,4):
    t.up()
    t.goto( t.pos() + (0,-radii(each_side)) )
    each_side = side_length*i
    for j in range(sides):
        if j==0:
            t.up()
            t.left(turn_angle)
            t.forward(each_side/2 if (i%2==0) else -each_side/2)
            t.down()
        t.up()
        t.left(turn_angle)
        t.forward(each_side)
        t.down()
        t.dot()
    t.up()
    t.goto( t.pos() + (0,radii(each_side)) )


turtle.exitonclick()
