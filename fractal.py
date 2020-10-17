# fractal with python turtle .
#stack every layer then fill them up


import turtle

ts = turtle.getscreen()
ts.colormode(255)

t = turtle.Turtle()
t.speed(5)
t.left(90)

#some variables
length = 80
stack = []


class branch:
    def __init__(self,length):
        self.length = length
    def show(self):
        print(self.length)
        t.forward(self.length)
    def revert(self):
        t.up()
        t.backward(self.length)
        t.down()
    def brancher():
        rb = branch(self.length/6)
        lb = branch(self.length/6)


root = branch(length)
root.show()
turtle.exitonclick()
