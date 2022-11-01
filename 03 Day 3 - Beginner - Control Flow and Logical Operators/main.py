# number = int(input("choose a number:\n"))
# if number % 2 == 0:
#     print("it  is even")
# else:
#     print("it is not even")


# is_height = input("Your height is greater then 120cm?\n")
# if is_height != "y":
#     print("You can`t ride")
# else:
#     print("You can drive")
#     age = int(input("How old are you?:\n"))
#     if age < 12:
#         print("your price $5")
#     elif age <=18:
#         print("your pruce $7")
#     else:
#         print("your price $12")


# height = float(input("enter your height in m:"))
# weight = int(input("enter your weight in kg:"))
# bmi = weight/(height**2)
# bmi_int = round(bmi,2)
#
# print(bmi_int)
#
# if bmi_int <18.5:
#     print("You are underweight")
# elif bmi_int <25:
#     print("Normal weight")
# elif bmi_int <30:
#     print("overweight")
# elif bmi_int < 35:
#     print("obese")
# else:
#     print("clinic obese")

# def leap():
#     year = int(input("input year:"))
#     if year % 400 == 0:
#         print("LEAP")
#     elif year % 100 == 0:
#         print("NOT LEAP")
#     elif year % 4 == 0:
#         print("LEAP")
#     else:
#         print("NOT LEAP")
#
# while True:
#     leap()


# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S M or L?")
# add_peperoni = input("Do you want extra peperoni?")
# extra_cheese = input("Do you want extra cheese: Y or N")
#
# price = 0
#
# if size == "S":
#     price += 15
# elif size == "M":
#     price += 20
# else:
#     price += 25
# if add_peperoni == "Y":
#     if size == "S":
#         price += 2
#     else:
#         price += 3
# if extra_cheese == "Y":
#     price +=1
#
# print(f"Your  final bill is: ${price}")


# print("Welcome to the Love Calculator!")
# name1 = input("What is your name?\n")
# name2 = input("What is their name?\n")
#
# name_togather = name1+name2
#
# score = 0
#
# for i in name_togather.lower():
#     if i == 't' or i == 'r' or i == "u" or i == "e":
#         score += 10
#
# for i in name_togather.lower():
#     if i == 'l' or i == 'o' or i == "v" or i == "e":
#         score += 1
#
# print(score)
#
# if score <10 or score >90:
#     print(f"Your score is {score}, you go together like coke snd mentos")
# elif score >40 and score<50:
#     print(f"Your score is {score}, you are alright together")
# else:
#     print(f"Your score is {score}")




