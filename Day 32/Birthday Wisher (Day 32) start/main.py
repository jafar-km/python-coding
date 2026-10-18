import random
import smtplib
import datetime as dt
now = dt.datetime.now()
day_of_week = now.weekday()

my_email = "abdallah01.abdulrhaman01@gmail.com"
password = "vsvr npwe inxs gvfj"

if day_of_week == 0:
    with open("quotes.txt", "r") as data_file:
        quotes = data_file.readlines()
        random_quote = random.choice(quotes)

connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=15)
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email,
                    to_addrs="jafar.mohamed2006@gmail.com",
                    msg=f"Subject: Monday Motivation\n\n{random_quote}")
connection.close()





