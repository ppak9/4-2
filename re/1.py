import turtle
from time import *
from random import *

t = turtle.Turtle()
t.speed(0)
t.shape('turtle')

# ts = Screen()

# ts.addshape('/Users/jbak/uni/python/re/giphy.gif')
# t.shape('/Users/jbak/uni/python/re/giphy.gif')
# t.stamp()

# ts.exitonclick()
def drawpoly(t):
    k = textinput("draw polygon","what type?: ")
    # s = int(k)
    for _ in range(int(k)):
        t.fd(50)
        t.left(360/int(k))

def fact(i):
    fact = 1
    for k in range(1,i+1):
        fact = fact * k
        print(k)
    print(fact)

i = 1 
k = 1

def gugu(i,k):
    while True:
        print(i*k,"and i,k value is: ",i,k)
        k += 1
        if k > 9:
            i += 1
            k = 1
        if i == 9 and k == 9:
            break

def drawPoly(l):
    for _ in range(4):
        t.fd(l)
        t.left(90)

color = ['red','blue','yellow','pink','white']

# def drawit(x,y):
#     t.pu()
#     t.goto(x,y)
#     t.pd()
#     t.color('red')
#     t.begin_fill()
#     drawPoly(100)
#     t.end_fill
def draw(x,y):
    global t
    t.pu()
    t.goto(x,y)
    print(t.xcor(),t.ycor())
    t.pd()

sc = turtle.Screen()
sc.onscreenclick(draw)
# s.onscreenclick(drawit)



# s.exitonclick()