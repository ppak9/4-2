from turtle import *

colors = ['red','blue','green','pink','orange','purple','yellow','seashell']
speed('fastest')

for i in range(8):
    color(colors[i])
    begin_fill()
    for j in range(5):
        rt(72)
        fd(100)
    rt(45)
    end_fill()
    

exitonclick()