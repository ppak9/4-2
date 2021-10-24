from turtle import *

t = Turtle()
t.write("that's Home!")
fl = 200
bl = 100

k = int(input("type the polygon numbers: "))
colors = ['red','blue','green','pink','orange','purple']


for i in range(6):
    t.color(colors[i])
    t.begin_fill()
    t.fd(fl)
    for _ in range(k):
        t.fd(25)
        t.rt(360/k)
    t.backward(bl)
    t.rt(120)
    t.fd(100)
    t.rt(120)
    t.fd(100)
    t.rt(120)
    t.fd(100)
    t.end_fill()
    t.rt(60)


exitonclick()