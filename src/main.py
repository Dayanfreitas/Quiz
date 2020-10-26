# -*- coding: UTF-8 -*-
from Tkinter import *

# class Frame(Tkinter.Frame):
    # def __init__(self, )
class Application:
    def __init__(self, master=None):
        master.title("Questionario de pessoas boas!")
        master.geometry('300x300')

        self.widget1 = Frame(master)
        self.widget1.pack()



        self.sair = Button(self.widget1)
        self.sair["text"] = "Finalizar"
        self.sair["width"] = 20
        self.sair["command"] = self.destroy
        self.sair.pack()

root = Tk()
Application(root)
root.mainloop()