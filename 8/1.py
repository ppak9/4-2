from turtle import Turtle as t, Screen as s, exitonclick, onscreenclick

t1 = t()
t1.speed(0)
t1.color('red')
t1.ht()

def petal():
    for _ in range(2):
        t1.circle(30,110)
        t1.left(70)

def drawFlower(x,y):
    t1.pu()
    t1.goto(x,y)
    t1.pd()
    t1.begin_fill()
    for _ in range(6):
        petal()
        t1.lt(60)
    t1.end_fill()

    t1.color('green')
    t1.begin_fill()
    t1.pu()
    t1.goto(x,y-10)
    t1.pd()
    t1.circle(10)
    t1.end_fill()
    t1.color('red')

onscreenclick(drawFlower)
