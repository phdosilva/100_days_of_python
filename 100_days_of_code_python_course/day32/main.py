##################### Extra Hard Starting Project ######################
import random
import pandas
import datetime
import smtplib
from os import listdir

# 1. Update the birthdays.csv
birthdays_data = pandas.read_csv("birthdays.csv")
birthdays_data_list = birthdays_data.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
now = datetime.datetime.now()

today_birthdays = [friend for friend in birthdays_data_list if friend["month"] == now.month and friend["day"] == now.day]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.
files_names = listdir("letter_templates")
my_email = "@gmail.com"
my_key = ""

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()  # make this connection secure
    connection.login(user=my_email, password=my_key)

    for birthday in today_birthdays:
        letter_file_name = random.choice(files_names)
        with open("letter_templates/" + letter_file_name, "r") as file:
            letter = file.read()

        connection.sendmail(from_addr=my_email,
                            to_addrs="@gmail.com",
                            msg="Subject:Happy birthday!\n\n" + letter.replace("[NAME]", birthday["name"]))













# my_email = "registraremcoisasaleatorias@gmail.com"
# my_key = "abc()12()34"

#                             to_addrs="phdosilva@gmail.com",

