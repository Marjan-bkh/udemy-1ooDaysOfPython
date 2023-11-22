from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list= [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    password= "".join(password_list)
    text_password.insert(0,password)
    pyperclip.copy(password)
    # print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = text_website.get()
    email = text_email.get()
    password = text_password.get()
    new_data= {
        website:{
            'email': email,
            'password':password,
        }
    }
    if len(website)<2 or len(email)<2 or len(password) <2:
        messagebox.showerror(title="Oops", message="Please dont leave any field empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data, data_file , indent=4)
        else:
            data.update(new_data)
            with open("data.json","w") as data_file:
                json.dump(data,data_file,indent=4)
        finally:
            text_website.delete(0,END)
            text_password.delete(0,END)

#----------------------------Search Password--------------------------#
def find_password():
    website = text_website.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message= "No Data File Found!")
    else:
        if website in data:
            messagebox.showinfo(title=website, message= f"email: {data[website]['email']} \n passwor:{data[website]['password']}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists!")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50, bg= "white")
canvas = Canvas(width= 200, height=200, bg="white",highlightthickness=0)
image_name= PhotoImage(file="logo.png")
canvas.create_image(100,100, image=image_name )
canvas.grid(row=0,column=1)

lable_website= Label(text="Website:" ,bg="white" )
lable_website.grid(row=1, column=0, sticky=W)

lable_email= Label(text="Email/Username:" ,bg="white")
lable_email.grid(row=2, column=0 , sticky=W)

lable_password= Label(text="Password:" ,bg="white")
lable_password.grid(row=3, column=0 , sticky=W)

text_website= Entry( width=35 )
text_website.grid(row=1, column=1 ,columnspan=2, sticky=W)
text_website.focus()

text_email= Entry( width=35 )
text_email.grid(row=2, column=1 ,columnspan=2 , sticky=W)
text_email.insert(0,"marjan@yahoo.com")

text_password= Entry( width=21 )
text_password.grid(row=3, column=1 , sticky=W)

button_search= Button(text= "Search", command= find_password)
button_search.grid(row=1 , column=2)
button_generate_pass= Button(text="GeneratePassword" ,command= generate_pass )
button_generate_pass.grid(row=3 ,column=2, sticky=W )

button_add= Button(text="Add" ,width=36 ,command= save)
button_add.grid(row=4 ,column=1, columnspan=2 )



# canvas.pack()
window.mainloop()