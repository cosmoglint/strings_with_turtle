# cube illusion with triangles

import turtle
import math

t = turtle.Turtle()
t.speed(0)

change = 10
iterations = 10

maxsize = 6
minsize = 1.5
diffsize = (maxsize-minsize)/iterations

def up_triangle(counts,turt):
    global change
    turt.pensize(minsize)
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
    return (hyp*(counts),(change * (counts)), side)

def down_triangle(counts,turt):
    global change,diffsize
    side = 0
    curx,cury = turt.pos()
    hyp = change/math.sin(math.radians(30))
    diff = change/math.tan(math.radians(30))
    for j in range(1,counts+1):
        # t.pensize(1 + ((counts+2 - j)*0.1))
        t.pensize(diffsize * (counts + 2 - j) * minsize)
        turt.up()
        turt.goto(curx,cury + hyp * j)
        side += diff*2
        turt.down()
        for i in range(1,4):
            turt.forward(side)
            turt.left(120)


t.left(60)
for i in range(1,4):
    t.forward(5)
    t.left(120)

sharp_height,blunt_height,side = up_triangle(iterations,t)

t.up()
t.goto(t.pos()[0] + side/2, t.pos()[1] + blunt_height)
t.down()
t.left(180)
down_triangle(iterations,t)

t.up()
t.goto(t.pos()[0] - side/2, t.pos()[1] + blunt_height)
t.down()
down_triangle(iterations,t)

t.up()
t.goto(t.pos()[0] - side/2, t.pos()[1] - blunt_height - (sharp_height*2))
t.down()
down_triangle(iterations,t)

turtle.exitonclick()
