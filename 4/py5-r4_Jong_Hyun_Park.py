"""
    1. Programmer : Jong Hyun Park
    2. Date : 2021.10.07
    3. File_name : py5-r4_Jong_Hyun_Park
    4. Description : Drawing a bouquet.
"""

from turtle import *                                                                        #import the turtle and random library
from random import *

speed(0)                                                                                    #set the speed as fastest
ht()                                                                                        #hide the figure
colors = ['red','blue','green','pink','orange','purple','yellow','seashell']                #set the colors list

def drawFlower(a,b):                                                                        #set the function as the draw flower
        pu()
        goto(a,b)
        pd()
        for x in range(30):
            fillcolor(colors[randint(0,7)])                                                 #use the random function as fill the color
            begin_fill()
            circle(60,70)
            if x % 2 == 0:
                circle(10,70)                                                              
            end_fill()

def flowerCup(l):                                                                           #set the function as for draw the flower cup
    pu()
    goto(-90,-10)
    pd()
    fillcolor('green')
    begin_fill()
    fd(l)
    rt(120)
    fd(l)
    rt(120)
    fd(l)
    end_fill()


flowerCup(180)

for k in range(4):                                                                          #draw the flower closely
    drawFlower(15,15*k)
    print(k)

for k in reversed(range(4)):
    drawFlower(-15,15*k)
    print(k)

exitonclick()