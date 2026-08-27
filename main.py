##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

import smtplib
import datetime as dt
from email.mime.text import MIMEText
import pandas
from random import randint
import os


#To hold today date and month
today_day = dt.date.today().day
today_month = dt.date.today().month

def send_wishes(name, receiver_email):

    random_letter_number = randint(1,3)

    with open(f'letter_templates/letter_{random_letter_number}.txt', mode="r") as wishes:
        data = wishes.read()
    data = data.replace("[NAME]",name)

    # with open(f'letter_templates/letter_{random_letter_number}.txt', mode="w") as wishes:
    #     wishes.write(data)

    # --- your credentials ---
    sender_email = os.environ.get("sender_email")
    sender_password = os.environ.get("sender_password")
    receiver_email = receiver_email

    # --- build the message ---
    message = MIMEText(data)
    message["Subject"] = "HAPPY BIRTHDAY"
    message["From"] = sender_email
    message["To"] = receiver_email

    with smtplib.SMTP_SSL("smtp.wp.pl", 465, timeout=10) as connection:
        connection.login(sender_email, sender_password)
        connection.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully.")

    # with open(f'letter_templates/letter_{random_letter_number}.txt', mode="r") as wishes:
    #     data = wishes.read()
    # #data = data.replace(name, "[NAME]")
    #
    # with open(f'letter_templates/letter_{random_letter_number}.txt', mode="w") as wishes:
    #     wishes.write(data)


birthday_df = pandas.read_csv("birthdays.csv")
birthday_list = birthday_df.to_dict(orient="records")


for item in birthday_list:
    if item["day"] == today_day and item["month"] == today_month:
        print("Sending")
        birthday_name = item["name"]
        send_wishes(birthday_name, item["email"])




#Example
#print(birthday_df.year[birthday_df['email'] == "daniel.rosochacki.86@gmail.com"])





# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.





