from turtle import *
from random import randint

# For testing

t1 = Turtle()
# set the refree turtle, set the manual

t1 = Turtle()
t1.shape("turtle")
t1.color('red')

t2 = t1.clone()
t2.color('blue')

t1.pu()
t1.goto(-200,200)
t1.pd()
t2.pu()
t2.goto(-200,200)
t2.pd()

# explain about the red_sum
r_s = 0
b_s = 0

x = 0
y = 0

while True:
    r_r = randint(70,90)
    b_r = randint(70,90)
    r_s += r_r
    b_s += b_r

    if r_s >= 400 and x == 0:
        x += 90
        t1.fd(400-(r_s-r_r)) # select the pre-exist position
        t1.rt(x)
        t1.fd(r_s - 400)
        print(x)
    else: # x가 90이 아니기에, 나아가지 않음
        t1.fd(r_r)
    
    if b_s>= 400:
        print("the first y value",y)
        t2.fd(400-(b_s-b_r))
        t2.rt(90) #윗 부분과 비교해보면 잘 나오는데, if 루프에 걸려서 흐름이 넘어가는 구조
        t2.fd(b_s-400)
        """
        윗 부분과 x_loop와 비교하면 맞아 가는데, 각도 설정없이 계속해서 돌면은 결국 90에서 계속해서 돔
        결국 원하는 분기점에서 if조건에 맞춰서 넘어가야 하기 때문
        """
    else:
        t2.fd(b_r)
        print("the second y value",y)

    if r_s >= 700 and b_s >=700:
        break

if r_s>b_s:
    t2.ht()
    t1.pu()
    t1.goto(300,-300)
    t1.pd()
    t1.write("red is won",font=("Verdona",15,"bold"))
elif b_s>r_s:
    t1.ht()
    t2.pu()
    t2.goto(300,-300)
    t2.pd()
    t2.write("blue is won",font=("Verdona",15,"normal"))
else:
    t1.ht()
    t2.ht()
    t1.pu()
    t1.goto(300,-300)
    t1.pd()
    t1.write("draw",font=("Verdona",15,"normal"))


exitonclick()