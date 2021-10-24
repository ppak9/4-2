"""
    1. Programmer : Jong Hyun Park
    2. Date : 2021.09.16
    3. File_name : py5-r1_Jong_Hyun_Park
    4. Description : Hexagon + Circle
"""

from turtle import *
from math import pi, sin as sine
# for pause final result import python module
import time 

# Start a work Screen
 
# Define a Turtle Instance
t = Turtle()
# for export final result, export turtle library of the getscreen
l = 300

inside_angle = 4 /3 * pi
rotating_angle = pi - inside_angle
radius = l/(2 * sine(pi / 6))


# set the color list
colors = ['red','blue','green','pink','orange','purple']
#hiding figure
t.speed(0)

# for set start position
t.pu()
t.goto(-100,200)
t.pd()
n = int(input("enter the value of N: "))
# executing loop 6 times for 6 sides
for i in range(6):
    # Move forward by 200 units
    t.color(colors[i])
    # use begin_fill function
    t.begin_fill()
    # forward 300 and backward 100 
    t.fd(l)
    for _ in range(n):
        t.fd(25)
        t.right(360/n)
    t.backward(100)
    t.rt(300)
    t.fd(l)
    # Turn left the turtle by 300 degrees  
    t.end_fill()
 
#  export final result of the picture
exitonclick()