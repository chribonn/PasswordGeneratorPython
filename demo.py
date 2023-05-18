from tkinter import *

class GUI:
    def DoSomething(self):
        self.passText='Goodbye World'
        self.genPassText

    def __init__(self):
        # root window
        self.root = Tk()
        self.root.title("Demo")
        self.root.geometry("800x280")
        self.root.resizable(width=FALSE, height=FALSE)

        # pass length information
        self.genPassButton = Button(self.root, text = "Generate Password", command=self.DoSomething).grid(row=1, column=0, padx=5, pady=5)
        self.passText = StringVar(self.root, value="Hello World!")
        self.genPassText = Entry(self.root, width=50, bd=3, textvariable=self.passText).grid(row=1, column=1, padx=5, pady=5)
        
        #load the icon
        self.copy_icon = PhotoImage(file='./Assets/copy.png')
        self.img_label = Label(image=self.copy_icon)
        self.copyButton = Button(self.root, image=self.copy_icon, command=lambda:self.genPassText.event_generate("<<Copy>>")).grid(row=1, column=2)



if __name__ == '__main__':
    mainwindow = GUI()
    mainloop()
    
  