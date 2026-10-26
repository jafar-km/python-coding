import pandas as pd
import random
import datetime as dt
import smtplib

my_email = "abdallah01.abdulrhaman01@gmail.com"
password = "blah"


# 2. Check if today matches the date in the greetings.csv
today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv("greetings.csv")
greeting_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in greeting_dict:
    greeted_person = greeting_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]",greeted_person["name"])


with smtplib.SMTP("smtp.gmail.com", 587, timeout=15) as connection :
    connection.starttls()
    connection.login(my_email, password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=greeted_person["email"],
        msg=f"Subject: Greetings! \n\n{contents}")





