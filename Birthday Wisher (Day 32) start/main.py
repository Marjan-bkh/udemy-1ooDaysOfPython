import smtpd
import datetime as dt
import random
import smtplib
my_email='appbrweryinfo@gmail.com'
my_pass="abcd1234"
now=dt.datetime.now()
weekday=now.weekday()
if weekday==6:
    with open('quotes.txt','r') as quote_file:
        all_quote=quote_file.readlines()
        quote=random.choice(all_quote)
        print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,my_pass)
        connection.sendmail(from_addr=my_email,to_addrs=my_email,msg=f"Subject:Saturday Motivation\n\n{quote}")