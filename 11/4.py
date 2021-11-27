from tkinter import*
import math

cal = Tk()
cal.title("Calculator")
operator= ""
text_Input = StringVar()

txtDisplay = Entry(cal, font=('fixedsys', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                    bg='Orange', justify='right')
txtDisplay.grid(columnspan=4)


def btnClick(number):
    global operator
    operator = operator + str(number)
    text_Input.set(operator)

def btnClear():
    global opderator
    operator=''
    text_Input.set('')

def btnEquals():
    global operator
    result = str(eval(operator))
    text_Input.set(result)
    operator=''

class Calc():
    def __init__(self):
        self.total=0
        self.total=""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def btnsin(self):
        self.result = False
        self.current = math.sin(float(txtDisplay.get()))
        self.display(self.current)

    def btncos(self):
        self.result = False
        self.current = math.cos(float(txtDisplay.get()))
        self.display(self.current)

    def btntan(self):
        self.result = False
        self.current = math.tan(float(txtDisplay.get()))
        self.display(self.current)



added_value = Calc()

#SIN, COS AND TAN BUTTONS
btnsin=Button(cal, padx=16, pady=16, bd=8, fg='white', font=('fixedsys', 20, 'bold'),
            text='Sin', bg='Blue', command=added_value.btnsin).grid(row=1, column=0)

btncos=Button(cal, padx=16, pady=16, bd=8, fg='white', font=('fixedsys', 20, 'bold'),
            text='Cos', bg='Blue', command=added_value.btncos).grid(row=1, column=1)

btntan=Button(cal, padx=16, pady=16, bd=8, fg='white', font=('fixedsys', 20, 'bold'),
            text='Tan', bg='Blue', command=added_value.btntan).grid(row=1, column=2)

#Buttons

btn7=Button(cal, padx=16, pady=16, bd=8, fg='white', font=('fixedsys', 20, 'bold'),
            text='7', bg='Blue', command=lambda:btnClick(7)).grid(row=2, column=0)

btn8=Button(cal, padx=16, pady=16, bd=8, fg='white', font=('fixedsys', 20, 'bold'),
            text='8', bg='Blue', command=lambda:btnClick(8)).grid(row=2, column=1)

btn9=Button(cal, padx=16, pady=16, bd=8, fg='white', font=('fixedsys', 20, 'bold'),
            text='9', bg='Blue', command=lambda:btnClick(9)).grid(row=2, column=2)

btnAdd=Button(cal, padx=16, pady=16, bd=8, fg='white', font=('fixedsys', 20, 'bold'),
            text='+', bg='Blue', command=lambda:btnClick('+')).grid(row=2, column=3)

#MoreButtons

btn4=Button(cal, padx=16, pady=16, bd=8, fg='white', font=('fixedsys', 20, 'bold'),
            text='4', bg='Blue', command=lambda:btnClick(4)).grid(row=3, column=0)

btn5=Button(cal, padx=16, pady=16, bd=8, fg='white', font=('fixedsys', 20, 'bold'),
            text='5', bg='Blue', command=lambda:btnClick(5)).grid(row=3, column=1)

btn6=Button(cal, padx=16, pady=16, bd=8, fg='white', font=('fixedsys', 20, 'bold'),
            text='6', bg='Blue', command=lambda:btnClick(6)).grid(row=3, column=2)

btnSub=Button(cal, padx=16, pady=16, bd=8, fg='white', font=('fixedsys', 20, 'bold'),
            text='-', bg='Blue', command=lambda:btnClick('-')).grid(row=3, column=3)

#MoreButtons2

btn1=Button(cal, padx=16, pady=16, bd=8, fg='black', font=('fixedsys', 20, 'bold'),
            text='1', bg='Yellow', command=lambda:btnClick(1)).grid(row=4, column=0)

btn2=Button(cal, padx=16, pady=16, bd=8, fg='black', font=('fixedsys', 20, 'bold'),
            text='2', bg='Yellow', command=lambda:btnClick(2)).grid(row=4, column=1)

btn3=Button(cal, padx=16, pady=16, bd=8, fg='black', font=('fixedsys', 20, 'bold'),
            text='3', bg='Yellow', command=lambda:btnClick(3)).grid(row=4, column=2)

btnTimes=Button(cal, padx=16, pady=16, bd=8, fg='black', font=('fixedsys', 20, 'bold'),
            text='x', bg='Yellow', command=lambda:btnClick('*')).grid(row=4, column=3)

#MoreButtons3

btn0=Button(cal, padx=16, pady=16, bd=8, fg='black', font=('fixedsys', 20, 'bold'),
            text='0', bg='Yellow', command=lambda:btnClick(0)).grid(row=5, column=0)

btnClear=Button(cal, padx=16, pady=16, bd=8, fg='black', font=('fixedsys', 20, 'bold'),
            text='C', bg='Yellow', command=btnClear).grid(row=5, column=1)

btnEquals=Button(cal, padx=16, pady=16, bd=8, fg='black', font=('fixedsys', 20, 'bold'),
            text='=', bg='Yellow', command=btnEquals).grid(row=5, column=2)

btnDivide=Button(cal, padx=16, pady=16, bd=8, fg='black', font=('fixedsys', 20, 'bold'),
            text='/', bg='Yellow', command=lambda:btnClick('/')).grid(row=5, column=3)


#End Main Loop
cal.mainloop()