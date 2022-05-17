# Motivational Monday Quotes

# import random
# import smtplib
# import datetime
#
# my_email = "@gmail.com"
# my_key = ""
#
# now = datetime.datetime.now()
# day_of_week = now.weekday()
#
# try:
#     with open("quotes.txt", "r") as file:
#         quotes = file.readlines()
# except FileNotFoundError as err:
#     print(err)
#     quotes = []
#
# if day_of_week == 0 and len(quotes) != 0:
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()  # make this connection secure
#         connection.login(user=my_email, password=my_key)
#         connection.sendmail(from_addr=my_email,
#                             to_addrs="@gmail.com",
#                             msg="Subject:Motivational Monday Quotes\n\n" + random.choice(quotes))


# Birthday wisher project


