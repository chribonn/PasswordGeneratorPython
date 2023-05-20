from tkinter import *


class GUI:
    """
    Handles the GUI interface
    """   
    
    def __init__(self):
        """_summary_
        """        
        # root window
        self.root = Tk()
        self.root.title("Password Generator")
        self.root.geometry("800x300")
        self.root.resizable(width=FALSE, height=FALSE)

        # registering validation command
        vldt_ifnum_cmd = (self.root.register(self.ValidateIfNum),'%P', '%W')
 
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
            validate='focusout', 
            validatecommand=vldt_ifnum_cmd
            ).grid(row=0, column=1, padx=5, pady=5)

        self.Note = Label(self.root, text = "Press TAB to lose focus on Spinbox").grid(row=8, column=2)
      
        
    def ValidateIfNum(self, user_input, widget_name):
        # disallow anything but numbers in the input
        valid = user_input.isdigit()
        # now that we've ensured the input is only integers, range checking!
        if valid:
            # get minimum and maximum values of the widget to be validated
            minval = int(self.root.nametowidget(widget_name).config('from')[4])
            maxval = int(self.root.nametowidget(widget_name).config('to')[4])
            # check if it's in range
            if int(user_input) not in range (minval, maxval):
                valid = False
        if not valid:
            # reset the value to the original 
            self.passLen = IntVar(value=20) 
        return valid


if __name__ == '__main__':
    mainwindow = GUI()
    mainloop()
    
  