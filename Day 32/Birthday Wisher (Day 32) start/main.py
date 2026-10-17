import smtplib

my_email = "dummy text"
password = "dummy text"


connection = smtplib.SMTP("smtp.gmail.com")
connection.ehlo()
connection.starttls()
connection.ehlo()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="dummy text", msg="Blah Blah")
connection.close()
