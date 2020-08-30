from tkinter import *

window = Tk()
# width, depth = (input("Width: "), input("Depth: "))
# window.geometry(width+"x"+depth)
SCREEN_WIDTH = window.winfo_screenwidth() #int
SCREEN_HEIGHT = window.winfo_screenheight()

window.geometry(str(SCREEN_WIDTH//2)+"x"+str(SCREEN_HEIGHT//2))

text_entry_width      = Entry(window, bg = '#8f9b9c') #font = "Helvetica 40"
text_entry_depth      = Entry(window, bg = '#8f9b9c') #font = "Helvetica 40"
text_entry_percentage = Entry(window, bg = '#8f9b9c')

label_width = Label(window, text = "Hello World", bg = "blue")
label_width.pack(fill = X) #expand = True, fill = BOTH

canvas = Canvas()

def funcEnter(text,text2):
    print("Funcion: " + text + " " + str(text2))
    label_width["text"] = text2
    text_entry_width.pack_forget()
    text_entry_depth.pack_forget()
    button_start.pack_forget()
    canvas.create_rectangle(30, 10, 120, 80, outline="#fb0", fill="#fb0")
    canvas.pack()
    button_back.pack()

def funcBack():
    text_entry_width.pack()
    text_entry_depth.pack()
    button_start.pack()
    canvas.pack_forget()
    button_back.pack_forget()

button_start = Button(window, text = "Enter", padx = 20, pady = 10, command = lambda: funcEnter(text_entry_width.get(),text_entry_depth.get()))
button_back = Button(window,text = "<-", padx = 20, pady = 10, command = funcBack)

text_entry_width.pack()
text_entry_depth.pack()
button_start.pack()
window.mainloop()
