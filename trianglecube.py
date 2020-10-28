# cube illusion with triangles

import turtle
import math

t = turtle.Turtle()
t.speed(0)


def up_triangle(counts,turt):
    change = 5
    side = 0
    print(math.tan(math.radians(30)))
    hyp = change/math.sin(math.radians(30))
    diff = change/math.tan(math.radians(30))
    for j in range(1,counts+1):
        turt.up()
        turt.goto(0,-hyp * j)
        side += diff*2
        turt.down()
        for i in range(1,4):
            turt.forward(side)
            turt.left(120)
    return (hyp*(counts+1),(10 * (counts+1)), side)

def down_triangle(counts,turt):
    change = 5
    side = 0
    hyp = change/math.sin(math.radians(30))
    diff = change/math.tan(math.radians(30))
    for j in range(1,counts+1):
        turt.up()
        turt.goto(0,-hyp * j)
        side += diff*2
        turt.down()
        for i in range(1,4):
            turt.forward(side)
            turt.left(120)


t.left(60)
sharp_height,blunt_height,side = up_triangle(10,t)

turtle.exitonclick()
