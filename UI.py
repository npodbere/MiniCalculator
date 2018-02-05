from tkinter import *
window = Tk()

def printVal():
    canvas = Canvas(window, width = 100, height = 100)
    canvas.grid(row = 0, column = 0, columnspan = 2)
    string = entryval.get()
    canvas.create_text(50,50, text = string)

entryval = Entry(window)
entryval.grid(row = 1, column = 0)
button = Button(window, text = "Print", command = printVal)
button.grid(row = 1, column = 1)

window.mainloop()