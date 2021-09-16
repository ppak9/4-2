import turtle
import time

# Start a work Screen
ws = turtle.Screen()
 
# Define a Turtle Instance
t = turtle.Turtle()
ts = turtle.getscreen()

colors = ['red','blue','green','pink','orange','purple']
t.ht()
t.penup()
t.setpos(0,200)
t.pendown()

# executing loop 6 times for 6 sides
for i in range(6):
 
    # Move forward by 200 units
    t.color(colors[i])
    t.begin_fill()
    t.fd(300)
    t.circle(50)
    t.bk(100)
    # Turn left the turtle by 300 degrees
    t.right(60)
    t.end_fill()

time.sleep(3)
ts.getcanvas().postscript(file="result.eps")

