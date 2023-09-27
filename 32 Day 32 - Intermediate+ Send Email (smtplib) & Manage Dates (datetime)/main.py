##################### Hard Starting Project ######################
import random
import pandas
import smtplib
import datetime

my_email = "altynd85@gmail.com"
password = ""

# what is day and month today
now_month = datetime.datetime.now().month
now_day = datetime.datetime.now().day

#import csv with pandas
df = pandas.read_csv("birthdays.csv")
names = df.name[df.day==now_day].values
for name in names.tolist():
    email=df.email[df.name==name].values
    i = random.randint(1,3)
    with open(f"letter_templates/letter_{i}.txt") as file:
        letter = file.read()
        letter = letter.replace("[NAME]", name)

    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(user=my_email, password=password)
    #     connection.sendmail(from_addr=my_email,to_addrs=email, msg=new_letter)

    print(f"connection.sendmail(from_addr={my_email},to_addrs={email}, msg={letter})")


# #search throw df how is bithday today
# df = df[df.month == now_month][df.day == now_day]
#
# #make lists names and emails
# names = df.name.values
# emails = df.email.values

# #for each people birthday
# for people in range(len(names)):
#     # open letter
#     new_letter = ""
#     i = random.randint(1,3)
#     with open(f"letter_templates/letter_{i}.txt") as file:
#         letter = file.readlines()
#
#     name = names[people]
#     email = emails[people]
#     #change name in letter
#     for string in letter:
#         string = string.replace("[NAME]", name)
#         new_letter+=string
#
#     my_email = "altynd85@gmail.com"
#     password = ""
#
#     # # with smtplib.SMTP("smtp.gmail.com") as connection:
#     # #     connection.starttls()
#     # #     connection.login(user=my_email, password=password)
#     # #     connection.sendmail(from_addr=my_email,to_addrs=email, msg=new_letter)
#     #
#     print(f"connection.sendmail(from_addr={my_email},to_addrs={email}, msg={new_letter})")


# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
# HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)


# import  smtpd
# import smtplib
#
#
# my_email = "altynd85@gmail.com"
# password = ""
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,to_addrs="altynd@mail.ru", msg="Subject:Hello Hello\\nThis is body")


# import datetime as dt
# now = dt.datetime.now()
# now=now.isoweekday()
#
# date_of_birth = dt.datetime(year=1985,month=12,day=15,hour=4)
# print(date_of_birth)

############################
# import datetime
# import smtplib
# import random
#
#
# my_email = "my@mail.ru"
# my_password = "password"
# smtp = "smtp.mail.ru"
# now = datetime.datetime.now().isoweekday()
#
#
# with open("text.txt") as file:
#     data = file.readlines()
#     quote = random.choice(data)
#
#     if now == 1:
#         with smtplib.SMTP(smtp) as connection:
#             connection.starttls()
#             connection.login(user=my_email,password=my_password)
#             connection.sendmail(
#                 from_addr=my_email,
#                 to_addrs=my_email,
#                 msg=f"Subject\\n{quote}")
#         print(quote)
##############################
