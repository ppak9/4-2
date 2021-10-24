from turtle import *
from random import randint

t1 = Turtle()
t2 = t1.clone()

y_list = []
t2.pu()
t2.goto(-300,-100)
t2.pd()
r_s = 0

def test(t2,list):
    for i in range(len(list)):
        t2.color("blue")
        t2.begin_fill()
        t2.left(90)
        t2.fd(list[i])
        t2.rt(90)
        t2.write(list[i],move="True",font=("Verdona",15,"normal"))
        t2.fd(30)
        t2.rt(90)
        t2.fd(list[i])
        t2.rt(90)
        t2.fd(30)
        t2.end_fill()
        t2.rt(180)
        t2.fd(40)

while True:
        rand = randint(100,140)
        t1.fd(rand)
        r_s += rand
        y_list.append(rand)
        print("total:",r_s)
        if r_s >= 700:
            break   

test(t2,y_list)

exitonclick()