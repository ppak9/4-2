from random import *

y_list =[]
r_s = 0
def test(list):
    for i in range(len(list)):
        print(list[i])

while True:
    rand = randint(100,120)
    r_s += rand
    y_list.append(rand)
    test(y_list)
    if r_s >= 700:
        break
    
    