from turtle import *
from random import randint
                                                                        
def drawGraph(t,list,x,y):                                              #A function to draw a bar graph.
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
                                                    
t0 = Turtle()                                                           #set the turtle               
t0.color('green')
t0.width(8)
t0.speed(0)
t0.pu()
t0.goto(-100,300)
t0.pd()
t0.write('Two of turtle race',font=("Verdona",24,"bold"))
t0.pu()
t0.goto(-200,210)
t0.pd()
t0.write("*Start",font=("Verdona",14,"bold"))
t0.pu()
t0.goto(10,100)
t0.pd()
t0.write('*Finish',font=("Verdona",14,"bold"))

t0.pu()                                                                  #draw the track
t0.goto(-200,200)
t0.pd()
t0.fd(500)
t0.rt(90)
t0.fd(300)
t0.rt(90)
t0.fd(300)
t0.rt(90)
t0.fd(200)


t1 = t0.clone()                                                          # set the red and blue turtle
t2 = t0.clone()
t1.color('red')
t2.color('blue')
t1.shape('turtle')
t2.shape('turtle')
t1.shapesize(2,2)
t2.shapesize(2,2)
#set t1
t1.pu()
t1.goto(-200,200)
t1.pd()
t1.rt(90)
#set t2
t2.pu()
t2.goto(-200,200)
t2.pd()
t2.rt(90)

r_s = 0                                                                  #set the sum and the angle
b_s = 0

x = 0
y = 0


xlist = []                                                               #set up the x,y lists.
ylist = []

while True:
    r_r = randint(150,190)
    b_r = randint(150,190)
    r_s += r_r
    b_s += b_r
    xlist.append(r_r)
    ylist.append(b_r)

    if r_s >= 500 and x == 0:   
        t1.fd(500-(r_s-r_r))
        t1.rt(90)
        t1.fd(r_s - 500)
        x += 1
    elif r_s >= 800 and x == 1:
        t1.fd(800-(r_s-r_r))
        t1.rt(90)
        t1.fd(r_s-800)
        x += 1
    elif r_s >= 1100 and x == 2:
        t1.fd(1100-(r_s-r_r))
        t1.rt(90)
        x += 1
    else:
        t1.fd(r_r)
    
    # if b_s >= 500 and x2 == 0:                                           #set t2 as well.
    #     x2 += 90
    #     t2.fd(500-(b_s-b_r))
    #     t2.rt(x2)
    #     t2.fd(b_s - 500)
    # elif b_s >= 800 and y2 == 0:
    #     y2 += 90
    #     t2.fd(800-(b_s-b_r))
    #     t2.rt(y2)
    #     t2.fd(b_s-800)
    # elif b_s >= 1100 and z2 == 0:
    #     z2 += 90
    #     t2.fd(1100-(b_s-b_r))
    #     t2.rt(z2)
    # else:
    #     t2.fd(b_r)
    
    # if r_s >= 1300 or b_s >= 1300 :
    if r_s >= 1300:
        break
        #                                         #Go to the last point and decide who will win.
        # if r_s >= b_s:
        #     t2.ht()
        #     t1.ht()
        #     t2.pu()
        #     t2.goto(100,100)
        #     t2.pd()
        #     t2.write('t2 is lose'+' '+str(b_s),font=('Verdona',14,'bold'))
        #     t1.pu()
        #     t1.goto(100,150)
        #     t1.pd()
        #     t1.write('t1 is win'+' '+str(r_s),font=('Verdona',14,'bold'))
        #     t1.ht()
        #     break
        # elif b_s >= r_s:
        #     t1.ht()
        #     t2.ht()
        #     t2.pu()
        #     t2.goto(100,150)
        #     t2.pd()
        #     t2.write('t2 is win'+' '+ str(b_s),font=('Verdona',14,'bold'))
        #     t1.pu()
        #     t1.goto(100,100)
        #     t1.pd()
        #     t1.write('t1 is lose'+' '+str(r_s),font=('Verdona',14,'bold'))
        #     t2.ht()
        #     break
        # else:
        #     t2.ht()
        #     t1.pu()
        #     t1.goto(100,100)
        #     t1.pd()
        #     t1.write('draw',font=('Verdona',14,'bold'))
        #     break

# t1.rt(90)
# t2.rt(90)                                                                       #Draw a graph based on the number on the list.
# drawGraph(t1,xlist,-500,-350)                                                   
# drawGraph(t2,ylist,100,-350)                                                    #adjusted the coordinates so that they don't overlap                                                                         
exitonclick()