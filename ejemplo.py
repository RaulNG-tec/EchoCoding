from tkinter import *
from math import log, e

COLORS = {'white': '#FFFFFF','light_blue':'#B6DDF2','bright_blue':'#6CC2F0','medium_blue':'5598BD','dark_blue':'#04507A','darkest_blue':'#325B70'}

def funcEnter(text_entry_width,text_entry_depth,canvas,button_start,button_back):
    canvas.create_rectangle(0, 0, int(text_entry_width.get()), int(text_entry_depth.get()), outline=COLORS['darkest_blue'], fill=COLORS['darkest_blue'])
    canvas.pack()
    text_entry_width.pack_forget()
    text_entry_depth.pack_forget()
    button_start.pack_forget()
    button_back.pack()

def funcBack(text_entry_width, text_entry_depth, button_start, canvas, button_back):
    text_entry_width.pack()
    text_entry_depth.pack()
    button_start.pack()
    canvas.pack_forget()
    button_back.pack_forget()

def main():
    window = Tk(className="Solución reto BlueYonder")
    window.configure(bg = "black")

    SCREEN_WIDTH = window.winfo_screenwidth() #int
    SCREEN_HEIGHT = window.winfo_screenheight()

    window.geometry(str(SCREEN_WIDTH//2)+"x"+str(SCREEN_HEIGHT//2))


    frame_width      = Frame(window, background = 'BLACK', borderwidth = 5, relief = SUNKEN)
    frame_depth      = Frame(window, background = 'BLACK', borderwidth = 5, relief = SUNKEN)
    frame_percentage = Frame(window, background = 'BLACK', borderwidth = 5, relief = SUNKEN)
    text_entry_width      = Entry(window, borderwidth = 0, fg = COLORS['light_blue'], bg = COLORS['dark_blue']) #font = "Helvetica 40"
    text_entry_depth      = Entry(window, borderwidth = 0, fg = COLORS['light_blue'], bg = COLORS['dark_blue']) #font = "Helvetica 40"
    text_entry_percentage = Entry(window, borderwidth = 0, fg = COLORS['light_blue'], bg = COLORS['dark_blue'])

    label_width      = Label(window, text = "Width", bg = COLORS['darkest_blue'], fg = 'white') #expand = True, fill = BOTH
    label_depth      = Label(window, text = "Depth", bg = COLORS['darkest_blue'], fg = 'white')
    label_percentage = Label(window, text = "Percentage", bg = COLORS['darkest_blue'], fg = 'white')

    window.update()

    canvas = Canvas(window, width = window.winfo_width()*3//4, height = window.winfo_height()*3//4)
    
    button_start = Button(window, text = "Enter", padx = 20, pady = 10, command = lambda: funcEnter(text_entry_width,text_entry_depth,canvas,button_start,button_back))
    button_back = Button(window,text = "<-", padx = 20, pady = 10, command = lambda: funcBack(text_entry_width, text_entry_depth, button_start, canvas, button_back))

    label_width.pack()
    text_entry_width.pack()
    label_depth.pack()
    text_entry_depth.pack()
    label_percentage.pack()
    text_entry_percentage.pack()

    button_start.pack()
    window.mainloop()

if __name__ == "__main__":
    main()