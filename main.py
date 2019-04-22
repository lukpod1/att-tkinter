from tkinter import *
from tkinter import ttk
from tkinter import filedialog

# root = Tk()

# photo = PhotoImage(file = "./img/tela.png")
# label = Label(root, image = photo)
# label.pack()

# root.mainloop()

class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.labelFrame = ttk.LabelFrame(self, text = "Open a file")
        self.labelFrame.grid(column = 0, row = 1, padx = 20, pady = 20)

        self.button()
    
    def button(self):
        self.button = ttk.Button(self.labelFrame, text = "Browser a file", command = self.fileDialog)
        self.button.grid(column = 1, row = 1)

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir = "./img/", title = "Select a file", filetypes = (("jpeg", "*.jpg"),("png", "*.png"), ("All Files", "*.*")))
        self.label = ttk.Label(self.labelFrame, text = "")
        self.label.grid(column = 1, row = 2)
        self.myimage = PhotoImage(file = self.filename)
        self.upimage = Label(self, image=self.myimage)
        self.upimage.pack()
        # self.label.configure(text = self.filename)

if __name__== "__main__":
    root = Window()
    root.mainloop()
# root = Tk()

# Window(root)

# root.mainloop()