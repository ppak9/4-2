"""
    1. Programmer : Jong Hyun Park
    2. Date : 2021.10.20
    3. File_name : py5-r6_Jong_Hyun_Park
    4. Description : Turtle race & Add a random value graph
"""

from turtle import *
from random import randint

def drawGraph(t,select,list):                                               #A function to draw a bar graph.
    for i in range(len(list)):
        t.ht()
        t.color(select)
        t.begin_fill()
        t.left(90)
        t.fd(list[i])
        t.rt(90)
        t.write(list[i],move="True",font=("Verdona",15,"normal"))
        t.fd(30)
        t.rt(90)
        t.fd(list[i])
        t.rt(90)
        t.fd(30)
        t.end_fill()
        t.rt(180)
        t.fd(40)

t1 = Turtle()

t1 = Turtle()
t1.shape("turtle")
t1.color('red')

t2 = t1.clone()
t2.color('blue')

t3 = t1.clone()                                                             # Clone the turtle
t4 = t2.clone()

t1.pu()
t1.goto(-200,200)
t1.pd()

t2.pu()
t2.goto(-200,200)
t2.pd()

t3.pu()                                                                     #set the position of clone turtle
t3.goto(-600,-300)
t3.pd()

t4.pu()
t4.goto(250,-300)
t4.pd()
r_s = 0
b_s = 0

x = 0
y = 0

t1_list = []                                                                # add the list of the position
t2_list = []

while True:
    r_r = randint(100,140)
    b_r = randint(100,140)
    r_s += r_r
    b_s += b_r
    t1_list.append(r_r)
    t2_list.append(b_r)

    if r_s >= 400 and x == 0:
        x += 90
        t1.fd(400-(r_s-r_r))                                                # select the pre-exist position
        t1.rt(x)
        t1.fd(r_s - 400)
        print(x)
    else: 
        t1.fd(r_r)
    
    if b_s>= 400 and y ==0:
        y += 90
        t2.fd(400-(b_s-b_r))
        t2.rt(y) 
        t2.fd(b_s-400)
    
    else:
        t2.fd(b_r)

    if r_s >= 700 and b_s >=700:
        break

if r_s>b_s:
    t2.ht()
    t1.pu()
    t1.home()
    t1.pd()
    t1.write("red is won",font=("Verdona",15,"bold"))
elif b_s>r_s:
    t1.ht()
    t2.pu()
    t2.home()
    t2.pd()
    t2.write("blue is won",font=("Verdona",15,"normal"))
else:
    t1.ht()
    t2.ht()
    t1.pu()
    t1.home()
    t1.pd()
    t1.write("draw",font=("Verdona",15,"normal"))

drawGraph(t3,"red",t1_list)                                                 #use the function to draw the graph                                                       
drawGraph(t4,"blue",t2_list)


exitonclick()