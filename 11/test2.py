from tkinter import *
from tkinter import messagebox
from math import sin, cos, tan

window = Tk()
window.geometry("279x442")
window.title("Calculator")
#function

def clickButton(item):
    global expression
    inputText.set(inputText.get()+(str(item)))

def clearButton():
    global expression
    expression = ""
    inputText.set(inputText.get()[0:-1])

def clearAll():
    inputText.set("")

def equalButton():
    result = ""
    try:
        result = eval(inputText.get())
        inputText.set(result)
    except:
        result = "ERROR..."
        inputText.set(result)

expression = ""
inputText = StringVar()
inputField = Entry(window,bg="orange", font='arial 20 italic bold', textvar=inputText, bd="10",justify=RIGHT)
inputField.grid(row = 0,columnspan=4)



plus = Button(window, text="+", fg="white", bd=0, bg="black", cursor="hand2", padx=16 , pady=16,
              command=lambda: clickButton("+")).grid(row=1,column=0)
divide = Button(window, text="/",  bd=0, bg="black",fg="white",cursor="hand2",
                padx= 16,pady =16,command=lambda: clickButton("/")).grid(row=1, column= 1)
minus = Button(window, text="-", fg="white", bd=0, bg="black", cursor="hand2",
               padx= 16,pady = 16, command=lambda: clickButton("-")).grid(row=1, column=2)
multiply = Button(window, text="*", fg="white", bd=0, bg="black", cursor="hand2",
                  padx=16,pady=16,command=lambda: clickButton("*")).grid(row=1, column=3)
                
seven = Button(window, text="7", fg="white",  bd=0, bg="black", cursor="hand2",
               padx=16,pady=16,command=lambda: clickButton(7)).grid(row=2, column=0)
eight = Button(window, text="8", fg="white", bd=0, bg="black", cursor="hand2",
               padx=16,pady=16,command=lambda: clickButton(8)).grid(row=2, column=1)
nine = Button(window, text="9", fg="white", bd=0, bg="black", cursor="hand2",
              padx=16,pady=16,command=lambda: clickButton(9)).grid(row=2, column=2)


four = Button(window, text="4", fg="white", bd=0, bg="black", cursor="hand2",
              padx=16,pady=16,command=lambda: clickButton(4)).grid(row=3, column=0)
five = Button(window, text="5", fg="white",  bd=0, bg="black", cursor="hand2",
              padx=16,pady=16,command=lambda: clickButton(5)).grid(row=3, column = 1)
six = Button(window, text="6", fg="white",  bd=0, bg="black", cursor="hand2",
             padx=16,pady=16, command=lambda: clickButton(6)).grid(row=3, column=2)



one = Button(window, text="1", fg="white", bd=0, bg="black", cursor="hand2",
             padx=16,pady=16,command=lambda: clickButton(1)).grid(row=4, column=0)
two = Button(window, text="2", fg="black", bd=0, bg="black", cursor="hand2",
             padx=16,pady=16,command=lambda: clickButton(2)).grid(row=4, column=1)
three = Button(window ,text="3", fg="black", bd=0, bg="black", cursor="hand2",
               padx=16,pady=16,command=lambda: clickButton(3)).grid(row=4, column=2)



zero = Button(window, text="0", fg="white", bd=0, bg="black", cursor="hand2",
              padx=16,pady=16,command=lambda: clickButton(0)).grid(row=5, column=0)
point = Button(window, text=".", fg="white", bd=0, bg="black", cursor="hand2",
               padx=16,pady=16,command=lambda: clickButton(".")).grid(row=5, column=1)
equals = Button(window, text="=",  fg="white", bd=0, bg="black", cursor="hand2",
                padx=16,pady=16,command=lambda: equalButton()).grid(row=5, column=2)
clear = Button(window, text="AC",  bd=0, bg="black",fg="white", 
               padx=16,pady=16,cursor = "hand2",padx = 16, pady = 16, command=lambda: clearButton()).grid(row=1, column=0)
bracket1 = Button(window, text="(", fg="white", bd=0, bg="black", cursor="hand2",
               padx=16,pady=16,command=lambda: clickButton("(")).grid(row=6, column=0)
bracket2 = Button(window, text=")", fg="white", bd=0, bg="black", cursor="hand2",
               padx=16,pady=16,command=lambda: clickButton(")")).grid(row=6, column=1)
sin_btn = Button(window, text="sin", fg="white", bd=0, bg="black", cursor="hand2",
               padx=16,pady=16,command=lambda: clickButton("sin")).grid(row=7, column=0)
cos_btn = Button(window, text="cos", fg="white", bd=0, bg="black", cursor="hand2",
               padx=16,pady=16,command=lambda: clickButton("cos")).grid(row=7, column=1)
tan_btn = Button(window, text="tan", fg="black", bd=0, bg="black", cursor="hand2",
               padx=16,pady=16,command=lambda: clickButton("tan")).grid(row=7, column=2)

