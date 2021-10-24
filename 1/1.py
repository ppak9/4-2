from turtle import *

l = 200
bl = 50
t = Turtle()

colors = ['red','blue','green','pink','orange','purple']
k = int(input("type the polygonal numbers: "))
t.shape('turtle')
t.ht()

for i in range(6):
    t.color(colors[i])
    t.begin_fill()
    t.fd(l)
    for _ in range(k):
        t.fd(50)
        t.rt(360/k)
    t.backward(bl)
    t.right(60)
    t.end_fill()
exitonclick()