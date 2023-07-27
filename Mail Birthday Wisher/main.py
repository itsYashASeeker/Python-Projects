##################### Automate Mail Birthday wisher ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
import random

import pandas
import datetime as dt

key_value = -1
def key_now():
    global key_value
    key_value = key_value + 1
    return key_value
now = dt.datetime.now()
birthday_file = open(file="birthdays.csv")
new_data = pandas.read_csv(birthday_file, header=0, index_col=0)
print(new_data)
today_is_birthday = {key_now(): [row.name_of_person, row.month, row.day] for (index, row) in new_data.iterrows()
                     if row.month == now.month
                     if row.day == now.day}
print(today_is_birthday)
# # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
for data in today_is_birthday:
    list_of_letter = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    chosen_type_letter = random.choice(list_of_letter)
    letter = open(file=f"letter_templates/{chosen_type_letter}")
    letter = letter.read()
    name_of_person = today_is_birthday[data][0]
    print(name_of_person)
    birthday_letter = letter.replace("[NAME]", name_of_person)
    print(birthday_letter)
    with open(f"letter_for_{name_of_person}", "w") as letter_data:
        letter_data.write(birthday_letter)
# 4. Send the letter generated in step 3 to that person's email address.
import smtplib

yahoo_mail = "email"
yah_pass = "email"
to_mail_address = "email"

with smtplib.SMTP("smtp.mail.yahoo.com") as yah_connection:
    yah_connection.starttls()
    yah_connection.login(user=yahoo_mail, password=yah_pass)
    yah_connection.sendmail(from_addr=yahoo_mail, to_addrs=to_mail_address, msg=birthday_letter)