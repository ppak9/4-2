from turtle import *

pu()
ht()

speed('fastest')

def petal():
    pd()
    for x in range(40):
        fd(10)
        lt(x)
    pu()

for _ in range(8):
    petal()
    goto(0,0)
    lt(-15)

exitonclick()