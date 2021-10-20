from math import pi, sin as sine
from turtle import Screen, Turtle

colors = ['red','blue','green','pink','orange','purple']


def triangular_polygon(turtle, length, n, k):
    inside_angle = (n - 2) * pi / n / 2
    rotating_angle = pi - inside_angle
    radius = length / (2 * sine(pi / n))

    turtle.penup()
    turtle.forward(radius)
    turtle.left(rotating_angle)
    turtle.pendown()

    for i in range(n):
        turtle.color(colors[i])
        turtle.begin_fill()
        turtle.forward(length + 100)
        for i in range(k):
            turtle.fd(30)
            turtle.rt(2*pi/k)
        turtle.backward(100)
        turtle.left(rotating_angle)
        turtle.forward(radius)
        turtle.backward(radius)
        turtle.right(inside_angle)
        turtle.end_fill()

screen = Screen()
bob = Turtle()
bob.radians()  # switch turtle to radians to match math functions
bob.speed('slowest')
k = int(input("write the value of k: "))

triangular_polygon(bob, 100, 6, k)

bob.hideturtle()
screen.exitonclick()