# flower made with dots of increasing sizes

import turtle
import math


t = turtle.Turtle()
t.speed(0)

sides = 30
turn_angle = 360/30


in_radius = 20 #initial radius of first circle


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
        t.width(0.23*j)
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





def draw_triangle(counts,dir,turt):
    each_move = 10
    height = math.sqrt((10**2)-(5**2))
    print(height)

    for i in range(1,counts+1):
        turt.sety(height)
        x = i * (10)
        for j in range(1,4):
            turt.forward(x)
            turt.left(120)
        # turt.sety(yval)


def draw_triangle(counts,dir,turt):

    change = 20
    turt.sety(change/2)
    height = 0
    side = height/ math.sin((120))
    print(side)

    for i in range(counts):
        turt.sety(-height/2)
        height += change
        side = (height) / math.sin(math.degrees(120))
        for j in range(1,4):
            turt.forward(side)
            turt.left(120)

turtle.exitonclick()
