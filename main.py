import smtplib
import datetime as dt
import random

my_gmail = ""
my_ymail = ""
password = ""


now = dt.datetime.now()
day = now.weekday()
if day == 0:

    with open("quotes.txt", "r") as quotes:
        lines = [line for line in quotes]
        with smtplib.SMTP("smtp.gmail.com") as connection:
            # Secure connection
            connection.starttls()
            # Login
            connection.login(user=my_gmail, password=password)
            # Send mail
            connection.sendmail(
                from_addr=my_gmail,
                to_addrs=my_ymail,
                msg=f"Subject: Wsp \n\n {random.choice(lines)}")


# Yahoo connection
# connection = smtplib.SMTP("smtp.mail.yahoo.com")
# Gmail connection
# connection = smtplib.SMTP("smtp.gmail.com")
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#
#     # Secure connection
#     connection.starttls()
#     # Login
#     connection.login(user=my_gmail, password=password)
#     # Send mail
#     connection.sendmail(
#         from_addr=my_gmail,
#         to_addrs=my_ymail,
#         msg="Subject: Wsp \n\n Hello")

