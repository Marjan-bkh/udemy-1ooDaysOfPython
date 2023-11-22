import tkinter
from tkinter import *
def mile_to_km():
    miles= float(input_text.get())
    km = miles* 1.609
    lable_resualt.config( text= f"{km}")



window = Tk()
window.title("Mile to Km convertor")
window.config(pady=20 , padx=20)
input_text = Entry(width= 7)
input_text.grid(column= 1, row= 0)

lable_mile= Label(text= "Mile")
lable_mile.grid( column=2 ,row= 0)

lable_isequal= Label(text= "is equal to ")
lable_isequal.grid( column=0 ,row= 1)

lable_resualt= Label(text= "0 ")
lable_resualt.grid( column=1 ,row= 1)

lable_km= Label(text= "km ")
lable_km.grid( column=2 ,row= 1)

btn_calculate= Button(text= "calculate" ,command=mile_to_km )
btn_calculate.grid(column= 1, row=2)

window.grid_columnconfigure(1, weight=1)
window.mainloop()