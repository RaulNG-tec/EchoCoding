from tkinter import *

window = Tk()

# width, depth = (input("Width: "), input("Depth: "))
# window.geometry(width+"x"+depth)

window.geometry("500x500")


label = Label(window, text = "Hello World", bg = "blue")
label.pack(fill = X) #expand = True

window.mainloop()

