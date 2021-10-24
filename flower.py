from turtle import *

t = Turtle()
t.speed(0)
# def tri(t):
#     for _ in range(3):
#         t.fd(30)
#         t.rt(120)
t.pensize(7)
t.color('red')
t.circle(70)
t.rt(45)
t.pensize(5)
t.color('yellow')
for i in range(12):
    for i in range(2):
        t.fd(38)
        t.lt(360/3)
    t.lt(180)
    t.rt(30)
t.color('green')
t.rt(45)
t.fd(100)
t.lt(120)

for i in range(9):
    t.begin_fill()
    t.fd(15)
    t.rt(10)
    t.end_fill()
t.rt(90)
for i in range(9):
    t.begin_fill()
    t.fd(15)
    t.rt(10)
    t.end_fill()
t.lt(150)
t.fd(100)
t.rt(60)
for i in range(9):
    t.begin_fill()
    t.fd(15)
    t.rt(10)
    t.end_fill()
t.rt(90)
for i in range(9):
    t.begin_fill()
    t.fd(15)
    t.rt(10)
    t.end_fill()
t.rt(30)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(180)
t.fd(200)
t.ht()

exitonclick()