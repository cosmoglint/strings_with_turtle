# we need a square boundary
import turtle

t = turtle.Turtle()

t.speed(0.2)



for i in range(180):
    t.forward(200)
    t.up()
    t.backward(200)
    t.down()
    t.backward(200)
    t.up()
    t.forward(200)
    t.down()
    t.left(1)


turtle.exitonclick()
