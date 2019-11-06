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

def printButtonValue(value):
    global displayAccumulator
    displayAccumulator += int(value)
    displayFrame.config(text=str(displayAccumulator))


if __name__ == "__main__":
    MainWindow = Tk()
    MainWindow.title("KoolKalculator")

    displayFrame = Label(MainWindow)
    displayAccumulator = 0

    displayFrame.grid()
    # Button List
    buttons = []
    for i in range(0, 10):
        buttons.append(Button(text=str(i), command=lambda c=i: printButtonValue(buttons[c].cget('text'))))

    # Place Buttons in grid
    buttons[1].grid(row=3)
    buttons[2].grid(row=3, column=1)
    buttons[3].grid(row=3, column=2)
    buttons[4].grid(row=2, column=0)
    buttons[5].grid(row=2, column=1)
    buttons[6].grid(row=2, column=2)
    buttons[7].grid(row=1, column=0)
    buttons[8].grid(row=1, column=1)
    buttons[9].grid(row=1, column=2)

    MainWindow.mainloop()
