##################### Extra Hard Starting Project ######################
import datetime
import pandas as pd
import os
import random
import smtplib
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
today= datetime.datetime.today()
df = pd.read_csv("../birthdays.csv")
birthday_dict= {(data_row["month"],data_row["day"]):data_row for (index,data_row) in df.iterrows()}

data_dict= df.to_dict('records')
for i in data_dict:
    if i['month'] == today.month and i['day']==today.day :
        name= i['name']
        email= i['email']
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
txt_dir= "../letter_templates"
txt_files= [f for f in os.listdir(txt_dir)]
random_letter = random.choice(txt_files)
with open(f"../letter_templates/{random_letter}", "r") as infile :
    data = infile.read()

data = data.replace("[NAME]", name)
with open(f"../letter_templates/newfile", "w") as newfile:
    newfile.write(data)


# 4. Send the letter generated in step 3 to that person's email address.
my_email="rdisseo@gmail.com"
password = "qvdhawwnztiumfut"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(my_email,password)
    connection.sendmail(from_addr=my_email,to_addrs="marjanbakhtiariit@gmail.com", msg=f"Subject:BirthdayWisher\n\n{data}")





