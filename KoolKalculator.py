# Jose Torres
# 11/6/2019

# The goal is to create a fully functional calculator. Overtime the 'Kalculator' will
# become 'Kool' with added animations and more advanced math features.

from tkinter import *

# Handles the display of the calculator
def display():
    temp = ''
    for i in range(0, len(operators)):
        temp += operands[i] + operators[i]
    temp += operands[-1] # There is one more operands than operator
    displayLabel.config(text=temp)
    print(displayLabel.cget("text"))

maxCharOnDisplay = 17
# Appends operators into list, moves to the next operand
def operationIn(_operator):
    if len(displayLabel.cget("text")) >= maxCharOnDisplay:
        return
    operators.append(_operator)
    operands.append('')# Create a placeholder
    display()

# Performs the operation
def performOper():
    global operands
    global operators
    temp = displayLabel.cget("text")
    temp = eval(temp)
    operands = [str(temp)]
    operators = []
    display()

# Clears the last operand or all operands/operators
def clear(value):
    global operands
    global operators
    if operands == ['']:
        return
    if value == 'ce':
        operators = []
        operands = ['']
    elif operands[-1] == '':
        operands.pop()
        operators.pop()
    else:
        operands[-1] = ''
    display()

# Appends the number pressed on the calculator to the latest operand
def addNumber(value):
    global operands
    if len(displayLabel.cget("text")) >= maxCharOnDisplay:
        lastOperand = operands[-1]
        lastOperand = lastOperand[0:-1] + value
        operands[-1] = lastOperand
    else:
        operands[-1] = operands[-1] + value
    display()


if __name__ == "__main__":
    MainWindow = Tk()
    MainWindow.title("KoolKalculator")

    # Window is composed to two sections: Display and NumberPad
    # DisplayFrame
    displayLabel = Label(MainWindow)
    operands = ['']
    operators = []
    displayLabel.pack(side=TOP, expand=True, fill='both')

    # NumberPad
    numberPadFrame = Frame(MainWindow)
    numberPadFrame.pack(side=TOP, expand=True, fill='both')

    # Button List
    buttons = []
    for i in range(1, 10):
        buttons.append(Button(numberPadFrame, text=str(i), command=lambda c=i: addNumber(buttons[c-1].cget('text'))))
    zeroButton = Button(numberPadFrame, text='0', command=lambda: addNumber('0'))
    deciButton = Button(numberPadFrame, text='.', command=lambda: addNumber('.'))

    # Operation Buttons
    addButton = Button(numberPadFrame, text='+', command=lambda: operationIn('+'))
    subButton = Button(numberPadFrame, text='-', command=lambda: operationIn('-'))
    multButton = Button(numberPadFrame, text='*', command=lambda: operationIn('*'))
    divButton = Button(numberPadFrame, text='/', command=lambda: operationIn('/'))

    execButton = Button(numberPadFrame, text='ENTER', command=performOper)
    cButton = Button(numberPadFrame, text='C', command=lambda: clear('c'))
    ceButton = Button(numberPadFrame, text='CE', command=lambda: clear('ce'))

    # Place Buttons in grid
    for i in range(0, 5):
        Grid.rowconfigure(numberPadFrame, i, weight=1)
        Grid.columnconfigure(numberPadFrame, i, weight=1)

    buttons[0].grid(sticky=N+S+E+W, row=3, column=0)
    buttons[1].grid(sticky=N+S+E+W, row=3, column=1)
    buttons[2].grid(sticky=N+S+E+W, row=3, column=2)
    buttons[3].grid(sticky=N+S+E+W, row=2, column=0)
    buttons[4].grid(sticky=N+S+E+W, row=2, column=1)
    buttons[5].grid(sticky=N+S+E+W, row=2, column=2)
    buttons[6].grid(sticky=N+S+E+W, row=1, column=0)
    buttons[7].grid(sticky=N+S+E+W, row=1, column=1)
    buttons[8].grid(sticky=N+S+E+W, row=1, column=2)

    zeroButton.grid(sticky=N+S+E+W, row=4, columnspan=2)
    deciButton.grid(sticky=N+S+E+W, row=4, column=2)

    addButton.grid(sticky=N+S+E+W, row=1, column=3)
    subButton.grid(sticky=N+S+E+W, row=2, column=3)
    multButton.grid(sticky=N+S+E+W, row=3, column=3)
    divButton.grid(sticky=N+S+E+W, row=4, column=3)

    execButton.grid(sticky=N+S+E+W, row=1, rowspan=4, column=4)
    cButton.grid(sticky=N+S+E+W, row=0, columnspan=2, column=0)
    ceButton.grid(sticky=N+S+E+W, row=0, columnspan=3, column=2)

    MainWindow.mainloop()