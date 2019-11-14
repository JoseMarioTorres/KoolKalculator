from tkinter import *
from KoolKalculator import *


class SimpleCalc(KoolKalculator):
    
    def __init__(self):
        super().__init__()

        # NumberPad
        self.numberPadFrame = Frame(self.root)
        self.numberPadFrame.pack(side=TOP, expand=True, fill='both')

        # Button List
        self.buttons = []
        for i in range(1, 10):
            self.buttons.append(Button(self.numberPadFrame, text=str(i), command=lambda c=i: self.addNumber(self.buttons[c - 1].cget('text'))))
        self.buttons.append(Button(self.numberPadFrame, text='0', command=lambda: self.addNumber('0')))  # 10
        self.buttons.append(Button(self.numberPadFrame, text='.', command=lambda: self.addNumber('.')))  # 11

        # Operation Buttons
        self.operationButtons = [Button(self.numberPadFrame, text='+', command=lambda: self.operationIn('+')),
                            Button(self.numberPadFrame, text='-', command=lambda: self.operationIn('-')),
                            Button(self.numberPadFrame, text='*', command=lambda: self.operationIn('*')),
                            Button(self.numberPadFrame, text='/', command=lambda: self.operationIn('/'))]

        self.miscButton = [Button(self.numberPadFrame, text='ENTER', command=self.performOper),
                      Button(self.numberPadFrame, text='C', command=lambda: self.clear('c')),
                      Button(self.numberPadFrame, text='CE', command=lambda: self.clear('ce'))]

        # Place Buttons in grid
        for i in range(0, 5):
            Grid.rowconfigure(self.numberPadFrame, i, weight=1)
            Grid.columnconfigure(self.numberPadFrame, i, weight=1)

        for i in range(0, 9):
            self.buttons[i].grid(sticky=N + S + E + W, row=3 - int(i / 3), column=i % 3)
        self.buttons[9].grid(sticky=N + S + E + W, row=4, columnspan=2)  # zero
        self.buttons[10].grid(sticky=N + S + E + W, row=4, column=2)  # decimal

        for i in range(0, 4):
            self.operationButtons[i].grid(sticky=N + S + E + W, row=1 + i, column=3)

        self.miscButton[0].grid(sticky=N + S + E + W, row=1, rowspan=4, column=4)  # Execution Button("Enter")
        self.miscButton[1].grid(sticky=N + S + E + W, row=0, columnspan=2, column=0)  # Clear Button("c")
        self.miscButton[2].grid(sticky=N + S + E + W, row=0, columnspan=3, column=2)  # Clear Everything("ce")

        # Status Bar
        self.statusLabel = Label(self.root, text="Status")
        self.statusLabel.pack(side=BOTTOM, fill=X)

        self.begin()

if __name__ == '__main__':
    SimpleCalc()