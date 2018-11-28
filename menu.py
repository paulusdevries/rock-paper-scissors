from tkinter import *


class Menuutje:

    def __init__(self, master):
        menu = Menu(master)
        master.config(menu=menu)

        subMenu = Menu(menu)
        menu.add_cascade(label="File", menu=subMenu)
        subMenu.add_command(label="New Game...", command=self.doNothing)
        subMenu.add_command(label="New...", command=self.doNothing)
        subMenu.add_separator()
        subMenu.add_command(label="Exit", command=self.doNothing)

        editMenu = Menu(menu)
        menu.add_cascade(label="Edit", menu=editMenu)
        editMenu.add_command(label="Redo", command=self.doNothing)


    def doNothing(self):
        print("Okay I do nothing..")
