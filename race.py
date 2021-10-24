from turtle import *
from random import randint

t0 = Turtle()
t0.color('black')
t0.pensize(5)
t0.pu()
t0.goto(-100,300)
t0.write("Turtle race",font=("Verdona",15,"normal"))
t0.pu()
t0.goto(-200,200)
t0.pd()
t0.fd(400)
t0.right(90)
t0.fd(300)
t0.shape('classic')

t1 = t0.clone()
t2 = t0.clone()
t1.color('red')
t2.color('blue')

t1.pu()
t1.goto(-200,200)
t1.pd()

t2.pu()
t2.goto(-200,200)
t2.pd()

t1.lt(90)
t2.lt(90)

# confusing point
r_s = 0
b_s = 0
x = 0
y = 0

xlist = []
ylist = []

while True:
    r_r = randint(70,90)
    b_r = randint(70,90)
    xlist.append(r_r)
    ylist.append(b_r)

    r_s += r_r
    b_s += b_r

    if r_s >= 400 and x == 0:
        x += 90
        t1.fd(400-(r_s-r_r))
        t1.rt(x)
        t1.fd(r_s - 400)
    else:
        t1.fd(r_r)
    
    if b_s >= 400 and y == 0:
        y += 90
        t2.fd(400-(b_s-b_r))
        t2.rt(y)
        t2.fd(b_s - 400)
    else:
        t2.fd(b_r)
    
    if r_s >= 700 or b_s >= 700:
        if r_s >= b_s:
            t2.ht()
            t1.pu()
            t1.goto(0,300)
            t1.pd()
            t1.write("t1 is win")
            t1.ht()
            break
        elif b_s >= r_s:
            t1.ht()
            t2.pu()
            t2.goto(0,300)
            t2.pd()
            t2.write("t2 is win")
            t2.ht()
            break
        else:
            t1.ht()
            t2.ht()
            t1.home()
            t1.write("draw")
            break

def drawGraph(t,list):

    for y in list:
        t.lt(90)
        t.fd(y)
        t.rt(90)
        t.write(y)
        t.fd(30)
        t.rt(90)
        t.fd(y)
        t.rt(90)
        t.fd(30)
        t.rt(180)
        t.fd(40)

t3 = t1.clone()
t3.pu()
t3.goto(-250,-250)
t3.pd()
t3.lt(90)
drawGraph(t3,xlist)

exitonclick()