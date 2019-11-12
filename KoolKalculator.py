# Jose Torres
# 11/6/2019

# The goal is to create a fully functional calculator. Overtime the 'Kalculator' will
# become 'Kool' with added animations and more advanced math features.

from tkinter import *


def display():
    '''Handles the display of the calculator'''
    temp = ''
    for i in range(0, len(operators)):
        temp += operands[i] + operators[i]
    temp += operands[-1]  # There is one more operands than operator
    displayLabel.config(text=temp)


def operationIn(_operator):
    '''Appends operators into list, moves to the next operand'''
    if len(displayLabel.cget("text")) >= maxCharOnDisplay:
        return
    operators.append(_operator)
    operands.append('')  # Create a placeholder
    display()


def performOper():
    '''Performs the operation by evaluating the string expression'''
    global operands
    global operators
    temp = displayLabel.cget("text")
    temp = eval(temp)
    operands = [str(temp)]
    operators = []
    display()


def clear(value):
    '''Clears the last expression('c') or all operands/operators('ce')'''
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


def addNumber(value):
    '''Appends the number pressed on the calculator to the latest operand'''
    global operands
    if len(displayLabel.cget("text")) >= maxCharOnDisplay:
        lastOperand = operands[-1]
        lastOperand = lastOperand[0:-1] + value
        operands[-1] = lastOperand
    else:
        operands[-1] = operands[-1] + value
    display()


def darkMode():
    global buttons
    global operationButtons
    global miscButton
    global displayLabel
    global menu
    global submenu

    menu.config(bg='black', fg='white')
    submenu.config(bg='black', fg='white')

    for button in buttons:
        button.config(bg='black', fg='white')
    for button in operationButtons:
        button.config(bg='black', fg='white')
    for button in miscButton:
        button.config(bg='black', fg='white')
    displayLabel.config(bg='black', fg='white')
    statusLabel.config(bg='black', fg='white')


if __name__ == "__main__":
    MainWindow = Tk()
    MainWindow.title("KoolKalculator")

    # Window is composed to four sections: Toolbar, Display, NumberPad and Status bar
    # Toolbar
    menu = Menu(MainWindow)
    MainWindow.config(menu=menu)
    submenu = Menu(menu)
    menu.add_cascade(label='File', menu=submenu)
    submenu.add_command(label="DARK MODE", command=darkMode)
    submenu.add_separator()

    # DisplayFrame
    displayLabel = Label(MainWindow, font={15})
    operands = ['']
    operators = []
    maxCharOnDisplay = 17
    displayLabel.pack(side=TOP, expand=True, fill='both', ipadx='10', ipady='15')

    # NumberPad
    numberPadFrame = Frame(MainWindow)
    numberPadFrame.pack(side=TOP, expand=True, fill='both')

    # Button List
    buttons = []
    for i in range(1, 10):
        buttons.append(Button(numberPadFrame, text=str(i), command=lambda c=i: addNumber(buttons[c - 1].cget('text'))))
    buttons.append(Button(numberPadFrame, text='0', command=lambda: addNumber('0')))  # 10
    buttons.append(Button(numberPadFrame, text='.', command=lambda: addNumber('.')))  # 11

    # Operation Buttons
    operationButtons = [Button(numberPadFrame, text='+', command=lambda: operationIn('+')),
                        Button(numberPadFrame, text='-', command=lambda: operationIn('-')),
                        Button(numberPadFrame, text='*', command=lambda: operationIn('*')),
                        Button(numberPadFrame, text='/', command=lambda: operationIn('/'))]

    miscButton = [Button(numberPadFrame, text='ENTER', command=performOper),
                  Button(numberPadFrame, text='C', command=lambda: clear('c')),
                  Button(numberPadFrame, text='CE', command=lambda: clear('ce'))]

    # Place Buttons in grid
    for i in range(0, 5):
        Grid.rowconfigure(numberPadFrame, i, weight=1)
        Grid.columnconfigure(numberPadFrame, i, weight=1)

    for i in range(0, 9):
        buttons[i].grid(sticky=N + S + E + W, row=3 - int(i / 3), column=i % 3)
    buttons[9].grid(sticky=N + S + E + W, row=4, columnspan=2)  # zero
    buttons[10].grid(sticky=N + S + E + W, row=4, column=2)  # decimal

    for i in range(0, 4):
        operationButtons[i].grid(sticky=N + S + E + W, row=1 + i, column=3)

    miscButton[0].grid(sticky=N + S + E + W, row=1, rowspan=4, column=4)  # Execution Button("Enter")
    miscButton[1].grid(sticky=N + S + E + W, row=0, columnspan=2, column=0)  # Clear Button("c")
    miscButton[2].grid(sticky=N + S + E + W, row=0, columnspan=3, column=2)  # Clear Everything("ce")

    statusLabel = Label(MainWindow, text="Status")
    statusLabel.pack(side=BOTTOM, fill=X)

    MainWindow.mainloop()