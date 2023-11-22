import tkinter
from tkinter import *

THEME_COLOR = "#375362"
class QuizInterface:
    def __init__(self):
        self.window= Tk()
        self.window.title("QuizLer")
        self.window.config(bg=THEME_COLOR)
        self.window.geometry('350x650')
        self.canvas= Canvas(self.window, width= 340, height= 350, bg="white")
        self.canvas.create_text(100, 30, text="HELLO WORLD", fill="black", font=('Arial 20 italic'),)
        self.canvas.pack(padx=20,pady=20)
        self.gif1 = tkinter.PhotoImage(file='images/true.png')

        # Put gif image on canvas.
        # Pic's upper-left corner (NW) on the canvas is at x=50 y=10.

        self.canvas_img.create_image(20, 350, image=self.gif1, anchor=NW)

        self.window.mainloop()

