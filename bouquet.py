from turtle import *

t = Turtle()
t.speed(0)
t.ht()

def drawlips(t):
    for _ in range(2):
        for _ in range(9):
            t.fd(10)
            t.rt(10)
        t.rt(90)

def drawFlower(x,y):
    t.pu()
    t.goto(x,y)
    t.pd()
    for _ in range(6):
        t.lt(60)
        t.color('yellow')
        t.begin_fill()
        drawlips(t)
        t.end_fill()

    # t.pu()
    t.goto(x,y-15)
    # t.pd()
    t.color('red')
    t.begin_fill()
    t.circle(15)
    t.end_fill()

def drawCup(t,l,a):
    t.fd(l)
    t.rt(a)
    t.fd(l)
    t.rt(a)
    t.fd(l)

xcor = [50,0,-50]
ycor = [50,100,50]
drawFlower(0,0)
for i in range(3):
    drawFlower(xcor[i],ycor[i]) 
t.pu()
t.goto(-100,0)
t.pd()
print(t.pos())
t.color('green')
t.begin_fill()
drawCup(t,200,120)
t.end_fill()

exitonclick()