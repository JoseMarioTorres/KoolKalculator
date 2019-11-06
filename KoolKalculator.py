# Jose Torres
# 11/6/2019

# The goal is to create a fully functional calculator. Overtime the 'Kalculator' will
# become 'Kool' with added animations and more advanced math features.

from tkinter import *

# Ignore Comments, skip to main.

# Label(MainWindow, text='name', sticky=E)
# CheckButton(MainWindow, text='name')
# Entry(MainWindow)

# Drop Down menu
# Menu = Menu(menu)
# root.config(menu=menu)
# subMenu = Menu(menu)
# menu.add_cascade(label="File", menu=subMenu)
# subMenu.add_command(label="New Project...", command="")
# subMenu.add_separator()

# editMenu = Menu(menu)
# menu.add_cascade(label="Edit", menu=editMenu)

# Handles the display when buttons are pressed
def printButton(value):
    global displayAccumulator
    if len(displayAccumulator) >= 8:
        displayAccumulator = displayAccumulator[0:-1] + value
    else:
        displayAccumulator += str(value)
    displayLabel.config(text=str(displayAccumulator))

#def operationIn():



if __name__ == "__main__":
    MainWindow = Tk()
    MainWindow.title("KoolKalculator")

    #Grid.rowconfigure(MainWindow, 1, weight=1)
    #Grid.columnconfigure(MainWindow, 0, weight=1)

    # Window is composed to two sections: Display and NumberPad
    # DisplayFrame
    displayLabel = Label(MainWindow)
    displayAccumulator = ''
    displayLabel.pack(side=TOP, expand=True, fill='both')

    # NumberPad
    numberPadFrame = Frame(MainWindow)
    numberPadFrame.pack(side=TOP, expand=True, fill='both')

    # Button List
    buttons = []
    for i in range(1, 10):
        buttons.append(Button(numberPadFrame, text=str(i), command=lambda c=i: printButton(buttons[c-1].cget('text'))))
    zeroButton = Button(numberPadFrame, text='0', command=lambda: printButton('0'))
    deciButton = Button(numberPadFrame, text='.', command=lambda: printButton('0.1'))

    # Operation Buttons
    plusButton = Button(numberPadFrame, text='+')
    minusButton = Button(numberPadFrame, text='-')
    multButton = Button(numberPadFrame, text='x')
    divButton = Button(numberPadFrame, text='/')

    # Place Buttons in grid
    for i in range(0, 4):
        Grid.rowconfigure(numberPadFrame, i, weight=1)
        Grid.columnconfigure(numberPadFrame, i, weight=1)

    buttons[0].grid(sticky=N+S+E+W, row=2, column=0)
    buttons[1].grid(sticky=N+S+E+W, row=2, column=1)
    buttons[2].grid(sticky=N+S+E+W, row=2, column=2)
    buttons[3].grid(sticky=N+S+E+W, row=1, column=0)
    buttons[4].grid(sticky=N+S+E+W, row=1, column=1)
    buttons[5].grid(sticky=N+S+E+W, row=1, column=2)
    buttons[6].grid(sticky=N+S+E+W, row=0, column=0)
    buttons[7].grid(sticky=N+S+E+W, row=0, column=1)
    buttons[8].grid(sticky=N+S+E+W, row=0, column=2)

    zeroButton.grid(sticky=N+S+E+W, row=3, columnspan=2)
    deciButton.grid(sticky=N+S+E+W, row=3, column=2)

    plusButton.grid(sticky=N+S+E+W, row=0, column=3)
    minusButton.grid(sticky=N+S+E+W, row=1, column=3)
    multButton.grid(sticky=N+S+E+W, row=2, column=3)
    divButton.grid(sticky=N+S+E+W, row=3, column=3)

    MainWindow.mainloop()