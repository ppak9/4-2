from turtle import *


def drawlips(t):
    for _ in range(2):
        for _ in range(9):
            t.fd(15)
            t.rt(10)
        t.rt(90)

t = Turtle()
t.speed(0)
for _ in range(6):
    t.lt(60)
    t.color('yellow')
    t.begin_fill()
    drawlips(t)
    t.end_fill()

# t.pu()
t.goto(0,-15)
# t.pd()
t.color('red')
t.begin_fill()
t.circle(15)
t.end_fill()
exitonclick()