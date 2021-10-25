from turtle import *

t = Turtle()

def drawmaze(x,y):
    for i in range(2):
        t.pu()
        if i == 1:
            t.goto(x+100,y+100)
        else:
            t.goto(x,y)
        t.pd()
        t.fd(300)
        t.rt(90)
        t.fd(300)
        t.lt(90)
        t.fd(300)

def turn_left():
    t.lt(10)
    t.fd(10)

def turn_right():
    t.rt(10)
    t.fd(10)

def st():
    t.fd(10)

def bk():
    t.bk(10)

s = Screen()
drawmaze(-300,200)
s.onkey(turn_left,'Left') #onkey 가 먹어가는 방식
s.onkey(turn_right,'Right')
s.onkey(st,'Up')           # 방향키 앞 키
s.onkey(bk,'Down')         # 방향키 뒷 키
t.pu()
t.goto(-300,250)
t.pd()
s.listen() # 지정한 onkey가 먹어야 하기 때문에
s.mainloop()
