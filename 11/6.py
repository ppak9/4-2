from tkinter import *
from math import *
import tkinter.messagebox
  
root = Tk()
root.title("Calculator")
root.configure(background = 'white')
root.resizable(width=True, height=True)
root.geometry("480x568+450+90")
calc = Frame(root)
calc.grid()


#----------------- Declare Class that use for the Calculator -------------

class Calc():
    def __init__(self):
        self.total=0                                                # for use total value
        self.current=''                                             # for use the current value + use for display in the entry value
        self.input_value=True
        self.check_sum=False
        self.op=''
        self.result=False
        self.check_sum = False
  
    def numberEnter(self, num):
        self.result=False
        firstnum=txtDisplay.get()
        secondnum=str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value=False
        else:                                                       # showing the float number
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)
  
    def sum_of_total(self):
        self.result=True
        self.current=float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:                                                        # get the result for trigonometric function
            self.total=float(txtDisplay.get())
  
    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)
  
    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value=True
        self.check_sum=False
        self.display(self.total)
  
    def operation(self, op):                                           # self is for using function and op is the call that wanted
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result=False
  
    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value=True
  
    def All_Clear_Entry(self):
        self.Clear_Entry()
        self.total=0

    def cos(self):
        self.result = False
        self.current = cos(radians(float(txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = tan(radians(float(txtDisplay.get())))
        self.display(self.current)
    
    def sin(self):
        self.result = False
        self.current = sin(radians(float(txtDisplay.get())))
        self.display(self.current)

added_value = Calc()
txtDisplay = Entry(calc, font=('Helvetica',20,'bold'),
                   bg='black',fg='white',
                   bd=30,width=28,justify=RIGHT)
txtDisplay.grid(row=0,column=0, columnspan=4, pady=1)
txtDisplay.insert(0,"0")


numberpad = "789456123"
i=0
btn = []

for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2,
                          bg='black',fg='white',
                          font=('Helvetica',20,'bold'),
                          bd=4,text=numberpad[i]))
        btn[i].grid(row=j, column= k, pady = 1)                                             #row = 2,3,4 column = 0,1,2
        btn[i]["command"]= lambda x = numberpad[i]:added_value.numberEnter(x)
        i+=1




# ---------- Declare the Button ------------ 

btnClear = Button(calc, text=chr(67),width=6,
                  height=2,bg='powder blue',
                  font=('Helvetica',20,'bold')
                  ,bd=4, command=added_value.Clear_Entry
                 ).grid(row=1, column= 0, pady = 1)
  
btnAllClear = Button(calc, text=chr(67)+chr(69),
                     width=6, height=2,
                     bg='powder blue', 
                     font=('Helvetica',20,'bold'),
                     bd=4,
                     command=added_value.All_Clear_Entry
                    ).grid(row=1, column= 1, pady = 1)

btnAdd = Button(calc, text="+",width=6, height=2,
                bg='powder blue',
                font=('Helvetica',20,'bold'),
                bd=4,command=lambda:added_value.operation("add")
                ).grid(row=1, column= 3, pady = 1)
  
btnSub = Button(calc, text="-",width=6,
                height=2,bg='powder blue',
                font=('Helvetica',20,'bold'),
                bd=4,command=lambda:added_value.operation("sub")
                ).grid(row=2, column= 3, pady = 1)
  
btnMul = Button(calc, text="x",width=6, 
                height=2,bg='powder blue', 
                font=('Helvetica',20,'bold'),
                bd=4,command=lambda:added_value.operation("multi")
                ).grid(row=3, column= 3, pady = 1)
  
btnDiv = Button(calc, text="/",width=6, 
                height=2,bg='powder blue',
                font=('Helvetica',20,'bold'),
                bd=4,command=lambda:added_value.operation("divide")
                ).grid(row=4, column= 3, pady = 1)
  
btnZero = Button(calc, text="0",width=6,
                 height=2,bg='black',fg='white',
                 font=('Helvetica',20,'bold'),
                 bd=4,command=lambda:added_value.numberEnter(0)
                 ).grid(row=5, column= 0, pady = 1)

btnDot = Button(calc, text=".",width=6,
                height=2,bg='powder blue', 
                font=('Helvetica',20,'bold'),
                bd=4,command=lambda:added_value.numberEnter(".")
                ).grid(row=5, column= 1, pady = 1)

btnEquals = Button(calc, text="=",width=6,
                   height=2,bg='powder blue',
                   font=('Helvetica',20,'bold'),
                   bd=4,command=added_value.sum_of_total
                  ).grid(row=5, column= 3, pady = 1)

btnCos = Button(calc, text="Cos",width=6, 
                height=2,bg='black',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=added_value.cos
               ).grid(row=6, column= 1, pady = 1)
  
btntan = Button(calc, text="tan",width=6, 
                height=2,bg='black',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=added_value.tan
               ).grid(row=6, column= 2, pady = 1)
  
btnsin = Button(calc, text="sin",width=6,
                height=2,bg='black',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=added_value.sin
               ).grid(row=6, column= 3, pady = 1)

