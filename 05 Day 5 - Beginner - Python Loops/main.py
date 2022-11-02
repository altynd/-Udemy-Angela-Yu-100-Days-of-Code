# import random
#
# print("Welcome to the PyPassword Generator")
# letters = int(input("How many letters would you like in your password?"))
# symbols = int(input("How many symbols would you like?"))
# numbers = int(input("How many numbers would you like?"))
#
# letters_data = ["a","b","c","d","e","f","g"]
# symbols_data = ["!", "@", "#", "$", "%", "^"]
#
# password=[]
#



# students_heights = [180, 124, 165, 173, 189, 169, 146]
# # sum_height=0
# # for height in students_heights:
# #     sum_height += height
# # sum_height = sum(students_heights)
#
# average_height = int(round(sum(students_heights)/len(students_heights),0))
# print(average_height)


# student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
#
# print(f"The highest score in class is: {highest_score}")

#
# for number in range(len(student_scores)):
#     print(number)
# sum=0
# for even_number in range (2,101,2):
#     # print(even_number)
#     sum+=even_number
# print(sum)

# for i in range(1,101):
#     if i % 15 == 0:
#         print("FIZZBUZZ")
#     elif i % 3 == 0:
#         print("FIZZ")
#     elif i % 5 == 0:
#         print("BAZZ")
#     else:
#         print(i)


for i in range(0,letters):
    letter_random = random.choice(letters_data)
    rand_cap = random.randint(0,1)
    if rand_cap == 1:
        letter_random = letter_random.title()
    password.append(letter_random)

for i in range(0,symbols):
    symbol_random = random.choice(symbols_data)
    password.append(symbol_random)

for i in range(0,numbers):
    number_random = random.randint(0,9)
    password.append(str(number_random))

random.shuffle(password)

pas_str=""
for i in password:
    pas_str = pas_str + i

print(pas_str)