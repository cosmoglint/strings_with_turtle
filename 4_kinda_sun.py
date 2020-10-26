import turtle
import math


t = turtle.Turtle()

t.speed(0)

circle_radius = 200

chord_length = 2 * circle_radius * math.sin(math.pi/7)

print(chord_length)


tot_angles = 360

sides = 60
circle_angle = 360
side_length = 10

each_angle = tot_angles/sides
per_turn = each_angle * (sides//6)


for i in range(60):
    curang = per_turn
    t.left(each_angle)
    t.left(curang)
    t.forward(chord_length)
    t.up()
    t.backward(chord_length)
    t.down()
    t.right(curang)
    t.forward(side_length)


turtle.exitonclick()
