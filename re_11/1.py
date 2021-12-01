from tkinter import *
from math import *


window = Tk()
window.title("My Calculator")
display = Entry(window, width=33, bg="yellow").grid(row=0, column=0, columnspan=8)
 
button_list = [
'7', '8', '9', '/', 'C',
'4', '5', '6', '*', 'sin',
'1', '2', '3', '-', 'cos',
'0', '.', '=', '+', 'tan' ]

# ----- Basic Frame ----- #
def click(key):
    if key == "=":
        result = eval(display.get())
        display.insert(END, str(result))
    elif key == "sin":
        result = int(display.get())
        display.delete(0,END)
        display.insert(END, sin(radians(result)))
    else:
        display.insert(END, key)
 
row_index = 1
col_index = 0
 
for button_text in button_list:
    def process(b = button_text):
        click(b)
    Button(window, text=button_text, width=5,
           command=process).grid(row=row_index, column=col_index)
    col_index += 1
    if col_index > 4:
        row_index += 1
        col_index = 0
        
"""
Reference: https://076923.github.io/posts/Python-tkinter-4/
"""