# I experimented with line lengths and variable lengths


import turtle
import math
import random

turtle.bgcolor('black')

ts = turtle.getscreen()
ts.colormode(255)


t = turtle.Turtle()
t.speed(0)
t.width(3)
t.color(200,255,255)


def variable_line(length,initial_width,final_width,t):
    width_diff = final_width - initial_width
    each_increment = width_diff/length
    for i in range(1,length+1):
        t.width(each_increment*i)
        t.forward(1)


def slen_rad(radius):
    side_len = radius * 2 * (math.sin(math.radians(180)/sides))
    return side_len



sides = 120
turn_angle = 360/sides


in_radius = 120 #initial radius of first circle

side_length = slen_rad(in_radius)

t.up()
t.sety(-in_radius/2)
t.down()

t.width(5)
t.circle(in_radius)

t.width(3)

for i in range(sides):
    t.forward(side_length)
    t.right(90)
    mval = random.randrange(30,120)
    t.color(mval,255,255)
    t.forward(mval)
    t.up()
    t.backward(mval)
    t.left(90)
    t.left(turn_angle)
    t.down()

turtle.exitonclick()
