from turtle import *

t = Turtle()

def drawPoly(n):
    for _ in range(n):
        t.fd(100)
        t.lt(360/n)

n = int(input("type the poly angle numbers: "))

def drawit(x,y):
    global n
    t.pu()
    t.goto(x,y)
    t.pd()
    drawPoly(n)

s = Screen()
s.onscreenclick(drawit)

# if you wanna use onscreenclick don't use VSC , use python editor