#from tkinter import *
import tkinter as tk
'''class Window(Frame) #inherits base class Frame;multiple inheritance is possible:

    def __init__(self,master=None):
        Frame.__init__(self,master) #Constructor initialization

        self.master=master

        self.init_window()
        
    def init_window(self):

        self.master.title("Tkinter GUI")
        self.pack(fill=BOTH, expand=1)

        quitButton= Button(self,text="Quit", command=self.client_exit)
        quitButton.place(x=180, y=120)

        menu= Menu(self.master)
        self.master.config(menu=menu)
        
        file= Menu(menu)
        file.add_command(label='Save',command=self.client_exit)
        file.add_command(label='Exit',command=self.client_exit)
        menu.add_cascade(label='File', menu=file)
        
        edit= Menu(menu)
        edit.add_command(label='Undo')
        menu.add_cascade(label='Edit',menu=edit)

    def client_exit(self):
        exit()
        
root= Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()'''

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
