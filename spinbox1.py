from tkinter import *
import random, string, pyperclip


def passwdgen(passLen: int, useDigits: bool, useLower: bool, useUpper: bool, useSpecial: bool, firstAlfaNum: bool, hideAmbiguous: bool):
    """
    Generates a password of the desired length based on the passed parameters.

    Args:
        passLen (int): password length
        useDigits (bool): should the password use [0-9]
        useLower (bool): should the password use [a-z]
        useUpper (bool): should the password use [A-Z]
        useSpecial (bool): should the password use special characters
        firstAlfaNum (bool): Does the first digit of the password have to be alfanumeric (not symbol)
        hideAmbiguous (bool): Should characters that can be misread be dropped.

    Returns:
        string: generated_password
    """
    random.seed()
    
    output = ""
    symbol_pool = ""
    if passLen < 1:
        return output
    
    if useDigits:
        symbol_pool += string.digits
    
    if useLower:
        symbol_pool += string.ascii_lowercase
    
    if useUpper:
        symbol_pool += string.ascii_uppercase
    
    # The user's selection cannot generate the requested password
    if firstAlfaNum:
        if symbol_pool:
            output = "".join(random.sample(symbol_pool, 1))
            passLen -= 1
        else:
            # There are no characters to generate a password from
            return output
        
    if useSpecial:
        symbol_pool += """`~!@#$%^&*()_-+={}[]\|:;"'<>,.?/"""
        
    if hideAmbiguous:
        # the following are being considered ambiguous
        # l, I, O, 0, 1
        
        ambiguous = ['l', 'I', 'O', '0', '1']
        for char in ambiguous:
            if char in symbol_pool:
                symbol_pool = symbol_pool.replace(char, '')

    if symbol_pool:
        return output + "".join(random.choices(symbol_pool, k=passLen)) if symbol_pool else ""
    else:
        # There are no characters to generate a password from
        return output


class GUI:
    """
    Handles the GUI interface mechanism
    """    

    def GeneratePass(self):
        generatedPass = passwdgen(
                self.passLen.get(), 
                self.digits.get(), 
                self.lowChars.get(), 
                self.upChars.get(), 
                self.specChars.get(), 
                self.fristAlfaNum.get(), 
                self.hideAmbiguousChars.get()
            )
        self.passText.set(value=generatedPass)
        pyperclip.copy(generatedPass)
        
      
        
    def ValidateIfNum(self):
        user_input = self.passLen.get()
        # disallow anything but numbers in the input
        valid = isinstance(user_input, int)
        # perform range checking
        # if valid:
        #     # get minimum and maximum values of the widget to be validated
        #     minval = int(self.passLenSb.config('from_')[4])
        #     maxval = int(self.passLenSb.config('to')[4])
        #     # check if it's in range
        #     if user_input not in range (minval, maxval):
        #         valid = False
        return valid

    def __init__(self):
        """_summary_
        """        
        # root window
        self.root = Tk()
        self.root.title("Password Generator")
        self.root.geometry("800x320")
        self.root.resizable(width=FALSE, height=FALSE)

        # pass length information
        self.passTitle = Label(self.root, text = "Passowrd Length: ").grid(row=0, column=0, padx=5, pady=5, sticky=E)
        self.passLen = IntVar(value=20)
        self.passLenSb = Spinbox(
            self.root, 
            from_=1, 
            to=100, 
            textvariable=self.passLen, 
            width=10, 
            justify=CENTER, 
            bd=3, 
            command=self.ValidateIfNum
            ).grid(row=0, column=1, padx=5, pady=5)

        self.digitsLabel = Label(self.root, text = "Use Numbers: ").grid(row=1, column=0, padx=5, pady=5, sticky=E)
        self.digits = IntVar(value=1)
        Checkbutton(self.root, width=10, variable=self.digits).grid(row=1, column=1)

        self.lowCharsLabel = Label(self.root, text = "Use lower letters: ").grid(row=2, column=0, padx=5, pady=5, sticky=E)
        self.lowChars = IntVar(value=1)
        Checkbutton(self.root, width=10, variable=self.lowChars).grid(row=2, column=1)

        self.upCharsLabel = Label(self.root, text = "Use upper letters: ").grid(row=3, column=0, padx=5, pady=5, sticky=E)
        self.upChars = IntVar(value=1)
        Checkbutton(self.root, width=10, variable=self.upChars).grid(row=3, column=1)

        self.specCharsLabel = Label(self.root, text = "Use special characters: ").grid(row=4, column=0, padx=5, pady=5, sticky=E)
        self.specChars = IntVar(value=1)
        Checkbutton(self.root, width=10, variable=self.specChars).grid(row=4, column=1)

        self.fristAlfaNumLabel = Label(self.root, text = "Force 1st char as number / letter: ").grid(row=5, column=0, padx=5, pady=5, sticky=E)
        self.fristAlfaNum = IntVar(value=1)
        Checkbutton(self.root, width=10, variable=self.fristAlfaNum).grid(row=5, column=1)

        self.hideAmbiguousLabel = Label(self.root, text = "Avoid Confusing Characters: ").grid(row=6, column=0, padx=5, pady=5, sticky=E)
        self.hideAmbiguousChars = IntVar(value=0)
        Checkbutton(self.root, width=10, variable=self.hideAmbiguousChars).grid(row=6, column=1)
        
        # pass length information
        self.genPassButton = Button(self.root, text = "Generate Password", command=self.GeneratePass).grid(row=8, column=0, padx=5, pady=5)
        generatedPass = passwdgen(
            self.passLen.get(), 
            self.digits.get(), 
            self.lowChars.get(), 
            self.upChars.get(), 
            self.specChars.get(), 
            self.fristAlfaNum.get(), 
            self.hideAmbiguousChars.get()
            )
        pyperclip.copy(generatedPass)
        self.passText = StringVar(value=generatedPass)
        self.genPassText = Entry(self.root, width=50, bd=3, font=('Bold'), textvariable=self.passText).grid(row=8, column=1, padx=5, pady=5)
        
        #load the icon
        self.copy_icon = PhotoImage(file='./Assets/copy.png')
        self.img_label = Label(image=self.copy_icon)
        self.copyButton = Button(self.root, image=self.copy_icon, command=lambda:pyperclip.copy(self.passText.get())).grid(row=8, column=2)
        
        # display note that text is automatically copied to the clipboard
        self.img_label = Label(self.root, text = "Password copied to clipboard").grid(row=9, column=0, columnspan=3, padx=5, pady=5)
        self.copyButton = Button(self.root, image=self.copy_icon, command=lambda:pyperclip.copy(self.passText.get())).grid(row=8, column=2)


if __name__ == '__main__':
    mainwindow = GUI()
    mainloop()
    
  