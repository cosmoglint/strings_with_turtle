# flower made with dots of increasing sizes

import turtle
import math

ts = turtle.getscreen()

ts.colormode(255)

t = turtle.Turtle()
t.speed(0)

sides = 30
turn_angle = 360/sides


in_radius = 60 #initial radius of first circle


def slen_rad(radius):
    side_len = radius * 2 * (math.sin(math.radians(180)/sides))
    return side_len


side_length = slen_rad(in_radius)   #side length of first circle


each_side = side_length

for i in range(1,10):
    t.width(i)
    radius = in_radius + i*20
    each_side = slen_rad(radius)
    t.up()
    t.sety(radius*(-1))
    t.setx(-each_side/2)
    for j in range(sides):
        if (i%2==0):
            t.up()
            t.forward(each_side)
            t.left(turn_angle)
            t.down()
            t.dot()
        else:
            t.up()
            t.forward(each_side/2)
            t.down()
            t.dot()
            t.up()
            t.forward(each_side/2)
            t.left(turn_angle)
            t.down()


turtle.exitonclick()
