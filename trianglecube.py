# cube illusion with triangles

import turtle
import math

t = turtle.Turtle()
t.speed(0)


def draw_triangle(counts,dir,turt):

    # first height
    fh = 10;
    mv = 10/ math.sin(30)
    change = mv + 10
    side = fh / math.sin(60)


    for i in range(1,counts+1):
        for j in range(1,4):
            turt.forward(side)
            turt.left(120)
        turt.sety(i*mv)
        side = (fh + (change*i))/math.sin(60)


# def draw_triangle(counts,dir,turt):
#
#     change = 20
#     turt.sety(change/2)
#     height = 0
#     side = height/ math.sin((60))
#     print(side)
#
#     for i in range(counts):
#         turt.sety(-height/2)
#         height += change
#         side = (height) / math.sin(math.degrees(60))
#         for j in range(1,4):
#             turt.forward(side)
#             turt.left(120)


t.left(60)
draw_triangle(5,"down",t)

turtle.exitonclick()
