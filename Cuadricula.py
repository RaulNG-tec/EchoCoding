from tkinter import *

UNIT_LENGTH = 0.5;

COLORS = {'white': '#FFFFFF','light_blue':'#B6DDF2','bright_blue':'#6CC2F0','medium_blue':'5598BD','dark_blue':'#04507A','darkest_blue':'#325B70'}

window = Tk()
SCREEN_WIDTH = window.winfo_screenwidth() #int
SCREEN_HEIGHT = window.winfo_screenheight()
window.geometry(str(SCREEN_WIDTH//2)+"x"+str(SCREEN_HEIGHT//2))

text_entry_width = Entry(window, textvariable = '0', selectborderwidth = 0, fg = COLORS['light_blue'], bg = COLORS['dark_blue']) #font = "Helvetica 40"
text_entry_depth = Entry(window, textvariable = '0', selectborderwidth = 0, fg = COLORS['light_blue'], bg = COLORS['dark_blue']) #font = "Helvetica 40"

length = int(text_entry_width.get())//UNIT_LENGTH
width = int(text_entry_depth.get())//UNIT_LENGTH

buttons=[]
for i in range (length*2):
    line=[]
    for j in range(width*2):
        line.append(Button(window, text = " ", width = 5, hieght = 5))
    buttons.append(line)

for i in range (length*2):
    for j in range(wdt*2):
        buttons[i][j].width(row = i, column = j)

window.mainloop()