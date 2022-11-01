
# two_digits_number = input("Input the number:\n")
# first_digit = int(two_digits_number[0])
# second_digit = int(two_digits_number[1])
#
# sum = first_digit + second_digit
# print(sum)


# height = float(input("enter your height in m:"))
# weight = int(input("enter your weight in kg:"))
# bmi = weight/(height**2)
# bmi_int = round(bmi,2)
#
# print(bmi_int)


# age = int(input("What is your current age?:"))
# age_left = 90 - age
# months = age_left*12
# weeks = age_left*52
# days = age_left*365
#
# print(f"You have {days}, {weeks} weeks and {months} months left")


print("Welcome to the tip calculator.")
bill = float(input("What is the total bill?:$\n"))
people = int(input("How many people to split the bill?:\n"))
tip = int(input("What percentage tip would you like to give?: 10, 12 or 15\n"))

should_pay = (bill + bill * tip / 100) / people
should_pay=round(should_pay,2)

print(f"Each person should pay$: {should_pay}")