# def calc(a, b, operator):
#     if operator == "+":
#         return a + b
#     elif operator == "/":
#         return a / b
#     elif operator == "-":
#         return a - b
#     elif operator == "*":
#         return a * b
#
# a=None
# is_continue=True
# while is_continue:
#     if a == None:
#         a = int(input("What`s the first number:"))
#     else:
#         a = c
#     print(
#           "+\n"
#           "-\n"
#           "*\n"
#           "/"
#           )
#     operator = input("Pick a operator:")
#     b = int(input("What`s next number?:"))
#     c = calc(a, b, operator)
#     print(f"{a} {operator} {b} = {c}")
#     if input(f"type y fo continue calculating with {c}") != "y":
#         is_continue = False



# def leap(year):
#     """ returns leap year """
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True
#     else:
#         return False
#
# def day_in_month(year, month):
#     month = month-1
#     month_days =[31,28,31,30,31,30,31,31,30,31,30,31]
#     if leap(year):
#         month_days[1] = 29
#     days = month_days[month]
#     return days
#
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = day_in_month(year, month)
# print(days)
