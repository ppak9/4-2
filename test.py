from turtle import *

# flower ver 1
t = Turtle()
t.speed(0)
l = 50

def drawsquare(t,l):
    for _ in range(4):
        t.fd(l)
        t.rt(90)

def drawFlower1(t):
    t.lt(18)
    drawsquare(t,50)

def drawFlower2(t):
    for i in  range(200):
        t.color('pink')
        t.begin_fill()
        t.fd(i)
        t.lt(110)
        t.end_fill()

def test(t):
    t.color('green')
    for _ in range(2):
        for i in range(9):
            t.fd(15)
            t.lt(10)
        t.lt(90)
t.rt(10)
test(t)
t.lt(120)
test(t)
t.rt(20)
t.fd(100)
print(t.pos())
t.pu()
t.goto(100,200)
t.pd()
t.circle(100)
for i in range(12):
    for _ in range(2):
        t.fd(38)
        t.rt(120)
    t.rt(180)
    t.rt(30)

    
# t.pensize(5)
# t.rt(20)
# t.circle(100)
# t.rt(20)
# t.fd(160)
exitonclick()
