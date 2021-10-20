"""
    1. Programmer : Jong Hyun Park
    2. Date : 2021.10.16
    3. File_name : py5-r5_Jong_Hyun_Park
    4. Description : Turtle race
"""

from turtle import *
from random import randint                                             # Import the necessary library

speed(0)                                                               # set the track
pu()
goto(-200,200)
pd()
write("(-200,200)", font=('Verdana',15,"normal"))
pu()
goto(200,200)
pd()
write("(200,200)",font=("Verdona",15,"normal"))
pu()
goto(200,-100)
pd()
write("(200,-100)",font=("Verdona",15,"normal"))

t1 = Turtle()                                                           # set the turtles
t1.color('red')
t1.shape('turtle')
t1.pu()
t1.goto(-200,200)
t1.pd()

t2 = Turtle()
t2.color('blue')
t2.shape('turtle')
t2.pu()
t2.goto(-200,200)
t2.pd()

x1cor_list = []                                                         #Make a list to get the right number for the condition statement.
x2cor_list = []

while True:
    rand1 = randint(70,90)                                              # use the different status
    rand2 = randint(70,90)
    x1pos = t1.xcor() 
    y1pos = t1.ycor()
    x2pos = t2.xcor()
    y2pos = t2.ycor()
    finalX1 = x1pos + rand1
    finalY1 = y1pos - rand1
    finalX2 = x2pos + rand2
    finalY2 = y2pos - rand2
    
    if finalX1 < 200:                                                   #It continues to advance until the x-coordinate 200.
        t1.setx(finalX1)
        x1cor_list.append(x1pos)
    
    elif finalX2 < 200:                                                 #x2 is the same thing 
        t2.setx(finalX2)
        x2cor_list.append(x2pos)

    elif finalX1 and finalX2 >= 200:                                    #If it arrives at midpoint 200, it rotates 90 degrees.
        x1left = finalX1 - 200
        x1fd = 200 - x1cor_list[-1]
        middleX1 = x1cor_list[-1] + x1fd
        t1.setx(middleX1)
        t1.sety(finalY1)
    
        x2left = finalX2 - 200
        x2fd = 200 - x2cor_list[-1]
        middleX2 = x2cor_list[-1] + x2fd
        t2.setx(middleX2)
        t2.sety(finalY2)

        if y1pos <= -190 or y2pos <= -190:                              #Set the turtle that arrived first to win. Additionally,I set it to 190 more comfortably than 200.
            if y1pos < y2pos:
                pu()
                goto(300,-200)
                pd()
                ht()
                write("red is won",font = ("Verdona",12,"bold"))
                break
            elif y1pos > y2pos:
                pu()
                goto(300,-200)
                pd()
                ht()
                write("blue is won",font = ("Verdona",12,"bold")) 
                break
            else:
                pu()
                goto(300,-200)
                pd()
                ht()
                write("draw",font = ("Verdona",12,"bold"))             
                break

exitonclick()