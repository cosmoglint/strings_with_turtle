# we need a square boundary
import turtle

t = turtle.Turtle()

st = turtle.Turtle()
dt = turtle.Turtle()

dt.speed(0)
st.speed(0)
t.speed(0)

diagonal_length = 400
half_diagonal_length = diagonal_length/2
side_length = diagonal_length/(2**(1/2))

rotations = 180
turn_angle = 1

for i in range(rotations//turn_angle):
    t.forward(half_diagonal_length)
    t.up()
    t.backward(half_diagonal_length)
    t.down()
    t.backward(half_diagonal_length)
    t.up()
    t.forward(half_diagonal_length)
    t.down()
    t.left(turn_angle)

#side turtle

st.up()
st.backward(side_length/2)
st.right(90)
st.forward(side_length/2)
st.left(90)
st.down()
for i in range(4):
    st.forward(side_length)
    st.left(90)

# direction turtle

small_len = side_length/90
turner = turn_angle

dt.up()
dt.backward(side_length/2)
dt.right(90)
dt.forward(side_length/2)
dt.left(90)
dt.down()

# for i in range(90):
#     turner += turn_angle
#     dt.left(turner)
#     dt.forward(diagonal_length)
#     dt.up()
#     dt.backward(diagonal_length)
#     dt.right(turner)
#     dt.forward(small_len)
#     dt.down()

for i in range(int(side_length),0,-1):
    dt.forward(i)
    dt.left(90)
    dt.forward(i)
    dt.left(90)
    dt.left(turn_angle)


turtle.exitonclick()
