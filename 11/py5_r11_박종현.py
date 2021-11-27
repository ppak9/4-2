"""
    1. Programmer : Jong Hyun Park
    2. Date : 2021.11.28
    3. File_name : py5-r11_박종현
    4. Description : Calculator using Tkinter
"""


from tkinter import *
from tkinter import messagebox
from math import *

#------ Tkinter setting ------ #
window = Tk()
window.geometry("279x442")
window.title("Calculator")

#------ set the Command ------ # 
def clickButton(item):
    inputText.set(inputText.get()+(str(item)))

def clearButton():
    inputText.set(inputText.get()[0:-1])

def clearAll():
    inputText.set("")

def equalButton():
    result = 0
    try:
        result = eval(inputText.get())
        inputText.set(result)
    except:
        result = "ERROR..."
        inputText.set(result)

#------- Main function Explain ------ #

"""
   The character variable in Entry is set to inputtextfield to switch from character value to actual value with eval function 
"""

inputText = StringVar()
inputField = Entry(window,bg="orange", font='arial 20 italic bold', textvar=inputText, bd="10",justify=RIGHT)
inputField.grid(row = 0,columnspan = 8)

#------- set the Button ------ #

numberpad = "789456123"
i = 0
btn = []
for j in range(2,5):
    for k in range(3):
        btn.append(Button(window,bg='black',fg='white',
                          font='arial 20 italic bold',
                          bd=8,text=numberpad[i],cursor="hand2",padx=16,pady=16))
        btn[i].grid(row=j, column= k )                                             #row = 2,3,4 column = 0,1,2
        btn[i]["command"]= lambda x = numberpad[i]:clickButton(x)
        i+=1

plus = Button(window, text="+", font="arial 20 italic bold",fg="white", bd=8, bg="black", cursor="hand2", padx=16 , pady=16,
              command=lambda: clickButton("+")).grid(row=1,column=0)
minus = Button(window, text="-", fg="white", font="arial 20 italic bold",bd=8, bg="black", cursor="hand2",
               padx = 16,pady = 16, command=lambda: clickButton("-")).grid(row=1, column=1)
multiply = Button(window, text="*", fg="white", bd=8, font="arial 20 italic bold",bg="black", cursor="hand2",
                  padx = 16,pady = 16,command=lambda: clickButton("*")).grid(row=1, column=2)
divide = Button(window, text="/",  bd=8, bg="black",fg="white",font="arial 20 italic bold",cursor="hand2",
                padx = 16,pady = 16,command=lambda: clickButton("/")).grid(row=1, column= 3)
sin_btn = Button(window, text="sin", fg="white", bd=8, bg="black", cursor="hand2",font="arial 20 italic bold",
               padx=16,pady=16,command=lambda: clickButton("sin")).grid(row=2, column=3)
cos_btn = Button(window, text="cos", fg="white", bd=8, bg="black", cursor="hand2",font="arial 20 italic bold",
               padx=16,pady=16,command=lambda: clickButton("cos")).grid(row=3, column=3)
tan_btn = Button(window, text="tan", fg="white", bd=8, bg="black", cursor="hand2",font="arial 20 italic bold",
               padx=16,pady=16,command=lambda: clickButton("tan")).grid(row=4, column=3)
clear = Button(window, text="C",  bd=8, bg="black",fg="white", font="arial 20 italic bold",
               padx=16,pady=16,cursor = "hand2",command=lambda: clearButton()).grid(row=5, column=0)
allclear = Button(window, text="AC",  bd=8, bg="black",fg="white", font="arial 20 italic bold",
               padx=16,pady=16,cursor = "hand2",command=lambda: clearAll()).grid(row=5, column=1)
zero = Button(window, text="0", fg="white", bd=8, bg="black", cursor="hand2",font="arial 20 italic bold",
              padx=16,pady=16,command=lambda: clickButton(0)).grid(row=5, column=2)
point = Button(window, text=".", fg="white", bd=8, bg="black", cursor="hand2",font="arial 20 italic bold",
               padx=16,pady=16,command=lambda: clickButton(".")).grid(row=5, column=3)
bracket1 = Button(window, text="(", fg="white", bd=8, bg="black", cursor="hand2",font="arial 20 italic bold",
               padx=16,pady=16,command=lambda: clickButton("(")).grid(row=6, column=0)
bracket2 = Button(window, text=")", fg="white", bd=8, bg="black", cursor="hand2",font="arial 20 italic bold",
               padx=16,pady=16,command=lambda: clickButton(")")).grid(row=6, column=1)
rad= Button(window, text="rad",  fg="white", bd=8, bg="black", cursor="hand2",font="arial 20 italic bold",
                padx=16,pady=16,command=lambda: clickButton("pi/180")).grid(row=6, column=2)
equals = Button(window, text="=",  fg="white", bd=8, bg="black", cursor="hand2",font="arial 20 italic bold",
                padx=16,pady=16,command=lambda: equalButton()).grid(row=6, column=3)
