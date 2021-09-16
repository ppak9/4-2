"""
    1. Programmer : Jong Hyun Park
    2. Date : 2021.09.16
    3. File_name : py5-r1_Jong_Hyun_Park
    4. Description : Hexagon + Circle
"""

import turtle
# for pause final result import python module
import time 


# Start a work Screen
ws = turtle.Screen() 
 
# Define a Turtle Instance
t = turtle.Turtle()
# for export final result, export turtle library of the getscreen
ts = turtle.getscreen()

# set the color list
colors = ['red','blue','green','pink','orange','purple']
#hiding figure
t.ht()

# for set start position
t.penup()
t.setpos(-100,200)
t.pendown()

# executing loop 6 times for 6 sides
for i in range(6):
 
    # Move forward by 200 units
    t.color(colors[i])
    # use begin_fill function
    t.begin_fill()
    # forward 300 and backward 100 
    t.fd(300)
    t.circle(50)
    t.bk(100)
    # Turn left the turtle by 300 degrees
    t.right(60)
    t.end_fill()

# pause the run of the turtle, for check about the result
time.sleep(3)
 
#  export final result of the picture
ts.getcanvas().postscript(file="result.eps")
