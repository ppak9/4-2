"""
    1. Programmer : Jong Hyun Park
    2. Date : 2021.10.16
    3. File_name : py5-r5_Jong_Hyun_Park
    4. Description : Turtle race (added function)
"""


from turtle import *
from random import randint as ri

s_list = [500,800,1100,1300]                                                        #Set the turning point
r_s = 0
b_s = 0
x = 0
y = 0
r_list = []
b_list = []

def drawGraph(t,list,x,y):                                                          #draw graph function
    t.setheading(0)
    t.pu()
    t.goto(x,y)
    t.pd()                                                   
    for i in range(len(list)):
        t.ht()
        t.begin_fill()
        t.left(90)
        t.fd(list[i])
        t.rt(90)
        t.write(list[i],move="True",font=("Verdona",14,"bold"))
        t.fd(30)
        t.rt(90)
        t.fd(list[i])
        t.rt(90)
        t.fd(30)
        t.end_fill()
        t.rt(180)
        t.fd(40)   

def test(t1,t2,list,deg1,deg2,sum1,sum2):                                         #Set the function where the turtle races.
    i1 = 0
    i2 = 0
    while True:
        r_r = ri(150,190)
        r_list.append(r_r)
        b_r = ri(150,190)
        b_list.append(b_r)
        sum1 += r_r
        sum2 += b_r
        
        if sum1 >= list[i1] and deg1 == i1:
            t1.fd(list[i1]-(sum1-r_r))
            t1.rt(90)
            t1.fd(sum1-list[i1])
            i1 += 1
            deg1 += 1
        else:
            t1.fd(r_r)
        
        if sum2 >= list[i2] and deg2 == i2:
            t2.fd(list[i2]-(sum2-b_r))
            t2.rt(90)
            t2.fd(sum2-list[i2])
            i2 += 1
            deg2 += 1
        else:
            t2.fd(b_r)
        
        if sum1 >= 1200 or sum2 >= 1200:
            break
        
    if sum1 > sum2:
        t2.ht()
        t1.pu()
        t1.goto(100,0)
        t1.pd()
        t1.write("red is win" +": " + str(sum1),font=("Verdona",14,"bold"))
        drawStar(t1,200,100,"red")
        t1.ht()
    elif sum2 > sum1:
        t1.ht()
        t2.pu()
        t2.goto(100,0)
        t2.pd()
        t2.write("blue is win" +": "+ str(sum1),font=("Verdona",14,"bold"))
        drawStar(t2,200,100,"blue")
        t2.ht()
    else:
        t2.ht()
        t1.pu()
        t1.goto(100,0)
        t1.pd()
        t1.write("same",font=("Verdona",14,"bold"))      

def drawTrack(t,t1,t2):                                                             #Set up the initial route
    t.pu()
    t.goto(0,300)
    t.pd()
    t.write("Turtle race",font=("Verdona",24,"bold"))
    t.pu()
    t.goto(-200,200)
    t.write("*Start",font=("Verdona",14,"bold"))
    t.pd()
    t.fd(500)
    t.rt(90)
    t.fd(300)
    t.rt(90)
    t.fd(300)
    t.rt(90)
    t.fd(200)
    t.write("*Finish",font=("Verdona",14,"bold"))
    t.ht()
    t1.pu()
    t1.goto(-200,200)
    t1.pd()
    t2.pu()
    t2.goto(-200,200)
    t2.pd()

def drawStar(t,x,y,select):                                                         #Set the function of draw Star
    t.setheading(0)
    t.pu()
    t.goto(x,y)
    t.pd()
    t.color(select)
    t.begin_fill()
    for _ in range(5):
        t.fd(15)
        t.rt(144)
        t.fd(15)
        t.lt(72)
    t.end_fill()

t0 = Turtle()
t0.speed(0)
t0.shape('turtle')
t1 = t0.clone()
t2 = t0.clone()
t0.color('green')
t1.color('red')
t2.color('blue')

drawTrack(t0,t1,t2)
test(t1,t2,s_list,x,y,r_s,b_s)
drawGraph(t1,r_list,-500,-350)
drawGraph(t2,b_list,100,-350)
exitonclick()

