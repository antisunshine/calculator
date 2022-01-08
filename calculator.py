"""Simple calculator
   Susanne Koljonen 28.11.2021"""

from tkinter import *

root = Tk()
root.title("Calculator")


# functions

def buttonClick(number):
    current = entryBox.get()
    entryBox.delete(0, END)
    entryBox.insert(0, str(current) + str(number))


def buttonClear():
    entryBox.delete(0, END)


def buttonAdd():
    firstNo = entryBox.get()
    global fNum
    global math
    math = "+"
    fNum = int(firstNo)
    entryBox.delete(0, END)


def buttonSub():
    firstNo = entryBox.get()
    global fNum
    global math
    math = "-"
    fNum = int(firstNo)
    entryBox.delete(0, END)


def buttonDiv():
    firstNo = entryBox.get()
    global fNum
    global math
    math = "/"
    fNum = int(firstNo)
    entryBox.delete(0, END)


def buttonMul():
    firstNo = entryBox.get()
    global fNum
    global math
    math = "*"
    fNum = int(firstNo)
    entryBox.delete(0, END)


def buttonEqual():
    secondNo = entryBox.get()
    entryBox.delete(0, END)
    if math == "+":
        entryBox.insert(0, fNum + int(secondNo))
    elif math == "-":
        entryBox.insert(0, fNum - int(secondNo))
    elif math == "*":
        entryBox.insert(0, fNum * int(secondNo))
    elif math == "/":
        if int(secondNo) == 0:
            entryBox.insert(0, "ERROR!")
        else:
            entryBox.insert(0, fNum / int(secondNo))


# entry widgets
entryBox = Entry(root, width=40, borderwidth=5)

# button widgets
button1 = Button(root, text="1", padx=40, pady=20, command=lambda: buttonClick(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: buttonClick(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: buttonClick(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: buttonClick(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: buttonClick(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: buttonClick(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: buttonClick(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: buttonClick(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: buttonClick(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: buttonClick(0))

buttonPlus = Button(root, text="+", padx=39, pady=20, command=buttonAdd)
buttonMinus = Button(root, text="-", padx=40, pady=20, command=buttonSub)
buttonMultiply = Button(root, text="*", padx=41, pady=20, command=buttonMul)
buttonDivide = Button(root, text="/", padx=41, pady=20, command=buttonDiv)
buttonEqual = Button(root, text="=", padx=70, pady=20, command=buttonEqual)

clearButton = Button(root, text="CLEAR", padx=24, pady=20, command=buttonClear)

# shove in program
entryBox.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

buttonPlus.grid(row=4, column=0)
button0.grid(row=4, column=1)
buttonMinus.grid(row=4, column=2)

buttonMultiply.grid(row=5, column=0)
buttonDivide.grid(row=5, column=1)
clearButton.grid(row=5, column=2)

buttonEqual.grid(row=6, column=0, columnspan = 3)
# main loop
root.mainloop()
