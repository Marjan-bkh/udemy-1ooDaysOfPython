from tkinter import  *
import pandas as pd
import random
data_dict={}
to_learn ={}

try:
    df=pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('data/french_words.csv')
else:

data_dict = df.to_dict(orient='records')
random_data={}

def generate_new_word():
    global random_data,flip_timer
    window.after_cancel(flip_timer)
    random_data=random.choice(data_dict)
    canvas.itemconfig(text_French,text='French',fill="black" )
    canvas.itemconfig(text_English, text=random_data['French'] , fill="black" )
    canvas.itemconfig(canvas_img, image=card_front)
    flip_timer = window.after(3000, func=fip_card)

def fip_card():
    canvas.itemconfig(canvas_img,image=card_back)
    canvas.itemconfig(text_French, text='English', fill= "white")
    canvas.itemconfig(text_English, text=random_data['English'] , fill= "white")


def Is_known():
    data_dict.remove(random_data)
    data= pd.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv")
    generate_new_word()



BACKGROUND_COLOR = "#B1DDC6"
window= Tk()
window.title("Flashy")
window.config(padx=50, pady=50 , bg= BACKGROUND_COLOR)

flip_timer = window.after(3000, func= fip_card)

canvas= Canvas(width=800, height=526)
canvas.pack()
card_front=PhotoImage(file="./images/card_front.png")
card_back= PhotoImage(file="./images/card_back.png")
right_img= PhotoImage(file="./images/right.png")
wrong_img= PhotoImage(file="./images/wrong.png")
canvas_img= canvas.create_image(400,263,image= card_front)
text_French= canvas.create_text(400,150,text="" , font=("Arial", 40, "italic"))
text_English= canvas.create_text(400,263, text="",font=("Arial",60, "bold"))
canvas.grid(row=0 , column=0, columnspan=2)
canvas.config(bg= BACKGROUND_COLOR, highlightthickness=0)

button_wrong= Button(image=wrong_img,highlightthickness=0 ,command= generate_new_word)
button_wrong.grid(row=1,column=0)
button_right= Button(image=right_img ,highlightthickness=0 ,command=Is_known)
button_right.grid(row=1 , column=1)

generate_new_word()

window.mainloop()

