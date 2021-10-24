"""
    1. Programmer : Jong Hyun Park
    2. Date : 2021.09.30
    3. File_name : py5-r3_Jong_Hyun_Park
    4. Description : Draw a Flower using a turtle
"""

from turtle import Turtle,Screen #import a turtle library to use a Turtle & Screen function

t1 = Turtle() #Designate turtle one by one
t2 = Turtle() 
s = Screen() #import the turtle screen


t1.fillcolor('red')  #Set the t1
t1.pencolor('red')
t1.pensize(3)
t1.speed('fastest')

t2.fillcolor('blue') #Set the t2
t2.pencolor('blue')
t2.pensize(3)
t2.speed('fastest')

def drawSquare(t, l): #A function to draw a square.
    for i in range(4):
        t.forward(l)
        t.left(90)

def drawFlower(t,x,y): #A function to draw a flower. and the parameters are turtles and x,y coordinates.
    t.ht()
    t.penup()
    t.setpos(x,y)
    t.pendown()

    for _ in range(20):
        t.left(18)
        drawSquare(t, 50)
    
    t.penup()
    t.setpos(x+50,y-100) 
    t.pendown()
    t.write(arg="JHP", align="left", font=("Comic Sans", 10, "normal")) #use write function

drawFlower(t1,-200,0) #call the function twice to draw a flower
drawFlower(t2,200,0)

s.exitonclick()