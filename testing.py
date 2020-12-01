import turtle


t1 = turtle.Turtle()
t2 = turtle.Turtle()

ts = turtle.getscreen()
t1.speed(0)
ts.colormode(255)

t1.color(3, 252, 186)
t2.color(65, 3, 252)


len = 100
count = 0

while True:
    count += 1
    t1.size(count*5)
    t1.forward(100 - count)
    t1.left(72 - count)

turtle.exitonclick()
