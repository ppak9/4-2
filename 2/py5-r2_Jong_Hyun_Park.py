"""
    1. Programmer : Jong Hyun Park
    2. Date : 2021.09.23
    3. File_name : py5-r2_Jong_Hyun_Park
    4. Description : hexagon divided into isosceles triangle + draw the polygon with value k as the polygon sides
"""

# import turtle with function of turtle library  
from turtle import Screen,Turtle

t = Turtle()
#set the speed of the turtle
t.speed(0)
#hide the figure 
t.ht()
# set the hexagon sides
n = 6
# rta mean as the rotating angle
rta = 180*(n-2)/n

colors = ['red','blue','green','pink','orange','purple']
# set the sides of polygon 
k = int(input("insert the value of k: "))

for i in range(n):
    t.color(colors[i])
    t.begin_fill()
    t.fd(100)
    # rotate to right sides by rta
    t.right(rta)
    t.fd(100)
    t.right(rta)
    t.fd(100)
    t.right(rta)
    t.fd(130)
    # make the polygon on the k-side
    for _ in range(k):
        t.fd(30)
        t.left(360/k)
    t.bk(30)
    t.right(rta/2)
    t.end_fill()
# using screen function for capture
screen = Screen()
screen.exitonclick()