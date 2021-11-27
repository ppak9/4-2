"""
    1. Programmer : Jong Hyun Park
    2. Date : 2021.11.20
    3. File_name : py5-r10_박종현
    4. Description : select asteriods or drawFlower of the two for using tkinter
"""


from tkinter import *
from turtle import Turtle as tk, onscreenclick
from random import randint as ri

window = Tk()
total = 0

#[1]function that asteriods 

def asteriods():
    t1 = tk()                                                                      #set the player
    t1.color('blue')
    t1.shape('turtle')
    t1.pu()
    t1.speed(0)
    s = t1.getscreen()

    s_w,s_h = s.screensize()                                                       #set the calculate that screensize

    
    score = tk()
    score.pu()
    score.ht()
    score.color('green')
    score.goto(-(s_w+50),s_h+50)

    def get_score(total):                                                          #calculate score function
        score.clear()
        score.write("score: "+ str(total),font =('Courier',20,'bold'))

    get_score(total)
    asteriods = []                                                                  
    for i in range(10):                                                            #making 10 Asteroid
        a1 = tk()
        a1.color('red')
        a1.shape('circle')
        a1.pu()
        a1.speed(0)
        a1.goto(ri(-300,300),ri(-300,300))
        asteriods.append(a1)

    def tl():
        t1.lt(30)
    def tr():
        t1.rt(30)
    def fd():
        t1.fd(30)
    def bk():
        t1.backward(30)
    s.onkeypress(tl,"Left")
    s.onkeypress(tr,"Right")
    s.onkeypress(fd,"Up")
    s.onkeypress(bk,"Down")
    s.listen()

    def collision(player_x,player_y):                                             #It is a function that eliminates asteroids when an asteroid and a spaceship collide.
        for a in asteriods:
            if round(player_x)-30 <= round(a.xcor()) and round(player_x)+30 >= round(a.xcor()) and round(player_y)-30 <= round(a.ycor()) and round(player_y)+30 >= round(a.ycor()):
                global total
                total = total + 1
                get_score(total)
                a.ht()
                a.write("kill",font=('Courier',10,'bold'),align="right",move="True")
                asteriods.remove(a)

    def play():                                                                   #It's a function that repeats the game. (I set it so that the player can come back when going out of the screen.)
        tx = t1.xcor()
        ty = t1.ycor()
        
        collision(tx,ty)
        if tx >= s_w or tx <= -(s_w) or ty >= s_h or ty <= -(s_h):
            t1.backward(4)
            t1.setheading(ri(30,330))
        t1.fd(10)

        for a in asteriods:
            ax = a.xcor() 
            ay = a.ycor()

            if ax >= s_w or ax <= -(s_w) or ay >= s_h or ay <= -(s_h):
                a.backward(4)
                a.setheading(ri(30,330))
            else:
                a.right(ri(-180,180))
            a.fd(2)
        
        if not len(asteriods):
            finish = tk()
            finish.ht()
            finish.color("black")
            style = ('Courier',50,'italic')
            finish.write("END",font=style,align="center")
            return
        s.ontimer(play,10)
    s.ontimer(play,10)
    return

#[2]function that drawFlower function

def drawFlower():
    t1 = tk()
    t1.speed(0)
    t1.color('red')
    t1.ht()

    def petal():
        for _ in range(2):
            t1.circle(30,110)
            t1.left(70)

    def drawFlower(x,y):
        t1.pu()
        t1.goto(x,y)
        t1.pd()
        t1.begin_fill()
        for _ in range(6):
            petal()
            t1.lt(60)
        t1.end_fill()

        t1.color('green')
        t1.begin_fill()
        t1.pu()
        t1.goto(x,y-10)
        t1.pd()
        t1.circle(10)
        t1.end_fill()
        t1.color('red')

    onscreenclick(drawFlower)


#---------------------------------------#

l1 = Label(window,text = "asteriods")                                           #to display the text                               
l2 = Label(window,text = "Flower")
l1.grid(row = 0, column=1)                                                      #set the position of text
l2.grid(row = 1, column=1)

b1 = Button(window, text = "play asteriods",command= asteriods)                 #to set the button that play function
b2 = Button(window, text = "play drawFlower",command = drawFlower)
b1.grid(row =2 , column = 0)                                                    #set the button position
b2.grid(row =2 , column = 1)

window.mainloop()
window.quit()