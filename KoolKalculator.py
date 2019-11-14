# Jose Torres
# 11/6/2019

# The goal is to create a fully functional calculator. Overtime the 'Kalculator' will
# become 'Kool' with added animations and more advanced math features.

from tkinter import *

class KoolKalculator:
    '''An abstract calculator that contains the minimum attributes'''

    def __init__(self):
        '''Each Calculator will contain the same toolbar and Display'''
        self.root = Tk()
        self.root.title("KoolKalculator")
        
        # Tool Bar
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)
        self.submenu = Menu(self.menu)
        self.menu.add_cascade(label='File', menu=self.submenu)
        self.submenu.add_command(label="DARK MODE", command=self.darkMode)
        self.submenu.add_separator()
    
        # DisplayFrame
        self.displayLabel = Label(self.root, font={15})
        self.operands = ['']
        self.operators = []
        self.maxCharOnDisplay = 17
        self.displayLabel.pack(side=TOP, expand=True, fill='both', ipadx='10', ipady='15')


    def begin(self):
        self.root.mainloop()


    def display(self):
        '''Handles the display of the calculator'''
        temp = ''
        for i in range(0, len(self.operators)):
            temp += self.operands[i] + self.operators[i]
        temp += self.operands[-1]  # There is one more operands than operator
        self.displayLabel.config(text=temp)


    def operationIn(self, operator):
        '''Appends operators into list, moves to the next operand'''
        if len(self.displayLabel.cget("text")) >= self.maxCharOnDisplay:
            return
        self.operators.append(operator)
        self.operands.append('')  # Create a placeholder
        self.display()


    def performOper(self):
        '''Performs the operation by evaluating the string expression'''

        temp = self.displayLabel.cget("text")
        temp = eval(temp)
        self.operands = [str(temp)]
        self.operators = []
        self.display()

    def clear(self, value):
        '''Clears the last expression('c') or all operands/operators('ce')'''

        if self.operands == ['']:
            return
        if value == 'ce':
            self.operators = []
            self.operands = ['']
        elif self.operands[-1] == '':
            self.operands.pop()
            self.operators.pop()
        else:
            self.operands[-1] = ''
        self.display()

    def addNumber(self, value):
        '''Appends the number pressed on the calculator to the latest operand'''
        if len(self.displayLabel.cget("text")) >= self.maxCharOnDisplay:
            lastOperand = self.operands[-1]
            lastOperand = lastOperand[0:-1] + value
            self.operands[-1] = lastOperand
        else:
            self.operands[-1] = self.operands[-1] + value
        self.display()

    def darkMode(self):
        '''A classic aesthetic feature'''
        self.menu.config(bg='black', fg='white')
        self.submenu.config(bg='black', fg='white')

        for button in self.buttons:
            button.config(bg='black', fg='white')
        for button in self.operationButtons:
            button.config(bg='black', fg='white')
        for button in self.miscButton:
            button.config(bg='black', fg='white')
        self.displayLabel.config(bg='black', fg='white')
        self.statusLabel.config(bg='black', fg='white')