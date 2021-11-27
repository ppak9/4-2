from tkinter import *
import tkinter.messagebox as tmsg 
from math import *

root = Tk()
root.title('Calculator')
root.geometry('350x500')
root.configure(bg="black")

operator = ""
text = StringVar() #use in tkinter for text

def click(number):
    global operator
    operator += str(number)
    text.set(operator)

def clear():
    global operator
    operator = ""
    text.set(operator)

def equal():
    global operator
    try:
        result = eval(operator)
        operator = str(result)
        text.set(result)
    except:
        tmsg.showinfo("Calculator_error")

def sin():
    global operator
    try:
        result = sin(radians(float(text.get())))
        operator = str(result)
    except:
        tmsg.showinfo("Calculator_error")

def cos():
    global operator
    try:
        result = cos(eval(text.get()))
        operator = str(result)
        text.set(result)
    except:
        tmsg.showinfo("Calculator_error")

def tan():
    global operator
    try:
        result = tan(eval(text.get()))
        operator = str(result)
    except:
        tmsg.showinfo("Calculator_error")


entry1= Entry(root,bg="orange",font="arial 20 italic bold",bd="30",justify=RIGHT,textvar=text)
entry1.grid(row=0,columnspan=4)

btn7=Button(root,text="7",font="arial 20 italic bold",bd="8",padx=16,pady=16,command=lambda :click(7),activebackground="green",activeforeground="white",bg="powder blue").grid(row=1,column=0)
btn8=Button(root,text="8",font="arial 20 italic bold",bd="8",padx=16,pady=16,command=lambda :click(8),activebackground="green",activeforeground="white",bg="powder blue").grid(row=1,column=1)
btn9=Button(root,text="9",font="arial 20 italic bold",bd="8",padx=16,pady=16,command=lambda :click(9),activebackground="green",activeforeground="white",bg="powder blue").grid(row=1,column=2)
add=Button(root,text="+",font="arial 20 italic bold",bd="8",padx=16,pady=16,command=lambda :click("+"),activebackground="red",activeforeground="white",bg="powder blue").grid(row=1,column=3)

btn4=Button(root,text="4",font="arial 20 italic bold",bd="8",padx=16,pady=16,command=lambda :click(4),activebackground="green",activeforeground="white",bg="powder blue").grid(row=2,column=0)
btn5=Button(root,text="5",font="arial 20 italic bold",bd="8",padx=16,pady=16,command=lambda :click(5),activebackground="green",activeforeground="white",bg="powder blue").grid(row=2,column=1)
btn6=Button(root,text="6",font="arial 20 italic bold",bd="8",padx=16,pady=16,command=lambda :click(6),activebackground="green",activeforeground="white",bg="powder blue").grid(row=2,column=2)
sub=Button(root,text="-",font="arial 20 italic bold",bd="8",padx=19,pady=16,command=lambda :click("-"),activebackground="red",activeforeground="white",bg="powder blue").grid(row=2,column=3)

btn1=Button(root,text="1",font="arial 20 italic bold",bd="8",padx=16,pady=16,command=lambda :click(1),activebackground="green",activeforeground="white",bg="powder blue").grid(row=3,column=0)
btn2=Button(root,text="2",font="arial 20 italic bold",bd="8",padx=16,pady=16,command=lambda :click(2),activebackground="green",activeforeground="white",bg="powder blue").grid(row=3,column=1)
btn3=Button(root,text="3",font="arial 20 italic bold",bd="8",padx=16,pady=16,command=lambda :click(3),activebackground="green",activeforeground="white",bg="powder blue").grid(row=3,column=2)
btnmulti=Button(root,text="*",font="arial 20 italic bold",bd="8",padx=18,pady=16,command=lambda :click("*"),activebackground="red",activeforeground="white",bg="powder blue").grid(row=3,column=3)

btn0=Button(root,text="0",font="arial 20 italic bold",bd="8",padx=16,pady=16,command=lambda :click(0),activebackground="red",activeforeground="white",bg="powder blue").grid(row=4,column=0)
btnclear=Button(root,text="C",font="arial 20 italic bold",bd="8",padx=16,pady=16,command=clear,activebackground="red",activeforeground="white",bg="powder blue").grid(row=4,column=1)
btnequal=Button(root,text="=",font="arial 20 italic bold",bd="8",padx=16,pady=16,command=equal,activebackground="red",activeforeground="white",bg="powder blue").grid(row=4,column=2)
btndiv=Button(root,text="/",font="arial 20 italic bold",bd="8",padx=19,pady=16,command=lambda :click("/"),activebackground="red",activeforeground="white",bg="powder blue").grid(row=4,column=3)

btnsin=Button(root,text="Sin",font="arial 11 italic bold",bd="8",padx=18,pady=26,command=sin,activebackground="red",activeforeground="white",bg="powder blue").grid(row=0,column=4)
btncos=Button(root,text="Cos",font="arial 11 italic bold",bd="8",padx=17,pady=27,command=cos,activebackground="red",activeforeground="white",bg="powder blue").grid(row=1,column=4)
btntan=Button(root,text="Tan",font="arial 11 italic bold",bd="8",padx=17,pady=27,command=tan,activebackground="red",activeforeground="white",bg="powder blue").grid(row=2,column=4)
