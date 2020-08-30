from tkinter import *

UNIT_LENGTH = 0.5

COLORS = {'white': '#FFFFFF','light_blue':'#B6DDF2','bright_blue':'#6CC2F0','medium_blue':'5598BD','dark_blue':'#04507A','darkest_blue':'#325B70'}

def show():
    length = int(text_entry_width.get())//UNIT_LENGTH
    width = int(text_entry_depth.get())//UNIT_LENGTH

    buttons=[]
    for i in range (int(length)):
        line=[]
        for j in range(int(width)):
            button = Button(window, text = "")
            line.append(button)
        buttons.append(line)

    for i in range (int(length)):
        for j in range(int(width)):
            buttons[i][j].grid(row = i, column = j+3)
        

window = Tk()
frame = Frame(window,width=500,height=500,relief="sunken",bd=20)

SCREEN_WIDTH = window.winfo_screenwidth() #int
SCREEN_HEIGHT = window.winfo_screenheight()

window.geometry(str(SCREEN_WIDTH*2//3)+"x"+str(SCREEN_HEIGHT*2//3))

label_width = Label(window,text="Width",font = ("Helvetica", 15)).grid(row = 0)
label_depth = Label(window,text="Depth",font = ("Helvetica", 15)).grid(row = 1)
text_entry_width = Entry(window, selectborderwidth = 0, fg = COLORS['light_blue'], bg = COLORS['dark_blue']) #font = "Helvetica 40"
text_entry_depth = Entry(window, selectborderwidth = 0, fg = COLORS['light_blue'], bg = COLORS['dark_blue']) #font = "Helvetica 40"
text_entry_depth.grid(row=0,column=1)
text_entry_width.grid(row=1,column=1)

button_show = Button(window, text = "Enter", command = show).grid(row=3)

window.mainloop()